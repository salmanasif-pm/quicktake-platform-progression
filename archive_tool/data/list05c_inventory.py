"""
Real Drive inventory for the third List 05 batch, gathered read-only.

Cards whose discovery is COMPLETE: either the linked folder has no subfolders,
every subfolder has been walked, or the linked folder/file is gone.

Entries are (file_id, name, mimeType, size_bytes, containing_folder_name).
`errors` lists sources that could not be read at all.
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
SLIDES = "application/vnd.google-apps.presentation"
PDF = "application/pdf"
MP4 = "video/mp4"
MOV = "video/quicktime"
GVID = "application/vnd.google-apps.vid"
DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
PNG = "image/png"
CSV = "text/csv"
ZIP = "application/zip"
BIN = "application/octet-stream"
APK = "application/vnd.android.package-archive"

GONE = "Requested entity was not found (deleted or access revoked)"

INVENTORY = {
    423: {
        "source_folders": ["1LbMqLQWktvyjqH-bzFZfiG5GKszmQuqJ"],
        "files": [
            ("1S6yo0ziZfRG2evDlSQKthMNBS40I6Vp3", "Discovery call.mp4", MP4, 271063269, ""),
        ],
        "errors": [("folder:1LbMqLQWktvyjqH-bzFZfiG5GKszmQuqJ", GONE),
                   ("file:1lFy2aU-rw0BpgIz0thf1RVMXc1N-1qDm1s3dHQZm4gA", GONE)],
    },
    425: {
        "source_folders": ["19d5e0y1lIqoOMs6zI2OXPNKTTuQvh1Jr"],
        "files": [
            ("1fjcXdWDOHRtva5nQcQn6V4Fe-wmDiqLhry9gGGzGh6A", "Professional Service Documentation", DOC, 1476380, ""),
            ("1XC_hWyAi2HTABRwCehBPqORM1F8D5X2W9Z6IpERCDtc", "AMI Product Documentation", DOC, 1475939, ""),
            ("1Ld6VASsEZGwOhmScPzv9bGuhmtjM-JvZ", "AMI Product Documentation.docx", DOCX, 223112, ""),
            ("1Pab7aQBLJSsp4VrEgyI-OWO26sOc_aco", "professional service.docx", DOCX, 9603, ""),
            ("1cfHeFw38cN1iZf_29tPyFUbtXsPtGR5s", "Trimmed version - Proxy.mp4", MP4, 49761245, ""),
            ("1wsDW1-0b0z01rXQ2h2GoMUBZQ3ERNXD8", "Technical call.mp4", MP4, 38867609, ""),
            ("1QQGLjwC1uLxl94SeB_ew59IvdAiehKqV", "Kickoff call.mp4", MP4, 39761945, ""),
            ("1tCtQj3fbngxAL88xRJyE05w6ckh_HDH01XmeStv-q88", "Steps to Publish an Amazon Machine Image (AMI)-2 on AWS Marketplace - Solution Document", DOC, 19279, ""),
            ("1yEjNUb0R5i744y3cUM04IFx58z7vnGPyTmKqj-tqalE", "Steps to Publish an Amazon Machine Image (AMI) on AWS Marketplace - Solution Document", DOC, 19425, ""),
            ("1gnWvxxxe1Egwp9MF7OaAwO7dxTcBiUlQ", "zia_purelogics_credentials_no_pass.csv", CSV, 103, ""),
            ("1wIuaF5rOK_nN2npjb0hMvFLSSETfkWzI", "AMI Publishing Requirements.docx", DOCX, 9184, ""),
            ("1E9sHpEkjUa-7_zWIX5u4jcq_KokDBXW3cTr8zcQEB5Q", "DISCARDED - Guide To Launch Container Product On Aws Marketplace - Solution Document", DOC, 18007, ""),
            ("145ofofTUx-tVA05WBd-ZMXEMtjBjb00OCE0q_LPq9jw", "Updated Requirement", DOC, 1024, ""),
            ("1A78giiugK8cYIpfICwHL0BG5twQKw4pge8Go5WvouXM", "Requirement Document", DOC, 2574, ""),
        ],
        "errors": [("file:1TJionrEDb7479EKxYfw7pEpthMa87KsSuVAu5nEdcLA", GONE),
                   ("file:1DGo8ZjOXZxf48PGmfV7oAoyFytY1v0cr", GONE)],
    },
    426: {
        "source_folders": ["19jQdAq6sKrSrULIaTRk9umVeqQb1-f12"],
        "files": [
            ("1oV-PLY1h5m00-9veap9pMcYAPNBFhFSZN4wT9Wmq26c", "BlockRock Web App Enhancements - Solution Document", DOC, 20231, ""),
            ("1WYcjOtMUTawV2Zk2ICiNYU6Rgs-U0WCi", "BlockrockDesignReview.pdf", PDF, 7280525, ""),
        ],
    },
    427: {
        "source_folders": ["1Q8H_1T7PhJFDCmzcz_9swrYvvx0tW_BF"],
        "files": [
            ("1y6SPwB2fct_93FqwOz7qIH_Z-BDqKgTaYhlKDiC4Wpo", "BlockRock Blockchain - Roadmap and Estimates", SHEET, 19335, ""),
            ("1s2RI6ZlQy_Z_XWbFg6J5UjJ54lJQsTLl", "Updated meeting 6 sep.mp4", MP4, 460683964, ""),
            ("1UZezCW-vlDxSZzEeEHgUXdVloz55ESf9YwBabkeo6Kg", "BlockRock Blockchain Idea - Solution Document Updated", DOC, 19501, ""),
            ("1uJdLYg2GyzlGIf-prrf9nmlbxh6t5Fex-1VUtNQMP5Y", "Design Time Line (Trimmed)", DOC, 15879, ""),
            ("1A_UitbQ_VbvUVf0Ix5IurqzCDB1uU0oQ", "DesignTimeLine.pdf", PDF, 88764, ""),
            ("10-I0-tc0KR426jnIMloPUSZux07ZcvpM", "QUESTIONS-QUERIES-ROADBLOCKS (1).pdf", PDF, 82138, ""),
            ("1TLn-ugiM88ZUJslxCsLs9BypBsB2_OHAHwy5XYqslms", "Updated Requirements", DOC, 1921, ""),
            ("1MpVIFULC5Im6oqIrhuiacI-_cRO4bZof", "EAI - ECOSISTEMA DE AUTOGESTION INTELIGENTE - MEMORIA TECNICA V1 (1).pdf", PDF, 1824085, ""),
            ("1CXxm4rnb4Tz2vEeaAItaWwE_A_yRdRYD", "EAI PROTOTYPE - SSME EAI ENGLISH V2.2 (1).PDF", PDF, 3377070, ""),
            ("1YDz7orYfG0k2ihMsCybZArC6Mvr79YuS", "EAI PROTOTYPE - SSME EAI esp V2.2 (1).pdf", PDF, 3435345, ""),
            ("1dYhsQw7LpmADL_omFjgJysBYHFmNJJlP", "GatacaWallet (1).apk", APK, 45857648, ""),
            # subfolder: Translated Documents
            ("10Lu03P04UQQLnpM1ft0XfkbVHHVbmdxt", "EAI - ECOSISTEMA DE AUTOGESTION INTELIGENTE - MEMORIA TECNICA V1 (1)-EN.pdf", PDF, 956128, "Translated Documents"),
            ("1-Iff00s7aHBtX4pNro_LBG6ho4H4Fh7QAosIBOhNtxQ", "EAI - ECOSISTEMA DE AUTOGESTION INTELIGENTE - MEMORIA TECNICA V1 (1)-EN", DOC, 1005681, "Translated Documents"),
            # subfolder: Architecture and data flux  -> diagram folder
            ("1u9_yE9qagHyhMCUh8q8A9W06-yTAQHRW", "DataFlow Updated.drawio.pdf", PDF, 51240, "Architecture and data flux"),
            ("16RGdXoGWIKPIGTtlAe7tRyz-bpeMQNMn", "DataFlow.drawio", BIN, 19416, "Architecture and data flux"),
            ("1kVAr0-uu_e4myYF2_9awQGlhuSprCA3s", "BlockRock Atchitecure.drawio", BIN, 124956, "Architecture and data flux"),
            ("1EFTpGgP-Z6FUKt2Wc52V9QOPiY_okKWO", "BlockRock Architecture.pdf", PDF, 203705, "Architecture and data flux"),
        ],
    },
    428: {
        "source_folders": [],
        "files": [
            ("1KEmJhwzCG9uUFUOrobrF-YcsyJAdNgrLxfjaEHZoJ1Y", "Requirements for Yardi report engineer", DOC, 6376, ""),
        ],
    },
    429: {
        "source_folders": ["1PflZHlZzbdjUFy_jFuAb3CvYvEQ7U5S4"],
        "files": [],
        "errors": [("folder:1PflZHlZzbdjUFy_jFuAb3CvYvEQ7U5S4", GONE),
                   ("file:1Eey9i2-cmX2Z8UJgwqNr_v_BKpPlUbuhVlTOgDsmUOs", GONE)],
    },
    430: {
        "source_folders": [],
        "files": [],
        "note": "card description contains no Drive links at all - card.md only",
    },
    432: {
        "source_folders": ["10-dz2CmwFJgWYie3HT0QtrEHyqV7leVy"],
        "files": [
            ("1sdLBOgdan1mAOiVe2jMn4o_E4vH7shmpU9L0ymEuimg", "1. Jobs Searching Application | Hybrid Mobile App Development - Roadmap & Estimate", SHEET, 41077, ""),
            ("1Ze7_izsAVqFajVmfVVLOTKYYNwQwLSvQ", "video1913476924.mp4", MP4, 215249846, ""),
            ("1xN9qD2KygdHpZ7D6Jzi-TzfPVjhp3H_T", "Discovery Call.mp4", MP4, 351299050, ""),
            ("1M2ufvL0d4qhj730d-KwrZzwQrCNte-IL", "Second call.mp4", MP4, 111727323, ""),
            ("1-5c9gB8xXrAaQAvtqbaiz3p_kHBrVm8C", "video1088678053.mp4", MP4, 107276949, ""),
            ("12k5L7ncY5uhpDo9ugPzTtblr3S4Aivtx", "Doable Pitch.docx", DOCX, 409798, ""),
            ("1pNaFNyQZMa5yLLPoea3qHtsAxlsxTsUWxRr4kT5vp4g", "Additional Features recommendation - 12th DEC", DOC, 2359, ""),
            ("1kUBSuc1xJCHzKVuRRdtaItB4GAeedntSkoIAiG8W3XM", "Adjustment & Requirements - 20th Nov", DOC, 5558, ""),
            ("1pCMd1_xRAdg6hJNYy0-oAw6Rx2TP6ve4z_PpRl1MeyI", "INTERNAL - Meeting Notes", DOC, 18266, ""),
            ("1PFii3lai8l4xRTUAYxwTnRbW8UN7ScbsceTbDFRW7fo", "Requirement", DOC, 3672, ""),
            # subfolder: Logos
            ("1mV7QDPqVk572rV7__43buWltiCIbl0hE", "package_highres_9qm4xxbn.zip", ZIP, 5910181, "Logos"),
            ("1s1xZXL09WVxHzbhYRj7cbFbko2tEOONh", "logo_basic.png", PNG, 221105, "Logos"),
        ],
        "errors": [("file:1nu4pRMAfuJn-UorWT1bbuIsevjKL8cag", GONE)],
    },
    437: {
        "source_folders": ["1iD8CuumE0sw1UzdtECmde1VH1Nfg5AHM"],
        "files": [
            ("1595tsEMJlP3ncyq7wo2CHEsaQH6jx6rS5Si2JHxz2wg", "RainCheck Platform - Roadmap & Estimate", SHEET, 29332, ""),
            ("1e0fiUbHvftzXjLmpLUuxuJFUjcATLO0w", "Mina __ PureLogics  - Apr 23 2026.mp4", MP4, 44281284, ""),
            ("1T0fUcd27bA5OOFnjTE8nP1NWXdtGu1bpKI24tyyunRA", "Figma", DOC, 1024, ""),
            ("1LCG8CUv872KqhnKOLVR0WIursuKGfvGISgY5QJnN4UA", "Transcript - Rainmaker", DOC, 18058, ""),
            ("1KmIqMzfOs16j1CN6cw-r71ps-EtQLmGe", "Lumyn __ PureLogics - Feedback Discussion  - Mar 30 2026 (1).mp4", MP4, 291215394, ""),
            # subfolder: BA Working
            ("1PeSoWfG97tPnsG6j-C2_cUplBq7TwrE_uteXYqyHR0w", "RainCheck Analysis Platform - Technical Assessment and Optimization Plan", DOC, 5306998, "BA Working"),
            ("1YKMRtox6cORtVk4czRz22_TT2Q0a43ys", "1. Manus Offered Models.png", PNG, 39342, "BA Working"),
            ("1DFkNWSivH4qA7DzRpQ1C6L3hRPkw0TK5", "6. Manus Webhook Logs.pdf", PDF, 5405959, "BA Working"),
            ("1TkRgYxIGakp8w6b-L-adlp_KnQ0bzp1n", "2. Manus 1.6 Pro | RainCheck-Invest-in-Azure-Printed-Homes (3).pdf", PDF, 67090690, "BA Working"),
            ("1jiJAabAfr-T7l3fpwqFv08gEfiUO91gg", "5. Analyze Deal Logs.pdf", PDF, 1734017, "BA Working"),
            ("1xxZFW-ylKP6cCEnrydrmxFLz9T0IlpHo", "3. Manus 1.6-Max | RainCheck-Invest-in-Azure-Printed-Homes (1).pdf", PDF, 66826214, "BA Working"),
            ("194VPK4qOOkSDeBU4SEedt20IUpEfsvOY", "4. Manus 1.6-Lite | RainCheck-Invest-in-Azure-Printed-Homes (2).pdf", PDF, 40669532, "BA Working"),
        ],
    },
    453: {
        "source_folders": ["1Gqj51ULRGsHwjC4rzoYEyDdc7QMbozEc"],
        "files": [
            ("1VGoWqf8Rk618-9GwXvxDZZBXfUAERanuj9kf_rs0dxc", "Working Investor POC - Solution Document", DOC, 5659382, ""),
            ("1TsCqZ2wPE2Vuxm9sO0F6BXY2ci6VXHrj", "Student_Pathways_Working_POC_Scope_Lock_and_Solution_Brief.pdf", PDF, 318897, ""),
            ("1ccrYBzMNwfQ5axg3zUi7ZZu1srmk1GiV05DaZHMUZ2U", "POC | Student Pathways AI Platform - Roadmap & Estimations", SHEET, 25662, ""),
            ("1SH-JKtsTAivPtano1zsNZzi0yEGato2D4uovhc0_uM8", "Student Pathways Prototype - Technical Requirements Document", DOC, 8071, ""),
            ("1BNand3MCTau0UgUBFcOEoeWuVBL17S-gC_dCtolfwM8", "1. Student Pathways AI Platform - Roadmap & Estimations", SHEET, 71562, ""),
            ("1IdwJy3b5nOl_YquptZDKEklcvWPaRvoB", "4. Parent Flow Diagram.png", PNG, 1490648, ""),
            ("1yEp-bHVtbdbUCzGTws4zZMv867ZwgnUJ", "3. Guidance Counselor Flow Diagram.png", PNG, 1483857, ""),
            ("1xQrWp8HYn7j7UXdpAoqNI7DGbdxmLZOd", "2. Student Flow Diagram.png", PNG, 1540830, ""),
            ("12FDDV6O1zCe-t7lZbommliQzyCPA-gFRi0Tqej9Aa90", "Student Pathways AI Platform - Roadmap ", SHEET, 34950, ""),
            ("1Ay_Wu0khj4Qf9VFJik7c2F2GW0wLk_lT", "Student Use Case for Beta .docx", DOCX, 328150, ""),
            ("1FC_VhXPpsM6JGRapNuo-T82WeI4kC8dwiXjvH3IDrlw", "Frank Cilurzo: Consultation Call - July 17", DOC, 30056, ""),
            ("1kwuWD819AnNBp8kIczZ4jzWsZD9qzU4NZ89gUTaOB_8", "Meeting Link - 24 June ", DOC, 1024, ""),
            ("1kvRG98wr4PZCIgzrkfnDFvUsTePqe8mAD33JGxWN_B4", "Frank Cilurzo __ PureLogics - Jun 2 2026", GVID, 311410642, ""),
            ("1kRKKaM7V2b0BoS17niBpCPWBK2eEwAGM", "Frank Cilurzo __ PureLogics - Jun 2 2026.mp4", MP4, 311410076, ""),
        ],
    },
}

# List 05 cards whose discovery is still incomplete, with the subfolders that
# remain to be walked. Recorded so the work is not rediscovered.
STILL_TO_DISCOVER = {
    41:  ("1SHRzslEwud9zYHY7rvakKOEE1xFsH3Q5", "12 subfolders, none walked"),
    82:  ("1Vut4AX2L5vL_wOxVIesbG6-6bUMlg9Ad", "9 subfolders, none walked"),
    109: ("1qZ8vEoG0eH7l5Jd4ly0fdJwSMIfusgUG", "5 subfolders, none walked"),
    202: ("1CxvqCkQvfjqYGnVQNTIMNGfMue58ayLJ", "7 subfolders, none walked"),
    205: ("1-EjvI0QHlBzyImiOX_fDBjI7TErzFfjT", "10 subfolders, none walked"),
    206: ("1ATu9B-oegm2pH-xAT5UdXqQ7oZqvP-um", "7 subfolders, none walked"),
    424: ("1o_oQ0N8iO7WIeb3dCVyhlJyh7I-rXyd2",
          "top level + Latest Deliverables + Internal Meetings walked; "
          "still to walk: Prospect's System Screenshots (excluded by rule), "
          "and the level-2 diagram folders User Flow Diagrams / "
          "System Workflow Diagrams inside Latest Deliverables"),
    431: ("1e1NBfuYNLKuET2DwDZtGB5oe5fPdhaNV", "6 subfolders, none walked"),
    433: ("1bIV1njBfHrAPh7fLaPKXQlma-hDjPCkX",
          "top level + Admin Guide + Documents for live website walked; "
          "QA folder returned empty; still to walk: Meeting recordings"),
}
