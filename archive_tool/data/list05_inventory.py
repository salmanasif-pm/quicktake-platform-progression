"""
Real Drive inventory for List 05 (Closed Won) cards, gathered read-only.

Only cards whose discovery is COMPLETE are listed here — that is, cards whose
linked folder contains no subfolders, so a top-level listing is the whole set.
List 05 folders are live project folders (PMO / BA / QA / Deliverables /
Requirements subfolders), so the rest need the one-level recursion the script
does automatically.

Entries are (file_id, name, mimeType, size_bytes, containing_folder_name).
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
SLIDES = "application/vnd.google-apps.presentation"
PDF = "application/pdf"
MP4 = "video/mp4"
MOV = "video/quicktime"
DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

INVENTORY = {
    17: {
        "source_folders": ["1DVEn_yV4KJ8DGN0YbgIZZy5HxmcXjLoy"],
        "files": [
            ("1i3ECv-CE6nj77_zkhU84oifYPaIkO0i_", "video1535138495.mp4", MP4, 177110916, ""),
            ("1e33FSwWwe--xjlUiC6y4pVZavZO1sHoi", "Curtis - Engineering RoadMap .mp4", MP4, 528484828, ""),
            ("1ezqPo8zecXuoa7Q7ZA4ffe2gEEXdylwEquv4c1vM7CU", "Laboratory Results Data Visualization - Roadmap & Estimate", SHEET, 19993, ""),
            ("1yhomjnZqOJ-lszNyi9WjB2Bz0bcWiGN0", "Technical Requirements - Kurt .pdf", PDF, 65778, ""),
            ("1AJkhS5f_cm7mxsXAXcOG61ZKjGT4t9As", "Curtis <> PureLogics .mp4", MP4, 263130556, ""),
        ],
    },
    24: {
        "source_folders": ["1Ybw9e2iJtVlmfXJZ7Xab8qizd6q38O-y"],
        "files": [
            ("1A5aK88GZsBRe-UUV1XjdFc_dC4qF9K3J", "Upling LLC | GoDaddy to AWS Migration - Solution Comparison.pdf", PDF, 637185, ""),
            ("1vTrvzaqA3uRSHKYBf1-SXiJqAy2myYB3", "Upling LLC | GoDaddy to AWS Migration - PureLogics Solution Advantages.pdf", PDF, 2084584, ""),
            ("1nYsPtE-K4evBNLmVXcS-VF11TOJCWYpP", "Upling LLC | GoDaddy to AWS Migration - Development Phases Diagram.pdf", PDF, 6188473, ""),
            ("1FouteL6P8m6H7YHSaHwBZebebyPWcUkJKmh3XA09xho", "Upling LLC | GoDaddy to AWS Migration - Roadmap & Estimations", SHEET, 381591, ""),
            ("19bpb1SVPqLJEUqxBTwlKddOTxDBfs_1bE26Bd9y6KcU", "Upling - GoDaddy to AWS Migration  - Proposal Document", DOC, 6382652, ""),
            ("1NEWqXSsRzuS5O4zK3lzgnULCbVaUG7ltAe-zk21nUKE", "Virgent AI - GoDaddy to AWS Migration - RoadMap and Estimations", SHEET, 19650, ""),
            ("1I45UELkm9m7PJqL0rUrxPf19R5T3hZYLVASK3ZPseI8", "GoDaddy to AWS Migration - Solution Document ", DOC, 24941, ""),
            ("1yiynB9yVcJzaUB6Bd--gLaYhH724PHGV", "Architecture Diagram.pdf", PDF, 932445, ""),
            ("1YWQwnxqIeKa4CX_dHLm-oH9gP2h1_5k5", "Upling Update with Backend - Jan 3.mp4", MP4, 169296288, ""),
            ("1aETl2asmwKm33ONqTJLYJr9lBGuf_1bu", "Upling Update with Backend - Jan 3 (1).mp4", MP4, 169296288, ""),
            ("1yK8ZXUCOHWEYZUXZMLhD2Xfc2Ky958tN", "Engineering Call 1 .mp4", MP4, 87286104, ""),
            ("1i_49hDU_fWihe60kYOuh8m0eMJ9n1vhv", "Technical Document_ Cannabis Delivery Platform Enhancement with AI Integration.pdf", PDF, 62948, ""),
            ("19AVGwiBF0ra3m2yBEodfqDCmTK8dKthN", "GenAI Workshop Knowledge Transfer- Upling-1.pdf", PDF, 616736, ""),
            ("1FNMEoYglUOP48hlZDJkm4ZtiG6wkNJNj", "Engineering Call 2 .mp4", MP4, 461131444, ""),
        ],
    },
    49: {
        "source_folders": ["17NPcdZA5FeW6Ji_YDRVO6gyAGV2_74wP"],
        "files": [
            ("1R3FvCChSWaudPjTN6bUfTdQ6W88_wXRqqVgFrMjk0CA", "Tombola Application (Updated) - Roadmap & Estimations", SHEET, 20025, ""),
            ("1opgOtbtk4wXTmu3cJhz18oOc5YW7z1z1jg9k7O5DY8A", "Sports Application (Updated) - Roadmap & Estimations", SHEET, 19355, ""),
            ("1hBdGclXXIq0t-lXaCyzSCsgpHFpR6TYLyfJOpZwtDaQ", "Tombola (Lottery)- Roadmap & Estimations", SHEET, 15926, ""),
            ("1CYvSYI5lFcAxLe3DrDNdAlatvmTunOSRJUtEYj3BzhQ", "Sports Application - Roadmap & Estimations", SHEET, 16083, ""),
            ("15QhKsSHSwcE5wigk8YtWI9fya1JUw1rp", "Sports - Specifications (1).pdf", PDF, 5974104, ""),
            ("1i-WWhX3fsxFxoeJjiQqlt7B_jG7W2UXe", "Tombola (Lottery) - Specifications (1).pdf", PDF, 5732204, ""),
        ],
    },
    104: {
        "source_folders": ["1Q1CylzAK4YFxiaPJjlb-Wyi27njfihXS"],
        "files": [],
        "error": ("folder:1Q1CylzAK4YFxiaPJjlb-Wyi27njfihXS",
                  "Requested entity was not found (deleted or access revoked)"),
    },
    168: {
        "source_folders": ["1xUF-O16U0CwOyS8bQJNvG25_Ypdm0o4_"],
        "files": [
            ("14edW8mRcv-EsJGCHAUvtH42wDVzUUOfrf4WwCdjLb9A", "ECommerce Store Development - Roadmap & Estimate", SHEET, 29307, ""),
            ("1A19AOFDEE1UAt0Ix87eLwFaa8_QUjsHN6F_je3BUVCw", "Background & Context", DOC, 2827, ""),
            ("11Bmr5Vq5Fh8SRMoJSrQfVLX6G9qZnygBvJOw2n6r5aI", "BA Team Deliverables", DOC, 1024, ""),
            ("1o6VxB8yIgbHwgl4gaGLN1nVLDGJP4_K-aIiTPyrxms0", "Kitchen Cabinets Wholesale LLC ", SHEET, 25889, ""),
            ("1dFa6s5Zw0B-k0KmTiWX4JjccL6AKMYbK", "Highland Cabinetry - Tech Recording.mp4", MP4, 127565827, ""),
            ("1oXo_vbNKsMAVeFxT1J4WauN-Dc4odHvC", "Highland Cabinetry - Tech Recording 2.mp4", MP4, 123860196, ""),
        ],
    },
    203: {
        "source_folders": ["1nHu4p6SIYz00EE2mVbN8ySQBljfe63Ji"],
        "files": [
            ("18o0pTHQtABqOmCeKXJPiZZg5jUiYakaWM-aTjRcnw3k", "Data Collection - Mobile Application - Roadmap & Estimate", SHEET, 19956, ""),
            ("16v-du32V6ZmEM5CEuqbOB57RqskE0xdc", "Recording.mp4", MP4, 32435813, ""),
            ("1vXTTbjYIVi0uQYlWtuegYxVNhG0wpVsE", "Requirements.docx", DOCX, 199643, ""),
        ],
    },
    122: {
        "source_folders": ["1cSBUKpPhRTDBHuyJbzBmT4T5nZis9JwO"],
        "files": [
            ("1EKpcr2_E6EVvp9Ho7kLHq0Cu_oBQ6eB83crDDlIIKS0", "Transcript of Meeting from Scope discussion for MoneyMate - March 20, 2026", DOC, 18906, ""),
            ("1iFvfqoCt1A0aw8m6Kg9BG3ht8metWRuFFRY_8xZzxhc", "Emails recieved 24-03-2026", DOC, 7728, ""),
            ("1Tzil9edXE7cQ9I5YA6yoBLIkgf0jajBiw0ZczL7kiu8", "EpocHarvest SOW Review - Elena Findings vs. Change Requests", DOC, 19088, ""),
            ("19X5useLF0_ahm3tE9fxtPG-oOc-C0NcWGLWnDFwBLZc", "AWS DevOps Engagement Rules - MoneyMate / EpocHarvest", DOC, 10527, ""),
            ("1CVE-7Eg2wrXCqgC_pbN-br4zX8pVX88BrBe2Vg0LE0k", "Quries from Prospect's side", DOC, 7603, ""),
            ("1XB63VfLY7RdUOkCZxhasmR2zZxL1dmld", "MX_API_Call_Map.pdf", PDF, 396738, ""),
            ("1F9ImG3igqYq7jLMUSyPzvvvA9jX1fkaP8p5mJOrUT5A", "PM Tauqeer - R&D", DOC, 4545, ""),
            ("1q9vTDfsWUI87jcaWh-JZJvEMU6tj2y7YcqPu_xvjawA", "Email Responses", DOC, 4512, ""),
            ("1DazOVasEHhWFVVCwilGlmAXUPCVZ2uwB", "MoneyMate_RFP_Plaid_Migration (4).pdf", PDF, 158554, ""),
            ("1Fqv1x4lqXXkTN_9EK-lSMEPoFcQXDj9F", "MVP 2.0 Technical Requirements V4 (1).pdf", PDF, 7637286, ""),
            ("1NAYroiwRBhnSk1_ZAfnOei2Fy03_q7G6j6g7OWIFz7Y", "Details from Client on 5th March", DOC, 934062, ""),
            ("1-EzLdcqefbxF-AKLNUzljfcRy07aj-3dUJTYUHdxQuU", "Dev Request from another company", DOC, 2576, ""),
            ("1X5y2SojlVwE44x5PZBhgeMvtkUIkPeVBDAxC_ic605s", "Scoping Meeting - Integration, Account Identification & Feature Support", DOC, 327856, ""),
            ("1N4xRC0CsHwi8v2gy5lGT3DrMFCCHp8FAP2GtppbiNlg", "Last Email", DOC, 9963, ""),
            ("1FfGvSGo7_8IGrXXqc81cahYr4QXcgPjo", "Money_Mate_Code_Review_ (1).pdf", PDF, 31097502, ""),
            ("1T1oVrtxc0dmW0UHyscPq_1qx1uL2_mvo", "REQUEST FOR PROPOSAL - Plaid Migration.pdf", PDF, 136148, ""),
            ("1xdUpMjBtls_5C3HlKn8NKMFsSUvNVq4T7yV9KXXQcj0", "Email from Cleint", DOC, 2794, ""),
            ("1RXxsm9BgaYYZxK-92KI296_bqP2KDHXC", "Proprietary Information Intellectual Property and Nondisclosure Agreement for EpocHarvest Inc..pdf", PDF, 243788, ""),
            ("1ZmO1DOy2f5m7hrnSx72Il8YrO0-LP0BSO2afZ9c0iZ0", "QAs", DOC, 4145, ""),
            ("11UjKwZ4hDbLuh32wV8ZzrBimVqc2NYtM", "Intro call.mp4", MP4, 97122861, ""),
            ("1Tl1X3ygup6HfZiLpBOlWo1J3--Tj_mYJNjAQOlqXcFM", "MoneyMate |  WorkFlow & Kickoff Document", SLIDES, 1095233, ""),
            ("1uWSNHnClXXv1Y7nbk3pl0up6C3ZmsN56XC96sJKO5B8", "TechDebt Management - Roadmap", SLIDES, 512660, ""),
            # subfolder: Phase 2
            ("1TXAyNyjudzfpPgmst96O090J_h_e-GmL6qvJcJC93UU", "MoneyMate AWS Infrastructure Readiness / Observability Change Order", DOC, 20356, "Phase 2"),
            # subfolder: MX to Plaid BA Deliverables
            ("13a-vox5eill9hblfmSQU1lu4gapExrWZJKPw-o8BY3E", "MoneyMate - MX to Plain Migration - Task Breakdown", SHEET, 4115, "MX to Plaid BA Deliverables"),
            ("1vuy6O8zR2ncFGvKeIKKDMQ6U-dbsG76-", "MoneyMate Proposal - Proposal Document v1.1 (Plaid Migration & Targeted Security Remediation).pdf", PDF, 678051, "MX to Plaid BA Deliverables"),
            ("1GnD7cIFm_BY9JaZzfXgcXdFXi-FM3YyK", "MoneyMate Proposal Technical Companion - v1.1.pdf", PDF, 638686, "MX to Plaid BA Deliverables"),
            ("17UxaqIeQZdLjPrH3TZHlE2qqZNPAFcVZ", "MoneyMate Proposal Change Log - v1.1.pdf", PDF, 148384, "MX to Plaid BA Deliverables"),
            ("1eWbmmEFrGmnIgPyjiVovQfnuhycRaJ2A2P9GO8kmJmM", "Email March 5, 2026 - Next steps before our scoping call (CI + routing/I&E pipeline)", DOC, 2715, "MX to Plaid BA Deliverables"),
            ("18PdcIltOJrLiiM-1iwcZ6rHo1l7_TH7xn_ptcNLnskw", "Email - March 4, 2026 - MoneyMate Plaid migration and a few quick pre-reads", DOC, 3793, "MX to Plaid BA Deliverables"),
        ],
    },
    204: {
        "source_folders": ["1TdfvFOoLzOYwpgxd8pSwqoLC8PEjhW4j"],
        "files": [
            ("10cl6aRbiyKJA_sHCQbQuua5z07CMd0v5", "Berd (Tech) - Recording.mp4", MP4, 463926556, ""),
            ("1z8UkHKATI6ug1J_sdG70WcVx4RitaxJA", "Berd - Prekickoff Meeting.mp4", MP4, 170086223, ""),
            ("1T9vHDMeiH0WjSdtrUsYTzL3_y5VZo5YEK3MXJJOMtM4", "NOTES Captured", DOC, 3426, ""),
            ("1Wm_8Vf5MK0sOkRhFF72VPfB8qO57VVCDD_ctL-x7kNk", "MIRO Diagrams", DOC, 1024, ""),
            # subfolder: QA
            ("1ZtZxcljydqwwvKiSQ2eYDpQGP_iY-pH_NHPBgP4Dw40", "Berd Spoke Test Management Sheet", SHEET, 31517, "QA"),
            ("1IyRHpNX6VZG5vW5jabGPYzZ9MxhHttpB", "Berd Spokes Test Plan Document.docx", DOCX, 17866, "QA"),
        ],
    },
    422: {
        "source_folders": ["1SUcHFYDRj28jThUll2wz-jOhohZ4HIIq"],
        "files": [
            ("1w2bhGjyC0iZBLR2iXFlvCO9JDT0dUH9I", "Intro.mp4", MP4, 216883765, ""),
            ("10mQ45a98b7ufCtklPK0kZYBfjKSZERyL1vo6UMcUOaQ", "SkillResy Mobile App - Roadmap & Estimate", SHEET, 82426, ""),
            ("1PTf91jXxiSWGYmdrBeFjBuTvne4t9obh74dRRruHWcU", "SkillResy Web App - Roadmap & Estimate", SHEET, 29399, ""),
            ("1woqAgPqBRo0uC0UvC-9EZru9iMHXOZFc", "Interview Assistant (Dark Mode).pdf", PDF, 1924531, ""),
            ("1OL3mAnoVHrrEAUXSd71Qa947GEdmqLEp", "Interview Assistant (Light Mode).pdf", PDF, 1929522, ""),
            ("1EaIV8Au4NM3gmrIoKDI32CIUtEBfip_jMqtylKfOu58", "Marketing Requirements", DOC, 3046, ""),
            ("1Q67Pn1Ej8er6MnKiHakc_cJ0ckEVW4y7", "2nd - Trimmed call.mp4", MP4, 98580388, ""),
            ("1mu9q8AZhHDsi5kBooj-ZUg0d1uOYHtRisVOWb7ZG1Gk", "Notes & Requirements", DOC, 7119, ""),
        ],
    },
}

# Cards whose linked folder DOES contain subfolders, so discovery is not
# complete here and the script's one-level recursion is required. Recorded so a
# later run does not have to re-list the top level to learn this.
NEEDS_RECURSION = {
    41:  ("1SHRzslEwud9zYHY7rvakKOEE1xFsH3Q5", 12),
    82:  ("1Vut4AX2L5vL_wOxVIesbG6-6bUMlg9Ad", 9),
    109: ("1qZ8vEoG0eH7l5Jd4ly0fdJwSMIfusgUG", 5),
    122: ("1cSBUKpPhRTDBHuyJbzBmT4T5nZis9JwO", 2),
    202: ("1CxvqCkQvfjqYGnVQNTIMNGfMue58ayLJ", 7),
    204: ("1TdfvFOoLzOYwpgxd8pSwqoLC8PEjhW4j", 1),
    205: ("1-EjvI0QHlBzyImiOX_fDBjI7TErzFfjT", 10),
    206: ("1ATu9B-oegm2pH-xAT5UdXqQ7oZqvP-um", 7),
    422: ("1SUcHFYDRj28jThUll2wz-jOhohZ4HIIq", 0),
}
