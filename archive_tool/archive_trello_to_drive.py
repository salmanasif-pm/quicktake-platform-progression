#!/usr/bin/env python3
"""
Archive the Trello board "PL Sales with Ahmed(AE)" into an existing Google Drive
folder, per TRELLO_ARCHIVE_CLAUDE_CODE_SPEC.md.

Design notes
------------
* Trello is read-only. Every Trello request goes through `TrelloReader.get`,
  which refuses any verb other than GET. The script can also run entirely from a
  pre-pulled snapshot (`--snapshot`), which needs no Trello access at all.
* Drive writes are confined to the archive root by `Boundary`, which is asserted
  immediately before every create and every copy.
* The run is resumable: the manifest is read first, and the destination folders
  are reconciled against Drive itself, so an interrupted run neither redoes work
  nor creates duplicates.

Usage
-----
    python3 archive_trello_to_drive.py --snapshot data/trello_snapshot.json
    python3 archive_trello_to_drive.py --lists 04,05,06,07
    python3 archive_trello_to_drive.py --dry-run
"""

import argparse
import csv
import io
import os
import random
import re
import sys
import time
import traceback
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import classify as C

# --------------------------------------------------------------------------
# Identifiers (spec section 2)
# --------------------------------------------------------------------------

BOARD_SHORTLINK = "X9ZczKio"
BOARD_URL = "https://trello.com/b/X9ZczKio/pl-sales-with-ahmedae"

ARCHIVE_ROOT = "1LSAK21sUzMpyaUrO7HgZ5OcL6KDrCyUu"
CONTROL_FOLDER = "1dMjbuwBOnGomhUMBIZkxBcq52JAL3aHG"

# Legacy superseded duplicate of card 463: flag once, never touch.
LEGACY_FOLDER_ID = "1ZHAMwck-qIxpSyuY5TOnRYAsj5fD-7yC"
LEGACY_FOLDER_NAME = "Claude Test - 463 - HHC Operations Platform"

# Trello list name -> archive folder name. Existing folders are reused by id.
LIST_FOLDERS = [
    ("BA Team (Pending)",                     "01 - BA Team (Pending)",                     None),
    ("BA Team (In Progress)",                 "02 - BA Team (In Progress)",                 "1UakM0-kuWpygGKDBgZwFZfk_pPfZn22_"),
    ("HOE | Ahmed's Review",                  "03 - HOE | Ahmed's Review",                  "1NEEhIZMA7fbGAPV-0g3DaT1tKpLaVNWy"),
    ("Done, (Waiting on Decision)",           "04 - Done, (Waiting on Decision)",           "1uopGJmVeqvDP2hBHZwLEQFD1NVDnzdJC"),
    ("Closed Won",                            "05 - Closed Won",                            None),
    ("Closed Lost",                           "06 - Closed Lost",                           None),
    ("On Hold",                               "07 - On Hold",                               None),
    ("Unresponsive",                          "08 - Unresponsive",                          "1rdfgjU2QuV25RfSVA0INGdEpHw8v4flm"),
    ("Internal Cards - Done",                 "09 - Internal Cards - Done",                 "10NollXvnj8T3uvedGXTxCfa61zuxE0uh"),
    ("Solution Architect | AE (Final Review)", "10 - Solution Architect | AE (Final Review)", "15Q-1Dr54A6MZlRMPPNcukoyRjdj094AY"),
]
LIST_TO_FOLDER = {t: (n, i) for t, n, i in LIST_FOLDERS}

# Cards already archived by earlier runs (spec section 6), matched on idShort.
ALREADY_DONE = {
    414, 463,                                             # list 02
    434, 456,                                             # list 03
    462, 461, 460, 459, 457, 21, 207, 445, 438, 451,      # list 04
    38, 120, 11, 10, 15, 123, 108, 64, 46, 29, 13,        # list 08
    1,                                                    # list 09
    125, 129, 130, 128, 127, 126,                         # list 10
}

SUBFOLDER_TRELLO = "01 - Trello Record"
SUBFOLDER_SOURCES = "02 - Copied Source Files"
SUBFOLDER_DIAGRAMS = "04 - Final Diagrams"
SUBFOLDER_INDIVIDUAL = "Individual Diagrams"

MANIFEST_NAME = "archive-manifest.csv"
ERRORS_NAME = "errors.csv"
MANIFEST_COLUMNS = [
    "list_name", "card_idshort", "card_name", "card_url", "dest_folder_id",
    "source_file_id", "source_file_name", "copied_file_id", "copied_file_url",
    "status", "skip_reason", "timestamp",
]
ERROR_COLUMNS = ["timestamp", "card", "file", "error"]

