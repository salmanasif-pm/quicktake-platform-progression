"""
Real Drive inventory for List 07 (`On Hold`) batch 07e: cards 145, 146, 147,
148, 149, 150, 151, 153, 154, 155, 156, 157, 158, 159, 160 and 161.

Card 145 (`24/7 - Upsell`) links two folders where one is the other's child:
`24/7 Call-A-Doc (Updated)` sits inside `1ATu9B...`. Its two files are
inventoried once, under the child; the parent's own level-0 files and its
other level-1 subfolders are inventoried separately.

  NOT_WALKED   card 145's `Original Repositories ` and `Database Backup` -
               a source-code export and a database dump, neither a sales
               artefact, both deep; the same call made for card 34's redicare
               trees. `247 Call-A-Doc Mobile App` holds no files of its own,
               only the level-2 folder `247CallADoc`.

Diagram calls worth recording:

* Card 155 keeps five numbered role flow diagrams plus `6. Flow Roadmap.pdf`
  - all diagrams. Card 158's `User Flow Diagrams` subfolder holds four more,
  and card 161's `Diagrams` subfolder six.
* Card 146's `MindMapping` PDFs stay source documents: `mindmap` only counts
  on an image. Its `Project Phases Diagram.pdf`, `Flow Diagram Health App.pdf`
  and `Gantt Chart Health App.pdf` are diagrams.
* Card 153's `GAIL logo .png` and `module layout example copy.png` are
  ordinary imagery. Card 161's `Solution Summarized by Prospect.png` is a
  prospect's screenshot, not a final diagram, and is skipped.
* Card 146's nine `SRC4U - Screenshots` captures are excluded by folder name.

Card 145's `.DS_Store` (a macOS directory-metadata stub) is inventoried so
the manifest records it, and is skipped as not a document type.
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
SLIDES = "application/vnd.google-apps.presentation"
PDF = "application/pdf"
MP4 = "video/mp4"
MOV = "video/quicktime"
PNG = "image/png"
DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
BIN = "application/octet-stream"

DOCS = "247CAD-Documentation"
MEET = "Internal Meeting"
UPD = "24/7 Call-A-Doc (Updated)"
SHOTS = "SRC4U - Screenshots"
MIND = "MindMapping"
UFD = "User Flow Diagrams"
DIAG = "Diagrams"
UDR = "Updated Detailed Requirements"

INVENTORY = {
    145: {
        "source_folders": ["1JdWY5cHp3jUg6Xkh7hiWm7nwfxQaOjph",
                           "1ATu9B-oegm2pH-xAT5UdXqQ7oZqvP-um"],
        "files": [
            ("1lXQWnhRUKyb3Xj7tfcwA8DxMD3gVYIDa", "24/7 Call-a-Doc - System Walkthrough.mp4", MP4, 6221000, ""),
            ("1sm-oKHKF_NM_Przs3b6GERoRbOVxwC3xeo3tUUgsPms", "24/7 Work Progress", SHEET, 1024, ""),
            ("1VN9tXxOrFUz76glw43bklhb9O0F_GFlX", "247CAD-SystemOverview.docx", DOCX, 11575, ""),
            ("1h_jPll-M-1yzIoFgiGykhE4AStPR1wcB", "247CAD- Roadmap & Estimate.xlsx", XLSX, 51225, ""),
            ("1AY7AXN-_IOdkNowZC0vHBIbM4PBV3Yqf81CpXSkXzQU", "24/7 Call-a-Doc Project Roadmap", DOC, 7272, ""),
            ("1LgCb5anU2_mSeNmeUNMWYYLbKwqsnNjZmnn8RRBqGPE", "Copy of Dev Estimation", DOC, 19308, ""),
            ("1FoL71tK8MO6Svqj3LKji4ApdVCyScQa3bVWx6Ml-tk8", "247CAD - WorkFlow & Kickoff Document", SLIDES, 434412, ""),
            ("1aRvIjmS1RcARin4LzW1FIDjpUSXHhUJUuIfISajq3_c", "Dev Estimation", DOC, 18464, ""),
            # subfolder / second linked folder: 24/7 Call-A-Doc (Updated)
            ("1b0tED6-FImu51Thx1HP3XRy0d1WTfcYQtBsppoRo088", "24/7 Call-A-Doc - Roadmap & Estimate", SHEET, 20399, UPD),
            ("19QpHkIMfAm1YbyD4uFty_n9a0fs_FImg", "24_7 Call-A-Doc.pdf", PDF, 67324, UPD),
            # subfolder: Internal Meeting
            ("1uZKTYopEk6f5piMSt3L9AK-ZxAwi-Sbe", "video1332897272.mp4", MP4, 23495025, MEET),
            # subfolder: 247CAD-Documentation
            ("1pxxZ8tiS5--rziNbFhGHOvHIfM4p0tKK", "Member Enrollment Overview.docx", DOCX, 10055, DOCS),
            ("1ZSPN0JAP9hyKuPBE9-9IHDc6ZwjIPg2-", "247CAD-DevelopmentOverview.docx", DOCX, 11863, DOCS),
            ("1Zvnk_tC5NIMSl4wBnPRw28UBje52MiC9", ".DS_Store", BIN, 6148, DOCS),
            ("1lZiyzKtGOFACyFl2IUoVLigIvGo3kPxO", "247CAD-SystemOverview.docx", DOCX, 18618, DOCS),
            ("1oeh6qCTZ-TY1OzL6DUimYmQyN4cbMidx", "SQL Server Agents.xlsx", XLSX, 11356, DOCS),
            ("15MH2UDa4Cg477O1un-DbP0OdPfVDPl1v", "Description of Disaster Recovery Plan.docx", DOCX, 39140, DOCS),
        ],
    },
    146: {
        "source_folders": ["1XML1zm1YHp5HNpYE31yWfaJa5-KBNwvp"],
        "files": [
            ("1rVFdsZ6lM6u0CbfFxALVLjdiSWYy2kDd", "Recording 3.mp4", MP4, 65394296, ""),
            ("1gFh9ExpIJqHm58TXtm33eY_GExYhuCj9", "Recording 5.mp4", MP4, 56937582, ""),
            ("1LF3WyALQ1HWgAMjRuxgUUJvNNPyxcAIq", "Recording 2.mp4", MP4, 159711365, ""),
            ("1c3C4PCd3NLGp4QAUapwHQPkIUFKESBKU", "Recording 6.mp4", MP4, 325168987, ""),
            ("1QYM96DTqA8pVclaqLjQPHRne-NagoDM8", "Recording 1.mp4", MP4, 295129989, ""),
            ("1E0PFNOSKEJ8ygyW_6bDvPNiX04LIHZjg", "REZOLVIΛ Creative Brief.pdf", PDF, 150303, ""),
            ("1oj1IHyVhgiPVCt9Tznl80y0VjXkjLoYGb354BS5S3f0", "1. HealthTech Mobile App | Hybrid Mobile App Development - Roadmap & Estimate", SHEET, 76552, ""),
            ("1-y8mvKOerFYIxN7h-wygfxoRmAllryUH", "Project Phases Diagram.pdf", PDF, 8644601, ""),
            ("1mTVNN76kposHWZMFCXhpxrGAklpCcknO", "Zeely Case Study- AI-Driven Growth for Shopify & Instagram Sales.docx", DOCX, 17188, ""),
            ("15Na3SERjMZAb0ZPDdaVuDN4JaUtpryzCJ2VpTUX90ls", "Latest Requirements", DOC, 18233, ""),
            ("1OWMpHdt1UzVLJNka-WEGiUk9gUtdt-tW", "Flow Diagram Health App.pdf", PDF, 58079, ""),
            ("1X40AWSPWwCxiaLLFBf10ZBTOXXNvu03x", "Gantt Chart Health App.pdf", PDF, 129011, ""),
            ("1tL3rAoEdeuEb6-dVG4lriDAAfRm9lFm6", "Expert Enzymes - Requirements Doc.docx", DOCX, 344510, ""),
            # subfolder: MindMapping
            ("1lO-4aB-PkjA1j1PdWmtzfjbNtaw4CN3r", "3. HealthTech Marketing Site MindMapping.pdf", PDF, 1286948, MIND),
            ("1JAyhzHBlyV1USdln4I9qUdVb_x14EiLL", "2. HealthTech Mobile App MindMapping.pdf", PDF, 3142852, MIND),
            # subfolder: SRC4U - Screenshots
            ("1PToLS0qmu5KhR5D9NlWqIVIqQ_IeqaL3", "Screenshot 2025-02-25 at 11.15.09 PM.png", PNG, 1851561, SHOTS),
            ("1KvqYLX92XM-zu9sVYmiwvUyWZNUjmJdS", "Screenshot 2025-02-25 at 11.15.01 PM.png", PNG, 2302447, SHOTS),
            ("1rSESe9cSfCtSSvsLdX4IK5e8iyKpxJKx", "Screenshot 2025-02-25 at 11.01.28 PM.png", PNG, 2290632, SHOTS),
            ("1yBpzQrIENp1Nbjd-1XplxTNrvTeIE5v4", "Screenshot 2025-02-25 at 11.05.25 PM.png", PNG, 2396491, SHOTS),
            ("1OndFETxmsdrmz0hlyivlJ9HNnPcNNprG", "Screenshot 2025-02-25 at 11.01.17 PM.png", PNG, 2249879, SHOTS),
            ("1iv3R7LFlb2R2agRp9GWoF2HbhyX7d647", "Screenshot 2025-02-25 at 10.59.05 PM.png", PNG, 2516194, SHOTS),
            ("1gswIpLVvfikIlR7gvxB3hF2l6Rl3F_21", "Screenshot 2025-02-25 at 10.58.57 PM.png", PNG, 2065598, SHOTS),
            ("1sjEVIypzOOijIXgei4FLK4cEbwnftWEk", "Screenshot 2025-02-25 at 10.55.55 PM.png", PNG, 2766992, SHOTS),
            ("12mCmCIa28OTHDcUT82bJUt47_JlDSgYQ", "Screenshot 2025-02-25 at 10.54.33 PM.png", PNG, 1182749, SHOTS),
        ],
    },
    147: {
        "source_folders": ["1npXsCbxOlub5cg9M89Aj1uazNdqnc4w2"],
        "files": [
            ("1WedmN4JipDKHAG60QDsVeCiyqJRrH2e9", "Flow Roadmap.pdf", PDF, 148060, ""),
            ("1xp1QyOrIgKINlKqM6GByqif8MPdtBVNn", "Multi-Country Compliance Matrix.pdf", PDF, 68645, ""),
            ("1AWqVE5-UtPd4XBi-IVERx6oIj8YdURoP", "Fortitute Recording.mp4", MP4, 144844222, ""),
        ],
    },
    148: {
        "source_folders": ["1eQlCZmqpOl3iWA8YKJE2EcNX7_bdPDYF"],
        "files": [
            ("1z9pL9YGTXT5WOR3vojPAapE_QR3qNvN7", "Tech - Recording.mp4", MP4, 3339529, ""),
            ("15cVZ7pU4KVJjycZQbi-S_wKjJNX3vFnQ", "Tech - Recording.mov", MOV, 2784329, ""),
            ("1YeuTriYM9LFUNVclB8o-fUqKQYPpR4Q-3cl6SaC7Oxk", "Shared By Prospect in Writing", DOC, 7722, ""),
        ],
    },
    149: {
        "source_folders": ["1AEr1lZ96zYPlpG7Bmo34CzNXwYEy4DjZ"],
        "files": [
            ("1_oL_7Bu2JDKkJxMSJqhvq2sCfi9hTqtl", "Recording - Child Life On Call.mp4", MP4, 209338235, ""),
        ],
    },
    150: {
        "source_folders": ["1_og9NrvSFotKoTw9yJRVJxgu5t3VnCIj"],
        "files": [
            ("1rH2VrUgGP4wPgHRxb7UwS42qOalvwNCt", "Wellington - Engineering Recording.mov", MOV, 359778911, ""),
        ],
    },
    151: {
        "source_folders": ["1lYAcnVo4Doa5ek46WdCT0A9c_afn54r3"],
        "files": [
            ("1i1RBu019ceMRjcbohxSNFmDnVqOg7Sy8", "My Green Lunch - Tech Recording.mov", MOV, 445548991, ""),
        ],
    },
    153: {
        "source_folders": ["1ilZqMgfhnhBntH2pEmxA_LiflQvSZc1J"],
        "files": [
            ("1Kii62Rxt-0_cftqodvMGAj10henVXvmzXILvC356l1M", "GAIL – Global Adaptable Inclusive Learning (Solution Document)", DOC, 11718, ""),
            ("1TfUTaRkY4Si6-vf3oDW9bsnfMCDKjnrlb1tImarJqNs", "Read Me", DOC, 1024, ""),
            ("1sBELLdVcM_EbJKI1HV4TFSFrVs6MTPEYeexV-bjN67g", "Missing Features - MVP", DOC, 4658, ""),
            ("1x7ABhAAidsnUONoQedCUcJ8GyRCqN36g", "Recording - Irvine.mp4", MP4, 280353252, ""),
            ("14rnhZpL0vDzdV8fKweSBPlrhuMf8x76G", "GAIL logo .png", PNG, 1628593, ""),
            ("1qov1lyK_SxDhBzAzCziDh6zuHgqM8AS9", "module layout example copy.png", PNG, 1521879, ""),
            ("161xQYMQ4-WeBks5qIKsTUHPx3w9aqZg2", "GAIL_MVP_Developer_Brief_Full.docx", DOCX, 1933565, ""),
        ],
    },
    154: {
        "source_folders": ["1yY-4IcYD-WffSR-8xWotOmJvy37fJ3V4"],
        "files": [
            ("10zmugxcbMJPp2pP1KeD3EjCCf5nVIH3Y", "3. Lapapoe Web Application - User Flow Diagrams.pdf", PDF, 693270, ""),
            ("1od1RLt_RZZ_Jo3i5LQKPEQ_8vImPtg2Yis0Wi0XahkE", "1. Lapapoe Web Application - Roadmap & Estimate", SHEET, 19591, ""),
            ("11WykA2yZ_aaewYzdVBkl_BYiQlMfXPqV", "2. Lapapoe Web Application - Mindmap.pdf", PDF, 668956, ""),
            ("1eGb-COczfWcYqv_lJWsHy3Sy6VpcycKAyMlTQuGA9i8", "Deliverables", DOC, 1869, ""),
            ("1eThVjTh1DQdqFqpk3rWDBAl7JJzGLJXm", "Recording A M.mov", MOV, 46581306, ""),
        ],
    },
    155: {
        "source_folders": ["1u2O5VLvchK_Y38h5LegBc5rxyKAtU-Dp"],
        "files": [
            ("1EMBWp9nG8-EEeQ0uhPacF82BWNU-exiQ", "Optim - Tech Recording.mp4", MP4, 291219139, ""),
            ("1Wq41srCiTv3riUCr9X5fYxLD9dluwZBR_AKRNjzZ77c", "Read Me", DOC, 1024, ""),
            ("1CXzhTyrMbpk44wNxtt62IQgUQEqEaU3W", "6. Flow Roadmap.pdf", PDF, 132014, ""),
            ("1b7gf-LPQ3pR2DIGXpK3q-5-GDZm4gDGF", "SOP Assessment Tool With Gap Analysis Chart_CRB Water Final.xlsx", XLSX, 281709, ""),
            ("1t87krsXqLinhvs1y3XOu01e38gyUTvGn", "2. Site Manager Flow Diagram.pdf", PDF, 18023, ""),
            ("1c1D51ZEVUFNCA_RQsyI9xlYPh87Ur8Kd", "4. Field WorkerWarehouse Staff Flow Diagram.pdf", PDF, 15915, ""),
            ("1DPtF879QyhN4hmg9m5N-OjTOkb4bZzV3", "1. Admin Flow Diagram.pdf", PDF, 15333, ""),
            ("1W_UNN_agvpuCAnR9PKW_gm-hbkdebIi5", "3. Assessment Manager Flow Diagram.pdf", PDF, 15439, ""),
            ("1UN71yODTKutN5qxOzc66q14dSHAoKDvv", "5. App Flow Diagram.pdf", PDF, 20480, ""),
            ("1gvBB4drFGhNW3QFJyqlWLvv6NGhEJCjZ", "Ole Smoky Distillery  - Assessment & Action Plan List - Newport TN.xlsx", XLSX, 12719304, ""),
        ],
    },
    156: {
        "source_folders": ["1OEQ9ce8Ua4EmNsXvLIMdXcpQRcvQUAUe"],
        "files": [
            ("1nPfe__U_RaXMTdF_PRMQlYrjH7-8CgYM", "702 - Recording 2.mp4", MP4, 106552265, ""),
            ("1444qQSpOYIzZSUwxV6ABJCBE-NcVQNmW", "Tech Recording - 702.mov", MOV, 98818082, ""),
            ("1tDAE7XK-POTQPRVw6G-_j0qSKcXiz7RFGHk74ewctOU", "Miro Board", DOC, 1024, ""),
            ("16cdpnWtiYo_ETt_rikbVgm1fEOmuT6BbvcWCuWGe3Qw", "702 - E - Commerce | Roadmap & Estimations", SHEET, 15680, ""),
            ("1kl7F-WDz4REYGPGgrKpe9EWYD-4Bj5ai7XFADMmemXA", "702 - Solution", DOC, 7526, ""),
        ],
    },
    157: {
        "source_folders": ["1tI0Pz1Of_UYWeeShvtzsEKsNokbHYohD"],
        "files": [
            ("1psjMy7jpylTOv9wTXpSgYweSLn_lVKGZ", "Coastal Simple - Tech Recording 2.mp4", MP4, 122594225, ""),
            ("1gubQ3HffYMF4SEyhH3fTDfYNI3MLFs10Pr6DCDoNzO4", "Readme", DOC, 1024, ""),
            ("1Zic6qPfMxRSr-jNKgWeh6LialTrcyMw-", "Requirement Shared by prospect (SQDPP).docx", DOCX, 17167, ""),
            ("1ag9TE7i0q8-qwf-VQeB9apCjUjBpBDWb", "Tech - Coastal Simple.mp4", MP4, 111162177, ""),
        ],
    },
    158: {
        "source_folders": ["1Vb8--bQBPFMAPMtG17YyTk8XJUSKKv2a"],
        "files": [
            ("1hvjr7O_iiepY_p9j5oDx5yAPl-w3Hmld", "What The Future Education - Tech Recording 2.mp4", MP4, 203194526, ""),
            ("1nAsJi18Up-oeefUThsL5eX51N74BRRG2", "What The Future - Tech Recording.mov", MOV, 274962226, ""),
            # subfolder: User Flow Diagrams
            ("1f50pGF3lPNy4iIqy-ry6iKTB-XMyspEe", "01 Student Flow Diagram.pdf", PDF, 28515, UFD),
            ("1K8wv1jl8v263YtAb-Tm21377rklyiFA8", "02 Teacher Professor Flow Diagram.pdf", PDF, 16373, UFD),
            ("1jqmkwGAlp3qswYFHOonG_R5Pk8T8wnRG", "03 School Admin Flow Diagram.pdf", PDF, 26088, UFD),
            ("1GXIXzY974PkvyAUuWWX8jfTJPXughsiy", "04 Super Admin Flow Diagram.pdf", PDF, 19211, UFD),
        ],
    },
    159: {
        "source_folders": ["1VaZCarzviDhtgmbG6r3A0YO8kO8XZafg"],
        "files": [
            ("1iC3w_eUnl7AJI6r78uMU4eJuPQrsq_x5", "Revoscape - Tech Recording.mp4", MP4, 39693703, ""),
            ("1Ba32rt5S9REJxJN9oTiEyKR0CKrPGTuq", "Detailed  MVP Version 1 Development.pdf", PDF, 230510, ""),
            ("1rYxTnLFV6KgC1rfaoevfBJY5S5-Jlq7G", "8-17 Scope Document Phase 1 only.pdf", PDF, 129915, ""),
        ],
    },
    160: {
        "source_folders": ["1P7IW4HxsvV8zKaMu4_qApTh0is5-0Ikj"],
        "files": [
            ("1C9_SWM9k_xAgJSMFzCUfy7SyV4jsu5d5eHuzD8iH6rk", "SOW Shared by the clinet", DOC, 4843, ""),
        ],
    },
    161: {
        "source_folders": ["14pe5Tk84P8H6xRlx6AJTB8qBa7_0nSHC"],
        "files": [
            ("1x2hv7UyPsCUcsApU8uUbpholbiwbFsXLR9stL9APF-E", "Integration Best Practices", DOC, 24153, ""),
            ("1dnaLDNN8kDscN-ybSKSS35nGx8QSZ1n1n8piClujhMY", "Oasis Integration Playbook ", DOC, 23250, ""),
            ("14RpTn5ntzev3YKcjXgeIMVKONSbwfSQr6z8i3aKP9VI", "Second - Updated Business Requirements Shared by Prospect", DOC, 9342, ""),
            ("1vKgnVv49oRJrtPgc_4XL5DJtn4jIK-wuRqKjXf1kIR8", "First - Care Navigation Platform_ RFP 2025", DOC, 16331, ""),
            ("13umXBaIiEbB5sOcxIVy2xQswTppq6teL", "First - Care Navigation Platform_ RFP 2025.pdf", PDF, 427025, ""),
            ("1p0V7BIZgWHQNckd63ytOk5f71dGSNtfG", "Solution Summarized by Prospect.png", PNG, 1577793, ""),
            ("1DhSKWFw-6DfflkyhrKrLzWHJLKafgyJ5", "Muse Health - Recording 2.mp4", MP4, 727389220, ""),
            ("1hh93-mf-jlFTZL_gurxHQfZMLf0pTDPQmAWiGsn4Uno", "Oasis Care Navigation Platform Development - Proposal Document", DOC, 6263094, ""),
            ("1NT7-Wmwk0OlpvuTDSJM8rmj372nDLwO7UZ9e-zBWEmQ", "Read Me", DOC, 1024, ""),
            ("18vK1dZLQVZnpG5hrGh0OA6zoKz8zcAc8", "Recording - MyMuseHealth.mp4", MP4, 120255660, ""),
            # subfolder: Diagrams
            ("1xG8tcxokM8sRt0-Y-V0fk6GjtxOU3lCh", "01 Risk Stratification - Process Flow Diagram.pdf", PDF, 444342, DIAG),
            ("1pz0CR8bro6_m4uuru46d-JRA1IALM3Fg", "02 Operational Efficiency - Process Flow Diagram.pdf", PDF, 697560, DIAG),
            ("16DyD_3vLu_vdj-gDMYctD9y3J0Jt_KOp", "03 AI Coaching - Process Flow Diagram.pdf", PDF, 451347, DIAG),
            ("1srXwuY0qKetvVoqcrxnlF5V9YSeLQVKa", "04 Virtual Flow - Process Flow Diagram.pdf", PDF, 508771, DIAG),
            ("1nNfM_y-iyDy_tlPXHvISUxbiP4_NIRy9", "05 Real-Time Monitoring and Visualization - Process Flow Diagram.pdf", PDF, 887222, DIAG),
            ("1v5AI-WE7aKu-hBRR_4YkC0h_Czf9QKvo", "Flow Diagram.pdf", PDF, 40521, DIAG),
            # subfolder: Updated Detailed Requirements
            ("1EsaiEJpqeOtRVCF_uldTFnDhkoJfMXLl", "Muse Health - Recording 3.mp4", MP4, 1481663722, UDR),
            ("10cJT4FvkQ9jd2NiqT75WzHbNtG2GlWe1ctUd0q9ELZk", "Oasis Health Platform Development - Roadmap & Estimate", SHEET, 29248, UDR),
            ("14piPkwubpVY87oy57KcfiZTQQhn69Iov", "DrGlennMarshak_Strategy to Reduce Emergency Department Admissions in the Heritage Health System_April062025_V2.pdf", PDF, 26534039, UDR),
            ("1DRZvmAXy7MBhZ_US1mCUZqlkD52aCEPX", "RMG_Muse Health & Oasis Platform – Transforming Care Navigation Through Modular Pod Partnerships_July222025.pdf", PDF, 4028517, UDR),
        ],
    },
}

NOT_WALKED = {
    145: [("1X1UPz1lrB-RAsH8U1ZR0oQQLUZNSNjpp",
           "Original Repositories  - source-code export, not a sales artefact"),
          ("1jGNy73q1qIFMA3DEnDXJe0iOwNcjG8iM",
           "Database Backup - database dump, not a sales artefact"),
          ("1lYUhqZIbFPkLCmu53PVraMplfuHqp6f6",
           "247 Call-A-Doc Mobile App - holds no files, only the level-2 "
           "folder 247CallADoc")],
}

SUBFOLDERS_TO_WALK = {
    145: [("1QuCl6TxVg9vT19xjN5TuW41hs9dLLfV2", "247CallADoc (level 2, under 247 Call-A-Doc Mobile App)"),
          ("1YFr8Ck9KDS6QOUbOP_vG6A7ivnSmztbu", "Eligibility & API (level 2, under 247CAD-Documentation)"),
          ("1B_8pz_28AOG9KYEKsd9Fd9SYANRZ28An", "SQL Scripts (level 2, under 247CAD-Documentation)"),
          ("1vAiY39jlqbITFOSv0JjFFU2H5yE7obtL", "Config Screenshots (level 2, under 247CAD-Documentation)")],
    161: [("1x34UqAlwSZxErwArXsCZq4QoL1H7ffqO", "Discarded (level 2, under Diagrams)")],
}
