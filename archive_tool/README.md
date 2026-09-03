# Trello → Google Drive archive tool

Completes the archive of the Trello board **PL Sales with Ahmed(AE)**
(`X9ZczKio`) into the Drive folder `1LSAK21sUzMpyaUrO7HgZ5OcL6KDrCyUu`, per
`TRELLO_ARCHIVE_CLAUDE_CODE_SPEC.md`.

## Status

| | |
|---|---|
| Cards on the board | 368 |
| Archived before this work | 32 |
| Archived by the runs in this repo | 15 (57 files copied, 2 diagrams) |
| **Remaining** | **321** — list 05 (22 of 28 left), list 06 (80), list 07 (219) |

List 04 `Done, (Waiting on Decision)` is complete at 19/19. List 05
`Closed Won` has 6 of 28 done (cards 17, 24, 49, 104, 168, 203) — the six whose
linked folder has no subfolders, so a single listing was complete discovery.
`01 - BA Team (Pending)` has 0 cards, so no folder is needed for it.

The 22 List 05 cards still open are live project folders with PMO / BA / QA /
Deliverables / Requirements subfolders; `data/list05_inventory.py` records which
ones need the script's one-level recursion, and how many subfolders each has, so
that work does not have to be rediscovered.

## Files

| file | what it is |
|---|---|
| `archive_trello_to_drive.py` | the resumable archiver: discovery, copying, manifest, report |
| `classify.py` | pure decision rules (spec §7) — no I/O, fully unit-tested |
| `test_classify.py` | 65 tests, no credentials or network needed |
| `plan_from_inventory.py` | runs the classifier over a recorded inventory and prints the plan, without touching Drive |
| `data/trello_snapshot.json` | all 368 cards, pulled read-only |
| `data/archive-manifest.csv` | manifest for the List 04 run + the 32 prior cards |
| `data/errors.csv` | inaccessible sources |
| `data/list04_*` | the recorded inventory, plan, destination folder ids and copy results for the completed run |
| `data/cardmd/*.md` | the `card.md` written for each List 04 card |

## Running it

```bash
pip install google-api-python-client google-auth-oauthlib requests

# Google: OAuth desktop client, authorised as the archive root's owner
#   (salman.asif@purelogics.net). A service account will NOT work — several
#   source folders belong to other people and are not shared with it.
#   Put the client secret at ./credentials.json; a token.json is cached.

# Trello (only needed without --snapshot): read-only key + token
export TRELLO_KEY=...  TRELLO_TOKEN=...

cd archive_tool

# see what it would do, no writes at all
python3 archive_trello_to_drive.py --snapshot data/trello_snapshot.json \
    --work-dir data --dry-run

# finish the archive
python3 archive_trello_to_drive.py --snapshot data/trello_snapshot.json \
    --work-dir data

# or one list / a few cards at a time
python3 archive_trello_to_drive.py --snapshot data/trello_snapshot.json \
    --work-dir data --lists 05
python3 archive_trello_to_drive.py --snapshot data/trello_snapshot.json \
    --work-dir data --cards 295,452 --limit 2

python3 -m unittest test_classify        # 65 tests
```

`--snapshot` replays the committed board pull and needs no Trello access at
all. Omit it to read the board live; either way Trello is read-only —
`TrelloReader.request` raises on any verb other than GET, and every call goes
through `requests.get`.

## Safety properties

- **Write boundary.** `Boundary.assert_in_boundary` runs immediately before
  every folder create, file copy and text upload. Its trusted set starts as
  `{archive root, control folder}` and grows only via `Boundary.trust(child,
  parent)`, which itself asserts the parent is already trusted — so the trusted
  set cannot escape the root by construction. A violation raises and aborts the
  run after flushing the manifest.
- **Originals are never touched.** Transfers use `files.copy` only. There is no
  `files.update` call that changes `parents` (which would *move* the original);
  the one `files.update` is a content-only rewrite of a `card.md` the tool
  itself wrote inside the boundary.