DRIVE_SCOPES = ["https://www.googleapis.com/auth/drive"]
DRIVE_FIELDS = (
    "id,name,mimeType,size,quotaBytesUsed,modifiedTime,webViewLink,owners(emailAddress),trashed"
)
WRITE_SLEEP = 0.15          # spec section 9: ~150 ms between Drive writes
MAX_RETRIES = 5


def now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def log(msg):
    sys.stdout.write("%s  %s\n" % (datetime.now().strftime("%H:%M:%S"), msg))
    sys.stdout.flush()


# --------------------------------------------------------------------------
# Hard write boundary (spec section 4)
# --------------------------------------------------------------------------

class BoundaryViolation(RuntimeError):
    pass


class Boundary:
    """
    Every Drive write must name a parent inside the archive root.

    `known_good` starts as {ARCHIVE_ROOT} and grows only with folders that were
    themselves created or discovered under an already-trusted parent, so the
    trusted set can never escape the root by construction.
    """

    def __init__(self, root=ARCHIVE_ROOT, extra=(CONTROL_FOLDER,)):
        self.root = root
        self.known_good = {root}
        self.known_good.update(extra)

    def assert_in_boundary(self, parent_id):
        if parent_id not in self.known_good:
            raise BoundaryViolation(
                "BOUNDARY VIOLATION: parent %r not under archive root %s"
                % (parent_id, self.root)
            )

    def trust(self, folder_id, parent_id):
        """Admit a folder to the trusted set, but only under a trusted parent."""
        self.assert_in_boundary(parent_id)
        self.known_good.add(folder_id)
        return folder_id


# --------------------------------------------------------------------------
# Trello, read-only
# --------------------------------------------------------------------------

class TrelloReadOnlyViolation(RuntimeError):
    pass


class TrelloReader:
    """GET-only Trello client. Any other verb raises before a socket is opened."""

    BASE = "https://api.trello.com/1"

    def __init__(self, key, token):
        import requests
        self._requests = requests
        self.key = key
        self.token = token
        self.calls = 0
        self.writes_attempted = 0

    def request(self, method, path, **params):
        if method.upper() != "GET":
            self.writes_attempted += 1
            raise TrelloReadOnlyViolation(
                "refusing %s %s: this tool is read-only against Trello"
                % (method, path)
            )
        return self.get(path, **params)

    def get(self, path, **params):
        params.update(key=self.key, token=self.token)
        url = "%s/%s" % (self.BASE, path.lstrip("/"))
        for attempt in range(MAX_RETRIES):
            r = self._requests.get(url, params=params, timeout=60)
            self.calls += 1
            if r.status_code == 429 or r.status_code >= 500:
                time.sleep(_backoff(attempt))
                continue
            r.raise_for_status()
            return r.json()
        raise RuntimeError("Trello GET %s failed after %d retries" % (path, MAX_RETRIES))

    def lists(self):
        return self.get("boards/%s/lists" % BOARD_SHORTLINK)

    def cards(self, list_id):
        return self.get(
            "lists/%s/cards" % list_id,
            fields="id,idShort,name,desc,shortUrl,url,closed,dueComplete,due,"
                   "dateLastActivity,labels",
            attachments="true",
            attachment_fields="name,url,bytes",
        )


def _backoff(attempt):
    return min(60.0, (2 ** attempt) + random.uniform(0, 1.0))


# --------------------------------------------------------------------------
# Card normalisation: live API and MCP snapshot both reduce to one shape
# --------------------------------------------------------------------------

RE_ID_SHORT = re.compile(r"/c/[^/]+/(\d+)-")


def normalise_card(raw, list_name=None):
    """Reduce a Trello card, from either source, to the fields the archive needs."""
    url = raw.get("shortUrl") or raw.get("webUrl") or raw.get("url") or ""

    id_short = raw.get("idShort")
    if id_short is None:
        m = RE_ID_SHORT.search(raw.get("webUrl") or raw.get("url") or "")
        id_short = int(m.group(1)) if m else None

    if list_name is None:
        lst = raw.get("list") or {}
        list_name = lst.get("name") if isinstance(lst, dict) else None

    labels = []
    for lab in raw.get("labels") or []:
        nm = lab.get("name") if isinstance(lab, dict) else str(lab)
        if nm:
            labels.append(nm)

    attachments = []
    for a in raw.get("attachments") or []:
        if isinstance(a, dict) and a.get("url"):
            attachments.append({"name": a.get("name") or "", "url": a["url"],
                                "bytes": a.get("bytes")})

    return {
        "id_short": id_short,
        "name": raw.get("name") or "",
        "desc": raw.get("desc") or "",
        "url": url,
        "list_name": list_name or "",
        "closed": bool(raw.get("closed")),
        "due_complete": bool(raw.get("dueComplete")),
        "due": raw.get("due"),
        "last_activity": raw.get("dateLastActivity") or raw.get("lastActivityAt"),
        "labels": labels,
        "attachments": attachments,
    }


