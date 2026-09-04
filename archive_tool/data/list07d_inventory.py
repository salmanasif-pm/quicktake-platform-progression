"""
Real Drive inventory for List 07 (`On Hold`) batch 07d: cards 96, 98, 102,
105, 110, 112, 114, 115, 118, 121, 131, 133, 135, 136, 137, 138, 139, 141,
142, 143 and 144, plus the three remaining no-Drive-link cards (249, 403,
455).

  DEAD_FOLDERS   cards 96, 98, 102 and 105 - the linked folder answers
                 "Requested entity was not found".
  EMPTY_FOLDERS  cards 114 and 115 - both `Engineering `, both created
                 2026-02-17 and never filled; the folders resolve fine.

Card 143's `Screenshots` holds 31 PNG captures. They are listed here so the
manifest records each one, but the folder-name exclusion drops them all:
screen captures are working material, not the final diagrams the spec asks
for. Its `Sample Data Shared by Prospect` holds five shipper PDFs, which are
documents and are copied.

Card 139 keeps two parallel `Engineering` / `Sales` folders that share four
files by content (`Recording.mp4`, `Recording 3.mp4`, `XPRIZE Call for
Future Positive Ideas.docx`, `Imp Links Shared By Prospect`); the deduper
keeps one of each. `Solution Related Docs (Prepared by Zukhruf based on
Figma)` sits under `Engineering` and is therefore level 2.

Card 121's one card-level file link points at `Client email`, which is
already inside the card's folder, so it is inventoried once.
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
PDF = "application/pdf"
MP4 = "video/mp4"
MOV = "video/quicktime"
PNG = "image/png"
JPEG = "image/jpeg"
DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
PPTX = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
TXT = "text/plain"

GONE = "Requested entity was not found (deleted or access revoked)"

SHOTS = "Screenshots"
SAMPLE = "Sample Data Shared by Prospect"

INVENTORY = {
    96: {"source_folders": ["1CgqM9zyZFW3WNISNcSAMyFr5B-QC06vS"], "files": [],
         "errors": [("folder:1CgqM9zyZFW3WNISNcSAMyFr5B-QC06vS", GONE)]},
    98: {"source_folders": ["1de31bOJDCr1kp1L7f2KvQIlQXCVVXcRd"], "files": [],
         "errors": [("folder:1de31bOJDCr1kp1L7f2KvQIlQXCVVXcRd", GONE)]},
    102: {"source_folders": ["1EyjYqyZ_arGIbhUBjjj6kIywwqDkpb4I"], "files": [],
          "errors": [("folder:1EyjYqyZ_arGIbhUBjjj6kIywwqDkpb4I", GONE)]},
    105: {"source_folders": ["1wGrEhXT4jgcVzFa2LP9aqY49w9L9N6Gy"], "files": [],
          "errors": [("folder:1wGrEhXT4jgcVzFa2LP9aqY49w9L9N6Gy", GONE)]},
    110: {
        "source_folders": ["1Dj_H12WMOEduRMfdHBRhgPaYdvYbAXue"],
        "files": [
            ("1xxGv1fkNq3elbs7fhrstWb6C-di_OZ93lOVvHHNpVu8", "Meeting 1 & 2 Summary", DOC, 5308369, ""),
            ("1WjyHFP_MCxe03WXgCcSxSrTacDtlM_u4QqTtn6fHS80", "TerraVox Ventures Platform - Understanding Document", DOC, 5300823, ""),
            ("1JMHS5SnAstl9bQPecSR7jQLqEKx5SSph", "Lloyd - Solution Sync  - Jan 21 2026.mp4", MP4, 413253926, ""),
            ("1DrSQrtXmyysqs0G3uPWvdXWxfg6XgkOu", "System Workflow Diagram.pdf", PDF, 439865, ""),
            ("1wY2_4aRz_8tdTepG7H4ZxNNArOxvdWo0", "Verdant Impact Partners, Inc - Dec 9 2025 (2).mp4", MP4, 157400726, ""),
            ("1HTRGWziDLiuY8bXxZbTBD_nb1VOyd1Nlb8vhMVqpXv4", "Project Name: TerraVox Ventures Investment & Venture Studio Platform", DOC, 8381, ""),
        ],
    },
    112: {
        "source_folders": ["1YM4xFBM9XYoFMjUrxZD_L1uruS8RIe5M"],
        "files": [
            ("1PMB80DJ5c2qGye58ukPG9wIlCeL5zrFHigop85MSgUs", "Copy of Centralized Healthcare Analytics Platform - Solution Document", DOC, 5433766, ""),
            ("1GehxK5iqLqIHnSyMg2GjjmGWUlY_8Mg5KU3LADMEX_E", "Centralized Healthcare Analytics Platform - Solution Document", DOC, 5431189, ""),
            ("1BDbg81a2MPdw_wjbaXSe4SD58zbzMqgK", "Flow Diagram.pdf", PDF, 421328, ""),
            ("13RR6A_Mu1yHUAouRaPwgXV_r1tdoJjqq", "f85f1866-c2b3-4733-8ec3-f2e24a2f22b8.jpg", JPEG, 123084, ""),
        ],
    },
    114: {"source_folders": ["1paJ73jy3WaMw9NRiQVqZSMz3LDZ0WrE6"], "files": []},
    115: {"source_folders": ["1VgT1FhZhuQcLV2UkCwpgS21X6BeeXoG-"], "files": []},
    118: {
        "source_folders": ["1u7ifZAc7qQCWtRqiXy32Zlva0qua870X"],
        "files": [
            ("1n9yXu6J58a0HwjxEPJpVouA4r7Zf29fQ", "Video Project 2.mp4", MP4, 977410913, ""),
            # subfolder: Documentation
            ("1UOx52jmsTEBEBPb1ASEhgomp0gVRtsUq", "ClientCallAnalysis.docx", DOCX, 13256, "Documentation"),
            ("10qqtRUYkROeW4lRxG4XpMepyRFoOLqY2", "Technical Discovery Document.docx", DOCX, 13264, "Documentation"),
        ],
    },
    121: {
        "source_folders": ["1ttUAcKipc12dWrZKTzLy8u2XcErcbt2L"],
        "files": [
            ("16hWf192IQwXdutVPhXHvKv8tj6LHN1lh", "input.txt", TXT, 1740, ""),
            ("1pwl5-jVNrWfBOmyDmnWFW8hval1kD92B", "output.txt", TXT, 1787, ""),
            ("1Sy0tMZa21p7AM3qG_GNdkwRXd7KJtMqHKTbzAGC1ppg", "Client email", DOC, 6854, ""),
            ("1JNmIiiAXQ9Cd_EoQfVEXXbbqRVr0KKj8", "2024-08-23 11_56_54-WPGetAPI ‹ Ecommunity Fiber — WordPress.png", PNG, 83994, ""),
            ("1rZSlESsRRHOLAT2xUoYm7Kr-R98mxymt", "2024-08-23 10_15_56-WPGetAPI ‹ Ecommunity Fiber — WordPress.png", PNG, 34652, ""),
            ("15gZK9JXeRfx_n-5T907SctWS-1o9JiGh", "2024-08-23 11_56_17-.png", PNG, 83906, ""),
            ("1-gwfv9CiJLvM93u0wlO61cFUHjn1oCGZ", "2024-08-23 11_55_52-WPGetAPI ‹ Ecommunity Fiber — WordPress.png", PNG, 63637, ""),
        ],
    },
    131: {
        "source_folders": ["1Axp9C4mstDpFe2HlgBzXR1vFaALoSLKx"],
        "files": [
            ("1t3KjX5o577caOZnErmXts_iMLqnFrCf6qxjsfsBxelM", "Diagnostic Ventures - Understanding Document", DOC, 5309555, ""),
            ("163QTCar8C5kYx2dmYiMZTwF6F-cAo7gj", "Tech Recording - Diagnostic Ventures.mp4", MP4, 544679219, ""),
            ("1BlmIzjCrDfX4NapnM9zY31c1bAdv9i9-6Ke4TtnLmUw", "Additional Information Shared by Founder as Answers to our Questions", DOC, 3634, ""),
            ("1HxAyxa1VLIOG1jh-UAURFgqVGm2Ao7zR", "Key Questions for Clarification.docx", DOCX, 202063, ""),
            ("1Pbk71htSyJSh-15ICNfbj6Y31UsDZ16s", "Zhang '24 CellSortingByRaman - sciadv.adn6373 (1).pdf", PDF, 3444861, ""),
            ("1U1RCH73f5d7-h8NkYxbZLpVKSnrdpayd", "Li '25 Rapid_culture-free_diagnosis_of_clinical_pathogens.pdf", PDF, 6542835, ""),
        ],
    },
    133: {
        "source_folders": ["1r4Ame8W8V02Amly0mCUsPcJzb2Hk476m"],
        "files": [
            ("1wUyWj7IkT6bZnFrQU0LDDrtMV2X-Znrr", "Reliable Robots - Tech Recording.mp4", MP4, 158519753, ""),
            ("1sOlPWpWeOaj3pWY69EDQ3lSYeGksynU_JJjCuFfVJZ4", "MIRO Solution", DOC, 1024, ""),
        ],
    },
    135: {
        "source_folders": ["1LzK0pgdYDF88iCjJrwsB4xiZF0UqkWUR"],
        "files": [
            ("1iJi51Wrs4zlK8NPYn46cv8LSUDcLqYtz", "Caltera Business Model Canvas - AI Real Estate Solution.pdf", PDF, 18192961, ""),
            ("1mk2BWWaROcDV2lyqkUEOjBSYPzEwHr8h", "AI Scrapping Tool Recording.mp4", MP4, 42407829, ""),
            ("1Dx16x2I40Hs5BMAlRODV8BKA9uzDLVbX", "Scrapping Recording 2.mp4", MP4, 100181398, ""),
            ("16mu3W3SpoF0IRA_8TR5NHzkY9PJBVFC0", "Kalterra - Goals.pdf", PDF, 55693, ""),
            ("1DxGBnOr4PRfDu1lAW21vTizoClIp-Nz2", "Flow Diagram of Solutoin.png", PNG, 549519, ""),
            ("1-f4zU9nqisnzXoKKP4EM8Qqh7UFYhoatDPidqlrwoDQ", "Kaltera Potential Data Sources", DOC, 20267, ""),
            ("1uC0-6sxjyfa8gmwrYCzzrjLCRIFxAdIDKSFNQmwiUE4", "AI Scraping Tool - Solution Document", DOC, 15558, ""),
        ],
    },
    136: {
        "source_folders": ["1VyVXZoOEsaDhUNaXMPsHJzubfwKEHFCS"],
        "files": [
            ("1pBkaV14QAT9pdjpbJzqyV-EtUXBJFQ4zrWG32oFadwQ", "Enhancing Patient Device Onboarding and Integration for Healthcare Solutions - Solution Document", DOC, 20070, ""),
            ("1V2WrIKIxRmFpJ-mnMGwgjMfgyn_YzJBQ", "Device Integration - Recording 2.mov", MOV, 125341761, ""),
            ("1k8iaBlfcbEfAWfwhY8oO3iopdf8WkAld", "Recording - Discovery.mov", MOV, 82322199, ""),
        ],
    },
    137: {
        "source_folders": ["1TGYlpJjJmT5ICXJ2Qb_P6-7proKPElfc"],
        "files": [
            ("10pwPRHBSr2bdJDDTYCjS4PnggAMYLiYLKLOTvRBCZDk", "Cloudbeds Based PMS", DOC, 22735, ""),
            ("1ShhHEmQ7PwQSpvhLAn5wGeiaG05apri4", "QloApps MindMap.pdf", PDF, 1294748, ""),
            ("11Q3IqNixpCOT8WZ36G0FtGE2BOHGAb8ugJKIc5-wRtg", "PMS Open-Source Recommendation - Solution Document", DOC, 14785, ""),
            ("1mkc-JT8ipQeqre75STKQeCDlZ4h9MUAdEXy077sHjJg", "Property Management System (PMS) | Web App Development - Roadmap & Estimate", SHEET, 19906, ""),
            ("11pvInTwv_Lovzsj_bsJkqRIQe7oHQfInGWLWCttEOfc", "Imp Links", DOC, 1024, ""),
            ("1x0h-r1aK5DA7aHxndkwYkGt-96HdAnxp", "Recording 2.mp4", MP4, 195302661, ""),
            ("15ffiZrstgcztfbarsqB9pxXTIu5C630I", "PMS - Recording.mp4", MP4, 136521696, ""),
        ],
    },
    138: {
        "source_folders": ["1jxLl9TV5-lFz_l8qjN9FjBpJfnS86Umx"],
        "files": [
            ("1Oow5HVeKEkFov7WvHIoARjCExUEBUfZx", "Process Diagram.png", PNG, 676192, ""),
            ("1PKFWwy1_5XQKka2P_CH27gBu8kpEGPBU", "userflow_for_schadual.drawio.png", PNG, 42634, ""),
            ("19RfS0zKmGTpZNZEqv-zwN_WaE45fzKgD", "Recording 2.mp4", MP4, 293979254, ""),
        ],
    },
    139: {
        "source_folders": ["1kelpV-ghkhv8Vzrr6Fwbaz8LYRru4_tW"],
        "files": [
            # subfolder: Engineering
            ("1Piqh_dW3qT9_CS5RCUgn0ruUgPEM26q8xJche0tQYgc", "Bk12 - E D - Roadmap & Estimate", SHEET, 19427, "Engineering"),
            ("1K4b5csUTXOpejz2tuC8icgZU43XIIaMxlTWlAJnBpII", "Imp Links Shared By Prospect", DOC, 1439, "Engineering"),
            ("11hnYUcLaIltOE8coaj0x-PGut5v0sYhV", "Recording 3.mp4", MP4, 198505603, "Engineering"),
            ("1N_hooIIA_yURvrW-Xapn2xzslnwx6q55", "Recording.mp4", MP4, 175734316, "Engineering"),
            ("1Y7VPWb6mcgDZW4X5yO7X77G9py6gQM04YAG8oqRJu0U", "EdTech Platform Monetization Models - Solution Document", DOC, 30212, "Engineering"),
            ("1Q8G0hKyvQ9olxtdoZCshKGlXPdt4QafS", "XPRIZE Call for Future Positive Ideas.docx", DOCX, 3358041, "Engineering"),
            # subfolder: Sales
            ("1oo16DeG1OwwV42qY5iT4kzpKwdTTGOsuiWKwTD3X-rQ", "AI EdTech - Pricing Template", SHEET, 3165, "Sales"),
            ("1NmSpa8bBLxjKodS6IUom2aDm8x_1SLgM", "Beyond Technology Education AI Platform - Proposal.pptx", PPTX, 7200347, "Sales"),
            ("1jQfOWoL2Y4zSpKqRdkqVqttr_qEhFGWw2B-bmnjqBPI", "Imp Links Shared By Prospect", DOC, 1024, "Sales"),
            ("1NyS6xRsabpywwv8r1ZLY2hE18x4vIC2a", "Recording 4.mp4", MP4, 475587178, "Sales"),
            ("1nreZJb8oIisQAqrbFV2MOCe3ulMyD6qz", "Recording 3.mp4", MP4, 198505603, "Sales"),
            ("1SUA-fumOH2g-63Ppr0b3aEkaiwDebgW9", "Recording.mp4", MP4, 175734316, "Sales"),
            ("15DRv--pv5yxnyEyt8loQC3fOYb76eLnE", "XPRIZE Call for Future Positive Ideas.docx", DOCX, 3358041, "Sales"),
        ],
    },
    141: {
        "source_folders": ["1tA12JoZfQCakizrfPyeCgw3Q-9Pyjq1x"],
        "files": [
            ("1b798BTYbkwoZ-iFM_PY6dwN8nSOaRP8D", "ARTLINK - Flowradmap.pdf", PDF, 76115, ""),
            ("1MVmyRBs2oNH8QJP9I_pAXe0IdIZI296u", "ARTLINK - Process Flow Diagram.pdf", PDF, 193352, ""),
            ("1vhGq2f84WipEBsRpjDLb5n0ZJ8aQ12pYP2Xgd4rPcCs", "ArtLink - Solution Document", DOC, 1476588, ""),
            ("1CZiCkr1LQwzoj07foCo7H5Qji5Ba7ELP", "Recording - Artlink.mp4", MP4, 216171818, ""),
        ],
    },
    142: {
        "source_folders": ["1CLsKyIUY1wjpSoa4XW1egJNSK_2tazkQ"],
        "files": [
            ("1nWwUE9h4ToeYfA5DBKfVQ0R-vZ5Ae-1b", "SHSS - Recording.mov", MOV, 305575496, ""),
        ],
    },
    143: {
        "source_folders": ["1KU2LSTk2JEtluVaae8U8IdIKiJH-BGog"],
        "files": [
            ("1-M9oh5rZSQOHskiwAbGDTVUEIHkiJwRV", "Recording 3.mp4", MP4, 248844790, ""),
            ("1zmavgSfWZa7KXbmtPo_pmTNVL0QYfKpS", "RGB - Recording 2.mp4", MP4, 90913193, ""),
            ("1o6VmEXqpnsPxDPMI6vdmn3tih6JHA32g", "Recording - RGB.mp4", MP4, 289457680, ""),
            # subfolder: Sample Data Shared by Prospect
            ("1hCi5fnwJ33GUK65fIPOBz7JBs95GiI_u", "ESHIPPER DIR.PDF", PDF, 59549, SAMPLE),
            ("1ADsdxxaIE9mP9HQKHVSogSt-z2N5wQt8", "C-CEE Shipper.PDF", PDF, 24162, SAMPLE),
            ("1NTxwaCRmyCG_S4z0ZOB2MBSzjNANNQix", "82083A SHIP ORG.PDF", PDF, 190868, SAMPLE),
            ("11zFf6xjFCJWMiJQ9H7Ii4pVRJ82uin8l", "AHTECH Shipper.PDF", PDF, 25946, SAMPLE),
            ("1LuUskb3D6AkMwKiCXndoL_J1kft0bH-S", "82083A Ship Master.PDF", PDF, 216938, SAMPLE),
            # subfolder: Screenshots - 31 captures, all excluded by folder name
            ("1AfOJ7tL9bkqAlMTjWtQ3jJ5fG1WkKOBw", "Screenshot 2025-06-05 at 8.04.49 PM.png", PNG, 2785221, SHOTS),
            ("1mlC8Md5_n02YTTT7GtcT9eTtbFgzUIng", "Screenshot 2025-06-05 at 7.55.40 PM.png", PNG, 2221198, SHOTS),
            ("1Yv48IfIVvub6fLeUjvuzJKU7JPVjwjlF", "Screenshot 2025-06-05 at 7.56.00 PM.png", PNG, 2487541, SHOTS),
            ("1WZujp4E2ncZDl5oU75PVNYXalcNQnVni", "Screenshot 2025-06-05 at 7.55.23 PM.png", PNG, 2421112, SHOTS),
            ("1x_l4RHlBmSwhczf-eI6J8tNu6ZZ-P6aD", "Screenshot 2025-06-05 at 7.49.14 PM.png", PNG, 2766628, SHOTS),
            ("1RtOmBAid8rg85N0JlrFA0D8ETSwoDP8h", "Screenshot 2025-06-05 at 7.50.25 PM.png", PNG, 2561174, SHOTS),
            ("1DknPwhdKFEd6GmBaIfEd-PNUvXazjJ9d", "Screenshot 2025-06-05 at 7.46.37 PM.png", PNG, 1852179, SHOTS),
            ("1KMiJr-7i3QX2Kw2k3dFXDhfhxZLR9xdL", "Screenshot 2025-06-05 at 7.48.33 PM.png", PNG, 2576746, SHOTS),
            ("1ngCVxfJowOgoL2aCOeKUvYKwd2sS_Fcm", "Screenshot 2025-06-05 at 7.42.40 PM.png", PNG, 2591097, SHOTS),
            ("1NVgAtRrh2OhK7HGu1lmlGE2QBz5YLPWB", "Screenshot 2025-06-05 at 7.40.39 PM.png", PNG, 2426773, SHOTS),
            ("1YT77iqXXDDlL7yC1D4GEFoL4CbDQWEiM", "Screenshot 2025-06-05 at 7.44.32 PM.png", PNG, 1587994, SHOTS),
            ("1QDWwCdL8oMVqno446SOR4lGOwk2p6dM_", "Screenshot 2025-06-05 at 7.41.20 PM.png", PNG, 2430920, SHOTS),
            ("1h_T1Uyk1jAim-2ZoiBYb4OAFDQe0djPT", "Screenshot 2025-06-05 at 7.40.09 PM.png", PNG, 2270525, SHOTS),
            ("1-4P0SHJ1H_QN_AXJjR8RE8pQz4SVLIsf", "Screenshot 2025-06-05 at 7.31.13 PM.png", PNG, 1838053, SHOTS),
            ("1pcUY8LuGPIq3U1dQFg3r0nJp1Boi4ZHh", "Screenshot 2025-06-05 at 7.23.18 PM.png", PNG, 2341588, SHOTS),
            ("16aphmPzmNFNOvyYYMSDOU24EcqNVMego", "Screenshot 2025-06-05 at 7.23.14 PM.png", PNG, 1236020, SHOTS),
            ("1C-DLptsnzdI0j6d1EI2Q1u2HVpwCCIqv", "Screenshot 2025-06-05 at 7.18.32 PM.png", PNG, 1771944, SHOTS),
            ("11mqeDXxZPQng-X_Nw0f27xGBRx27C_2O", "Screenshot 2025-06-05 at 7.19.27 PM.png", PNG, 2083290, SHOTS),
            ("1BgCw-tOGUVWmW33EePkopISHOvvfSBpL", "Screenshot 2025-06-05 at 7.22.29 PM.png", PNG, 2473769, SHOTS),
            ("1kJofRVxSQILBg3kJOKJeGKxbLvhMuvn9", "Screenshot 2025-06-05 at 7.19.18 PM.png", PNG, 1847768, SHOTS),
            ("1FbY7N86kd1dbJ3gJ1zbwukWXrYlPDK-J", "Screenshot 2025-06-05 at 7.17.59 PM.png", PNG, 2054065, SHOTS),
            ("1KjZAiEwlW0w6Bilk8Rv42_G7P1AuVwYU", "Screenshot 2025-06-05 at 7.26.59 PM.png", PNG, 947383, SHOTS),
            ("1JgK7Sqnc7QQ0w7R694P1Z3lwmN0t_-dA", "Screenshot 2025-06-05 at 7.14.31 PM.png", PNG, 1214591, SHOTS),
            ("1Ho3x6IOFrTXZfJVc1x63Nvou3YO_fMY_", "Screenshot 2025-06-05 at 7.13.03 PM.png", PNG, 1336999, SHOTS),
            ("1aFSGTOf-zNqq8glVV1J37YMG5n4hf4_y", "Screenshot 2025-06-05 at 7.10.36 PM.png", PNG, 1687019, SHOTS),
            ("1vvzt3thYgk4RDxT3cFJSfNem1S4PeBYW", "Screenshot 2025-06-05 at 7.11.50 PM.png", PNG, 1176028, SHOTS),
            ("1ddaJjUQue-9m1p0Nv3oKcEmdl1lvcQFo", "Screenshot 2025-06-05 at 7.14.14 PM.png", PNG, 1402097, SHOTS),
            ("1fXNlB1neic2YOrr1-RAiB86BrOdz4ZkD", "Screenshot 2025-06-05 at 7.12.32 PM.png", PNG, 1393917, SHOTS),
            ("15q7nQmGYXTJkWDz9xv27OrgOm42RzMoD", "Screenshot 2025-06-05 at 7.14.23 PM.png", PNG, 1211066, SHOTS),
            ("1P9IN4tHtRDHG5EUZgrfuHEJai8OAwZLW", "Screenshot 2025-06-05 at 7.10.40 PM.png", PNG, 1645674, SHOTS),
            ("1hiLnvNsJGgfgfW0hMTBDXjVvTZWJ5pf_", "Screenshot 2025-06-05 at 7.12.51 PM.png", PNG, 1521614, SHOTS),
            ("17_ekEA11O6cDxhULDILxnVUj1sz6nd21", "Screenshot 2025-06-05 at 7.12.00 PM.png", PNG, 827899, SHOTS),
            ("1Np46FLcFNl9ssWTV_xajwL1rWScuXCVS", "Screenshot 2025-06-05 at 7.11.36 PM.png", PNG, 1412045, SHOTS),
        ],
    },
    144: {
        "source_folders": ["1eDE-TqitA-fsO9ojseFF_9t-BmflRTyH"],
        "files": [
            ("1CC3_tD16SfcdV_xWLULKCRxl-Al7RCoIvnmxRGo9uP8", "EPICompliance Modular Add-Ons Development - Roadmap & Estimate", SHEET, 25781, ""),
            ("1fUI25TlydSIzh5SHozgbxSncAQ2LBgWm", "Recording 2.mp4", MP4, 298692679, ""),
            ("1qwrxwc355Lun7LncWqTQW-pKhImbm0km", "Customizable Modules Project Plan  5.28.25.pdf", PDF, 587251, ""),
        ],
    },
    249: {"source_folders": [], "files": []},
    403: {"source_folders": [], "files": []},
    455: {"source_folders": [], "files": []},
}

DEAD_FOLDERS = {
    96: [("1CgqM9zyZFW3WNISNcSAMyFr5B-QC06vS", GONE)],
    98: [("1de31bOJDCr1kp1L7f2KvQIlQXCVVXcRd", GONE)],
    102: [("1EyjYqyZ_arGIbhUBjjj6kIywwqDkpb4I", GONE)],
    105: [("1wGrEhXT4jgcVzFa2LP9aqY49w9L9N6Gy", GONE)],
}

EMPTY_FOLDERS = {
    114: [("1paJ73jy3WaMw9NRiQVqZSMz3LDZ0WrE6", "Engineering ")],
    115: [("1VgT1FhZhuQcLV2UkCwpgS21X6BeeXoG-", "Engineering ")],
}

SUBFOLDERS_TO_WALK = {
    139: [("1BAFzWc2RkvFhijDZ-Yilv6J_6FRtPAvB",
           "Solution Related Docs (Prepared by Zukhruf based on Figma) "
           "(level 2, under Engineering)")],
}