- **No Trello writes.** Enforced in code, and reported as such.

## Resumability

Three independent layers, so an interrupted run neither redoes work nor
duplicates it:

1. The 32 cards from earlier runs are hardcoded in `ALREADY_DONE` and matched on
   `idShort` (not list, so a card that has since moved is still skipped).
2. The manifest is read first — from `--work-dir` and from the control folder in
   Drive — and any card with a `card_complete` row, or file with a `copied` row,
   is skipped. It is flushed every `--flush-every` cards (default 10).
3. Drive itself is reconciled: folders are reused by name via `files.list`
   before being created, and a file already present in the destination by name
   is recorded as `already present` rather than copied again. This is what makes
   the tool safe to run over the List 04 cards that were archived through a
   different path.

## Two deliberate deviations from the spec

1. **`architecture` and `integration` are not diagram signals on PDFs.** §7
   lists them as diagram keywords for `.pdf` as well as images, but they are
   ordinary words in document titles — the real card-295 file
   `EduCommand AI Level 3 Beta Architecture Materials FINAL.pdf` is a document,
   not a diagram. On images they are still honoured (`Architecture.png` is a
   diagram); on paged formats a stronger signal is required (`diagram`,
   `workflow`, `flow`, `wireframe`, `system map`, …) or a diagram-ish containing
   folder. See `WEAK_DIAGRAM_KEYWORDS`.
2. **Files are classified before duplicates are suppressed.** §7 presents dedup
   first. Running it first makes a skipped video get reported as "duplicate of
   the copy of itself" instead of as a video, which distorts the §10 category
   totals. Dedup now applies only to the copy-worthy set; the net set of copied
   files is the same.

Both are covered by tests.

## Things found that the spec got wrong

- **Card 452 (Seaver Construction)** was expected to have no Drive links. It
  links folder `11zbFhO5DOk3rjxY4EBbOB_oH4vBiQcwc`, holding a roadmap sheet
  (copied) and a 159 MB mp4 (skipped).
- **Card 458 (Shoreline Credit Union)** is the real card.md-only case: its
  folder `1Z7cT9Gkc9xjcR546q7NXGallISTAnHb2` returns *Requested entity was not
  found*. Worth restoring — the card asks for a roadmap, a user flow diagram and
  an architecture diagram.
- **Card 414 (Heart ID)** has moved from `BA Team (In Progress)` to
  `HOE | Ahmed's Review`. Its archived copy stays under
  `02 - BA Team (In Progress)`; it is skipped on `idShort` so it is not
  duplicated.
- Two lists therefore differ from the spec's per-list counts by ±1 (02 has 1,
  03 has 3); the total of 368 is unchanged.

## A Drive query trap worth knowing

Listing several parents at once with `parentId = 'a' or parentId = 'b'` is not
safe: if **any one** parent in the disjunction is inaccessible, the whole query
comes back as an empty result rather than an error, silently hiding the children
of the parents that *were* readable. This was hit twice (cards 458 and 104, both
of whose folders are gone). Folders must therefore be listed one parent per
query, which is what the script does — `Drive.list_children` takes a single
folder id and records a per-folder error on failure.

## Known limitations

- The Trello MCP snapshot carries no card **attachments** (the REST API does).
  Discovery for the 327 remaining cards therefore relies on Drive links in card
  descriptions, which is where they are in practice. Run without `--snapshot`,
  with `TRELLO_KEY`/`TRELLO_TOKEN`, to pick up attachments too.
- Discovery recurses exactly one level into subfolders, as the spec specifies.
  Deliverables nested two levels down are not found.
- `archive-manifest.csv` for the List 04 run lives here in the repo; the control
  folder in Drive has `errors.csv` and
  `run-report-2026-09-03-list04.md`. The script uploads the full CSV to the
  control folder on its next run.