def load_snapshot(path):
    import json
    with open(path) as fh:
        data = json.load(fh)
    if isinstance(data, dict):
        data = data.get("cards", {}).get("nodes") or data.get("nodes") or []
    return [normalise_card(c) for c in data]


# --------------------------------------------------------------------------
# Drive client
# --------------------------------------------------------------------------

class Drive:
    def __init__(self, service, boundary, dry_run=False):
        self.svc = service
        self.boundary = boundary
        self.dry_run = dry_run
        self.copies = 0
        self.folders_created = 0
        self.list_calls = 0

    # -- retry wrapper ----------------------------------------------------
    def _exec(self, req, what):
        from googleapiclient.errors import HttpError
        for attempt in range(MAX_RETRIES):
            try:
                return req.execute()
            except HttpError as e:
                status = getattr(getattr(e, "resp", None), "status", None)
                body = ""
                try:
                    body = e.content.decode("utf-8", "replace")
                except Exception:
                    pass
                retryable = status in (429, 500, 502, 503, 504) or (
                    status == 403 and (
                        "rateLimitExceeded" in body or "userRateLimitExceeded" in body
                    )
                )
                if retryable and attempt < MAX_RETRIES - 1:
                    time.sleep(_backoff(attempt))
                    continue
                raise
        raise RuntimeError("%s failed after %d retries" % (what, MAX_RETRIES))

    # -- reads ------------------------------------------------------------
    def list_children(self, folder_id, page_limit=40):
        """All non-trashed children of a folder."""
        out, token, pages = [], None, 0
        while True:
            req = self.svc.files().list(
                q="'%s' in parents and trashed = false" % folder_id,
                fields="nextPageToken, files(%s)" % DRIVE_FIELDS,
                pageSize=1000,
                pageToken=token,
                supportsAllDrives=True,
                includeItemsFromAllDrives=True,
            )
            resp = self._exec(req, "list %s" % folder_id)
            self.list_calls += 1
            out.extend(resp.get("files", []))
            token = resp.get("nextPageToken")
            pages += 1
            if not token or pages >= page_limit:
                break
        return out

    def get_file(self, file_id):
        req = self.svc.files().get(
            fileId=file_id, fields=DRIVE_FIELDS, supportsAllDrives=True
        )
        return self._exec(req, "get %s" % file_id)

    def find_child(self, parent_id, name, folder_only=False):
        """Look up one child by exact name, so folders are reused not recreated."""
        safe = name.replace("\\", "\\\\").replace("'", "\\'")
        q = "'%s' in parents and name = '%s' and trashed = false" % (parent_id, safe)
        if folder_only:
            q += " and mimeType = '%s'" % C.GOOGLE_FOLDER
        req = self.svc.files().list(
            q=q,
            fields="files(%s)" % DRIVE_FIELDS,
            pageSize=10,
            supportsAllDrives=True,
            includeItemsFromAllDrives=True,
        )
        files = self._exec(req, "find %s" % name).get("files", [])
        self.list_calls += 1
        return files[0] if files else None

    # -- writes (boundary-checked) ----------------------------------------
    def ensure_folder(self, parent_id, name):
        """Reuse an existing folder of this name under `parent_id`, else create it."""
        self.boundary.assert_in_boundary(parent_id)
        existing = self.find_child(parent_id, name, folder_only=True)
        if existing:
            return self.boundary.trust(existing["id"], parent_id), False
        if self.dry_run:
            return self.boundary.trust("dry-run-%s" % name, parent_id), True
        req = self.svc.files().create(
            body={"name": name, "mimeType": C.GOOGLE_FOLDER, "parents": [parent_id]},
            fields="id",
            supportsAllDrives=True,
        )
        fid = self._exec(req, "create folder %s" % name)["id"]
        self.folders_created += 1
        time.sleep(WRITE_SLEEP)
        return self.boundary.trust(fid, parent_id), True

    def copy_file(self, source_id, parent_id, name):
        """
        files.copy only: never files.update with a parents change, which would
        move the original instead of copying it.
        """
        self.boundary.assert_in_boundary(parent_id)
        if self.dry_run:
            return {"id": "dry-run", "webViewLink": "", "name": name}
        req = self.svc.files().copy(
            fileId=source_id,
            body={"name": name, "parents": [parent_id]},
            fields="id,name,webViewLink",
            supportsAllDrives=True,
        )
        res = self._exec(req, "copy %s" % source_id)
        self.copies += 1
        time.sleep(WRITE_SLEEP)
        return res

    def upload_text(self, parent_id, name, text, mime="text/markdown"):
        self.boundary.assert_in_boundary(parent_id)
        if self.dry_run:
            return {"id": "dry-run", "webViewLink": ""}
        from googleapiclient.http import MediaIoBaseUpload
        media = MediaIoBaseUpload(
            io.BytesIO(text.encode("utf-8")), mimetype=mime, resumable=False
        )
        existing = self.find_child(parent_id, name)
        if existing:
            # Content-only update of a file already inside the boundary.
            req = self.svc.files().update(
                fileId=existing["id"], media_body=media,
                fields="id,webViewLink", supportsAllDrives=True,
            )
            res = self._exec(req, "update %s" % name)
        else:
            req = self.svc.files().create(
                body={"name": name, "parents": [parent_id]}, media_body=media,
                fields="id,webViewLink", supportsAllDrives=True,
            )
            res = self._exec(req, "create %s" % name)
        time.sleep(WRITE_SLEEP)
        return res

    def parent_chain_ok(self, file_id, root=ARCHIVE_ROOT, max_depth=12):
        """Walk parents upward and confirm the chain terminates at the root."""
        cur, depth = file_id, 0
        while cur and depth < max_depth:
            if cur == root:
                return True
            req = self.svc.files().get(
                fileId=cur, fields="id,parents", supportsAllDrives=True
            )
            meta = self._exec(req, "parents %s" % cur)
            parents = meta.get("parents") or []
            if not parents:
                return False
            cur = parents[0]
            depth += 1
        return False


