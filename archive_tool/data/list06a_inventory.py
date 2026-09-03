"""
Real Drive inventory for the first List 06 (`Closed Lost`) batch.

Cards 18, 25, 27, 31, 32, 35, 36, 39, 45, 47, 48, 53, 56, 59, 60, 63, 65, 66,
68, 72 and 99. Entries are (file_id, name, mimeType, size, folder_name).

Closed-lost cards are small: a roadmap, a requirements doc, and the sales
call recordings the spec skips. Several resolve to zero copies and are a
`card.md` only. Cards 60 and 99 point at the same Drive folder (Lumondt), so
both archive the same six files - the spec's structure is per card.
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
SLIDES = "application/vnd.google-apps.presentation"
PDF = "application/pdf"
MP4 = "video/mp4"
MOV = "video/quicktime"
DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
XLSM = "application/vnd.ms-excel.sheet.macroenabled.12"
PNG = "image/png"

_LUMONDT = [
    ("1ELoihge2nQWeTpc5r9TcuRjI5JtVWo1ICOSh2nL_7bs", "Bailey - Roadmap and Estimate ", SHEET, 34088, ""),
    ("1mY9zAnK6cF4QJwtclFJVOS0bx9P3S02C", "We Love Expats - Master 3 April 2026.pdf", PDF, 3483886, ""),
    ("1k1IqbAaNWwvCBBypgZkWQ9xlWXwbDBaKTuOkgAArvD0", "Bailey - Roadmap & Estimate", SHEET, 31588, ""),
    ("1Vq6mttDT9mMr_3ZYUrDLTHHexZRFpkJU", "Lumondt - Next Steps  - Nov 10 2025.mp4", MP4, 303393729, ""),
    ("1UAYw3lIA2B73mZAlIrU-MfNbePNaK6AchHItksX_-Vk", "Project: Meeting People App (Working Title)", DOC, 8583, ""),
    ("1LNS6KZE1ehEdHXYzPoGp3mvOLQWze8Wu", "Impromptu Zoom Meeting - Jun 25 2025.mp4", MP4, 385024131, ""),
]

INVENTORY = {
    18: {
        "source_folders": ["1VriKD1lcXZo8XuYTz3mZepgmXxN79-yO"],
        "files": [
            ("1gRB-gZNLfpe91f8jzCPB1tg9KQmPzNg5", "ThirdPartyApiIntegrationPKCE.pdf", PDF, 263596, ""),
            ("1HQ_Y9zzLh_fJtjhJWg-TX42iRA-pxIwl", "video1417315044.mp4", MP4, 50208939, ""),
        ],
    },
    25: {
        "source_folders": ["1QDWImsX77ABUsxgC3OCZeQ9mi3vhEQy-"],
        "files": [
            ("1SqL1bW5kxO9bxELiVvLkf0fLSmviyqPR", "CRM System for Employment Specialists - User Flow Diagram.pdf", PDF, 918333, ""),
            ("1H9OII-oT4mT3ou5VHn_H-QhJj_xLTZIh", "Vocation Depot - Aug 13 2025.mp4", MP4, 171410934, ""),
            ("1BHLJ2QSyZTvc5B8UAhjeGPFKNt650cnQ95rMXPlEdbg", "CRM System for Employment Specialists | Hybrid Mobile App Development - Roadmap & Estimations", SHEET, 45432, ""),
            ("1UBdL_DMQvhLIXcz4TpeC9BbzxZnUth2L", "For PL _Copy of KPI Spreadsheet 2024.xlsx", XLSX, 540828, ""),
            ("1KkySzBcPjOgtWbO6LyqilKehvE4lAB5H", "Meeting - 10th Jan 2025.mp4", MP4, 171453739, ""),
            ("1Om5caA2LODzwP1MqTht64jaZI9wVLTc18Ija0Vm-8zE", "CRM System for Employment Specialists", DOC, 6617, ""),
            ("1giKAOaRRGaLtXXthHZFoJhnNJ4MaAlTs", "CRM - Engineering.mp4", MP4, 410179630, ""),
            # subfolder: Documents 1
            ("1drrBaPljh13dKAE-LpkDLRNb5l62lmKm", "VR FORMS.xlsx", XLSX, 80756, "Documents 1"),
            ("1WXtqt7KN42yPz3agvLnCyQUtQUnvxOUF", "Referral Types, Benchmarks, Auths Exports.xlsx", XLSX, 71812, "Documents 1"),
            ("13-JulHy--RLH7NEEYGuG8snJGSpDLaMY-wDPL_SLwe4", "Context for Documents", DOC, 2597, "Documents 1"),
            # subfolder: Documents 2
            ("15o_x7B0PU2SyoKUED5XfOXaDUoKMUGX-", "Pending Billing from Aware.xlsx", XLSX, 10617, "Documents 2"),
            ("1fP8DicDm324_3v3s3R7UQ5GOK9G0I4brRbGtYWDn93E", "Copy of Example Billing Sheet", SHEET, 3654, "Documents 2"),
            ("1_r__Dy8LGlvf2YIAecI-jV90MhiDH1hG", "Referral Types, Benchmarks, Auths Exports.xlsx", XLSX, 75301, "Documents 2"),
            ("1UySflY5tDkvaR4cahAwX5s0EmT14KYkd", "FLAIR Billing - Paid.pdf", PDF, 134122, "Documents 2"),
            ("1veo37r4gMpQX9aEPMsiqc1pLG3H_S7r4", "Aware Draft Authorizations Download (1).xlsx", XLSX, 9670, "Documents 2"),
            ("1e1P0KNH35waUsynB7XCZ8wAOnkm7FkV0dv1y07yMT94", "Context for Documents", DOC, 1024, "Documents 2"),
            ("1Zi6VaE5kjK08uu3S2kZcTSD-cMKlQlCc", "Processed Billing from Aware.xlsx", XLSX, 10467, "Documents 2"),
            ("1_4G3PL0iJ3FazSzPxr2CPQ8LlbGq8sQW", "Aware Open Authorizations Download.xlsx", XLSX, 9860, "Documents 2"),
        ],
    },
    27: {
        "source_folders": ["1pq0wk8eb9Rk8dKXDmbaTWSt8Mx5l9RWC"],
        "files": [
            ("1gnQj3TvLc5IhL6wD-hR_nPlIuiErSnPsFvRuFs8_L5c", "POC - Accelerate Learning - Roadmap & Estimate", SHEET, 30069, ""),
            ("130vSZLqF8d1mfMmw6V1mYfQgSj6_uFWJglkXiL20vpA", "AI Education System | Phase 2 - Roadmap & Estimate", SHEET, 19752, ""),
            ("1sxnwcVilWV0lzwnxAq4VMPNTn-Qjg7j5WBVFRdyfSBI", "Accelerate Learning - Roadmap & Estimate", SHEET, 37605, ""),
            ("1KPuTEAkHyHX9dpE2OpUp_jyDu9Ll_6J-ZEZnKi2b64U", "Project Specification Document - Exam Generation", DOC, 4673, ""),
            ("1Ly0v2tbomnI5cccrALBp99m8ZKHFq8bX", "Dan Wearing - Engineering Final Meeting .mp4", MP4, 59603113, ""),
            ("13eKkcK4Woh85XW4WLoSLFnnRFD5KW54d", "CEM Select.pdf", PDF, 57342, ""),
            ("16LbL9SpbzDbNADT2FNi-wtrri_AdLmOR", "Primary Insights Test.pdf", PDF, 1607374, ""),
            ("15mN6Y1vOOacQl8ggxGLho2_bPOkhbQQ6", "Dan - Engineering MVP .mp4", MP4, 98112638, ""),
            ("1rUMWSa4CW4B475TA8erYwP0C4CmKfRWh", "image.png", PNG, 218157, ""),
            ("11s61UDpEWVd1-d5hW93EGZG78JjHbp4Y", "video1089352205.mp4", MP4, 78594163, ""),
            ("1bRaGEQfAM5bywmpC0mGk4zZThpyZizqSTDCIg27FgUg", "AI-Based Education System for Personalized Tutoring", DOC, 5828, ""),
            ("1Otd5a5J0wfLUl5TMquvsPLKryrHGWDw5", "Daniel - Engineering.mp4", MP4, 23055608, ""),
            # subfolder: Internal Meeting (recordings only)
            ("1xuOJGov6StQwSD4e1KJjpHZfNcS4P--I", "video1830195914.mp4", MP4, 77169762, "Internal Meeting"),
            ("1TETSnJmC7OQaLbD2Vvq4g9Kp70YbBrbp", "Pre - Kick Off .mp4", MP4, 47017614, "Internal Meeting"),
            ("1sy_x9IiaUTvIdWKj4Goc3RKXw_NCJesR", "video1298848136.mp4", MP4, 126825721, "Internal Meeting"),
        ],
    },
    31: {
        "source_folders": ["15sw4aoHmCnea7dVo9WWoZUMBZ9VsX1Yw"],
        "files": [
            ("1Rnqrm7bLCggnJXsuKZEkaGxbnuiF47oBkk0pmSBWyBY", "Task Progress Web Application - Roadmap & Estimate", SHEET, 23974, ""),
            ("1jckXMJhFT6TXzVgB-6HMz6fSjnCJSST8KURtH7El81g", "Task Progress Web Application - Proposal Document", DOC, 5975040, ""),
            ("1a_2Xhhp269I0qEApDGCut-i5YayNCV1F", "Bildschirmfoto 2025-01-23 um 16.39.30.png", PNG, 138071, ""),
            ("1AV_W0HgA4vU6wDDp6cg3XeSVPMICfDvu", "Bildschirmfoto 2025-01-23 um 16.34.55.png", PNG, 49754, ""),
            ("18USlrx_oJ3YyVvAw9MWfsd6m_T2EiCK4", "Bildschirmfoto 2025-01-23 um 16.35.14.png", PNG, 43271, ""),
            ("1Ve1AzvqMcCwAb_mUUh08iDS8WHWdAQqsTQLuIrEDs8M", "Client Goals Tasks Progress Application", DOC, 4946, ""),
            ("1uuZfeDZ05yfDgtRmkQFg0aeajpshAJMx", "Cassie - Engineering.mp4", MP4, 80327938, ""),
            ("1XmOxFUrBvfZbADHiadzKh5osDVaZ4xKiiseTkwKgIWo", "Roadmap - Cassie ", SHEET, 23646, ""),
        ],
    },
    32: {
        "source_folders": ["1Srl08MFxOV4Re54D372xafoqVv2ZpCX4"],
        "files": [
            ("1LwmvzMakvRwridoehVvTZIhU_nv2Yh0wIV2fY5IFWBw", "Concierge HealthCare - RoadMap & Estimations ", SHEET, 23646, ""),
            ("1RakF4vsmvcD68d9pJj_iBXR4C0Rw819E", "AHMED_COD_video1210806721.mp4", MP4, 22008747, ""),
            ("1e1kINjz1UgF93tw5elf7x2hJL5TEs9oZXUuYh45SC4g", "Care on Demand Type APP Technical Document", DOC, 4556, ""),
            ("1M-JeDrAu4G2zIwGe7LaQKtWCRRhNYpvL", "Rob - Engineering.mp4", MP4, 168258037, ""),
        ],
    },
    35: {
        "source_folders": ["1e-iJFKzhENuO6R2QH1KEoHEw9Adu5GbV"],
        "files": [
            ("128-bMiFR1AlLvBXUaJOlk-UuTSLiCcdW", "Untitled video - Made with Clipchamp (5).mp4", MP4, 108909976, ""),
            ("1mkbdSI6sgxvA25vXYu_k_32RyU25JP-x", "SkyOcean - Process Flow Diagram.pdf", PDF, 1720789, ""),
            ("1Nsmxe4AYXCpG9bwZXc3dQ_mkPuJQqNVwxSnRCiz_9k4", "SkyOcean", DOC, 7748, ""),
            ("11WSE8JpgBXCAJ6_7KWD6SPKHuZoD8Q75tJ9EOV-srME", "MVP Progress So Far - SkyOcean", DOC, 2900, ""),
            ("1XAI5wZY_svuGEAU2oL6NfHk3Yy-ClG8K", "video1226908924.mp4", MP4, 118516247, ""),
        ],
    },
    36: {
        "source_folders": ["1Z28llIypHpVCuZL7OyGjAua6wX7ulD2q"],
        "files": [
            ("1UKAVn7p2Zc7VcAIMz6vs6gofxW6ZdArtk9CXmlcpP_0", "CK Sorting Station - Roadmap & Estimate", SHEET, 19969, ""),
            ("1xow1n9yd53wwcJQAGt_XAN7iD_5taSKR", "CK Sorting Station - Process Flow Diagram.pdf", PDF, 502992, ""),
            ("1mIKjwk4eOLY4SHaflmZ8b97s1OdszYm4", "CK SORTING STATION PTL.pdf", PDF, 473477, ""),
            # subfolder: 2023 Requirements
            ("1CIz5b1Ljq-NapWYFDpmj_5q2TWe1-Ihctbt6ttoEyjs", "Chasdei Food Application - Roadmap & Estimations", SHEET, 6292, "2023 Requirements"),
            ("1wAorYlyMUhY7z4w-zpocoVXImpm1HcmtPViZKTY_pQg", "Ariel Requirements", DOC, 1064, "2023 Requirements"),
            ("1XvdP1b2Vx-lH0rPIRP_-286CbC3t7yF8", "Jetnetix_Feedback5.docx", DOCX, 8985, "2023 Requirements"),
            ("12wxqV0hGLrmUarf3jDo4AswFZFs5tody", "Ariel Trimmed.mp4", MP4, 85471434, "2023 Requirements"),
        ],
    },
    39: {
        "source_folders": ["1jBh1BkKFaPyKYAMTId8irGQ7uyUrK9qR"],
        "files": [
            ("13gmjN6MMc_MnRaAkgmFFQzm-hdT6f43RqalZ8z6LpE0", "AI-Powered Real Estate Proforma Automation System - Roadmap & Estimate", SHEET, 24242, ""),
            ("1I8CFLWN8j_ShZDyWZyqPQhX1ude6F_fPUUQfCIw4zsY", "Technical Requirements Document - Real Estate ", DOC, 8280, ""),
            ("19zZGUtMWfViv3jZX4HXZ2v4iI0ydwWaD", "video1529948729.mp4", MP4, 157998972, ""),
        ],
    },
    45: {
        "source_folders": ["1_OoRsIzXDK55CDIOBvG2Ta7BkAn-z1Ic"],
        "files": [
            ("1rGvPH9D-h9W64QPtvICdShY41Ng-wmv51l1B-TQhMxY", "SIS Dashboard Development - Roadmap & Estimate", SHEET, 24284, ""),
            ("1rA_vvYLkbun6yzj6ALGcbPQ_Qc3WzGe-", "The Gowan Group - Presentation - Apr 8 2025.mp4", MP4, 431978614, ""),
            ("1P6T75NZ-ZydOyHypiZ8-im68bLu9olEt", "Enrollment%2Bexcel%2Bfile--sample.xlsm.xlsm", XLSM, 391617, ""),
            ("1YNj9huOU0sVW3ei9_PFN7LP4s4SrbrxypYXXc-CU25Q", "Data Ingestion Automation via Excel VBA Macro - Solution Document", DOC, 1574374, ""),
            ("1kRiBXJYISHgnF1MB0mCu8YfN5crTgcWS", "video1860898308.mp4", MP4, 181601752, ""),
            ("14m2KJI35IK5PdusJVJvwKv1Mv5JjWS78", "MindMap | School Data Dashboard System.pdf", PDF, 124291, ""),
            ("1Tk4OFjPZHhmijBhQF6ILM049do3kk1ck", "Purelogics X Gowan Group - Mar 28 2025.mp4", MP4, 248928672, ""),
            ("18DZqCJAMITDiLKVLNp4gcubOTPxAT00qJON7ozHm0DE", "Dashboards", DOC, 5817, ""),
        ],
    },
    47: {
        "source_folders": ["1eOdF5_t8BEAdTxwsn2i24KiwdwGuPxzK"],
        "files": [
            ("1Yn0I1hsXvevU6FfwHqu5jhN-_vmjpBuF", "Summit2 X PureLogics - Apr 14 2025 Engineering.mp4", MP4, 251384463, ""),
            ("1n4TGZpGnyfHzp3tccb4RzZeXtjAuCtIpdHRrZQ02TyQ", "Technical Requirements Document - Project Martha", DOC, 6331, ""),
        ],
    },
    48: {
        "source_folders": ["1uy1NQuopxVlKHcMM5-iG4LnwYcqYj9ZK"],
        "files": [
            ("1k75zU_viXCZvFDwDJubIXpINpuWwMLHO", "Engineering - Nadeem .mp4", MP4, 34731948, ""),
        ],
    },
    53: {
        "source_folders": ["1zBEOqkg3UWZLmPdf4NiymhT_MlDA-f0t"],
        "files": [
            ("1GbzwROdpmLjijs-c5ZELeCTxKRublX0fIbfGCrUryVA", "ADAA Microsite - Proposal Document", DOC, 6241062, ""),
            ("1loPUvBNRZE5EqhUW2BbpJ-cd0Xj1G0A-", "ADAA Microsite – RFP .docx", DOCX, 37838, ""),
        ],
    },
    56: {
        "source_folders": ["1NSAtSjU6XR4KFa84SjcLTSguvgW6nyCo"],
        "files": [
            ("1Lx97jWyrMP4pHQvD-RmwrDhQZxQiepo9", "Engineering - Stephen .mp4", MP4, 192333875, ""),
        ],
    },
    59: {
        "source_folders": ["1uNDPWL_A62XPrXfXpYA_PIhesv0zsfiG"],
        "files": [
            ("1UG6l76JTlcuW1BSvmu-_ehS_vj9ePZGl", "Chris - Loxo  - Oct 2 2025.mp4", MP4, 234228425, ""),
            ("1U2zk3uyfM3BsQsNwgEG_jsDZ6jMMIoiEK6ViSMNyhq8", "Read Me", DOC, 1024, ""),
            ("1ojAxWUjNp5RkwTwY9iulApAL5AKEfXpq", "Chris - Email Bot  - Sep 9 2025.mp4", MP4, 98229514, ""),
            ("1TSw7GHl8yENh85nmMWlKen6gHURew-si", "Chris - Engineering .mp4", MP4, 210139473, ""),
        ],
    },
    60: {"source_folders": ["1kk4af9x_5C8zso-yYucISBPT5R8oxzw2"], "files": list(_LUMONDT)},
    63: {
        "source_folders": ["14KsDWx26QQYKdAgmoi2BajpV8YbLMNT0"],
        "files": [
            ("1Gv7ZNgdWJUPEZPx6yAZjBA59bHERkDDv", "Admissions Angle - Engineering .mp4", MP4, 50677070, ""),
        ],
    },
    65: {
        "source_folders": ["1amgdNFg1gvjehWP98OvVx_8UlKST3PUr"],
        "files": [
            ("1-mC_sYA3CddKA8aDyu5UzHA6IduSGld0", "Julian - Engineering - Scanner .mp4", MP4, 545338858, ""),
            ("1a_U650D9d-97N_jb6eXz1DESBNvT0gKn", "Scanner App Requirements.pdf", PDF, 96350, ""),
            ("1yb92NU3iKeZ1_XfdMb6I4va7zitlfpf0", "MUEHLMEIER Bodyshaping - Jul 2 2025 (1).mp4", MP4, 262913946, ""),
        ],
    },
    66: {
        "source_folders": ["19oGM74AklA7EdTAVV1OlfHmcOyGElsHF"],
        "files": [
            ("1LVSqIEBaCbt-fpF9HQ9EPv8glLL1pZM77pkMkzFkkNY", "Todo Gamified Application - William", DOC, 9839, ""),
            ("1k0uovvVuLcZbc9T8qvus3-kr9ifZhy8t", "William - Enginering .mp4", MP4, 119566575, ""),
        ],
    },
    68: {
        "source_folders": ["13Kx79g4WWMat_uf3Pv8DxlTpKLDErUK9"],
        "files": [
            ("1Q4eS0gfPwrzhEec4N1MVSRBHXG4wXtWbanYmd3J6z1A", "Requirement Specification Document - Kimberly", DOC, 6907, ""),
        ],
    },
    72: {
        "source_folders": ["1rVEUiNWxETqL04xMWVFhxgvzGGw7poca"],
        "files": [
            ("1KtYNqZyapH6LmLzgFw3Q9gK6ZCXKGyPl-pCxdrpro7o", "Federal Opportunity Radar - Solution Document", DOC, 1476495, ""),
            ("1bjod8K3hHmpn7l4vsYO3PEozerBa9vBZfTXEdTKF8Hg", "Rusty - Requirements", DOC, 3638, ""),
        ],
    },
    99: {"source_folders": ["1kk4af9x_5C8zso-yYucISBPT5R8oxzw2"], "files": list(_LUMONDT)},
}
