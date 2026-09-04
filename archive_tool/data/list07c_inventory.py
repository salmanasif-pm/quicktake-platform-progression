"""
Real Drive inventory for List 07 (`On Hold`) batch 07c.

Twenty cards with a linked Drive folder (43, 44, 51, 52, 54, 55, 57, 61, 62,
67, 71, 77, 78, 79, 80, 84, 86, 87, 88, 95) plus the twelve cards whose
descriptions carry no Drive link at all (9, 30, 50, 70, 73, 93, 140, 227,
228, 229, 231, 232), which are a `card.md` only.

Four reasons a card here copies nothing, recorded separately:

  DEAD_FOLDERS   cards 86, 87 and 95 - `get_file_metadata` on the linked
                 folder answers "Requested entity was not found", so the
                 folder was deleted or its sharing was revoked.
  EMPTY_FOLDERS  cards 55 and 80 - the folder still resolves and is readable,
                 it simply holds nothing.
  recordings     cards 43, 51, 52, 54, 57, 61, 78 and 88 hold only sales-call
                 recordings (and, on 57, one screenshot), which the spec skips.
  no Drive link  the twelve cards listed above.

Card 71 is the outlier: two linked folders, one of them the client's own
`app design` / `harmoni foundation` / `airtable base to export to glide app`
trees. Their level-1 files are inventoried here; the ten level-2 folders
under `airtable base` and the three under `app design` are out of the
one-level recursion and recorded in SUBFOLDERS_TO_WALK. The `harmoni`
subfolder under the second linked folder re-parents those same three trees a
level deeper, so its children are level 2 and duplicate what is already
walked - NOT_WALKED records that.

Card 44's `Mindmap.pdf` is deliberately NOT a diagram: `mindmap` is an
image-only keyword, so a paged PDF with it in the title stays a source
document. Card 71's `Harmoni Prototype Flow.pdf` and `Wireframe .pdf` are
diagrams (`flow`, `wireframe` are strong keywords).
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
PDF = "application/pdf"
MP4 = "video/mp4"
CSV = "text/csv"
PNG = "image/png"
ZIP = "application/x-zip-compressed"
PAGES = "application/x-iwork-pages-sffpages"
NUMBERS = "application/x-iwork-numbers-sffnumbers"

GONE = "Requested entity was not found (deleted or access revoked)"

INVENTORY = {
    9: {"source_folders": [], "files": []},
    30: {"source_folders": [], "files": []},
    43: {
        "source_folders": ["1RnUiJkCBOTu30bDqDDlX0NMoz3fDb0Nf"],
        "files": [
            ("1LJsWuNa1KmCXLxVI2o1k0tNPv0RuMG4M", "Copy of video1013002558.mp4", MP4, 39716405, ""),
        ],
    },
    44: {
        "source_folders": ["1WWbeO2VgUl1qnL-ec04F88WQ7D-6nUlV"],
        "files": [
            ("1BVsnn56f6Zt4GExQh-BWQ2EtLV0RZma1", "Solution Comparison Chart.pdf", PDF, 87794, ""),
            ("1_ooSVPWLQnq1slZliuRd2zX3bSQUOWTghwMD2x6rVao", "AI ChatBot Development - Roadmap & Estimate", SHEET, 18767, ""),
            ("1wrBTt7vLj2-mHCgQaOMLNuSfO9Gr-97J", "video1835655309.mp4", MP4, 77941510, ""),
            ("14xz1msXqZCNVt2Lz1JhuOOhT-bd8UHpj", "Mindmap.pdf", PDF, 74920, ""),
            ("1UB-30FbCdGwe2E2GPd2ioqidRrmKvyDu", "AI Chatbots - Todd and Siana.mp4", MP4, 178671321, ""),
            ("1NglO-n5PXnLef7I3K_GaEp1Qoo5TlLexffier5YrP3Y", "ChatBot Requirement", DOC, 4394, ""),
        ],
    },
    50: {"source_folders": [], "files": []},
    51: {
        "source_folders": ["1k5wzXMDf6JFkOt2ge4csa9DxxAnmxCX7"],
        "files": [
            ("1X6BtQNj_52ZShEynyzZqd3N3fqXPuLNG", "Injury Map Application Overview.mp4", MP4, 82505390, ""),
            ("1n1YeTWyE0abdfdvYIqyt3408YVntrSSn", "Engineering - Nick - HealthCare.mp4", MP4, 371592697, ""),
        ],
    },
    52: {
        "source_folders": ["1nepjfbIPjmJtJU3fhxm6VnvSAYhMIYyR"],
        "files": [
            ("11LNOeKjqJjmLHx5UtmJa4EhvAlkVzmqy", "Ron - MVP Engineering .mp4", MP4, 135490263, ""),
            ("19T1rNzV7CUczM21xoRlAsXURzos4G-pD", "Ron - Engineering .mp4", MP4, 15661780, ""),
            ("1T-xes0mJ43DPUG0mXVoaUfTNJN3fNhVS", "Ron - Engineering.mp4", MP4, 119552459, ""),
        ],
    },
    54: {
        "source_folders": ["12Y1qMiz5kaHblZmQxwzkP2ekEufc8CxB"],
        "files": [
            ("1LaXlSgs6FWCzYASWD4ijUXL9BlsPOBrC", "Bayo - VR Scope .mp4", MP4, 20247976, ""),
            ("1FEYcI9Mqm_C1rfnzaX1_Gi_Bz3NmjmRu", "Bayo - Engineering .mp4", MP4, 65909125, ""),
            ("14JkMFHkTsEcf8IGWNH_2oep4Q32ydCzU", "video1656400657.mp4", MP4, 94503378, ""),
        ],
    },
    55: {"source_folders": ["1XHuFIUXdw1Pn1Uw1npKiAJKbRCCfwh8l"], "files": []},
    57: {
        "source_folders": ["1U51t8lbvMEWL_qcETw-pQU_9A8zxpxBa"],
        "files": [
            ("1VPY5XI3vc9iZq0Q6R8CK6C_t8PD5A_mx", "Canvas_Education.png", PNG, 139205, ""),
            ("13M0AoqZysLzDtgU53fd45TZtUFGxngcE", "video1107208729.mp4", MP4, 120533423, ""),
            ("1tWy6j5nDmEgzA3xh8uxosBxpKMwEhLwN", "Justin - Engineering .mp4", MP4, 84365456, ""),
        ],
    },
    61: {
        "source_folders": ["1vxbd9aiX0QxUv0GrafCPYd0ia51Zus-b"],
        "files": [
            ("1MqM45h5W--bCugTzLeW5YnYvqOkK-9nh", "ERGONN's LLC X PureLogics  - Jun 25 2025.mp4", MP4, 108534484, ""),
        ],
    },
    62: {
        "source_folders": ["15BxFROb96WGTVNQNm6e9I-N98u3WYGb3"],
        "files": [
            ("1j3-UxMEwTv337Ogd6pWerH2ynBFrr86iu6-WdwuMw4k", "Technical Requirements Document - Femcare App ", DOC, 7142, ""),
        ],
    },
    67: {
        "source_folders": ["1sKNaB2ZmYOfVCsedD03LgEshzmSAHJ-r"],
        "files": [
            ("12vG1lCChFZiG8QOKXZ8VwYlwD9fpP3YT", "David Schatzkamer - Jul 3 2025.mp4", MP4, 48889485, ""),
            ("1KlF-u_W7pbh-LVHGmn6X4aRgVS4WHHcGQkj8-K_RkG8", "Therapist Patient Mobile Application - Feature Breakdown", DOC, 9622, ""),
        ],
    },
    70: {"source_folders": [], "files": []},
    71: {
        "source_folders": ["1nkwqr0Zfg9INJXNFtN8vDVQCCWqgzFt1",
                           "1iar6Yz5-Tk-2rwT7JFxU0lyFGWYD1URl"],
        "files": [
            ("1EPfKbLs8Xegkg_K0ufoXHnbl2ZFYqQ-FA84tHSqJ1qE", "Caregiver Application Development - Solution ", DOC, 1490195, ""),
            ("1RH6XwoWZ36B1ic39TFdr-jfCVys-rN1oWMtFARcfPIg", "Caregiver Application Development - Solution Document", DOC, 1491853, ""),
            ("1RRHH5UZBy09rWHqFDWQoENmp0vYNB4BG", "harmoni -20250721T131312Z-1-001.zip", ZIP, 36160642, ""),
            # subfolder: app design
            ("1s2KIITIsNYAyYzXUqYIwIsuZpbtz1Yw3", "Harmoni Prototype Flow.pdf", PDF, 58243, "app design"),
            ("1cGXBu9cVu7cewuimC58n3uC5HRzRupST", "Harmoni Prototype Layout.pdf", PDF, 19048, "app design"),
            ("1Kp4enU5MIJxxc18tq_Oe0eu3EvzB29JG", "Screen asset tracker .numbers", NUMBERS, 217073, "app design"),
            ("1GOS7Z4-jS2Y0blYzXqnb9ibFHqmdvaQg", "ui flow w: voice + emotional intelligence layer .pages", PAGES, 202341, "app design"),
            ("13jbuXkRj5O7vFguo0m2AuZ2tR1HZgWhm", "harmoni_success_error_icons.png", PNG, 2303, "app design"),
            ("1TZYp3KTWvYIteU-bReR9twKeU0t-sirG", "harmoni_ambient_background_tile.png", PNG, 85622, "app design"),
            ("1cNUl0u1Z2Gn12-K8inOspU_kENtssn4V", "harmoni_voice_style_selector_mockup.png", PNG, 15465, "app design"),
            ("12JKZinin1MuPQ4C1p4yfYUIA8JuVA4uA", "harmoni_welcome_screen_mockup.png", PNG, 14638, "app design"),
            ("1HpMRsKOKTGEZ6a7rVtCYrZdSxxmYjel1", "harmoni_calendar_sync_mockup.png", PNG, 15641, "app design"),
            ("1En8AtaEtccabz6GLAX1xAfkB-1HYllFi", "harmoni_harmony_mode_mockup.png", PNG, 16519, "app design"),
            ("193UFsnpt2FcWRATH8Uut-UH0ZR05wXjU", "harmoni_daily_snapshot_mockup_fixed.png", PNG, 16639, "app design"),
            ("1JFvd-rCJFiyiSYgzrGHTRsmRjiRBC4Ki", "harmoni_section_headers.png", PNG, 12845, "app design"),
            ("1KcpkRgIW3PdAMm-E7gwqzN_R3aOw2XrL", "harmoni_weekly_dashboard_mockup_fixed.png", PNG, 16367, "app design"),
            ("12XPzf6Ptlu_BG3QTX9IzDrHSiJ7fhYh8", "harmoni_priority_meal_cards.png", PNG, 17778, "app design"),
            ("1jthgqTEG9vl0Gdl31ZfbkuVRP_jflt8f", "harmoni_goal_selection_mockup_fixed.png", PNG, 15941, "app design"),
            ("1-Cgnnm86bWSYMI4SubDQz1u6x4zytQPt", "harmoni_navigation_bar.png", PNG, 9004, "app design"),
            ("10uZRIxOKbXoRuCP67dUpqCUH8RPoas1_", "harmoni_mood_support_popup_mockup.png", PNG, 15891, "app design"),
            ("1RtLdbxrIzFbfX5Ps9vCotybzgHOyxNIy", "welcome screen .png", PNG, 2187662, "app design"),
            ("1jENRk8YQaJveMpn9ES2wxrUIdGTrCQgX", "household size .png", PNG, 2287184, "app design"),
            ("14r2FT9sf7dfN52ra1vchp4rA7NUF7sfH", "Settings .png", PNG, 2178958, "app design"),
            ("1gT9A-TXq7Rtgb_a8vri6OGBVXDjFj5f-", "voice tone and visual vibe .png", PNG, 2461565, "app design"),
            ("19RZx8APemgkeWYxgtpH4njcgRLt9ZWiP", "weekly dashboard.png", PNG, 2202045, "app design"),
            ("1DJwbbsny2d_QOjIXDx53vwOAksVnnQE3", "prioritize.png", PNG, 2187299, "app design"),
            ("1inBLt8p02NIaYkxCYh9tZY7Uc6mN9S-b", "harmoni mode screen.png", PNG, 2296706, "app design"),
            ("1I0yo0Mg-2PMQWQI5ho8f8C4UsaD4qw7U", "preferences .png", PNG, 1676155, "app design"),
            ("1AWl3wiFO6Gz5NTHjiw1Mq_JAPy4XYXgs", "how are you feeling.png", PNG, 1967381, "app design"),
            ("10Cx_1lzCdeaTzDqR_taL7bzQSXOrp4_k", "name screen .png", PNG, 1125750, "app design"),
            ("1Q9hzs_zqquXzvMw0ybZ7lkvj39kDiF6C", "welcome screen.png", PNG, 2198589, "app design"),
            ("1JTUvAI1lEdCDg7sDRm4yD4sfMAdmd0MV", "primary intention 2.png", PNG, 1585101, "app design"),
            ("1f3vM3pz_NiSKTlUovKGnUN20cz-EGNvw", "step 4- primary intention .png", PNG, 1892609, "app design"),
            # subfolder: harmoni foundation
            ("1gSF5mCkQ2f21-7fHASpjzJBintNq-HcS", "Harmoni Prototype Flow.pdf", PDF, 58243, "harmoni foundation "),
            ("1LoSRfVkOFwps4VBKOo_9_N0uHtlRDQkZ", "Harmoni .pdf", PDF, 77968, "harmoni foundation "),
            ("1P4bJ9mXzCo-xtg6T9uqSZ6jiwMjgNt_V", "prototype.pdf", PDF, 179952, "harmoni foundation "),
            ("1mhyzSRGGHH1pkYR1QUgbsAdb-dWeEot4", "Wireframe .pdf", PDF, 86850, "harmoni foundation "),
            ("1XOVeEXlEETxXa4R-hyuGrTNcu8KSZ7Bo", "Wireframe .pdf", PDF, 86850, "harmoni foundation "),
            ("1vgTMHEVQdo2mAWeIZabwmXBo1K4tNEzF", "prototype layout .png", PNG, 1855443, "harmoni foundation "),
            ("1Ay2up7nb4Zo74UFPLpZwGSeL0y7ULsTp", "ui flow w: voice + emotional intelligence layer .pages", PAGES, 202341, "harmoni foundation "),
            ("1ijfFutBW-ydfIrHYRRI1zBK1R2V-ZIlU", "Harmoni .pages", PAGES, 211294, "harmoni foundation "),
            ("12nH1a2guB97EUeGvrt2I7QDQmDt3J_hR", "Harmoni landing page.pages", PAGES, 165998, "harmoni foundation "),
            ("1no6UIxGEEcb1P3YnnGm7ohUGcvJAq7v7", "Product roadmap .pages", PAGES, 240864, "harmoni foundation "),
            ("1ufFkJIbywNezYRlPeG_S5YQxrgvK3LS0", "Wireframe .pages", PAGES, 197974, "harmoni foundation "),
            ("1E1o_TzTptfPOeeulD7vYoKzsYOkevLjQ", "prototype.pages", PAGES, 295443, "harmoni foundation "),
            # subfolder: airtable base to export to glide app
            ("1YyVu7qCytSNwo3L9dvfYhYt4ITiyaoue", "Product roadmap .pdf", PDF, 80884, "airtable base to export to glide app"),
            ("1voF8MFxfL2wC6BaoSdLabtekl1aASX9z", "Harmoni_Migration_Checklist_ASCII copy.pdf", PDF, 27225, "airtable base to export to glide app"),
            ("1yJ0wiDDvTP_0lGyj6fGklUzCfznhRa5K", "Harmoni_Migration_Checklist_ASCII.pdf", PDF, 2341, "airtable base to export to glide app"),
            ("1dBhE69wcsrvUlAXDNrasO0PZa16KRUNm", "tasks-Todays View .csv", CSV, 173, "airtable base to export to glide app"),
            ("1Nyygwk5HtDO47gNJy7WsovSKJxfImpe8", "Delegation-Grid view.csv", CSV, 39, "airtable base to export to glide app"),
            ("1GAbYuE8iFBEio1ubZKV0_AHUpJ3FdPpA", "cycle sync-Grid view.csv", CSV, 94, "airtable base to export to glide app"),
            ("1JfigbQMlxTMmpPnK_ldfUkhmkVkAUH5o", "Routines-Grid view.csv", CSV, 73, "airtable base to export to glide app"),
            ("1lEsirW-M4m40D5qFmF3tOwQ_NTYbTpzC", "Self care-Grid view.csv", CSV, 121, "airtable base to export to glide app"),
            ("1o5H-SwerUnLOsrkJsv7WtRWkj6Yo2IaQ", "Meal Planning-Grid view.csv", CSV, 334, "airtable base to export to glide app"),
            ("1yec7mFZdfdmzZBV4kQW4lAkA5J0V5ei4", "Ai-suggestions-Grid view.csv", CSV, 54, "airtable base to export to glide app"),
        ],
    },
    73: {"source_folders": [], "files": []},
    77: {
        "source_folders": ["1tcC5fKf5fR6SRjT4xJZOmhWmRMc3RR3T"],
        "files": [
            ("1vx6YqgeKVJzLjtlgeYyZcdXARBuNwe0b", "Otegrity - Aug 13 2025.mp4", MP4, 142083112, ""),
            ("1DgwYOJnwzh6aGqSgB1R1bpaIlkMyd3JhUc27tiogFbQ", "Requirements - Otegrity", DOC, 6262, ""),
        ],
    },
    78: {
        "source_folders": ["1mudROGRDUsg2qO9FhWyusUq6cqvo1HvN"],
        "files": [
            ("1InwLsHCnyyqUiOOmmvtETGFWGtl00d3Z", "John Browning - Guardian Rock Wealth ", MP4, 634927937, ""),
        ],
    },
    79: {
        "source_folders": ["1rZEj5XMlPniI1GASROkVlt9F0BrOdfH2"],
        "files": [
            ("1RdtvGQqENe-llQObPmwrZdUrjNEIYOF0", "14th October - Danny <> PM Meeting ", MP4, 225858017, ""),
            ("1D5LV5KLwV353knCZWqoGrt7S1f-6EaXk", "PureLogics Final FVI Scope - Aug 26 2025.mp4", MP4, 270094097, ""),
            ("16sfPEjMcsMdRLIjGBExMWNoN1-qgh-OlgGMoN3fnU3A", "Canvas Diagram and Description", DOC, 312748, ""),
            ("1hEfpllov5XQMV8mvRz6tGYjSCylXAyEmOyDZOSKSCqc", "MoMs", DOC, 44526, ""),
            ("19uV5C5ErCBrxCvjA5s24WO4ZKF1hLZlg", "Meeting - 12th Aug 2025.mp4", MP4, 39728168, ""),
            ("1RUOpsyBdwiTd6xnx-BvB4pk4QauJzitT_g0jmys4TlE", "Read Me", DOC, 1024, ""),
            ("1YQnL3OVHlvWMbe7TBW0qBubLNoTadfqbf2ghaPJkU8A", "MVP - 3os ", DOC, 5441, ""),
            ("1cKYTmbDu6P4PBEQK8U3kvaoc3TBlW_vz_ANnFCAdS7g", "Link to Recording", DOC, 1024, ""),
            ("1b2BQ0Os5EJmSK1aYzTrOkQwzWPwsHoIIy6ImP0UOQ3w", "MVP - 3os ", DOC, 5441, ""),
            ("1QeWBNcefjcMUifujq2rZ8fbmKmroGsfytwqnAW-iib0", "\U0001f527 Engineering Requirements Document (Quote‑Ready)", DOC, 8566, ""),
            ("1RcDXfOk-jaQ3vBGIrPD8qkM6QH2oBZ7m", "video1119362356.mp4", MP4, 160603827, ""),
        ],
    },
    80: {"source_folders": ["1swhK9jk7Tj9QsQpulrmWGZ8J2wp69T9K"], "files": []},
    84: {
        "source_folders": ["1HNr8qRRe6OARblc7j6YeZ9UirIJC4aWn"],
        "files": [
            ("10pdufaAdH1OQtvYF1kOSv-FRQbZOZW-z", "David - Sep 19 2025 - Engineering.mp4", MP4, 63920446, ""),
            ("1dzC0eLVcHATFcCzsZEnHjXphjWitgTx5KmtdgMjEBNY", "David's MVP", DOC, 3898, ""),
        ],
    },
    86: {
        "source_folders": ["1hklHYeNHBgiZqW5FcP_z6d-Dp_JTiOsB"],
        "files": [],
        "errors": [("folder:1hklHYeNHBgiZqW5FcP_z6d-Dp_JTiOsB", GONE)],
    },
    87: {
        "source_folders": ["102LKjSRs1W-RR-KzpWWINZ1oWFNbMIc8"],
        "files": [],
        "errors": [("folder:102LKjSRs1W-RR-KzpWWINZ1oWFNbMIc8", GONE)],
    },
    88: {
        "source_folders": ["1W7-G_Bg0uAQHNR0FDcns2NdL5VsaVJzm"],
        "files": [
            ("1UEeL4e_wCexxn5J1ojICNwQU4PxUH_FY", "Greg Neil - Oct 9 2025.mp4", MP4, 224278823, ""),
        ],
    },
    93: {"source_folders": [], "files": []},
    95: {
        "source_folders": ["1ISHJkXeFFL4RhZrkd1vR1EcHiOXvc0v5"],
        "files": [],
        "errors": [("folder:1ISHJkXeFFL4RhZrkd1vR1EcHiOXvc0v5", GONE)],
    },
    140: {"source_folders": [], "files": []},
    227: {"source_folders": [], "files": []},
    228: {"source_folders": [], "files": []},
    229: {"source_folders": [], "files": []},
    231: {"source_folders": [], "files": []},
    232: {"source_folders": [], "files": []},
}

DEAD_FOLDERS = {
    86: [("1hklHYeNHBgiZqW5FcP_z6d-Dp_JTiOsB", GONE)],
    87: [("102LKjSRs1W-RR-KzpWWINZ1oWFNbMIc8", GONE)],
    95: [("1ISHJkXeFFL4RhZrkd1vR1EcHiOXvc0v5", GONE)],
}

EMPTY_FOLDERS = {
    55: [("1XHuFIUXdw1Pn1Uw1npKiAJKbRCCfwh8l", "Engineering ")],
    80: [("1swhK9jk7Tj9QsQpulrmWGZ8J2wp69T9K", "Engineering")],
}

NOT_WALKED = {
    71: [("1srDVZkdLR7GPNYO5Gm-PERfFB6t7Li46",
          "harmoni - re-parents the same app design / airtable base / "
          "harmoni foundation trees one level deeper; its files are level 2 "
          "and duplicate what is already inventoried above")],
}

SUBFOLDERS_TO_WALK = {
    71: [("1rRxUYAdOivjxqc6_bM8fa3vRmZ2myZHa", "Glide (level 2, under app design)"),
         ("1LcWUrTTHgo_hZDKPRc0yVE4ytvetoqJL", "harmoni assets (level 2, under app design)"),
         ("16bh4AtHwNIk15CxSCY3hkW0vchTUypjG", "harmoni_final_ui_elements (level 2, under app design)"),
         ("1f2gPYN69kpGrpNmQ6fWzgtONiUkGWvOy", "Ai suggestions (level 2, under airtable base)"),
         ("1r4LgGO4kgjw8NqN589f-OP_Jv7pWtLml", "tasks (level 2, under airtable base)"),
         ("1Na15Mpg_NZeRA5qOlBn1bGvTXInA_EOO", "self care (level 2, under airtable base)"),
         ("12j6xI3S5qHDzpi0sZnhHl6WssXS_Tj0b", "cycle sync (level 2, under airtable base)"),
         ("14G_jPTAkqU5S7O9KNO8Xk-5cBkxIFQy7", "weekly planner (level 2, under airtable base)"),
         ("1WSJCpeZh29Hh80qxxc0bwZsQ1OSMFfPK", "Routines (level 2, under airtable base)"),
         ("1uZI-vJNevFFAq5wdVsJBqWmfWDGZN5Kw", "non negotiables (level 2, under airtable base)"),
         ("1N8QPx89gJMuIKGkA8jzbrDdA8tqHz-Ip", "delegation (level 2, under airtable base)"),
         ("1EzTy0PTMlMCWNErsGiYCKund5nHvOJCM", "harmoni mode (level 2, under airtable base)"),
         ("1jS4Rsa2ovWvLPYXc1C3sBQP89cP_yc3e", "meal planning (level 2, under airtable base)")],
}