def build_drive(credentials_json, token_json):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build

    creds = None
    if os.path.exists(token_json):
        creds = Credentials.from_authorized_user_file(token_json, DRIVE_SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(credentials_json):
                raise SystemExit(
                    "Missing %s. Create an OAuth desktop client, download it to "
                    "that path, and re-run; authorise as the archive root's owner."
                    % credentials_json
                )
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_json, DRIVE_SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open(token_json, "w") as fh:
            fh.write(creds.to_json())
    return build("drive", "v3", credentials=creds, cache_discovery=False)


# --------------------------------------------------------------------------
# Manifest
# --------------------------------------------------------------------------

class Manifest:
    """
    Append-only run log that doubles as the resume index.

    Kept locally and flushed to the control folder in Drive every `flush_every`
    cards so an interrupted run resumes cleanly.
    """

    def __init__(self, drive, local_dir, flush_every=10):
        self.drive = drive
        self.path = os.path.join(local_dir, MANIFEST_NAME)
        self.errors_path = os.path.join(local_dir, ERRORS_NAME)
        self.flush_every = flush_every
        self.rows = []
        self.errors = []
        self.completed_cards = set()
        self.copied_sources = set()
        self._since_flush = 0

    def load_local(self):
        if not os.path.exists(self.path):
            return
        with open(self.path, newline="") as fh:
            for row in csv.DictReader(fh):
                self.rows.append(row)
                self._index(row)

    def load_from_drive(self):
        """Pull an existing manifest out of the control folder, if one is there."""
        found = self.drive.find_child(CONTROL_FOLDER, MANIFEST_NAME)
        if not found:
            return 0
        data = self.drive.svc.files().get_media(fileId=found["id"]).execute()
        text = data.decode("utf-8", "replace") if isinstance(data, bytes) else str(data)
        n = 0
        for row in csv.DictReader(io.StringIO(text)):
            self.rows.append(row)
            self._index(row)
            n += 1
        return n

    def _index(self, row):
        status = (row.get("status") or "").strip()
        card = (row.get("card_idshort") or "").strip()
        if status == "card_complete" and card:
            try:
                self.completed_cards.add(int(card))
            except ValueError:
                pass
        if status == "copied":
            sid = (row.get("source_file_id") or "").strip()
            if sid:
                self.copied_sources.add(sid)

    def add(self, **kw):
        row = {c: "" for c in MANIFEST_COLUMNS}
        row.update({k: ("" if v is None else str(v)) for k, v in kw.items()})
        row["timestamp"] = row["timestamp"] or now_iso()
        self.rows.append(row)
        self._index(row)
        return row

    def add_error(self, card, filename, error):
        self.errors.append({
            "timestamp": now_iso(), "card": str(card),
            "file": str(filename), "error": str(error)[:800],
        })

    def card_done(self, card):
        self._since_flush += 1
        return self._since_flush >= self.flush_every

    def write_local(self):
        _write_csv(self.path, MANIFEST_COLUMNS, self.rows)
        _write_csv(self.errors_path, ERROR_COLUMNS, self.errors)

    def flush(self):
        self.write_local()
        self._since_flush = 0
        if self.drive.dry_run:
            return
        try:
            with open(self.path) as fh:
                self.drive.upload_text(CONTROL_FOLDER, MANIFEST_NAME, fh.read(),
                                       mime="text/csv")
            if self.errors:
                with open(self.errors_path) as fh:
                    self.drive.upload_text(CONTROL_FOLDER, ERRORS_NAME, fh.read(),
                                           mime="text/csv")
        except Exception as e:
            log("WARNING: manifest flush to Drive failed: %s" % e)


def _write_csv(path, columns, rows):
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=columns)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in columns})


