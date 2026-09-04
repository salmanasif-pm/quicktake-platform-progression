"""
Real Drive inventory for List 07 (`On Hold`) batch 07i: cards 276 - 300
(no card 295 on this list).

Three grouped `parentId = ... or ...` listings covered all 24 linked folders
and all three came back non-empty, so every one is readable. Four subfolders
were walked one level down (`SUBFOLDERS_TO_WALK`).

  DEAD_FILES     ten card-level file links answer "Requested entity was not
                 found"; recorded per card in `errors`.
  EMPTY_FOLDERS  cards 293 (`VL-RS - Martin`) and 296 (`PayCom | API
                 Project`) - both were in listings that returned rows for
                 their siblings, so both are readable and, as far as a
                 listing can show, empty. Neither card links any file
                 either, so both archive as a card.md and nothing else.
  HELD_BACK      card 281's folder holds `lipsync-new-dev (1).pem`, a
                 private key. It is deliberately NOT copied and not listed
                 in `files`; see HELD_BACK below.

Card 285 (`CLAUNECKTECH LTD`) is the largest here: sixteen level-0 files -
the ClauneckTech business plan, pitch deck, marketing plan and revenue
projection alongside the Xtrinity app roadmaps and four brand JPGs - plus an
`INTERNAL` subfolder holding a third copy of the MVP roadmap.

Card 298 (`Athos Consulting, Inc - Design Work`) is a design-work card whose
folder holds two estimation docs and a `Screens` subfolder of eight app
screenshots.
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
PDF = "application/pdf"
MP4 = "video/mp4"
MOV = "video/quicktime"
PNG = "image/png"
JPG = "image/jpeg"
DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
PPTX = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
PEM = "application/x-x509-ca-cert"

GONE = "Requested entity was not found (deleted or access revoked)"

INTERNAL = "INTERNAL"
SALES = "Sales"
SCREENS = "Screens"
DESIGNS = "Designs"

INVENTORY = {
    276: {
        "source_folders": ["1rSLgdg94a-9UiQHE2kNsD0ma1qR2WSa7"],
        "files": [
            ("1WoyybWtbZpPhpASalCRGjk_m7xb_bORX", "Roadmap call.mp4", MP4, 178291912, ""),
            ("1xVtdPdPkQRkFimrMqntMN-KSWOF9SAq1", "Intro.mp4", MP4, 130129907, ""),
            ("1NST9zOGTgNBiJC1pB9g--YpHgwgkU7r4KvcB6ZiEmQo", "Changes & Additons", DOC, 3101, ""),
            ("1aHa6Q5dBzUWhuYEbHa0a0AO1iYku36okIvMMosScuuo", "Notes & Requirements", DOC, 6581, ""),
        ],
    },
    277: {
        "source_folders": ["1e330fMf8rHD1e_VGWHGeg8t_n29zCbFf"],
        "files": [
            ("1pEuxAolat0P4TMCb63K3NUD4J_9leU-1", "Intro call.mp4", MP4, 188034673, ""),
            ("1yIoJtwRyoqL8rbszY5C3yh17Bmf-FjZy", "Physaitry Pitch Presentation.pptx", PPTX, 23371376, ""),
            ("1NAcz5tMe0jN4lACmkGDeivz-sf6-5tE8", "Physaitry-India Overview (1).docx", DOCX, 31898, ""),
            ("1heqaxCcq6naK8bkr4fNdkjYVcJm4BCrS", "PHYSAITRYSCREENS (1).docx", DOCX, 31341, ""),
            ("1HcD6oMEgh5-6QVmwnpa5_70kx8Uxhusj", "Physaitry Overview US.docx", DOCX, 30581, ""),
            ("1Bt3T55DUltu9Qbp5p9XfEGcOlyhnRJhx", "ChatGPT Image Jun 12, 2025, 10_54_21 PM.png", PNG, 489, ""),
        ],
        "errors": [("file:1oXIsOzB7Lj5OEBXN3YdGB8lRUqMs35CV", GONE)],
    },
    278: {
        "source_folders": ["1JGt7e69j8808r9HYRykrE6b2HxITo_UQ"],
        "files": [
            ("1K9Bzc79CJAdCafyMPMbMFZKKXvzfDD8f", "Engineer intro call.mp4", MP4, 182772364, ""),
            ("13j3yAkIbfpJD-Ur0Z8V848tUUFDaVxFB", "Intro call.mp4", MP4, 250499622, ""),
            ("1y0hMecxWJGa998iNa19TR1t5PcJg2lRY0EdDSlKCekE", "LMS Platform - Key Requirements", DOC, 18066, ""),
            ("11GG5NCltAE2gtg3GQmGVpXn86d-3CQBdSijtfvpaWJo", "Notes & Requirements", DOC, 4486, ""),
            ("1ikFOxigBU9HQ1RIgPHvql7l5gBbg1eQP3p0Oenf5MGI", "Questions", DOC, 1024, ""),
        ],
        "errors": [("file:1qOx-3fU5DfL0gBri8wpUAqzEY08Pvg4f", GONE)],
    },
    279: {
        "source_folders": ["1WYerhcu_yC78ZLQwyLyEq3qVS2bEfHKx"],
        "files": [
            ("19zdLWWg2W-n5mW9MGCpceaPYnvzc6b73", "Intro call.mp4", MP4, 39945681, ""),
            ("14YJI01pJiK-AM4Qje8BKC2Uakggc4Y_eStw-DCA4F9w", "Notes & Requirements", DOC, 2706, ""),
        ],
    },
    280: {
        "source_folders": ["1CCkvXZySX2QE5pCGHDFJr0HLpQ3QytYe"],
        "files": [
            ("1k6ffaDsIgsBTQUshG1LSMv3MB--_a-Vl", "Trimmed - CSF 1.mp4", MP4, 198527243, ""),
            ("1ni2vxQ01IQ5KAy0Lilx8Xtx7vOrljXUr", "Trimmed - CSF 2.mp4", MP4, 219527338, ""),
            ("1Q6E3dK4IhOq75q65M592f_nRU99lpftL", "Product Roadmap.pdf", PDF, 591992, ""),
            ("1QCumt2sVYZDOTyPSnpLokqZqqF2KBLFpbkAm4njUDKs", "Notes", DOC, 5610, ""),
            ("17_dypaWw1spSgGrz8obaPInbf6Dyb_LEG9bzfGdJn84", "Copy of ProjectName - Solution Document", DOC, 1476662, ""),
        ],
    },
    281: {
        "source_folders": ["1Dqb9P9OoyaIpe8ozDSE-jE7Rr63EiTdp"],
        "files": [
            ("1C2f2BPF4LnFKXvhtVA-I0VCuCGGhGYny", "Follow up call 13th May.mp4", MP4, 50800718, ""),
            ("1s0VVY7K6gscK-iOsC6s1sXKc2cQym6K5", "Intro call.mp4", MP4, 204684235, ""),
            ("1nfjhrc2CtKRmNT4_Yx5XVxTla11PYSO3GtFSokDyTTU", "Notes from 13th May", DOC, 3622, ""),
            ("1TmROQo381dkGpsDJb4lUd7Bqn1SHnyyKj8k3SADxo50", "Copy of AI Sales Agent (Avatar Update) - Solution Document", DOC, 2154187, ""),
            ("14R-qrPTArFAQW-3SzCXajgc5sodyDYXe1RPeLIVD7xA", "AI Sales Agent (Avatar Update) - Solution Document", DOC, 2153614, ""),
            ("1_dChS6W8JXnjrFKTCs634n4vyyEDX_nCcaZ5mry0Z80", "Notes & Requirements", DOC, 3765, ""),
        ],
    },
    282: {
        "source_folders": ["15WGFwNhpNev7NZLo2POYtgVnaXg2ARpZ"],
        "files": [
            ("1Ds4UGF1heOYcEro9qmC4QYbyfa9ibHuR", "Recording (1).mp4", MP4, 93717260, ""),
            ("1tE4DidGyYe4dgrtIxOini-w3c60sZHEi84rGAQvQ9LE", "Copy of Notes - 19th Aug", DOC, 9653, ""),
        ],
        "errors": [
            ("file:1BVR-CQ3NuJM0JnkDPAMBNvR9uw8S0yoaAFNWPWfu2Gw", GONE),
            ("file:1P5bFP2x2uZuF0fGcew28SV7fM1NoSSFg", GONE),
        ],
    },
    283: {
        "source_folders": ["11YSJICiiHYdCdHd09_BD7SGUVk7Olsjn"],
        "files": [
            ("1fGvsfvSgHFz6T8WjsU1KKXQY9Je0p5G04oOod3Pi-WM", "Notes", DOC, 6456, ""),
            ("1DzaTPucN5J4n0i5o1zIcERCaKoeftklA", "Trimmed - Glass call.mp4", MP4, 103995792, ""),
        ],
    },
    284: {
        "source_folders": ["1NVoLP8Q-zgoasXU3H478O1k-gD4Elsww"],
        "files": [
            ("1tzB4MXkFBnC4lzw5G5l_ga5WGGr7Vpxy", "Aug 7th Call.mp4", MP4, 276452391, ""),
            ("1KYFylROS44EYhbNEmQOe6oYFOc3fl7dVcdDGsyo8Kgg", "Requirement 7th Aug", DOC, 7649, ""),
            ("18sd6dos1oRba_LbUipQuuhjnBBJ62cCHPqOz83pBZwA", "Requirement Doc", DOC, 5134, ""),
            ("18Gfkn5ovoZPoa3EywtuHJ1FSsVl6VM0q", "Discovery call Continued.mp4", MP4, 34965319, ""),
            ("1Se1B-0RrrVT6CT-v9ZoV_nYYQwv9rEjk", "Discovery call .mp4", MP4, 129359191, ""),
            ("1nmX68jdWDY4rb5-doLxloJPhGsd0qOaL", "Roadmap call - 12 Dec.mp4", MP4, 175806461, ""),
            ("1dTc8VZCr3ZkPTiIPsfMvOR4E9gaIbqyQ2vNDLpff6JE", "PBL Plans Website Enhancements - Roadmap & Estimate", SHEET, 20277, ""),
        ],
        "errors": [("file:1rIEY3R5cI2BM_qPyXIiHqEtgyPilWXHL", GONE)],
    },
    285: {
        "source_folders": ["15eOvOfjAVozQeaf5RfABzHmjsLG5MBV1"],
        "files": [
            ("1SJW58XxNmM_Ey7429VOOw7TUWlcFC__aan5fs3Wx0Rg", "MVP - Xtrinity Mobile App - Roadmap & Estimate", SHEET, 28090, ""),
            ("10a_OHIfB5aE6GK7g-0tWpwAZTX9xepI8VJLSDCN7xxA", "Xtrinity Mobile App - Roadmap & Estimate", SHEET, 93082, ""),
            ("1y01aSszBV4lrbW5SXghO-Dje_g4Lka0WtxiyELlO9mE", "CLAUNECHTECH INC - Solution Document", DOC, 1476655, ""),
            ("1vO5YiBIGW8eEvcXVielvD2Hb02H4xLS8wueGfWPM4Iw", "Read Me", DOC, 1024, ""),
            ("1F5LoJBqgwn-CDjN4RYf1UKtidbL4PdoA", "TrackonX.jpg", JPG, 125251, ""),
            ("1BS6jae1Vxwuw4mpqPnMX0qpYTbG95ku8", "Claunchtech.jpg", JPG, 120733, ""),
            ("1u0UvLJ6RW6Q2Tfza7Rm9P8TCoar8YyJo", "WelcomeX.jpg", JPG, 111591, ""),
            ("1X0Rl3TL1qHrQRxkjii2WfopGdPEzwExi", "VigilantX.jpg", JPG, 134776, ""),
            ("1EuR5CSWA2F2C8CITwmus-EHO3ZWqG8pk", "ClauneckTech_Competitor_Analysis_Updated.pdf", PDF, 3816, ""),
            ("1zuYPcCKPQBMQKn1IWYAU5rqx3scUaM9Wv6p1bNdJEhI", "PITCH DECK", DOC, 2531964, ""),
            ("1Quo9xFjK4O-F7xwzUfZThfYNJVL9hk3B", "Xtrinity Logo.jpg", JPG, 32196, ""),
            ("17Vexm5A1uvHrWi8DH-V5ohi4eh1gIW4b", "CLAUNECKTECH INC. REVENUE PROJECTION  (1).pdf", PDF, 295243, ""),
            ("1VVFwwYv2TaOIAEDgOcS-47WjRHBddYbI", "PARTNERSHIP PROPOSAL.pdf", PDF, 280899, ""),
            ("1AaQQVflvIWjBVJganQ0UTXXzR7o-ZjCV", "CLAUNECKTECH INC. MARKETING PLAN.pdf", PDF, 658819, ""),
            ("1FzW1EbVDEBiotINjN9w17Kun6JhsAFB-", "BUSINESS PLAN WITHOUT FINANCIAL OVERVIEW.pdf", PDF, 4895916, ""),
            ("1tWlIAjmMHoiKOAGmKww30OX4ADg3mOK-", "PITCH DECK.pdf", PDF, 2961761, ""),
            ("1yB54oubRgHJczEu3s7I7bpkT7v-wW17x6QXqW-bQRIY", "MVP | Xtrinity Mobile App - Roadmap & Estimate", SHEET, 29024, INTERNAL),
        ],
    },
    286: {
        "source_folders": ["1GxNx9M6UEtiSl5POz_58XbcH832viYbr"],
        "files": [
            ("1F8Il55gLGZfSkkSJZPTNTKKCi8MHL7x4", "trimmed - Stealth.mov", MOV, 26238057, ""),
            ("149JxWv1RUGZmFqXYE5R3qVZHPATTllndaJ8vrhwVTHM", "Read Me", DOC, 1024, ""),
            ("1-l8kJWrjyiuHX1JYeH01WcAb-MWic4XKqNVAFA1qg5w", "Requirements", DOC, 6679, ""),
        ],
    },
    287: {
        "source_folders": ["1JGZjVRIoBSpD_skrFWUqNdWOQT5lqGW3"],
        "files": [
            ("1TE_8xLTURqCXUZx5RhHAAJCUI-niuGbX", "Trimmed - Call.mp4", MP4, 316998772, ""),
            ("1SOGtfto4pRpnVGJ4rehxat88mLXlmP8ZnxLQFiptgh0", "Intelligent HR Management Platform - Roadmap & Estimate", SHEET, 49908, ""),
            ("1ZXhPXZcwGdT12zlRW55alImGziPoE2CNW7bjJjnzw5M", "Intelligent HR Management Platform - Solution Document", DOC, 1476495, ""),
            ("1nOLiOtqMnFpDsa9iG_ykD0W5ajY6G0e80WVZ16ML7nI", "Client shared Requirement", DOC, 7881, ""),
            ("1udJPzYovAdXdqlRXu8-ACJ-BeizEOwNQvG0ZWzInjVA", "Demo Requirements", DOC, 7686, ""),
        ],
        "errors": [("file:12-IO5t594thv-X1UMjkePbWwULbQlLOu", GONE)],
    },
    288: {
        "source_folders": ["1kzbiSn8pxXecjFwMPA3-aEIFgcB4OT4j"],
        "files": [
            ("1QLa8i0iKENO1JEN0mAgJ7yBjtbB66XCmfmPXs-X1Dyg", "Read Me", DOC, 1024, ""),
            ("1whoZHcIKXj_a9OjdJox_GWrr6JZQHp9WoQ8C9PHMqn4", "Time-Tracking Mobile App Development - Solution Document", DOC, 1494724, ""),
            ("1l_6MuhjrjcStm_iU0U0My7IxkseTcxy4XPnxkaoLSyU", "Notes", DOC, 4394, ""),
        ],
    },
    289: {
        "source_folders": ["1EEFOZKQGIwcKeV5Wd3bci1_hOqaZqa6P"],
        "files": [
            ("15WnEbYE1HFCJEJ_A-CDGMsAAJGWwE4xr", "Trimmed - Audio.mov", MOV, 19204029, ""),
            ("18TFRiwepheSjcfQdQAVkd50vs48hU-ewa_qEi9R0DMM", "Requirements", DOC, 9098, ""),
        ],
    },
    290: {
        "source_folders": ["11e6VQWyu0LS_DE2KQdWL13irF5yecFLp"],
        "files": [
            ("1CLMaJ2AYc_8Vbiqb8t-AsQhqz-DPUTjb", "Demo call.mp4", MP4, 140326407, ""),
            ("1cV_Vz0QBnl9_1q7Ghc2GYD0FhH78tv-kSbEEBZL8xX8", "Demo call notes", DOC, 1024, ""),
            ("1Hqq_UBZvDXv5ySJg_JK_YGSYFTPbowD9", "Intro call.mp4", MP4, 127330124, ""),
            ("1hiscPAl6tlDfCnMLTYqZqON6Oph_fOuUkYu3qU2_T-Q", "Notes from our 13th June call", DOC, 7214, ""),
        ],
        "errors": [("file:1VdELnvnLd3vcROFzS_OvQWl-ZWG_shy3", GONE)],
    },
    291: {
        "source_folders": ["1lAcLCyVGzGSQ0Eb5Nke8Dy0SEgcfEtJU"],
        "files": [
            ("1L24cDKQm3a_pC2Ussbzn5GHmyRK-lcBP", "Requirement call.mp4", MP4, 43819711, ""),
            ("1k5n5RHvyxyg1LLa0f1w7h8GJTZUrnIdddp2z_Nnfch0", "Low Code Project Ideas - Solution Document", DOC, 1497662, ""),
            ("1JS_6cLvZWPMyM6NIIF7et_Hk5sSeWaZj213bX_vT16c", "Projects Requirement Document", DOC, 8628, ""),
            ("1hKloTk75LlgD0K3YwJcmwXX-VzlxI9o9", "Vantage IQ Feedback Friday Pitch Deck 221.pdf", PDF, 6391343, ""),
            ("1NxZmZaJRVk-r8s5QkuC2U982mY58wosa", "Copy of  Pricing.xlsx", XLSX, 111967, SALES),
        ],
    },
    292: {
        "source_folders": ["1yS7vojOL20fnAmUeKb6OAdeezbZwm5Z0"],
        "files": [
            ("1rt81eDJAWFlRUU5ik-NBB9RSnVh7muqf", "QR Code.png", PNG, 19806, ""),
            ("15xj5756elaYj6E1_Rh1dvlz0dKhqZLxN5HEOFAquNs0", "Notes & Requirements", DOC, 3802, ""),
            ("1-9qsLs1GTNZ8nHJPkA5o_AfZwk0ePlInxW-vuZZ_rmU", "TLT Turbo QR Code Integrations - Solution Document", DOC, 1476658, ""),
            ("1j7t7HpJmb7ISs04tmSOtCW4Ib0RPcL1a", "Intro Call.mp4", MP4, 70156250, ""),
        ],
    },
    293: {"source_folders": ["1MYwD2LgtnssYjW62LRP7P39ElPz5a_yT"], "files": []},
    294: {
        "source_folders": ["1yIUvUIv1ilVNNCdA3JXwLERN0M_k5tfu"],
        "files": [
            ("1rYdoMlnlDbSLSaD3hjMXqjPqrsle-nwVNHcvqZ8iuRc", "Azure DevOps -  Solution Document for Fred", DOC, 10714, ""),
        ],
    },
    296: {"source_folders": ["1Z_TW9I5PHiYuuwa6M8LuMgpNVhxZyKPw"], "files": []},
    297: {
        "source_folders": ["16cbRl2ltL729Amjo9YYQ7sT-jbshHvQX"],
        "files": [
            ("1WB8SrkGgD1aGHD55vebS73gNnogKtOHa", "Intro call.mp4", MP4, 31305683, ""),
            ("1axfWUR6lQ4olMdYUi2AsTrTNcr178AIiVfde3SWdUgI", "Property Management System Development - Solution Document", DOC, 1476495, ""),
            ("1ryL6FUnq5lhKCoS0acKzkGdE40V42c7EI9FuEP_I0hA", "Notes", DOC, 4327, ""),
        ],
        "errors": [("file:1QfFW7UN6vGnTa-TuG8E9oZNoffYjQv3_", GONE)],
    },
    298: {
        "source_folders": ["1t-yIDDA6lUHTVHzYKHOa6NGm8k4UErAk"],
        "files": [
            ("1jEDh-azTq8Off0NRYZIVO42pgf8G4gcpH5Qi4UQh2ho", "Docs of Cannabis website redesign Estimations", DOC, 22895, ""),
            ("1Y2rgx3jopwBujEEC_0zSevWs1ps2oeRy0mjarClX9y4", "Copy of Docs of Cannabis website redesign Estimations", DOC, 22911, ""),
            ("1U0zu_I4SCdESsCBXWFkYthfTZo2bbEQpPsy93IakzyE", "Flight App Estimations", DOC, 20162, ""),
            ("1k8jPDmGiYnAaocv59A3rx3ZFN8PQ42Kh", "Results with Current Filter.png", PNG, 342765, SCREENS),
            ("1upGWCmWnfiY1rdQ68SOOVwUimBh5UYR9", "Results with Forecast Filter.png", PNG, 374049, SCREENS),
            ("1c06f1ktLbaWYiWLLNfna-V3l8U04mmDC", "WeatherIQ forecast/current screens.png", PNG, 237007, SCREENS),
            ("1lD_tcLh0TSGKL2rPPOqH-as4PZfP_w4z", "WeatherIQ detailed analysis modal.png", PNG, 143384, SCREENS),
            ("1RbD8Kd7sFyG6XAR22hZm-hE2udBq_93S", "Runway Info modal.png", PNG, 72666, SCREENS),
            ("1EfKbEWdIjbpLit71esJ_WkuUu7d-iER5", "Map view with airport markers.png", PNG, 3399149, SCREENS),
            ("1pDeMoU86-23xUBhLagxfy4mW8G0JPDtA", "Landing & airport requirement filters.png", PNG, 512538, SCREENS),
            ("1SqATQnLV23--qQ6nZNTtN8Huvfe-UISn", "Expanded airport data sheet.png", PNG, 545564, SCREENS),
        ],
    },
    299: {
        "source_folders": ["1YpMEBNlzguJp13Im7c_jSQoNCkpbPN5Q"],
        "files": [
            ("1Lrmh5s3L9y2LGSFIV6YZqdj-MqSWasWvWA77Qi8lHJE", "AI-enabled Telemedicine App - Roadmap & Estimate", SHEET, 69814, ""),
            ("1QXBxMHAu2XAdopJZ78E3U-teCFM8WqIB", "Intro call.mp4", MP4, 120457199, ""),
            ("1fAZ7K6ZBTZ4oOfUPYv68AP1dQ3-oJsVE", "Follow up meeting - 24th Sep.mp4", MP4, 79291936, ""),
            ("1jiIOKRm5pDKL-wsJ3c4DA0UHhJ0M3k48ghSw8OnG38A", "Notes ", DOC, 6424, ""),
        ],
        "errors": [("file:1CQ4nGuvDcmkm8-KNGWNEkVK0mfalXCE_", GONE)],
    },
    300: {
        "source_folders": ["1fuSzdIiL1GTtlJ_MQ_N5wDl_oZtZxhUP"],
        "files": [
            ("1insa1hKHNNQfQErnPbo5IdNnybk_FGl0", "Follow up meeting 22nd sep.mp4", MP4, 74268656, ""),
            ("1yRMCrnGT9SDAhCZo_tNo3Vmh2Oc-rXjo", "Trimmed - Boom.ai.mp4", MP4, 68020760, ""),
            ("1hA0eIbujx_U2fDKTnCTcUorrgb4LhBkm", "IMG_0116.jpeg", JPG, 102991, ""),
            ("1d_Ct2pkHt-qQbe-hp-eYKJbDFo87U_hQya1vZ_Nazok", "Notes from 22nd sep", DOC, 3628, ""),
            ("1U-LygiWqbEiaXV58hbXpvGc4n4PGp0-igln9HdcKdmM", "Notes", DOC, 8056, ""),
            ("1LVvKo0aiSfIzYe9R9YFGNz_KOQKPyyLZ", "B3AF7F04-4784-479B-A0B1-195187075B61.jpg", JPG, 100846, ""),
            ("1U3HhvihsW7xVjaXLdSYdteTj29ATREh1", "ChatGPT Image Sep 19, 2025, 10_19_37 PM.png", PNG, 1423259, DESIGNS),
        ],
        "errors": [("file:1SVqS0YXWqmLqbH7PfFxkyVQZ5Lsge6SZ", GONE)],
    },
}

EMPTY_FOLDERS = {
    293: [("1MYwD2LgtnssYjW62LRP7P39ElPz5a_yT", "linked folder")],
    296: [("1Z_TW9I5PHiYuuwa6M8LuMgpNVhxZyKPw", "linked folder")],
}

# Files found by discovery and deliberately NOT copied, with the reason.
HELD_BACK = {
    281: [("18yydPkKl3ecEBaircFSEzep9UJ0nHbU-",
           "lipsync-new-dev (1).pem",
           "private key material, not a deliverable")],
}

SUBFOLDERS_TO_WALK = {
    285: [("1ToLPdQUVWzK2KGONy4sNrMiVV8G9zE0o", INTERNAL)],
    291: [("1vVn8BMWNfOmygKJDZie3-KAnweOpqCTE", SALES)],
    298: [("1iOLULP_wuL0dhCDihQaWrPt-1AqUfsfa", SCREENS)],
    300: [("1blSPdNgQnzACVwtO87T2mBZzJDpnyYZB", DESIGNS)],
}
