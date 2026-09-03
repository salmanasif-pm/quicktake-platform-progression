#!/usr/bin/env python3
"""
Run the shipped classifier over a recorded Drive inventory and print the plan.

This mirrors `archive_card`'s decision order exactly (classify, then dedupe the
copy-worthy set) without touching Drive, so a plan can be reviewed before any
copy is issued, and re-checked afterwards.

    python3 plan_from_inventory.py            # print the plan
    python3 plan_from_inventory.py --json out.json
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))

import classify as C
from archive_trello_to_drive import normalise_card, render_card_md
from list04_inventory import INVENTORY

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
ORDER = [295, 448, 452, 447, 442, 119, 436, 116, 458]


def plan_for_card(card, inv):
    """Decide copies and skips for one card, in the orchestrator's order."""
    files = [{"id": i, "name": n, "mimeType": m, "size": str(s)}
             for i, n, m, s, _f in inv["files"]]
    folder_of = {i: f for i, n, m, s, f in inv["files"]}

    copies, skips = [], []

    # 1. classify, so a video is reported as a video and not as a duplicate
    copy_worthy = []
    for f in files:
        action, dest, reason = C.classify_file(f, folder_of.get(f["id"], ""))
        if action == "copy":
            copy_worthy.append((f, dest))
        else:
            skips.append((C.file_name(f), reason, C.file_size(f)))

    # 2. dedupe only what would be copied
    dest_of = {f["id"]: d for f, d in copy_worthy}
    kept, dropped = C.dedupe_files([f for f, _d in copy_worthy])
    for f, reason in dropped:
        skips.append((C.file_name(f), reason, C.file_size(f)))

    for f in kept:
        copies.append({
            "source_id": f["id"],
            "source_name": C.file_name(f),
            "dest_name": C.sanitise_name(C.file_name(f)),
            "dest": dest_of[f["id"]],
        })
    return copies, skips


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", help="write the plan to this path")
    args = ap.parse_args()

    with open(os.path.join(DATA, "trello_snapshot.json")) as fh:
        cards = {c["id_short"]: c for c in map(normalise_card, json.load(fh))}

    plan, n_copy, n_skip = {}, 0, 0
    for cid in ORDER:
        card, inv = cards[cid], INVENTORY[cid]
        copies, skips = plan_for_card(card, inv)
        n_copy += len(copies)
        n_skip += len(skips)
        plan[str(cid)] = {
            "card_folder": C.card_folder_name(cid, card["name"]),
            "card_url": card["url"],
            "list_name": card["list_name"],
            "copies": copies,
            "skips": [{"name": n, "reason": r, "size": s} for n, r, s in skips],
            "error": inv.get("error"),
            "card_md": render_card_md(
                card,
                [(c["dest_name"], "") for c in copies],
                skips,
            ),
        }

        print("\n=== %s -> %s" % (cid, plan[str(cid)]["card_folder"]))
        for c in copies:
            print("   COPY [%-20s] %s" % (c["dest"], c["dest_name"]))
        for n, r, _s in skips:
            print("   skip  %-62s <- %s" % (n[:62], r))
        if inv.get("error"):
            print("   ERROR %s: %s" % inv["error"])

    print("\nTOTAL: %d copies, %d skips across %d cards" % (n_copy, n_skip, len(plan)))
    print("cards with zero copies:",
          [k for k, v in plan.items() if not v["copies"]])
    by_dest = {}
    for v in plan.values():
        for c in v["copies"]:
            by_dest[c["dest"]] = by_dest.get(c["dest"], 0) + 1
    print("copies by destination:", by_dest)

    if args.json:
        with open(args.json, "w") as fh:
            json.dump(plan, fh, indent=1)
        print("plan written to", args.json)


if __name__ == "__main__":
    main()