# --------------------------------------------------------------------------
# card.md (spec section 5)
# --------------------------------------------------------------------------

def render_card_md(card, copied, skipped):
    labels = ", ".join(card["labels"]) if card["labels"] else "none"
    urls = C.extract_urls(card["desc"], *[a["url"] for a in card["attachments"]])

    out = []
    out.append("# %s (#%s)\n" % (card["name"], card["id_short"]))
    out.append("- **Card:** %s" % card["url"])
    out.append("- **List:** %s" % card["list_name"])
    out.append("- **Status:** %s, dueComplete=%s, due=%s" % (
        "closed" if card["closed"] else "open",
        card["due_complete"], card["due"]))
    out.append("- **Last activity:** %s" % card["last_activity"])
    out.append("- **Labels:** %s" % labels)
    out.append("\n## Description\n")
    out.append(card["desc"] if card["desc"].strip() else "_(no description)_")
    out.append("\n## Linked URLs found in description/attachments\n")
    out.extend(["- %s" % u for u in urls] or ["_(none)_"])
    out.append("\n## Files copied\n")
    out.extend(["- %s -> %s" % (n, l) for n, l in copied] or ["_(none)_"])
    out.append("\n## Files skipped\n")
    if skipped:
        for n, reason, size in skipped:
            mb = "" if size is None else " (%.2f MB)" % (size / 1048576.0)
            out.append("- %s - %s%s" % (n, reason, mb))
    else:
        out.append("_(none)_")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------
# Discovery (spec section 7)
# --------------------------------------------------------------------------

def discover_files(drive, card, stats, manifest):
    """
    Find every candidate file for a card.

    Returns a list of (file_dict, containing_folder_name). Subfolders are walked
    one level down, because deliverables hide in `BA Draft`, `Latest Updates`,
    `Diagrams` and friends.
    """
    text = card["desc"] + "\n" + "\n".join(
        (a.get("url") or "") + " " + (a.get("name") or "")
        for a in card["attachments"]
    )
    candidates = []
    seen_folders = set()
    seen_files = set()

    for fid in C.extract_folder_ids(text):
        if fid in seen_folders or fid == ARCHIVE_ROOT:
            continue
        seen_folders.add(fid)
        try:
            children = drive.list_children(fid)
        except Exception as e:
            manifest.add_error(card["id_short"], "folder:%s" % fid, e)
            stats["inaccessible_folders"] += 1
            continue

        try:
            folder_name = drive.get_file(fid).get("name", "")
        except Exception:
            folder_name = ""

        for ch in children:
            if ch.get("mimeType") == C.GOOGLE_FOLDER:
                if ch["id"] in seen_folders:
                    continue
                seen_folders.add(ch["id"])
                try:
                    sub = drive.list_children(ch["id"])          # one level down
                except Exception as e:
                    manifest.add_error(card["id_short"],
                                       "subfolder:%s" % ch.get("name"), e)
                    stats["inaccessible_folders"] += 1
                    continue
                for s in sub:
                    if s.get("mimeType") == C.GOOGLE_FOLDER:
                        continue
                    if s["id"] not in seen_files:
                        seen_files.add(s["id"])
                        candidates.append((s, ch.get("name", "")))
            else:
                if ch["id"] not in seen_files:
                    seen_files.add(ch["id"])
                    candidates.append((ch, folder_name))

    # Directly-linked documents with no parent folder in the description.
    for fid in C.extract_file_ids(text):
        if fid in seen_files:
            continue
        try:
            meta = drive.get_file(fid)
        except Exception as e:
            manifest.add_error(card["id_short"], "file:%s" % fid, e)
            stats["inaccessible_files"] += 1
            continue
        if meta.get("trashed"):
            continue
        seen_files.add(fid)
        candidates.append((meta, ""))

    return candidates


# --------------------------------------------------------------------------
# Per-card archive
# --------------------------------------------------------------------------

