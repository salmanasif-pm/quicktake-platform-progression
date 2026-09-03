"""
Real Drive inventory for the last List 06 (`Closed Lost`) batch.

Cards 33, 69, 94, 106, 185 and 441 - the six with no Drive folder linked from
the card at all. Four have no Drive link of any kind and are a `card.md`
only; two link a single file directly:

* Card 69's is a Google Doc and is copied.
* Card 106's is a 446 MB meeting recording, which the spec skips.
"""

DOC = "application/vnd.google-apps.document"
MP4 = "video/mp4"

INVENTORY = {
    33: {"source_folders": [], "files": []},
    69: {
        "source_folders": [],
        "files": [
            ("1zDtHkoOIs4000ti1ExhtpvcXLIw-ZI7eNKy60rYDvIg", "Project Overview - Political Mapping ", DOC, 10477, ""),
        ],
    },
    94: {"source_folders": [], "files": []},
    106: {
        "source_folders": [],
        "files": [
            ("1pTNrJBlsN03efSeJQAUnqBld76gIlKHB", "Purelogics__Frasers Mathematics Solutions - Nov 17 2025.mp4", MP4, 445798149, ""),
        ],
    },
    185: {"source_folders": [], "files": []},
    441: {"source_folders": [], "files": []},
}
