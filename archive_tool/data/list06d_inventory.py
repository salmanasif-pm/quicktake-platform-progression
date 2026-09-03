"""
Real Drive inventory for the fourth List 06 (`Closed Lost`) batch.

Cards 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 314,
435, 439, 443, 444, 449, 450 and 454.

Level-1 subfolders walked separately and merged in below: card 191's
`Project 1`/`Project 2`, card 196's three app folders, card 199's `Internal`,
cards 443/449's `BA DRAFT`, card 444's `DRAFT`, card 449's
`Prospect Requirements`. Cards 191 and 196 hold nothing but subfolders at
level 1.

Card 194's `Kare - C E - Process Flow Diagram with Questions.pdf` is 122 MB,
past the spec's 50 MB ceiling, and is copied anyway: `classify_file` applies
that ceiling only to files that are not doc-like, so a large PDF deliverable
is kept while a large video is not. The limit is there to skip bulky media,
not to drop the deliverable a card exists for.
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
PDF = "application/pdf"
MP4 = "video/mp4"
MOV = "video/quicktime"
DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
PPTX = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
XLS = "application/vnd.ms-excel"
XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
XLSM = "application/vnd.ms-excel.sheet.macroenabled.12"
CSV = "text/csv"
JPG = "image/jpeg"
SHORTCUT = "application/vnd.google-apps.shortcut"
PNG = "image/png"

INVENTORY = {
    189: {
        "source_folders": ["1HMXkgDmaLK4H_E-vy9J0JlLj-Qb54oKB"],
        "files": [
            ("1PgJbFiDa4USThrJdrOJvIUtM0icHbTAI", "Website Revamp - R H.mov", MOV, 90017139, ""),
            ("15fNSAk9waeE9akjO0-mB_gT2YGR65q66", "ZSC Website Revamp.png", PNG, 98736, ""),
            ("1AwJvOClxbolM8yEyc6LE8MjuLDJDhD88adqVmqK79Uc", "GDB Constructions (Website Built from Scratch)", DOC, 9085, ""),
            ("1igcoUXzcp--NSJV7fYl_sIbcXW3yitPJuZvvIHBJq0A", "ZSC Website Revamp - Roadmap & Estimations", SHEET, 15477, ""),
            ("1-njr_VtAhKeLetPcLONj16o4eHt1-xS5", "GDB Constructions Mindmap.pdf", PDF, 16956866, ""),
            ("1oMkceWjM0g_tBJwZaRFVHzrAgOtWsJAdt5CoLyh-G48", "GDB Constructions - Roadmap & Estimate", SHEET, 18987, ""),
            ("1zSM6m-YVgPXoGOIOBOeMVztt1T0hWK8GpRTILwwGsLM", "ZSC Enterprises (Website Revamp)", DOC, 14116, ""),
            ("16fwYuKF2wjC1FPMJUFCW2dDftLdRGteN", "Dunkin Brands - Requirements & Research.docx", DOCX, 19803, ""),
        ],
    },
    190: {
        "source_folders": ["1gHQqcpuKeJdGCallmxiCoDwFhB1g6Cpn"],
        "files": [
            ("1eIMSTVVlP1qTF7GnfS-2yeOl7BtQEBKHdFxh7RcgOfA", "Web Portal Development - Proposal Document", DOC, 6234808, ""),
            ("1wI-_g_DEMwdpdtVPUmOxxdsBKhHOcE-TrUQIeaFR9Nk", "Web Portal - Roadmap & Estimate", SHEET, 20296, ""),
            ("1fA6v7JqG3uLJFhgLrXaXp6978Lqbp1XGloINWMYs4RU", "Deliverables", DOC, 495813, ""),
        ],
    },
    191: {
        "source_folders": ["1rzMHnl-rNlDLQpFCiKVgiiPjoDL1fPXy"],
        "files": [
            # subfolder: Project 1 (its Flow Diagrams / Internal Meetings are level 2)
            ("1guMaPYFBonshJXBm_mrGW7YB8dmsKODl", "Moodle LMS Estimted Hosting Cost.pdf", PDF, 17054, "Project 1"),
            ("1ECU0tXxGGdUtu_Tt2wcUbsQMmmnawcVs", "Moodle LMS Recording.mp4", MP4, 198374978, "Project 1"),
            ("1mjXX_Lw4GuPFQOLDVosjB89mp_AboI5N", "radar_master (9).xlsx", XLSX, 19773, "Project 1"),
            ("1rQHzMOertUC0P-M8gdeqm9M1SKlqltsp9K6mMDBNrAk", "LMS (Learning Management System) Development - Roadmap & Estimate", SHEET, 23975, "Project 1"),
            ("1kLlNonzOSoJ4Khm2nk1BjmBZdIXeeBZ3", "Process Flow Diagram.pdf", PDF, 882879, "Project 1"),
            ("1Lh32x6u1zfH8uBsOy-aAsmHXvXkOWlX0KjzOF17qd1A", "Requirements Shared by Prospect", SHEET, 3614, "Project 1"),
            # subfolder: Project 2
            ("1C9_SWM9k_xAgJSMFzCUfy7SyV4jsu5d5eHuzD8iH6rk", "SOW Shared by the clinet", DOC, 4843, "Project 2"),
        ],
    },
    192: {
        "source_folders": ["1jRgnvtZ4TVxRm1VUOsAJ9_HLcECDVaAL"],
        "files": [
            ("1R151vw-yiWS2IH6rSe3ZpnVv4-BRexewRg5LtovAWso", "System - Roadmap & Estimate", SHEET, 20204, ""),
            ("1QIbh_KxJzFXUJZr8syAyTN7fxHCyPe4P", "Quor Project Brief Nov 2024-May 2025.docx", DOCX, 18771, ""),
        ],
    },
    193: {
        "source_folders": ["11IOaDQrUZqfclizZurlYK6_Ns7_97ye2"],
        "files": [
            ("1sQGBXQXRvRybdAm4qnDeZR2LwKHxVE4XPsmx_sTlQ8I", "Youth Sports Application - Roadmap & Estimate", SHEET, 50847, ""),
            ("170DUjOknFWa1f-RScQ43ScTrXMnbOJEVyPr5u5oNc9Q", "Youth Sports Application - Proposal Document", DOC, 5833305, ""),
            ("1a5wPCDQN_ba8eCA91zvICwZHmtTqb73N", "TeamMatch App - Process Flow Diagram.pdf", PDF, 879871, ""),
            ("1gm6ij38kNiw1ZbePVAaCVZof3yxNXc1g5GcRKjmICVo", "TMM — Beta MVP — Request for Proposal — 2025-02-21", DOC, 28298, ""),
            ("1fv8P6ksPOY78eOAjKy9PLx0qi1yKWBxpyrmWhU3W7Rk", "TMM RFP FAQs & Answers 2025-02-24", DOC, 26943, ""),
            ("19rB-lqkpgzpgltZkkvKQ6EZe6cdsCN_I", "TMM RFP FAQs & Answers 2025-02-24.pdf", PDF, 212369, ""),
            ("1GkCaEqCi-GJQgulzmMxyaH_IAOZfLCqh", "TMM MVP Org and Athlete Profile Wireframes.pdf", PDF, 37440055, ""),
            ("1y6IvegyT-EZNHRLmefF9ZOQPEXgxXi7V", "TMM — Beta MVP — Request for Proposal — 2025-02-21.pdf", PDF, 290589, ""),
        ],
    },
    194: {
        "source_folders": ["1Qn9uMb1RF1xsr4KNM_xQIaGiyZ0uKowW"],
        "files": [
            ("1Rfh5TE1tf3aBjuioKcGHglthwOYpNfCP", "Kare - C E - Process Flow Diagram with Questions.pdf", PDF, 128572795, ""),
            ("13D__ZyonuwjlB0oZOMjhrZm4-Ul31mMb", "PPT Introduction to KareOne.pptx", PPTX, 11641447, ""),
            ("1GOn8XX43kBsFX739cJsFSSs5Tj_M6gM2tCId3kYRY8A", "Pediatric case management for newborns. - Roadmap & Estimate", SHEET, 23644, ""),
            ("10JWr-EfkXKVu1F8kN3b6F4pteV-dbfSQ", "Recording.mov", MOV, 72093725, ""),
            ("1KbkoLe7-d25FJZ71hmGTjzCYJ2H3cipE", "Kare One - Proactive research.pdf", PDF, 57498, ""),
        ],
    },
    195: {
        "source_folders": ["1a50sktmSBIEz_nMT7GQ_SzBb-up9EDEp"],
        "files": [
            ("1YVVt_NoGZutcyZyTqtkCAGHLjtdgWjXiz1p1eu5NUG4", "Blink Sale App Migration - Proposal Document", DOC, 20276, ""),
            ("1g3haF_LJD69c7rsXCT4ZKiJe5NytuFHEnohgse17rmY", "Meeting ", DOC, 3566, ""),
            ("1AGuZSR6IKLvZUgr3PEgITSWz2lSoFlKF", "Recording - Project (Ave).mov", MOV, 150249519, ""),
        ],
    },
    196: {
        "source_folders": ["1q-y0W4C87vqLkf8SslYTzkCG00KLwCl_"],
        "files": [
            # subfolder: Field Sales Agent Order Taking App
            ("1JoNYTQQnaD4RpXBsZTkrTPpS9pUJuuh-B6smjdS1GEU", "Field Sales Agent - Roadmap & Estimate", SHEET, 20393, "Field Sales Agent Order Taking App"),
            ("1IY7Mr6o6Z7YkJCw-OPQT4yYsz1jJCZDF", "Field Sales Agent - Recording.mp4", MP4, 78759403, "Field Sales Agent Order Taking App"),
            ("1Un1ga3XaLIy7ouv8bRlo_VVYuzBEsZ1GcouOcDmiPTE", "Figma Files", DOC, 1024, "Field Sales Agent Order Taking App"),
            # subfolder: Lead Mgmt App
            ("15e0ejH3kMBvvtdZ_n4MGM5V5-Vw6B8NAY8NeePwXezA", "2. Sales Team Member Flow Diagram", DOC, 1306, "Lead Mgmt App"),
            ("1v6lKO4AXLUF8kueENcBI28cRxW4mP_0N6Jc_9wXneM0", "Figma Designs", DOC, 1024, "Lead Mgmt App"),
            ("10J_BdvljGmfoV5yLyQjQ7oIJjnrZabQ_Kf5f7jGNwU4", "1. Leads Management - Hybrid Mobile App Development", SHEET, 19736, "Lead Mgmt App"),
            ("1UOiNLjk895btsHBkPbZRtKq9jwNRWDN4tAYtNeZ2tIw", "MSP Phase 1 Screenshots", DOC, 511640, "Lead Mgmt App"),
            ("16bo3NwG_DBWSzdfRc2mJG8WJj9ZHcZZT", "2. Sales Team Member Flow Diagram.pdf", PDF, 626541, "Lead Mgmt App"),
            ("1zW25HR23Y7uwWZKS40_t0ljSTZ9HDIeK", "3. MindMapping.pdf", PDF, 757628, "Lead Mgmt App"),
            ("1t_EvItAcQ-SvoDb0upTCOyWysXAIxx6v", "MSP Phase 1 Screenshots.pdf", PDF, 1218644, "Lead Mgmt App"),
            ("1mYzn6zjTOz9HPIH7qeYtoO2kVe6hZeiZ", "TSMSOLMAN-Phase 1 - Leads-120824-032837.pdf", PDF, 292054, "Lead Mgmt App"),
            # subfolder: HiHello Screenshots - raw app screenshots, excluded by folder name
            ("1tM1WkhBib2m0WuSoiTHvm_EGl6GGsBs6", "10 Scan Card.jpg", JPG, 35791, "HiHello Screenshots"),
            ("1dOEe292aLFlDv2PdOfJU811qppB75QsO", "09 Cards.jpg", JPG, 33507, "HiHello Screenshots"),
            ("1xtAuswFqxJMbbamaGv5gAUgqhoTc0_vF", "05 Addition of Company.jpg", JPG, 25691, "HiHello Screenshots"),
            ("1Zz-ykccT5m8t15Y1VPdsPIyukyAq1vHR", "02 Signup b.jpg", JPG, 38873, "HiHello Screenshots"),
            ("1sit4wi7m86Xl0w6SzTV4NmZ9OI8FHNYR", "04 Addition of Full Name.jpg", JPG, 41804, "HiHello Screenshots"),
            ("128DPGGiYI-1g0FaiIn26oodOyc5AIXqV", "13 Settings.jpg", JPG, 38899, "HiHello Screenshots"),
            ("1MHGLTircTz4yvDXjcwrxGgbJfZQG7buB", "11 Contacts.jpg", JPG, 25525, "HiHello Screenshots"),
            ("1fl5Rcz3dKEIVsH7dmcPS3nELMmDIzWhz", "07 Addition of Phone Number.jpg", JPG, 21108, "HiHello Screenshots"),
            ("1YPRw2UoB5b2cVsmDcTbddsgPajwlfpgl", "06 Upload Photo.jpg", JPG, 39287, "HiHello Screenshots"),
            ("1my03TgOR9Zix1ZFHEdsmbQSDSd7TwXtj", "01 Signup a.jpg", JPG, 37530, "HiHello Screenshots"),
            ("1uQhqkSo-AK91Aec3gsiZg-X8RJFmuD0s", "08 Designs.jpg", JPG, 41941, "HiHello Screenshots"),
            ("1_T5R55I3GCZ2-xYeX25Z8cNkkV7B-WG0", "12 Discover.jpg", JPG, 51649, "HiHello Screenshots"),
            ("1gNZHHXraulQBDQDkuKayn-X0Bvdp3ICZ", "03 Make my First Card.jpg", JPG, 51802, "HiHello Screenshots"),
        ],
    },
    197: {
        "source_folders": ["1vzsWtE5rTN1rZcWDLMjPQPxgmBk_F0OS"],
        "files": [
            ("1sh0txUspZAwvRKVxajhLArLa0vpTI9fK", "FRISK - Recording.mp4", MP4, 532250345, ""),
            ("1zTtzEbLIH-dlptSFOG397Octu5JVExrU1_GMJApORj8", "Risk Management - Roadmap & Estimate", SHEET, 23645, ""),
        ],
    },
    198: {
        "source_folders": ["1OeAC3QvuKuHR6kQ7MoRxAkxxaHHTiVld"],
        "files": [
            ("1utiiUTTa7EpxWyw11W1bEe0k8WUXOIIS", "Recording - Little Kitchen Academy.mp4", MP4, 251810679, ""),
        ],
    },
    199: {
        "source_folders": ["1CZYQiRiF-uz4INxCOfvh2ttJD3TEv2Ea"],
        "files": [
            ("1KCkJ5-kS9BtEoqIngtiv9fv9saw-GXCu", "Team and Tech Stack.pdf", PDF, 38000, ""),
            ("1lErkkDU_dSr7kjkH2o_lezOrXlByEEWa", "Workflow Diagram.pdf", PDF, 35794, ""),
            ("15n3Qq2BJgi5722_ZQ5UhPg-fqR-NtAph", "Flow Roadmap.pdf", PDF, 164525, ""),
            ("1NmQV89CgkHZCp0lS3HZgfzOWjMiIFi8k", "Mobile Inventory App Demo.mp4", MP4, 66543976, ""),
            ("1qEPqAauLpUHrjq7yBrOEOztvTagXZd8d", "Recording 2.mp4", MP4, 395931930, ""),
            ("1ADFcJQ9GfoPSmNUvEFkJ6DfnN1Pr-x3UPpUdOw6n6f0", "Centralized Asset Management System - Roadmap & Estimate", SHEET, 25900, ""),
            ("1zK8MxOYB97z_2Aszt6ZWze6YHK3HxjX1", "DISH - C (Roadmap).xls", XLS, 44544, ""),
            ("1z5fPiJKkicIJpQB-aUVdB2bfKd1y0FMO", "Recording - DISH (Engineering).mov", MOV, 249409066, ""),
            # subfolder: Internal
            ("1NbxjDH2H5-JpjUFy5L10M0zhi3ceM6so", "Urdu | Mobile Inventory App Demo.mp4", MP4, 107084106, "Internal"),
        ],
    },
    200: {
        "source_folders": ["1wL2IUTeFkh-vh3o5XWhzVUhZssY7u83j"],
        "files": [
            ("1rMDC87pJGbXZ3D-omXGqU2W5yMc2AF1F", "Tech Agri Recording.mov", MOV, 124474091, ""),
            ("16OP3-W6niwxl7bgF_Xa4m7N9nXHOwnm7", "Agri-Tech Recording 2.mp4", MP4, 106941697, ""),
            ("1EPMI_HBOmW9DN1AcxyWF4MA6_f5WnNuY", "Architecture Diagram (Tech Agriculture Solution).pdf", PDF, 4977370, ""),
            ("1SJscLFPQpUlrztV7MlbtjHRmoLgxh3FrRc2HpIuFV2Y", "Tech Agriculture - Solution Document", DOC, 19867, ""),
            ("10GAQUITBbLGhM8oPT1OkPmCkIDb1O-Kv", "Relazione IoT - sensoristica.docx", DOCX, 64931, ""),
            ("1WT2kLzJV5bSVKl8deSFbca9uY6NEuwDD", "IoT costi.docx", DOCX, 22630, ""),
            ("1aCQHBtrz_oUKyWKTzrSonaHTn5oLyFdz", "Pump-Assisted-Backwashing-for-Bubble-Bead-Filters-10-15-03-1 (1).pdf", PDF, 263934, ""),
            ("1GVd5JgK-6eUiGfKjYIuR8v73ZXf-ZAkO", "IoT Sensors_Protocollo di uso e Manutenzione.docx", DOCX, 22901, ""),
            ("1-Vwi8dEtfUxuBdLhG-N2Y8zajbJn9Jjs", "BBF-XS300A-Instructions-09062019.pdf", PDF, 2148877, ""),
            ("1HJNfbvpkCtqy-UyWaKAGvdUfrgH4v15P", "Manual-SuperBead-GB.pdf", PDF, 1193286, ""),
            ("1k843bvstAAJmMbAM1Rl0IrCpD7_DRrUr", "Model-BBF-XF4000-XF10000-Users-Manual-10-05-2016 (1).pdf", PDF, 585903, ""),
        ],
    },
    201: {
        "source_folders": ["1WEMnDvYrg5UJwRdKxdc10k2PaV3jvrHO"],
        "files": [
            ("1nQU80GzICn94MKXcDpM_p7xjovCDBYyy", "Her - Engineering Recording.mov", MOV, 280804043, ""),
            ("1BjKsdT3cfeEAj5i43vsgAmmWhPTnT6KtyHvUyq0cGGo", "ProspHER - Roadmap & Estimations", SHEET, 20328, ""),
            ("1ZASaC3iIvASRSAkv8dNN5wb1JoMl5TanewuOITgihm0", "Solution Document for WordPress Feature Development", DOC, 4923, ""),
            ("1M1rJwttO_VNllfAzyABX-yrmYvOQ9gJTqOfhpWazJh4", "Tech Stack", DOC, 2331, ""),
            ("1pQ3KmxixlKolc6M_IysZEdsBYSkW-aLXM57WstitJhY", "Platform Demo", DOC, 1024, ""),
            ("1V8U8xZBn1Jt9zepig-_w8qDOM3wEImQP9fGYWorYaWM", "System Access", DOC, 1024, ""),
            ("1O7WRSxrJurEZVfkVPS14OCSijQ3HEw6H", "ProspHER - Gamification Suggestions.pdf", PDF, 61004, ""),
        ],
    },
    314: {
        "source_folders": ["1Sqb0W9NuFGzartT47fzUkni3xn-i1OSB"],
        "files": [
            ("1MRF3-BgtWXhgOE2-XCOkfBTEJDKpoTR1", "Solution call.mp4", MP4, 57655890, ""),
            ("1oZKtn4hsMy9bWwk_stCtukDeJez6qTnV4fBEJe7jxk0", "Utah Cancer Specialists - Understanding Document", DOC, 5434299, ""),
            ("17qDARSDEI0Bg1mQcGE-PizEOs73U61_gQH35IbRReY8", "Notes", DOC, 4870, ""),
            ("1tt78Qjan-4VCsC8IgGlBMegPbJQ8x9_P", "Trimmed Version.mp4", MP4, 87810482, ""),
        ],
    },
    435: {
        "source_folders": ["1exhkfdG60lRQrU1nQA2sVhm2Rnwva5Ff"],
        "files": [
            ("1xI9Tm06-myPiWlECXzY6WHDcYzhrIeyn", "Provectus Physiotherapy - Mar 24 2026 (1).mp4", MP4, 193471304, ""),
        ],
    },
    439: {
        "source_folders": ["1nHxxYGn6V73zccQvdzbRYL58OWG1l_Du"],
        "files": [
            ("18zDynezQIDjUuse89OnC_bw-PTH4WgQt", "Stephanie Emmons __ PureLogics - Apr 7 2026.mp4", MP4, 138074696, ""),
        ],
    },
    443: {
        "source_folders": ["1t9-k-VgA67wgqRQvlrK2Mgu0rZ0foP14"],
        "files": [
            ("1Y6RYhO3FLoXoZK94dx8zo5Hyr7gcHn-_82wwKAf9G0Q", "FuneralOS - Garry's Copy", SHEET, 69004, ""),
            ("1tcw9sGojldpl-KmiVPpA73syW-EvcNNewUoXBx34u-I", "FuneralOS Airtable SaaS Rebuild - Roadmap & Estimate", SHEET, 69643, ""),
            ("1zwLibme5WzB3B2xv8LyYx7GFA-JK4YMOOcFP4afQ9fw", "Reduced Estimates + Logic for ACU ", SHEET, 3903, ""),
            ("1u0UD_OGJSznZtpBjVxWyiIYg_9Jec3mc", "Anderson-Upper Cumberland Funeral Home__ PureLogics - Apr 20 2026 (3).mp4", MP4, 120905187, ""),
            # subfolder: BA DRAFT
            ("1Dxsl4hLMa0UBJjJIZva4Wit4GmjKkB2-", "FuneralOS_Airtable_SaaS_Rebuild_Scope_Workbook.xlsm", XLSM, 44725, "BA DRAFT"),
        ],
    },
    444: {
        "source_folders": ["14QzSR2hD3w_HgAidXgGSPGSWIzl_eTq-"],
        "files": [
            ("1VnzUxlM62z54YtA2efWy723j_bWQsz6k0gLxmQltKF4", "AI-Driven Outbound Growth & Engagement Intelligence System - Understanding Document", DOC, 1554663, ""),
            ("1V6WjSOVqQfCzyDQ9N7CnyQ-WiPg40o3x", "YADI LLC __ PureLogics and Di Wang - Apr 22 2026.mp4", MP4, 89102476, ""),
            ("1kPNS9H0svdQy9WT2ydjuhxh0jXVvSxNmVpYi3pUt_O0", "Client Shared Documents for context ", DOC, 1557, ""),
            # subfolder: DRAFT - holds only a shortcut to the document above
            ("1kppM2LoImtIZW6IA6OVemiJunbw_Sw_z", "AI-Driven Outbound Growth & Engagement Intelligence System - Understanding Document (PM)", SHORTCUT, 0, "DRAFT"),
        ],
    },
    449: {
        "source_folders": ["1sqh3VsXh0JVTOxXRdzn09D9NVSEka8gG"],
        "files": [
            ("1uW5zS8BZSbxUsa_hOzxJUB6TBn1jEVCZlnvE6dAmeqA", "V1.1 - AI Billing Engine - Roadmap & Estimations", SHEET, 30397, ""),
            ("1R7SeWPe9FP8LSb6RSqeJbAUdHqgLALk55_Zgb8EgaBA", "V1.0 - AI Billing Engine - Roadmap & Estimations", SHEET, 34682, ""),
            ("1wDjHgeMBC0lc7LEGETF4T347fCSJa2Ih", "PureLogics x Beacon Medical Services - May 20 2026 (1).mp4", MP4, 228622038, ""),
            ("1jJByJIX0r7rWE7oFt3gc1x2yr970rLRV", "Michael - Engineering .mp4", MP4, 213272492, ""),
            ("1hqAe6Pb4hgQL7gHZ3gZZ02n9o-UBSd_LVMpzj5suVfs", "Call Brief: Michael Georgiou — Beacon Podiatric Billing Services", DOC, 5175, ""),
            # subfolder: BA DRAFT
            ("1DlBfGygTft6SlSuv5jtNCltbJIydXoNO", "AI_Billing_Engine_Reduced_Roadmap_Estimates.csv", CSV, 18977, "BA DRAFT"),
            ("1tiVbSY40pXLLG98BkBLB1QcOn8XDndb_", "AI_Billing_CoPilot_Roadmap_Workbook.xlsm", XLSM, 89166, "BA DRAFT"),
            # subfolder: Prospect Requirements
            ("1BLIXGj2opTc1AHBTe51yhAWsjiXgArUU", "Beacon_AI_Billing_CoPilot_POC_Inputs_ROI_Validation.xlsm", XLSM, 109461, "Prospect Requirements"),
        ],
    },
    450: {
        "source_folders": ["15LZOmQ_8BrQl2WUr6o7Yn5rYmXNpSK8g"],
        "files": [
            ("1Wm_stCx0Ob0EvWikc0qbdwHKAEZfdqeEFVVHE-uvMag", "Untitled document", DOC, 24051, ""),
            ("1ejp_alhrqQrm88wsea7ZhXkn77cW7uO0", "20260506+TUB+Platform+Developer+Brief (1).docx", DOCX, 27958, ""),
            ("1ceOe8GBaAYz30m0-UEI2qqNKovzL65KhXC-4IbyrPHc", "TUB Platform — Lean Launch Scope of Work - v1.0", DOC, 5320886, ""),
            ("1c-5lYY9sp-ilGRTZ1OR18EYkHeyl6fhuOyF7bVsr2xs", "TUB - Alt Approach - Dev", DOC, 8127, ""),
            ("1N3p-cskcGimTStXP2lEcdFBTYwaQrZSB2mbZ4ObFeYA", "TUB Platform - Roadmap & Estimate", SHEET, 112420, ""),
            ("1GvIrALgU_8Rg2ZS8uvEwqjS4uBFHJUcTau0WD_iZ0OU", "TUB_Dev_Estimate_v3", SHEET, 15831, ""),
        ],
    },
    454: {
        "source_folders": ["1373DBp42YYXe8O3-SgnuyGsJyOHjkkN0"],
        "files": [
            ("1L_KXrvj5I7vvU8tqUs4xREaJ-tDjgcaZGFIlxOjUWO4", "ServiceRoute Optimizer - Roadmap & Estimate", SHEET, 40741, ""),
            ("1x-gco3DkjFZjA6CslgtsrXTkKvAS3o67", "Real Garage Life x PureLogics - Discovery Meeting  - Jun 17 2026.mp4", MP4, 70657436, ""),
            ("1HdUoWZPJLWcgNcNKGsMEXoXHYswyz18v", "[Internal] Real Garage Life x PureLogics - Discovery Meeting  - Jun 17 2026.mp4", MP4, 130409272, ""),
        ],
    },
}

# Level-1 subfolders still to walk, merged into INVENTORY once listed.
SUBFOLDERS_TO_WALK = {
    191: [("1MgIj3FqLWd4Jwv350nTW2x23IXjSzbuV", "Project 1"),
          ("1P7IW4HxsvV8zKaMu4_qApTh0is5-0Ikj", "Project 2")],
    196: [("1gHEeozJNCvGB22k8CRRVjYML4A6XLBaW", "Field Sales Agent Order Taking App"),
          ("1tXZsbsOiGkqt5VbFxIA-VZaJyoE_tyLb", "Lead Mgmt App"),
          ("1EOESBWbHFMos9TRrtMmv6_oYP-cBA1Kl", "HiHello Screenshots")],
    199: [("1tGL1XRtJJuyBL1Vc8kZlM49EMPRPfaBc", "Internal")],
    443: [("156nOau_rktLmglyiFS8_VU9FaKvzaa_n", "BA DRAFT")],
    444: [("1KZE_bOKF24tZGZz7Eo3eIWwPkPH5b-v7", "DRAFT")],
    449: [("1PhZUdfiNPIbbECdg_yPBlfBTk9MCjMhz", "BA DRAFT"),
          ("1EUkndvTUQ06gkp1Py35wBZlCPnGG-J_6", "Prospect Requirements")],
}
