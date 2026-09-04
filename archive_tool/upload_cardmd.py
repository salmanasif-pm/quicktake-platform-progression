#!/usr/bin/env python3
"""
Upload the pre-generated `card.md` files into the cards already archived.

Cards archived through the Drive connector in this repo have their folder tree
and copied files in place, and their `card.md` rendered locally under
`data/cardmd/`. Writing those into Drive is the one part that was deferred,
because `card.md` is the spec's lowest-priority artifact (section 1) and the
content had to round-trip through a tool call.

This script does that in one pass, in seconds, and is idempotent: it creates
`01 - Trello Record` only if missing, and skips a card whose `card.md` is
already there unless --force is given.

    python3 upload_cardmd.py              # upload everything missing
    python3 upload_cardmd.py --dry-run
    python3 upload_cardmd.py --force      # overwrite existing card.md
"""

import argparse
import glob
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import classify as C
from archive_trello_to_drive import (
    ARCHIVE_ROOT, SUBFOLDER_TRELLO, Boundary, Drive, build_drive,
)

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

# Destination folder maps written by the connector runs, newest last.
DEST_MAPS = ["list04_dest_folders.json", "list05_dest_folders.json",
             "list05c_dest_folders.json", "list05d_dest_folders.json",
             "list05e_dest_folders.json", "list06a_dest_folders.json",
             "list06b_dest_folders.json", "list06c_dest_folders.json", "list06d_dest_folders.json", "list06e_dest_folders.json", "list07a_dest_folders.json", "list07b_dest_folders.json", "list07c_dest_folders.json", "list07d_dest_folders.json", "list07e_dest_folders.json", "list07f_dest_folders.json", "list07g_dest_folders.json", "list07h_dest_folders.json"]


def load_dest_map():
    import json
    cards = {}
    for name in DEST_MAPS:
        path = os.path.join(DATA, name)
        if not os.path.exists(path):
            continue
        with open(path) as fh:
            cards.update(json.load(fh).get("cards", {}))
    return cards


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--credentials", default="credentials.json")
    ap.add_argument("--token", default="token.json")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="overwrite a card.md that is already in Drive")
    args = ap.parse_args()

    dest = load_dest_map()
    md_files = sorted(glob.glob(os.path.join(DATA, "cardmd", "*.md")))
    if not md_files:
        raise SystemExit("no card.md files under data/cardmd/")

    svc = build_drive(args.credentials, args.token)
    boundary = Boundary()
    drive = Drive(svc, boundary, dry_run=args.dry_run)

    # Trust each archived card folder: it is a known child of the archive root.
    for entry in dest.values():
        if entry.get("card"):
            boundary.known_good.add(entry["card"])
            if entry.get("trello"):
                boundary.known_good.add(entry["trello"])

    uploaded = skipped = missing = 0
    for path in md_files:
        cid = os.path.splitext(os.path.basename(path))[0]
        entry = dest.get(cid)
        if not entry or not entry.get("card"):
            print("SKIP %s: no destination folder recorded" % cid)
            missing += 1
            continue

        trello_dir = entry.get("trello")
        if not trello_dir:
            trello_dir, created = drive.ensure_folder(entry["card"],
                                                      SUBFOLDER_TRELLO)
            if created:
                print("created %s under card %s" % (SUBFOLDER_TRELLO, cid))
        else:
            boundary.known_good.add(trello_dir)

        if not args.force:
            existing = drive.find_child(trello_dir, "card.md")
            if existing:
                print("SKIP %s: card.md already present" % cid)
                skipped += 1
                continue

        with open(path) as fh:
            text = fh.read()
        res = drive.upload_text(trello_dir, "card.md", text)
        print("uploaded %s -> %s (%d bytes)" % (cid, res.get("id", "dry-run"),
                                                len(text)))
        uploaded += 1

    print("\nuploaded %d, skipped %d already present, %d without a destination"
          % (uploaded, skipped, missing))
    print("every write asserted a parent inside %s" % ARCHIVE_ROOT)


if __name__ == "__main__":
    main()