def archive_card(drive, card, list_folder_id, manifest, stats):
    id_short = card["id_short"]
    card_dir_name = C.card_folder_name(id_short, card["name"])
    card_folder, _ = drive.ensure_folder(list_folder_id, card_dir_name)

    candidates = discover_files(drive, card, stats, manifest)

    # One entry per file id, remembering the folder it was found in.
    folder_of, ordered = {}, []
    for f, folder_name in candidates:
        if f["id"] not in folder_of:
            folder_of[f["id"]] = folder_name
            ordered.append(f)

    copied, skipped = [], []

    def note_skip(f, reason):
        skipped.append((C.file_name(f), reason, C.file_size(f)))
        _tally_skip(stats, reason)
        manifest.add(list_name=card["list_name"], card_idshort=id_short,
                     card_name=card["name"], card_url=card["url"],
                     dest_folder_id=card_folder, source_file_id=f["id"],
                     source_file_name=C.file_name(f), status="skipped",
                     skip_reason=reason)

    # Classify first, so a skipped video is reported as a video rather than as
    # a duplicate of the copy of itself.
    copy_worthy = []
    for f in ordered:
        action, dest, reason = C.classify_file(f, folder_of[f["id"]])
        if action == "copy":
            copy_worthy.append((f, dest))
        else:
            note_skip(f, reason)

    # Duplicate suppression among the copy-worthy set only.
    dest_of = {f["id"]: dest for f, dest in copy_worthy}
    kept, dropped = C.dedupe_files([f for f, _dest in copy_worthy])
    for f, reason in dropped:
        note_skip(f, reason)

    plan = [(f, dest_of[f["id"]], folder_of[f["id"]]) for f in kept]

    # Destination subfolders are created only when they will hold something.
    dest_ids = {}

    def dest_folder(kind):
        if kind in dest_ids:
            return dest_ids[kind]
        if kind == "sources":
            fid, _ = drive.ensure_folder(card_folder, SUBFOLDER_SOURCES)
        elif kind == "diagrams":
            fid, _ = drive.ensure_folder(card_folder, SUBFOLDER_DIAGRAMS)
        elif kind == "individual_diagrams":
            parent, _ = drive.ensure_folder(card_folder, SUBFOLDER_DIAGRAMS)
            fid, _ = drive.ensure_folder(parent, SUBFOLDER_INDIVIDUAL)
        else:
            raise ValueError(kind)
        dest_ids[kind] = fid
        return fid

    for f, dest, _folder_name in plan:
        name = C.file_name(f)
        if f["id"] in manifest.copied_sources:
            stats["already_copied"] += 1
            continue
        try:
            parent = dest_folder(dest)
            # Reconcile against Drive: a file of this name already there is done.
            existing = drive.find_child(parent, name)
            if existing:
                stats["already_present"] += 1
                copied.append((name, existing.get("webViewLink", "")))
                manifest.add(list_name=card["list_name"], card_idshort=id_short,
                             card_name=card["name"], card_url=card["url"],
                             dest_folder_id=parent, source_file_id=f["id"],
                             source_file_name=name,
                             copied_file_id=existing["id"],
                             copied_file_url=existing.get("webViewLink", ""),
                             status="copied", skip_reason="already present")
                continue

            res = drive.copy_file(f["id"], parent, name)
            link = res.get("webViewLink", "")
            copied.append((name, link))
            stats["copied_total"] += 1
            if dest in ("diagrams", "individual_diagrams"):
                stats["copied_diagrams"] += 1
            manifest.add(list_name=card["list_name"], card_idshort=id_short,
                         card_name=card["name"], card_url=card["url"],
                         dest_folder_id=parent, source_file_id=f["id"],
                         source_file_name=name, copied_file_id=res.get("id", ""),
                         copied_file_url=link, status="copied")
        except BoundaryViolation:
            raise
        except Exception as e:
            stats["errors"] += 1
            manifest.add_error(id_short, name, e)
            manifest.add(list_name=card["list_name"], card_idshort=id_short,
                         card_name=card["name"], card_url=card["url"],
                         dest_folder_id=card_folder, source_file_id=f["id"],
                         source_file_name=name, status="error",
                         skip_reason=str(e)[:300])

    # 01 - Trello Record / card.md
    trello_dir, _ = drive.ensure_folder(card_folder, SUBFOLDER_TRELLO)
    drive.upload_text(trello_dir, "card.md", render_card_md(card, copied, skipped))

    if not copied:
        stats["cards_with_no_files"] += 1

    manifest.add(list_name=card["list_name"], card_idshort=id_short,
                 card_name=card["name"], card_url=card["url"],
                 dest_folder_id=card_folder, status="card_complete",
                 skip_reason="%d copied, %d skipped" % (len(copied), len(skipped)))
    return len(copied), len(skipped)


def _tally_skip(stats, reason):
    r = reason.lower()
    if "video" in r:
        stats["skipped_videos"] += 1
    elif "audio" in r:
        stats["skipped_audio"] += 1
    elif "archive" in r or "sql" in r:
        stats["skipped_archives"] += 1
    elif "oversize" in r:
        stats["skipped_oversized"] += 1
    elif "stub" in r:
        stats["skipped_stubs"] += 1
    elif "duplicate" in r:
        stats["skipped_duplicates"] += 1
    else:
        stats["skipped_other"] += 1


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def parse_list_filter(spec):
    """`04,05` -> the Trello list names those archive folders correspond to."""
    if not spec:
        return None
    want = {s.strip().lstrip("0") or "0" for s in spec.split(",")}
    return {t for t, (n, _i) in LIST_TO_FOLDER.items()
            if n.split(" - ")[0].lstrip("0") in want}


