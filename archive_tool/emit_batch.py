#!/usr/bin/env python3
"""
Turn a completed connector batch into manifest rows and `card.md` files.

The Drive connector runs in this repo copy files one call at a time, so the
bookkeeping the orchestrator would normally do in-process has to be replayed
afterwards from three recorded inputs:

  data/<batch>_inventory.py     what was in the source folders
  data/<batch>_dest_folders.json  where each card's subfolders live
  data/<batch>_copy_ids.json    where each copy landed, in one of
                                {"by_card": {card: {source id: file id}}}
                                  (most precise: two cards can point at the
                                  same source folder, as 60 and 99 do)
                                {"by_source": {source id: file id}}
                                {dest folder id: {copied title: file id}}

It re-runs the shipped classifier over the inventory (so the manifest reflects
the same decisions the script would make), matches each planned copy to the
file that actually landed, and appends `copied` / `skipped` / `card_complete`
rows to data/archive-manifest.csv. Cards already in the manifest are left
alone, so re-running is safe.

    python3 emit_batch.py list05d
    python3 emit_batch.py list05d --check   # report, write nothing
"""

import argparse
import csv
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
sys.path.insert(0, HERE)
sys.path.insert(0, DATA)

import classify as C
from archive_trello_to_drive import (
    MANIFEST_COLUMNS, MANIFEST_NAME, load_snapshot, now_iso, render_card_md,
)
from plan_from_inventory import plan_for_card

GOOGLE_URL = {
    "application/vnd.google-apps.document": "document",
    "application/vnd.google-apps.spreadsheet": "spreadsheets",
    "application/vnd.google-apps.presentation": "presentation",
}


def view_url(file_id, mime):
    kind = GOOGLE_URL.get(mime)
    if kind:
        return "https://docs.google.com/%s/d/%s/edit" % (kind, file_id)
    return "https://drive.google.com/file/d/%s/view" % file_id


def load_inventory(batch):
    path = os.path.join(DATA, "%s_inventory.py" % batch)
    spec = importlib.util.spec_from_file_location("%s_inv" % batch, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.INVENTORY


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("batch", help="batch prefix, e.g. list05d")
    ap.add_argument("--check", action="store_true", help="report only")
    args = ap.parse_args()

    inventory = load_inventory(args.batch)
    with open(os.path.join(DATA, "%s_dest_folders.json" % args.batch)) as fh:
        dest = json.load(fh)["cards"]
    with open(os.path.join(DATA, "%s_copy_ids.json" % args.batch)) as fh:
        copy_ids = json.load(fh)
    # Source-id keyed is preferred; a title-keyed map cannot represent two
    # copies that share a name (card 41 has two `Updated MacOS Plugins.xlsx`).
    by_card = copy_ids.get("by_card", {})
    by_source = copy_ids.get("by_source", {})
    renamed = copy_ids.get("renamed", {})

    cards = {c["id_short"]: c for c in
             load_snapshot(os.path.join(DATA, "trello_snapshot.json"))}

    manifest_path = os.path.join(DATA, MANIFEST_NAME)
    with open(manifest_path, newline="") as fh:
        rows = list(csv.DictReader(fh))
    seen = {r["card_idshort"] for r in rows}

    added, results, unmatched = [], {}, []
    for cid, inv in sorted(inventory.items()):
        card = cards[int(cid)]
        folders = dest[str(cid)]
        if str(cid) in seen:
            print("SKIP %s: already in the manifest" % cid)
            continue

        mime_of = {f[0]: f[2] for f in inv["files"]}
        copies, skips = plan_for_card(card, inv)

        copied_md = []
        for c in copies:
            folder = folders.get("diagrams" if c["dest"] == "diagrams"
                                 else "sources")
            landed = (by_card.get(str(cid), {}).get(c["source_id"])
                      or by_source.get(c["source_id"])
                      or copy_ids.get(folder, {}).get(c["dest_name"]))
            if not landed:
                unmatched.append((cid, c["dest_name"]))
                continue
            url = view_url(landed, mime_of[c["source_id"]])
            landed_name = renamed.get(c["source_id"], c["dest_name"])
            # Keyed by card, not by source: two cards can archive the same
            # source file (60 and 99 share a Drive folder).
            results.setdefault(str(cid), {})[c["source_id"]] = landed
            copied_md.append((landed_name, url))
            added.append({
                "list_name": card["list_name"], "card_idshort": cid,
                "card_name": card["name"], "card_url": card["url"],
                "dest_folder_id": folder, "source_file_id": c["source_id"],
                "source_file_name": c["source_name"], "copied_file_id": landed,
                "skip_reason": ("renamed to %s for uniqueness" % landed_name
                                if c["source_id"] in renamed else ""),
                "copied_file_url": url, "status": "copied",
                "timestamp": now_iso(),
            })

        for name, reason, size in skips:
            added.append({
                "list_name": card["list_name"], "card_idshort": cid,
                "card_name": card["name"], "card_url": card["url"],
                "dest_folder_id": "", "source_file_id": "",
                "source_file_name": name, "copied_file_id": "",
                "copied_file_url": "", "status": "skipped",
                "skip_reason": reason, "timestamp": now_iso(),
            })

        added.append({
            "list_name": card["list_name"], "card_idshort": cid,
            "card_name": card["name"], "card_url": card["url"],
            "dest_folder_id": folders["card"], "source_file_id": "",
            "source_file_name": "", "copied_file_id": "",
            "copied_file_url": "", "status": "card_complete",
            "skip_reason": "%d copied, %d skipped" % (len(copied_md), len(skips)),
            "timestamp": now_iso(),
        })

        if not args.check:
            md = render_card_md(card, copied_md, skips)
            with open(os.path.join(DATA, "cardmd", "%s.md" % cid), "w") as fh:
                fh.write(md)
        print("%s: %d copied, %d skipped" % (cid, len(copied_md), len(skips)))

    if unmatched:
        print("\nUNMATCHED planned copies (no landed file of that name):")
        for cid, name in unmatched:
            print("  %s  %s" % (cid, name))

    if args.check:
        print("\n--check: nothing written (%d rows would be added)" % len(added))
        return

    with open(manifest_path, "a", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=MANIFEST_COLUMNS)
        for row in added:
            w.writerow(row)
    with open(os.path.join(DATA, "%s_copy_results.json" % args.batch), "w") as fh:
        json.dump(results, fh, indent=1, sort_keys=True)
    print("\nappended %d manifest rows; %d copies recorded"
          % (len(added), sum(len(v) for v in results.values())))


if __name__ == "__main__":
    main()
