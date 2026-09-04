# Trello → Google Drive archive tool

Completes the archive of the Trello board **PL Sales with Ahmed(AE)**
(`X9ZczKio`) into the Drive folder `1LSAK21sUzMpyaUrO7HgZ5OcL6KDrCyUu`, per
`TRELLO_ARCHIVE_CLAUDE_CODE_SPEC.md`.

## Status

| | |
|---|---|
| Cards on the board | 368 |
| Archived before this work | 32 |
| Archived by the runs in this repo | 129 (620 files copied, 65 diagrams) |
| **Remaining** | **207** — list 07 `On Hold` (12 of 219 done) |

**Lists 04, 05 and 06 are complete**: `Done, (Waiting on Decision)` at
19/19, `Closed Won` at 28/28 and `Closed Lost` at 80/80. `01 - BA Team
(Pending)` has 0 cards, so no folder is needed for it. Only `On Hold` (219
cards) remains, and it is under way: `data/list07_links.json` holds the
per-card Drive folder ids for all 219, so each batch can pick up where the
last stopped without re-reading the board.

The two lists have opposite shapes. `Closed Won` cards are live project
folders with PMO / BA / QA / Deliverables / Requirements subtrees, up to
twelve subfolders each — card 41 alone yielded 45 files and card 205
fifty-five. `Closed Lost` cards are mostly a roadmap, a requirements doc and
the sales-call recordings the spec skips; nineteen of the eighty resolve to a
`card.md` with no copied files at all, for reasons the inventories record
individually (nothing but recordings, a source folder that no longer exists,
a folder that exists and is genuinely empty, or no Drive link on the card).

Each batch's inventory file records what was walked and what was deliberately
not — recording archives, level-2 sprint folders, a personal Google Takeout
export; see `NOT_WALKED` and `SUBFOLDERS_TO_WALK` in
`data/list0*_inventory.py`.

### card.md is deferred by design

`card.md` is the spec's lowest-priority artifact (section 1) and the most
expensive thing to write through a tool call, since the content has to
round-trip. All 129 are rendered locally under `data/cardmd/`; run
`upload_cardmd.py` once on a machine with credentials to place them:

```bash
python3 upload_cardmd.py          # idempotent, seconds
```

Every other part of those 129 cards — folder tree, copied files, diagrams —
is already in Drive.

## Files

| file | what it is |
|---|---|
| `archive_trello_to_drive.py` | the resumable archiver: discovery, copying, manifest, report |
| `classify.py` | pure decision rules (spec §7) — no I/O, fully unit-tested |
| `test_classify.py` | 71 tests, no credentials or network needed |
| `plan_from_inventory.py` | runs the classifier over a recorded inventory and prints the plan, without touching Drive |
| `upload_cardmd.py` | uploads the pre-rendered `data/cardmd/*.md` into the archived cards; idempotent |
| `data/trello_snapshot.json` | all 368 cards, pulled read-only |
| `emit_batch.py` | replays a completed connector batch into manifest rows and `card.md` files |
| `data/archive-manifest.csv` | manifest for every card archived here + the 32 prior cards |
| `data/errors.csv` | inaccessible sources |
| `data/list0*_inventory.py` | the recorded Drive inventory per batch, with scope notes on what was and was not walked |
| `data/list0*_dest_folders.json` | destination folder ids per card |
| `data/list0*_copy_ids.json` | copied title -> landed file id, per destination folder |
| `data/list0*_copy_results.json` | source file id -> copied file id |
| `data/cardmd/*.md` | the `card.md` rendered for each archived card |

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

python3 -m unittest test_classify        # 71 tests
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

## Deliberate deviations from the spec

1. **`architecture` and `integration` are not diagram signals on PDFs.** §7
   lists them as diagram keywords for `.pdf` as well as images, but they are
   ordinary words in document titles — the real card-295 file
   `EduCommand AI Level 3 Beta Architecture Materials FINAL.pdf` is a document,
   not a diagram. On images they are still honoured (`Architecture.png` is a
   diagram); on paged formats a stronger signal is required (`diagram`,
   `workflow`, `flow`, `wireframe`, `system map`, …) or a diagram-ish containing
   folder. See `WEAK_DIAGRAM_KEYWORDS`.
2. **Some diagram signals only count on images.** `schema`, `mind map` and
   `mindmap` join `architecture` and `integration` in `WEAK_DIAGRAM_KEYWORDS`:
   a PNG called `Database Schema as of 19 August 2026` (real card-205 file) is
   an ER diagram, but `Database Schema Specification.pdf` is a spec. Diagram
   detection also falls back to the mime type when a title carries no
   extension, which Drive-hosted images often don't — that same card-205 PNG
   would otherwise have been dropped entirely.
3. **Folder names match by substring, not exactly.** §7 lists diagram folders
   by exact name. Real folders are `Architecture and data flux` (holds
   `BlockRock Architecture.pdf`), `User Flow Diagrams` and
   `System Workflow Diagrams`; exact matching missed all three. Exclusions
   match by substring too and are checked first, so
   `Prospect's System Screenshots` is still excluded despite containing
   "System". Folders are named far more deliberately than files, which is why
   substring matching is safe here but not on filenames.
4. **Slides are diagrams only when the name says "diagram".** §7 allows "slides
   that are clearly a diagram deliverable", and the workflow/flow keyword family
   would have swept in the real decks `MoneyMate | WorkFlow & Kickoff Document`
   and `247CAD - WorkFlow & Kickoff Document`, which are kickoff documents. For
   Slides the name now has to contain "diagram" (or the containing folder has to
   be diagram-ish).
5. **Files are classified before duplicates are suppressed.** §7 presents dedup
   first. Running it first makes a skipped video get reported as "duplicate of
   the copy of itself" instead of as a video, which distorts the §10 category
   totals. Dedup now applies only to the copy-worthy set; the net set of copied
   files is the same.

Every one of these is covered by tests in `test_classify.py`.

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
  Discovery for the remaining cards therefore relies on Drive links in card
  descriptions, which is where they are in practice. Run without `--snapshot`,
  with `TRELLO_KEY`/`TRELLO_TOKEN`, to pick up attachments too.
- Discovery recurses exactly one level into subfolders, as the spec specifies.
  Deliverables nested two levels down are not found. Two cards needed a
  judgement call against that rule, both recorded in
  `data/list05d_inventory.py`: card 424's diagram sets sit at level 2
  (`Latest Deliverables/User Flow Diagrams` and `.../System Workflow
  Diagrams`) and were walked anyway, since separating final diagrams is the
  spec's second priority — 11 PDFs; card 431's `DSU Meetings` holds 90+ dated
  subfolders of meeting recordings, all of which the spec skips, so they were
  deliberately left unwalked.
- `archive-manifest.csv` lives here in the repo; the control folder in Drive
  has `errors.csv` and `run-report-2026-09-03-list04.md`. The script uploads
  the full CSV to the control folder on its next run.
