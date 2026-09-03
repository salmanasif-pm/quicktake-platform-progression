"""
Real Drive inventory for the third List 06 (`Closed Lost`) batch.

Cards 100, 101, 103, 107, 111, 113, 117, 124, 152, 162, 163, 166, 174, 176,
181, 182, 183, 184, 186, 187 and 188.

Three cards resolve to a card.md with no copied files, for two different
reasons worth keeping apart:

* Card 101's source folder is gone - files.get returns "Requested entity was
  not found". Logged in errors.csv.
* Cards 103 and 107 both point at a folder named `Engineering` that exists
  and is genuinely empty. An empty listing alone cannot tell that from an
  inaccessible folder, so both were confirmed with files.get; neither is an
  error.

Card 182's `Colored Photos - Meter Reader Taken` holds 31 meter photographs.
They are raw imagery, so the spec skips every one, but they are listed
individually rather than summarised so the manifest and the run report count
them honestly.
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
PDF = "application/pdf"
MP4 = "video/mp4"
DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
PNG = "image/png"
JPG = "image/jpeg"
M4A = "audio/x-m4a"

GONE = "Requested entity was not found (deleted or access revoked)"

DEAD_FOLDERS = {101: ["1MEaIaL05BaFKzyhZWq4_aW3fDiXBhGvx"]}
EMPTY_FOLDERS = {
    103: [("18xjs24i6rq3giG8FHn9U3-VOBybZWQI2", "Engineering")],
    107: [("1Y1oau-qLqQw7FCPAFmdP3UZFAum1iyGI", "Engineering")],
}

# Card 182, subfolder `Colored Photos - Meter Reader Taken`: (id, name, size).
_METER_PHOTOS = [
    ("1okaCHJmfkSRgjGBiZ2ewmOxWzw1XkuQ5", "alamo 13.jpg", 86927),
    ("1XKGnEVnputDIglJ0M-NwIO9WU7F3HR1N", "cswr13.jpg", 159190),
    ("102SkeBmQ5N6OZvHCxxkL2ZCA_FAXlRHG", "alamo 11.jpg", 172681),
    ("1yZann9VcTEJ7632ZYcv34CSDsdu6-g-U", "alamo 3.jpg", 111360),
    ("1s8Uq1m2k4KJwZNzL2YlSp9MxiX-O1Puq", "alamo 5.jpg", 146786),
    ("1pON4rAh-vXcpDKipSs1VLw8BgT2OT_df", "cswr 7.jpg", 131794),
    ("1NQJccr0vFF9l7TQvxBeixzJTaif3LrEp", "alamo 8.jpg", 166278),
    ("1PMLf69eBxpVtrZO8hzWFE8jRxENSDX1c", "cswr14.jpg", 164236),
    ("1f0GHLaPH_fhD4GEvrt5FemYwsNwCeDU8", "alamo 2.jpg", 123245),
    ("1gWbK7fL2W6HQz89GK81jfC0gbEHD00wF", "cswr 2.jpg", 130116),
    ("1eZdBkI6eCd-8DfLoESXYTTFqD6A_4dt4", "cswr 9.jpg", 115643),
    ("14rsoCVqmhb15qAQbeO72TYgw4iL6v27W", "alamo 4.jpg", 175116),
    ("1YS7Q5msAmJmseyWK_PMDIUQFgf1ySH8-", "cswr 4.jpg", 218593),
    ("1X_InUVhAU_XmXS7wzqM8dhJSNphEdJsB", "cswr 8.jpg", 132007),
    ("1j_p4YJrmE5b8l6VeU_yPVe2s_T0FE1-U", "alamo 9.jpg", 143162),
    ("1KbaadB5ceGF5VCcMGFWrSBmnUCww4OT9", "alamo 6.jpg", 147498),
    ("1z2hI1qpCVGD-j3Lrc2K8Jfs4P5ziyS2e", "alamo 10.jpg", 108926),
    ("1by894AW4BcAuqx33hWphA-wajGsdUk1z", "cswr 3.jpg", 183126),
    ("1xU1KrWyEizDieAPAAkzTAifotO93z6Qq", "alamo 1.jpg", 102991),
    ("1h8rUlkVspmLXx_dwTpJ4a0Qr68gzNUos", "cswr15.jpg", 149050),
    ("19N7mVPszvKAWYCEW4kSSlVk76ypDgBWp", "cswr10.jpg", 113297),
    ("17gQTpSKGLJu-hyR1cX496uY0cXMqPy4y", "alamo 14.jpg", 72283),
    ("1Dc3lBXRExwphF_wS_5Y3imORPHua9OJO", "alamo 12.jpg", 120532),
    ("1kz_7L7_4WadxodgsuCJIfw13oba86aLc", "cswr 5.jpg", 164243),
    ("10-zsz9Wst7gfCp_QzPvn9Q4hz7J7Bun9", "cswr11.jpg", 94291),
    ("1YVW3u_nAT105w_KeZ9YHVaprad6nTgqR", "cswr12.jpg", 147340),
    ("1YYnwyYY41GrpWCKu2lq05FcMfpkkMq1p", "alamo 16.jpg", 148721),
    ("1ZbqRJC3C5BkSbaO8TnYnIMMPbRSzu9QP", "cswr 6.jpg", 177303),
    ("18rm44OwXD23CPaTeuk22vM5RJNBN43pM", "cswr 1.jpg", 228799),
    ("10ETMUDWR9JV5ByM6q-5rvda805QeRwG9", "alamo 15.jpg", 120893),
    ("1YMxx2M9I58ntXalLbio5jIq4UaejGzHK", "alamo 7.jpg", 158630),
]

INVENTORY = {
    100: {
        "source_folders": ["1JXwyh3XejkSfMtOlcKjPp8pb-sInjukB"],
        "files": [
            ("1EvYv2FVQdaMlb4IQX1DeBy17QOIqWKCOh4YPY3bptdw", "CliniLink AI Assistant | Web App Development - Roadmap & Estimate", SHEET, 19108, ""),
        ],
    },
    101: {"source_folders": [], "files": []},
    103: {"source_folders": ["18xjs24i6rq3giG8FHn9U3-VOBybZWQI2"], "files": []},
    107: {"source_folders": ["1Y1oau-qLqQw7FCPAFmdP3UZFAum1iyGI"], "files": []},
    111: {
        "source_folders": ["1C6XSA6RVJyHc47RAppjqPQEVqjBxNFME"],
        "files": [
            ("1sQ9yMe7iimeHqowUjgZy2P8n_VEMs7yD", "Stairway (Syed Abdussamad) - Dec 12 2025.mp4", MP4, 144305519, ""),
        ],
    },
    113: {
        "source_folders": ["1zp-4pSP44qwYv18mg9djhhwUlsGrPIzt"],
        "files": [
            ("1tMKFIqR2VBe1p-4FUh_JBPbzwYigENPk5cUjMen1ZWc", "ERPVAR  - Audit/Review Report", DOC, 2702981, ""),
            ("1tWh34rnCOBQrh5hd4WqhMVk2Z5d_RoLqXGFRsZ1EGzQ", "ERPVAR Internal  - Code Audit/Review Report", DOC, 1480791, ""),
            ("1HJE9eqF4hPZnZIAlSMihArqfqGFKKKYY", "Meeting with ERPVAR - Dec 15 2025 (1) - Engineering .mp4", MP4, 188166624, ""),
            ("1IZF1GLvP5mJbqPtJj66zDaS7fEiBA6p3s57K8htDXlY", "Meeting with ERPVAR - December 16", DOC, 22508, ""),
        ],
    },
    117: {
        "source_folders": ["1_J8940WH3UR_GPX4irrhsDUOrqkD384M"],
        "files": [
            ("1uOE7bNNxy1OdFVGw8oxS9I47gD_GRNYx2t760eSY56Y", "Discuss Scorm Module set up - March 10 AI Notes ", DOC, 11851, ""),
            ("1Q10XZQxJ74QNOVjCY16oeNvrkYn9mJ-m", "Discuss Scorm Module set up - Mar 9 2026.mp4", MP4, 145316434, ""),
        ],
    },
    124: {
        "source_folders": ["1UiM88bxbDPWvDGy6viJgAQctPyoIPf91"],
        "files": [
            ("1-DjDCkeQDC5A_FU3tA9-Io9Y0xKSybyr9HWIcm_xbJM", "Email for Prospect - Post Cencero Presentation - May 06, 2026", DOC, 3316, ""),
            ("1QxGmt4HUG4UkfniHU-W8QfM5ZLjL6QEz", "Copy of Cencora __ PureLogics - Solution Call  - Apr 30 2026.mp4", MP4, 165572812, ""),
            ("1m-gm64S2vuoCts_HhCzr0FKBproqNGTXnTfw1aRzUt4", "Cencora - March 17", DOC, 23015, ""),
            ("1Z5T2SS8h-3PnDkODwjgymEwxwOwQtgfu", "Copy of Cencora - Mar 17 2026.mp4", MP4, 249123378, ""),
        ],
    },
    152: {
        "source_folders": ["1gMwxe-Q4cDHmooifhnQKLMsUOIl64DiI"],
        "files": [
            ("145gk8gh8Z6p2agZ69jvBEzcMeDPcAcaI", "Blxck - Recording 2.mp4", MP4, 111959771, ""),
            ("1A5PJfiVnTQ7kHCyuA9EQ29ro2HkDLjgZ", "Blxck - Recording tech.mp4", MP4, 261227848, ""),
            ("1HOkiLz928_wOIbWiVQNLh4rr0DYCruwMZ_ENVNHNwrM", "Read Me", DOC, 1024, ""),
        ],
    },
    162: {
        "source_folders": ["1b9YdpnEbvwnBFVWJ0dh51C21uSkif2RH"],
        "files": [
            ("1Np87gJuZdlRHY2NZGtaMCPmcMkRuqqnJuDiVRoHTlW4", "R&D regarding Payments Processing on Merchant’s Device", DOC, 1476530, ""),
            ("1l89euKhs9IYnW7IXR0Yf99K-wvpS33abLbqUyC1VtA0", "R&D Share with Prospect", DOC, 3381, ""),
            ("1gAfnZM8OTsZOugU5abBzgnYcPfSqo1-o", "Goldsands - Recording 2.mp4", MP4, 154216063, ""),
            ("1CSIl1oEnavuz9SGnM-JjfE0a24apcgLYgIlhcH6RvgU", "Questions to Ask", DOC, 2141, ""),
            ("1owivFcSU1pz0hXwCMPTUnkSwa3nkb-zHX9zyYxcz7Ls", "Requirements Shared By the Prospect", DOC, 1024, ""),
            ("1pv2SD7D9-_36y1bnLLgRxZaGYjMw4sL3", "Recording - Goldsands Group.mp4", MP4, 297830928, ""),
        ],
    },
    163: {
        "source_folders": ["1fhO5Bo-v7h5wgCxe3eY0suTqCL8Jzbzh"],
        "files": [
            ("1fG-4xvjs_hE3QIox6VJNSz5Ku7u6X7Kq", "01 Member Flow Diagram.pdf", PDF, 29676, ""),
            ("1CBENzUFpVa7YVmJuPXO8ZW9G7f4Py_oc", "06 GANTT Chart.pdf", PDF, 79299, ""),
            ("1xNjyNOe5R9zMtTW5UEbkEYkkHPvfAX1O", "05 Flow Roadmap.pdf", PDF, 204249, ""),
            ("18MliHJvg6P4mm2qKQS5y3vBK5LtunTkq0H4YmnHO6GY", "Higher Conscious Network - Proposal Document", DOC, 6366546, ""),
            ("1KdHTtloX84EL43uN8NrjDrjuee9dEg3E", "04 System Workflow Diagram.pdf", PDF, 76435, ""),
            ("1pNlmpKdo6XDChLSdXpM4NTNGmoTcXWah", "02 Provider Flow Diagram.pdf", PDF, 31519, ""),
            ("1JrUm6qZcRrpeVqrHM41c-FNyZfjENKEh", "03 Admin Flow Diagram.pdf", PDF, 26564, ""),
            ("1ZL-0LSf9GPZ_meCAQNekW9W1p2hPNsdicg2Hp14xsjU", "Read Me", DOC, 1024, ""),
            ("1qrbrm63Kmx2jq02N1I_FZJe5JZGZepIs", "Scope of Work.pdf", PDF, 174913, ""),
        ],
    },
    166: {
        "source_folders": ["15ev9u4GwbVVwbHOi2QVctWOVDfwKuzer"],
        "files": [
            ("1jP7xGQpbEmxQ5x-Y5pk1l9jMusxGyzrXweF33B8vl5E", "Baird Augustine Web App Enhancements - Roadmap & Estimate", SHEET, 29307, ""),
            ("1BERd30QJGbMlVGVRl564uObu0AAHQiIP", "Meeting with Ryan Baird - Mar 17 2026 (1).mp4", MP4, 228103406, ""),
            ("1HZMYs2yZdwphjRqVYPe4Z-FUHfTXtYHy", "Augustine - Tech Recording.mp4", MP4, 28851493, ""),
            ("1Q8kSXYAgSAGW48bliwi0jPnrtYyzY8dHW4uALW91Nbw", "Read Me", DOC, 1024, ""),
        ],
    },
    174: {
        "source_folders": ["1GL08MC_9HPHMQ3NCi1hMWu07fBnqTze2"],
        "files": [
            ("1hluFqnCbgJkh6D0xpUVGXDwTes8Q0FW-tmR4yrATrhk", "DRAFT - Leads Scraping Platform | Web App Development - Roadmap & Estimate", SHEET, 29310, ""),
            ("1SzMBI69qkKaxsEJHY6nFrBq4WOF9jN0YoRPwi8ryUoo", "PropStream Real Estate App - R&D Document", DOC, 1478898, ""),
            ("1UE74CyA7yBPEOWOH-8UBMjJBWPUiAfck", "Solution Discussion with BA.mp4", MP4, 39653358, ""),
            ("1oKPf0iOIZy26Tr2i7ewIremlDxQaLkg7hZrRK_OfQ_k", "Answers", DOC, 20253, ""),
            ("1wYgEO9-zCERnyhdZWLbmtbbUpn40a2TxxYhJ5xjLcOY", "Leads Scraping Platform - Question and Queries", DOC, 1475588, ""),
            ("1k_oGgS6HxutQofHCJIQ9tCpcnGX9_8LKMq-nEj9Nunk", "Read Me", DOC, 1024, ""),
            ("15HMxWRGWRoL2U4QrHPUtfbfGWkP2n9Sx", "Recording - Gatehouse.mp4", MP4, 94383298, ""),
        ],
    },
    176: {
        "source_folders": ["11Dp0v3Yhme7YYLIwzFOOj4Mu92fTb49-"],
        "files": [
            ("15wii39NbukqSLxS9HG7bxCNSz88spJzhWDeyAYnDfWM", "Readme", DOC, 1024, ""),
            ("16L2FRUGAXhqA2xomL3m3EvAg_KWXu63z", "Hireclout - recording.mp4", MP4, 72563597, ""),
        ],
    },
    181: {
        "source_folders": ["1lnsmGJc2UVyyPOpGbmfoINb8s4t5KAl2"],
        "files": [
            ("1T68w22P8_rvgaHqh_IOyQIxAjOXZbjuoXAW8CptVbSQ", "HustlePay - Roadmap & Estimate", SHEET, 20304, ""),
            ("1Z6AvsVg3DYNEqjtiiolETkvpUJqLgFnd", "HustlePay Business Models - Sheet1.pdf", PDF, 58099, ""),
            ("1QqrBZ96GfLc407cmfc715OGGqBRrRY1C", "HustlePay Brochure Text.pdf", PDF, 127432, ""),
            ("1x5ci1LjlJXPkTmE1r7qSYcL0xt5kRnQ8", "HustlePay MVP Eng Req. Ongoing.pdf", PDF, 143699, ""),
            ("1nXH1pp4lb6o_gc-JLEPjmI1Ciqf8OGTR", "HustlePay Deck_041824.pdf", PDF, 1554801, ""),
        ],
    },
    182: {
        "source_folders": ["1B32Hy43yBekqi8EFEMkLSlGmsyyv4tcN"],
        "files": [
            ("1V2P0QIqjqz0LcL9YqaF08qC_xIZCegnA", "OCR Meter Reading - System Flow Diagram.pdf", PDF, 1267950, ""),
            ("1LRF0yjVlggMRjRoYX9fb7dLrtV2bG-8Py-wSnKwpqKY", "Advanced OCR for Water Meters - Solution Document", DOC, 18869, ""),
            ("1ErP3kis-lR_73mI53IuivyI_09Qqg2Fu", "Phases Plan.png", PNG, 25609, ""),
            ("1JxTvOsAIZy_cwxJXbkIluDzsZ9nQiSEE", "Screenshot_from_2025-03-03_16-48-47.png", PNG, 116514, ""),
            ("1fxUNx8eJxrGAXAv9Pn4aKVE6D6qXB5Ay", "Screenshot_from_2025-03-03_16-48-09.png", PNG, 155161, ""),
            ("1hJQZ-bEmTCtdKiAac-a-W4UO_3dwfZgS", "Recording.mp4", MP4, 92224118, ""),
            ("102PRxhAGJkQzdM5Y9ZiIxvKcB2BBwcIL", "Black & White Sample CYCLOPS (device) Photos.docx", DOCX, 595978, ""),
            ("13Ws-pRd9ruswBRiul5Eop-Sg6FAYyriaNuIHgGQIrIc", "Copy of Advanced OCR for Water Meters - Solution Document", DOC, 19821, ""),
            ("1-0IeI4NaYMijhjI_IwytLlNXN6rE1Pmx", "Call Recording.m4a", M4A, 933150, ""),
        ] + [(i, n, JPG, s, "Colored Photos - Meter Reader Taken")
             for i, n, s in _METER_PHOTOS],
    },
    183: {
        "source_folders": ["1dmMzM1nKcTSZhFfnRSdgtK-VQtUuOpoJ"],
        "files": [
            ("19iFNQV4IKj3eDJ73cC0Yf4ytOkGsabcmhws5uvBtjjs", "CareConnect - Solution Document", DOC, 19628, ""),
            ("1sOmK2R3B5vJBS4ODIyq5H9P1RTNNu7sf", "System Flow Diagram.pdf", PDF, 4541317, ""),
            ("1iJlJ9sNnOr4i4VILtxdQajjrmBq_OjGu", "Senior - Recording.mp4", MP4, 317515115, ""),
        ],
    },
    184: {
        "source_folders": ["18a2-dmH9wKHbftqAqsJ1bKTs0dy8R1TA"],
        "files": [
            ("1WiGyPdGOGccYKzcAJeyWCDmmO8_66vpd4zII8S5qkVc", "Enhancing Case Management Deployment and Regulatory Compliance Assurance - Solution Document", DOC, 18390, ""),
            ("12ZUPcnHVTgZnCns3m2PeoR492yp9uQSj", "Recording.mp4", MP4, 64728130, ""),
        ],
    },
    186: {
        "source_folders": ["1PU-3q3OLkowFTfuij_IMHEbrxc_EGzOK"],
        "files": [
            ("1KptUN_xK_iUtz5M--ISMPI5m0OQKvFFFHwXXFX9tpeA", "Ideas related to Artificial Intelligence - Solution Document", DOC, 64577, ""),
            ("1G0VsNwAgFGrMqds-swq9YnWvMPE05qibGHEaqhwaCHo", "Requirements", DOC, 9167, ""),
        ],
    },
    187: {
        "source_folders": ["1Lt8gjHk76b5DpzMrYHiy_xu07dwDZp1T"],
        "files": [
            ("1gfLaxa4YtGCZ5BxywTRHdwgmofHPN1npMBzuU-vZZ1w", "Holland Parks & Recreation - Project Proposal Document", DOC, 6025817, ""),
            ("1XAm4miidqO4KBZbHxK1IeJGDug2xhHQU", "RDP.docx", DOCX, 97045, ""),
            ("1uY5gar0Ze8IMOgMbN2Okt5y1p8Ypx4X8JByJSAy36XQ", "Requirements", DOC, 2184, ""),
        ],
    },
    188: {
        "source_folders": ["1wbbAW7ECBMz6QGrKd53Swt6nktEXZsWG"],
        "files": [
            ("1GWV_xRkCWFjSXThiqFtDNkN-1s_DmBHA1_DWX7xlx9M", "InteleCom - Roadmap & Estimate", SHEET, 20295, ""),
            ("1NkLiof6WAlzSvjfR-1bezReXHZpco1xs", "InteleCOM ACP V1_2025.docx", DOCX, 16005, ""),
        ],
    },
}
