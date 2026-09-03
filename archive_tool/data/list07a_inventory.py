"""
Real Drive inventory for the first List 07 (`On Hold`) batch: cards 6, 12,
14 and 16.

Card 6's folder holds only two subfolders; `Sales` is empty and `Engineering`
holds one proposal. Card 16's `Screenshots` holds five panel PDFs plus six
level-2 folders (one per panel) that the one-level recursion does not reach;
the PDFs are copied to sources rather than treated as imagery, because the
folder-name exclusion applies to images and these are documents.
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
PDF = "application/pdf"
MP4 = "video/mp4"

INVENTORY = {
    6: {
        "source_folders": ["14BDs1Q_lLp6bOBcA5hLH3FtADSn7zyO_"],
        "files": [
            ("1dWqxVtxYEMvE43e12B_zyeZGLzY5_lPJdHQT9Sin52g", "All-Inclusive Enterprise Resource Planning (ERP) - Project Proposal Document", DOC, 5914098, "Engineering"),
        ],
    },
    12: {
        "source_folders": ["1CWLrPhK8Hkc8U5W83_noZbA5QG6S9RvM"],
        "files": [
            ("1oR00zNPCrg_ku9uijPb_UorJ2kNg6wBd57VD99SehJY", "Jacksonville Housing Authority - Project Proposal Document", DOC, 5894938, ""),
            ("1IHgPOrlLlbdxnHSAwHE8EagT3bUlX5NKBQmHcF4SZF4", "Jacksonville Housing Authority - Project Proposal Document", DOC, 5885233, ""),
            ("1ZimfqIKIuUOErdCR0_bJefZD6y-XILPl", "MOBI-1435_2024_10_23_07_29_02_9jzFC_P2uR7_Q9yMM.pdf", PDF, 1611311, ""),
        ],
    },
    14: {
        "source_folders": ["1dUAFzvfxPx4ih2kQDeqkO3WsfAc2xh5r"],
        "files": [
            ("1Xd3SpC3RAPpxRYejScibcbysqB8bnliG_wjK8jOFxVc", "Schools Auditing System - Roadmap & Estimate", SHEET, 17877, ""),
            ("1p192C09EQ-Bu3rgsM64VB0D-09JXbNLG", "video1275900503.mp4", MP4, 59066406, ""),
            ("1NUXNMWvohCk2XFavFqd-1XYQZMaPgjgtp5eKBbp7eCw", "Requirement Document - Richard ", DOC, 6632, ""),
            ("1AkmbtGWilg2Nv5KOrSkI0nM3UNpRql7c", "video1589396719.mp4", MP4, 125893317, ""),
        ],
    },
    16: {
        "source_folders": ["12hAG_69qZFQG7hDYKGwgiyJzDOvPOr_H"],
        "files": [
            ("1DkNxc-EsmO3SW2TRfNvspyoBLU6NyQeRkfHPVhLwmE4", "Client Version - Cobana Portal | Web Application Development - Roadmap & Estimate", SHEET, 59766, ""),
            ("1QcgXj2UvL1ziCH-9yP7eUAXbX50S5nZtLElx74ZUDB8", "1. Cobana Portal | Web Application Development - Roadmap & Estimate", SHEET, 56730, ""),
            ("1-uMTQipnX1-O2pmnXv3wqnINWq3NcuDOyO3gTculSSE", "3. Cobana Portal - DevOps Plan", DOC, 16283, ""),
            ("1ABXpyT7abu0w-qzbJGYKdsPFsCQaCNsv", "2. Process Flow Diagram.pdf", PDF, 531841, ""),
            ("19O14ILiXk-4Zue-h8EUxyn0zAZ9NzL_i", "Cobana - Engineering .mp4", MP4, 41936999, ""),
            ("11hOHTAY8jygpprw4JOIf9SjctpJI0FLkogr1_UwQE7A", "Cobana Portal - Code Review Report", DOC, 28674, ""),
            ("1MOzs5O-_PYgU8vX-nT0PdMFGg6s768Ss", "video1705583398.mp4", MP4, 111781632, ""),
            ("1ZlvmvliVHesrFDKdCXudoYBIVJUFhOLE", "CRM workflow.pdf", PDF, 1910251, ""),
            ("1Lp44JLhEmCgOY2VMskGH05_nkH-NJaNo", "video1836188897.mp4", MP4, 640356151, ""),
            # subfolder: Discarded
            ("1SBuxwf-EF5hufr6j6VLETV6Z-6r1PdX-", "2. Process Flow Diagram.pdf", PDF, 524719, "Discarded"),
            # subfolder: Screenshots (its six per-panel folders are level 2)
            ("12KPtm1Pygadls6EC9DOszXM5QksVAO2p", "1. Lead Generator Panel.pdf", PDF, 482103, "Screenshots"),
            ("1oI4VK514QrRTz2wK2BgKC3Obk28GTefw", "2. Sales Closer Panel.pdf", PDF, 641077, "Screenshots"),
            ("1z4cCsa5U7dVNnC_UpBHbJ9a1SC3U4m56", "3. Field Agent Panel.pdf", PDF, 351940, "Screenshots"),
            ("1lWpkj5krfn7wNseAz4AXRfognLyi4XbW", "4. Pre Sales Agent Panel.pdf", PDF, 638751, "Screenshots"),
            ("1orkj5lMMkhWnGkqVIsO7JGw7qCUJZl8e", "5. Post Sales Agent Panel.pdf", PDF, 331781, "Screenshots"),
        ],
    },
}

EMPTY_FOLDERS = {6: [("1J0sZ8ibJaSK5zQnXN8RMAdRVimMFEoHt", "Sales")]}