def build_queue(cards, want_lists=None, want_cards=None, skip_done=frozenset(),
                done_by_manifest=frozenset(), on_problem=None):
    """
    Select and order the cards to archive.

    Returns (queue, skipped_done). `on_problem(card, reason)` is called for
    cards that cannot be placed, so the caller can record them.
    """
    queue, skipped_done = [], 0
    for c in cards:
        if c["id_short"] is None:
            if on_problem:
                on_problem(c, "could not resolve idShort")
            continue
        if want_lists is not None and c["list_name"] not in want_lists:
            continue
        if want_cards is not None and c["id_short"] not in want_cards:
            continue
        if c["id_short"] in skip_done or c["id_short"] in done_by_manifest:
            skipped_done += 1
            continue
        if c["list_name"] not in LIST_TO_FOLDER:
            if on_problem:
                on_problem(c, "unknown list %r" % c["list_name"])
            continue
        queue.append(c)

    queue.sort(key=lambda c: (LIST_TO_FOLDER[c["list_name"]][0], c["id_short"]))
    return queue, skipped_done


def new_stats():
    keys = ("copied_total copied_diagrams cards_with_no_files skipped_videos "
            "skipped_audio skipped_archives skipped_oversized skipped_duplicates "
            "skipped_stubs skipped_other errors inaccessible_folders "
            "inaccessible_files already_copied already_present").split()
    return {k: 0 for k in keys}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--snapshot", help="Pre-pulled Trello JSON; skips Trello entirely")
    ap.add_argument("--lists", help="Comma-separated archive list numbers, e.g. 04,05")
    ap.add_argument("--cards", help="Comma-separated card idShorts to process")
    ap.add_argument("--limit", type=int, help="Stop after N cards (smoke test)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Classify and report without writing to Drive")
    ap.add_argument("--credentials", default="credentials.json")
    ap.add_argument("--token", default="token.json")
    ap.add_argument("--work-dir", default=".")
    ap.add_argument("--flush-every", type=int, default=10)
    ap.add_argument("--include-done", action="store_true",
                    help="Do not skip the cards recorded as already archived")
    args = ap.parse_args(argv)

    started = time.time()
    boundary = Boundary()
    stats = new_stats()

    # ---- Trello side ----------------------------------------------------
    if args.snapshot:
        cards = load_snapshot(args.snapshot)
        trello = None
        log("loaded %d cards from snapshot %s" % (len(cards), args.snapshot))
    else:
        key, token = os.environ.get("TRELLO_KEY"), os.environ.get("TRELLO_TOKEN")
        if not key or not token:
            raise SystemExit("Set TRELLO_KEY and TRELLO_TOKEN, or pass --snapshot")
        trello = TrelloReader(key, token)
        cards = []
        for lst in trello.lists():
            for raw in trello.cards(lst["id"]):
                cards.append(normalise_card(raw, lst["name"]))
        log("pulled %d cards from Trello across lists" % len(cards))

    lists_seen = sorted({c["list_name"] for c in cards})

    # ---- Drive side -----------------------------------------------------
    svc = build_drive(args.credentials, args.token)
    drive = Drive(svc, boundary, dry_run=args.dry_run)

    root = drive.get_file(ARCHIVE_ROOT)
    log("archive root: %s (owner %s)" % (
        root.get("name"),
        (root.get("owners") or [{}])[0].get("emailAddress", "?")))

    manifest = Manifest(drive, args.work_dir, flush_every=args.flush_every)
    manifest.load_local()
    from_drive = 0
    try:
        from_drive = manifest.load_from_drive()
    except Exception as e:
        log("no manifest read from Drive (%s)" % e)
    log("manifest: %d rows, %d cards already complete, %d files already copied"
        % (len(manifest.rows), len(manifest.completed_cards),
           len(manifest.copied_sources)))

    # ---- selection ------------------------------------------------------
    want_lists = parse_list_filter(args.lists)
    want_cards = None
    if args.cards:
        want_cards = {int(s) for s in args.cards.split(",") if s.strip()}

    queue, skipped_done = build_queue(
        cards,
        want_lists=want_lists,
        want_cards=want_cards,
        skip_done=frozenset() if args.include_done else frozenset(ALREADY_DONE),
        done_by_manifest=frozenset(manifest.completed_cards),
        on_problem=lambda c, why: manifest.add_error(
            c["id_short"] if c["id_short"] is not None else "?", c["name"], why),
    )
    if args.limit:
        queue = queue[: args.limit]
    log("queue: %d cards to archive, %d skipped as already done" % (len(queue), skipped_done))

    # ---- list folders ---------------------------------------------------
    list_folder_ids = {}
    for trello_name in sorted({c["list_name"] for c in queue}):
        folder_name, known_id = LIST_TO_FOLDER[trello_name]
        if known_id:
            boundary.trust(known_id, ARCHIVE_ROOT)
            list_folder_ids[trello_name] = known_id
            log("reusing list folder %s -> %s" % (folder_name, known_id))
        else:
            fid, created = drive.ensure_folder(ARCHIVE_ROOT, folder_name)
            list_folder_ids[trello_name] = fid
            log("%s list folder %s -> %s"
                % ("created" if created else "reusing", folder_name, fid))

    # ---- run ------------------------------------------------------------
    completed = 0
    for i, card in enumerate(queue, 1):
        tag = "#%s %s" % (card["id_short"], card["name"][:58])
        try:
            n_copy, n_skip = archive_card(
                drive, card, list_folder_ids[card["list_name"]], manifest, stats
            )
            completed += 1
            log("[%d/%d] %s  copied=%d skipped=%d" % (i, len(queue), tag, n_copy, n_skip))
        except BoundaryViolation as e:
            log("FATAL %s" % e)
            manifest.add_error(card["id_short"], "", e)
            manifest.flush()
            raise
        except Exception as e:
            stats["errors"] += 1
            manifest.add_error(card["id_short"], "", traceback.format_exc(limit=3))
            log("[%d/%d] %s  ERROR %s" % (i, len(queue), tag, e))
        if manifest.card_done(card["id_short"]):
            manifest.flush()
            log("    manifest flushed (%d rows)" % len(manifest.rows))

    manifest.flush()

    # ---- report (spec section 10) --------------------------------------
    elapsed = time.time() - started
    print("\n" + "=" * 74)
    print("TRELLO -> DRIVE ARCHIVE REPORT")
    print("=" * 74)
    print("board                       : %s" % BOARD_URL)
    print("archive root                : %s" % ARCHIVE_ROOT)
    print("mode                        : %s" % ("DRY RUN" if args.dry_run else "live"))
    print("lists discovered            : %d  (%s)" % (len(lists_seen), ", ".join(lists_seen)))
    print("cards discovered            : %d" % len(cards))
    print("cards queued                : %d" % len(queue))
    print("cards completed this run    : %d" % completed)
    print("cards skipped as already done: %d" % skipped_done)
    print("cards with zero files (card.md only): %d" % stats["cards_with_no_files"])
    print("-" * 74)
    print("files copied (total)        : %d" % stats["copied_total"])
    print("  of which diagrams         : %d" % stats["copied_diagrams"])
    print("files already present/copied: %d" % (stats["already_present"] + stats["already_copied"]))
    print("-" * 74)
    print("skipped videos              : %d" % stats["skipped_videos"])
    print("skipped audio               : %d" % stats["skipped_audio"])
    print("skipped archives/sql        : %d" % stats["skipped_archives"])
    print("skipped oversized           : %d" % stats["skipped_oversized"])
    print("skipped duplicates          : %d" % stats["skipped_duplicates"])
    print("skipped empty stubs         : %d" % stats["skipped_stubs"])
    print("skipped other (non-document): %d" % stats["skipped_other"])
    print("-" * 74)
    print("inaccessible folders        : %d" % stats["inaccessible_folders"])
    print("inaccessible files          : %d" % stats["inaccessible_files"])
    print("errors logged               : %d" % len(manifest.errors))
    for e in manifest.errors[:40]:
        print("   card %s | %s | %s" % (e["card"], e["file"], e["error"][:130]))
    if len(manifest.errors) > 40:
        print("   ... %d more in %s" % (len(manifest.errors) - 40, ERRORS_NAME))
    print("-" * 74)
    print("legacy folder flagged       : %s (%s) - left untouched"
          % (LEGACY_FOLDER_NAME, LEGACY_FOLDER_ID))
    if trello is None:
        print("Trello writes issued        : 0 (snapshot mode: no Trello calls at all)")
    else:
        print("Trello writes issued        : 0 (%d GETs; non-GET attempts: %d)"
              % (trello.calls, trello.writes_attempted))
    print("Drive: %d copies, %d folders created, %d list calls"
          % (drive.copies, drive.folders_created, drive.list_calls))
    print("every created object's parent chain terminates at %s : %s"
          % (ARCHIVE_ROOT,
             "asserted on every write (%d trusted folders)" % len(boundary.known_good)))
    print("manifest                    : %s (%d rows, %d loaded from Drive)"
          % (MANIFEST_NAME, len(manifest.rows), from_drive))
    print("elapsed                     : %.1f s (%.1f min)" % (elapsed, elapsed / 60.0))
    print("=" * 74)
    return 0


if __name__ == "__main__":
    sys.exit(main())
