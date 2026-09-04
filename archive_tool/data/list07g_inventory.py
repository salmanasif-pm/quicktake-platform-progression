"""
Real Drive inventory for List 07 (`On Hold`) batch 07g: cards 222, 223, 224,
225, 226, 230, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244,
245, 246, 247, 248, 250 and 251.

A folder listing can UNDER-REPORT. Card 235's folder lists two mp4s whether
queried alone or grouped, yet `get_file_metadata` on the card's own file
links reports two Google files - `Meeting Notes - Geniune AI ` and
`ChefLou's Army | AI Chatbot Development - Roadmap & Estimate` - whose
parentId IS that folder. Card 245's `Engineering` folder lists nothing at
all, yet its roadmap sheet reports that folder as its parent. Unioning the
card's own file links with the folder listing (which the shipped discovery
already does) is what recovers them; a folder listing alone is not proof of
a folder's contents.

  DEAD_FOLDERS   card 245's first linked folder.
  EMPTY_FOLDERS  cards 233 and 234 - `Engineering` and `Engneering` (sic),
                 both resolve and are readable. Card 245's second folder
                 lists empty but is not: see above.
  DEAD_FILES     eight card-level file links answer "Requested entity was
                 not found" - cards 235, 238, 241, 242, 244, 245, 250, 251,
                 one each; recorded per card in `errors`.

Cards 239's two card-level links live in a DIFFERENT folder
(1PXOtd01KGsKMf3jqUb5YOO6gkGsWXxnz) from the one the card links, so they are
inventoried with an empty containing-folder.

Card 243 is the deepest here: fifteen level-0 files spanning June 2024 to
January 2025 plus a `2023` subfolder with the predecessor project's roadmap
and requirements. Card 248's `Novemeber 26, 2024` (sic) subfolder holds
eleven more.
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
PDF = "application/pdf"
MP4 = "video/mp4"
PNG = "image/png"
CSV = "text/csv"
DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
ZIP = "application/zip"
M4A = "audio/x-m4a"

GONE = "Requested entity was not found (deleted or access revoked)"
Y2023 = "2023"
NOV26 = "Novemeber 26, 2024"

INVENTORY = {
    222: {
        "source_folders": ["1Fm0zyC84_g90yn63oNup22TBVfVHd5Ga"],
        "files": [
            ("1JHCQp9CazVMdf474jsQpJ5unf7315O7gNGAYb5uQ-1g", "1. DayHaul Mobile Application - Roadmap & Estimate", SHEET, 19889, ""),
            ("1NBkS2gdqSg7yLzckST6p-TGJPcQRdQRD", "2. MindMapping.pdf", PDF, 1766979, ""),
            ("16aZ7d4jLlNTjrOxn9afNxHpiF7WaJttN", "3. Process Flow DIagram.pdf", PDF, 198352, ""),
            ("1s8XyK6XsL3tR2bRIbm7swG3w5eGQftaI", "4. Contractor Balsamiq Mockups.pdf", PDF, 1184784, ""),
            ("1QmnYN31oWewyfdgJkfxRovj2m1lhZb2g", "5. Trucker Panel.pdf", PDF, 1119007, ""),
            ("1GwG4_LnZqWuFQFi3n7D-xhe6BgP-XX9P", "Recording.mp4", MP4, 126102803, ""),
        ],
    },
    223: {
        "source_folders": ["1duEDrljFPq-srwa00FcBUy9AqmFmeJYB"],
        "files": [
            ("1sRlT2reGrTJuY40lIvEBhPwvEgbg7zaz", "Recording - Deverg.mp4", MP4, 443449438, ""),
        ],
    },
    224: {
        "source_folders": ["1vstU2E-9CPLyJjVvhks_6nkGyu__RL4p"],
        "files": [
            ("1bZGzXcD3GfI26jHO-R9DURPBFvt4A77D", "1. Process Flow Diagram.pdf", PDF, 165779, ""),
            ("1hM7haZ2IDYO11lE6bwYyMUwqFKyzlPnl", "2. Mindmap.pdf", PDF, 58116, ""),
            ("1VAtHT0VlzaSnWllegIITriB06vyEoM6WMmu3j-B2BJY", "Requirements", DOC, 6394, ""),
            ("15Hk8Ohy1u9Buoq8BZxYX0xlfUMtW1QfK", "Hardigree Consulting - Solution (Prepared by Zukhruf).pdf", PDF, 292962, ""),
            ("16NJMFfcs6ihy_YZerwg6fJTZRT5hUBFd", "Hardigree - Engineering Recording.mp4", MP4, 78869892, ""),
        ],
    },
    225: {
        "source_folders": ["1UM4O3FZePSXujWhGMfgId5hmBfJnDHrI"],
        "files": [
            ("1T4ke5KEwKqBwBaUQvANSyPBM6lexsBvCj2TvUCbKS6c", "AI Proposal Generation - Solution Document", DOC, 1476370, ""),
            ("1jVNQqMt1sqiudZ6LD5q-Yam93rQIS8Zj", "Recording.mp4", MP4, 20259222, ""),
        ],
    },
    226: {
        "source_folders": ["1_fKEFKf_Yj6VArbuxZCn8RLJafBomY1P"],
        "files": [
            ("1m-DaD9_jTk_5g49L0oxyhfYU8wR36HnTQws5yi_zlIk", "Intellihance - Product Review & Understanding", DOC, 5300823, ""),
            ("1PEiJTrCEnli_Ps0OgTUMw2OBF_Ow9o7M-DiHPG76Fy8", "Intellihance 2.0 - Strategic Recommendations Document", DOC, 5300828, ""),
            ("1a9UYrLGix2uuPChmYYses2sdbb3bqeUpoiBBvIh8zoQ", "Questions from BA Team", DOC, 2300, ""),
            ("1fAOA-fqDayqcoQ7-BguDp6WJSWcXrPuqhkbSAJkN1HQ", "Notes", DOC, 12129, ""),
            ("1SSP_j5oNzqQLVkv2CSATVvWP96sJVAD0", "Intro call.mp4", MP4, 158786292, ""),
        ],
    },
    230: {
        "source_folders": ["1_SX2wQ-WTXRAuLWTFcd7VrCk_T5M_xD5"],
        "files": [
            ("1TQaUQ5N9Jn-N-1c89TDzNuwrr60dkylK", "THA Peer Review Platform Presentation.pdf", PDF, 6672458, ""),
            ("1MeDJCR5xKnIkWOv-A58kfEeEELqWzh7dj1c5uqjtuaU", "Peer Review & Case Management System - Roadmap", SHEET, 20422, ""),
            ("1n2zQ--a9OnOdMN6YXkXD2KN0A0L499zax_VGyQIRAks", "Read Me", DOC, 1024, ""),
            ("1mgdn7LTx2Dl7GaHodG9COIP2JOfsqxcRMCQ18gRzyio", "Notes & Requirements 15th Nov call", DOC, 8824, ""),
            ("1jDhyP9jNczK444VjYt3NtPKjHereEhRE", "Team demo call.mp4", MP4, 207005374, ""),
            ("1DhNzWGsGWzPKhfNGMsMn3JuFRduZMy6u", "Intro call.mp4", MP4, 338217363, ""),
        ],
    },
    233: {"source_folders": ["1bAdYVquwPhWtcDRql8ZvSklrn0SiRu1E"], "files": []},
    234: {"source_folders": ["1Yv0TRvFuv4drvUJNp5OT78ERArHq9Tm2"], "files": []},
    235: {
        "source_folders": ["1EN-FFlc1LqYNmBpFPqXUiryRv7u8klbF"],
        "files": [
            ("151gvv6xIRP3-Ef5CBYs3NnEnf0yv-3GwmfgwKfQM9aU", "Meeting Notes - Geniune AI ", DOC, 2367, ""),
            ("1GpT1ErQDwhklDnE1Jq674peloQ__cufZg1N660ElUgE", "ChefLou's Army | AI Chatbot Development - Roadmap & Estimate", SHEET, 19739, ""),
            ("1ifz7NJsQV657sXlx_sJqIoeKC4oW0DJd", "Intro Discovery call.mp4", MP4, 219347533, ""),
            ("1Bgu-wJY3qHqyipCgM6jug3Lhqs9ra2zF", "Follow up Feature Discussion Call.mp4", MP4, 70723748, ""),
        ],
        "errors": [("file:1KgDy6t9_rWPTb_dGn2AM96PzCV87ykNo", GONE)],
    },
    236: {
        "source_folders": ["10fbpVkX8_DpQGzuXlfmpDiwZ1n37MTgv"],
        "files": [
            ("1JuYqlSpJxAKyEVcVcobT0sri9sLn2Xp_3MAnPZ4mols", "Problem Statement for ARPA-H & Our capabilities", DOC, 3397, ""),
            ("110h39Ei3CMLuqxweTLOorclPTWf2CsiNXmZMyxUZKsk", "Problem Statement for Agentic AI for Health Care & Our Capabilities", DOC, 3899, ""),
            ("16UWmOBmukfx74mj6SzoVPRoA2mFJPnduqtPbeZTpdHI", "Notes & Requirements", DOC, 3553, ""),
            ("1u6wOxC6BbnT6rSow64gMgXFGh_309BFpmnajNEytElw", "Copy of Solution Document - Template", DOC, 15557, ""),
            ("1xokuSVlaeYbUC4R0EIg-lRHlVnfOete-", "ARPA-H_RFI_75N992-25-RFI-106.pdf.pdf", PDF, 103123, ""),
            ("1ob_0p5u2ffsxuVAL_CQ8CczKQSrBkgty", "ARPA-H_RFI_75N992-25-RFI-106_-_Revised.pdf.pdf", PDF, 103008, ""),
            ("1aewf122XPTs1uyaK9IJOoxAHq4Ng26nI", "AGENTIC ARTIFICIAL INTELLIGENCE FOR HEALTHCARE (AI).pdf", PDF, 1312235, ""),
        ],
    },
    237: {
        "source_folders": ["1iAcdPTtBuYQKdPGXY0-2CGOeugKN4nxf"],
        "files": [
            ("1tOffIayE8tplXudojTpcnRNi5rUMf3SKEotdcbL8FNQ", "Optimizing Healthcare Operations Through System Integration and Modernization - Solution Document", DOC, 30234, ""),
            ("1m1OeUT9RP4N43D9P43Nb3V5d5SK4jhOEMSZV9Ze-tPQ", "REQUIREMENTS:", DOC, 2461, ""),
            ("1WM0zk_y52ZzUCM7jivzV83Wr85gI4YWy", "Discovery Call.mp4", MP4, 63330302, ""),
        ],
    },
    238: {
        "source_folders": ["1e4smEyjEH0zjQC8jTQyylWtm9aFMMV-S"],
        "files": [
            ("1l1Sg19ROGGRu-CVqB7QIbyPioGZLh78B5kCwceh-OjI", "Property Analytics App - Solution Document", DOC, 39253, ""),
            ("1m0XAfMTo-Lo-LiZuX7DF_tr0h3DP_0XMrRPL0rJVuAM", "REQUIREMENTS:", DOC, 5905, ""),
            ("1iDOD1SZyRSjPWpPSINoCMCEnzbMkfuNoQXLqxjRdGS0", "Notes", DOC, 1228, ""),
            ("1FMium3lKsWOxjwr2FkpzDTxm1xQby_SXX5vUse8lLsM", "Copy of Master Template - Roadmap & Estimate", SHEET, 23642, ""),
            ("1XIPKtSS6-h_zUqF9U_BiXqsI2tKP_gGf", "Trimmed Discussion.mp4", MP4, 193306251, ""),
        ],
        "errors": [("file:1y43GMxzy6rvdT5EdYNDHlcMzYuBSHOtY", GONE)],
    },
    239: {
        "source_folders": ["1s7JYFJZ5FtNsIEeKCbgvGygDl0BchPu-"],
        "files": [
            ("1RCBUgnGGlfRN7-M4NTIiE9WzMW8AgskANM5GaBrH4tU", "Copy of Solution Document - Template", DOC, 15558, ""),
            ("1W1JO3er5ylIquuaomANTsN7bvWMyj_j2", "Trading Platfom Updates.pdf", PDF, 1767165, ""),
            ("1oR7rEsYhsAGPs8bkwqlNBEUzPR-mG-SQ", "video1051363293.mp4", MP4, 160935240, ""),
            ("1qZyyrni5PCp2EAiAMpu3EdmM2_xU96Fr", "video1058895111.mp4", MP4, 33507146, ""),
        ],
    },
    240: {
        "source_folders": ["1LiuC3_B_EvhP4f6EBpwo1xWZiXjXNIjY"],
        "files": [
            ("1P-gqFvfi_ZPDzTmu9OjCuoSBeZ6xSC4duImGpi_pYiE", "TourLife.eu -  Solution Document ", DOC, 19401, ""),
            ("1v539BJ7Sk5eRWXh7gxR3Jd7fSNNkALkNUm-NEFjT7Pc", "FeatureList", SHEET, 14022, ""),
            ("13sx3Hkqy3VXhqBNF74JnkB4dCvdDYf02", "MindMapping.pdf", PDF, 123112, ""),
            ("1lhpgY7WwhVczcbI6aUa0p9lwtZC0JdzR", "PureLogic.docx", DOCX, 17962, ""),
            ("1QbVgJFAgPS7X87FFF2YyDDbFlukQHaX3yfDF2CIWtVA", "Notes & Requirements", DOC, 2832, ""),
            ("1tfpdUwBGu-AxgZreLGQ7u0VHtoaJhYYMCo-Fj51qxA8", "Copy of Solution Document - Template", DOC, 15557, ""),
            ("1U31R5IsREjETuqVzfQ8V2bxx5RdXHmvb", "Trimmed - Design Needs.mp4", MP4, 67845289, ""),
        ],
    },
    241: {
        "source_folders": ["1OwoX0WjVK3MpGFI2sWS-LIWuRK_Vw-JZ"],
        "files": [
            ("1_kcraZ-viIbPBQV5XieEevjrpFxec1YC", "Flow Diagrams.pdf", PDF, 5031435, ""),
            ("1sq3QRPEK07Qp4cvtNtrvzJOypZedh6NS", "MindMapping.png", PNG, 557610, ""),
            ("1S9oHU8fSudiNdENQlGNNunegST6qrrEAIeB4e9a8IM8", "Requirements", DOC, 8662, ""),
            ("1Gp28nPltlqcEYGM7e8MRkULIqa0bTxJBN9BXDPHS1zs", " Notes from 28th Jan call", DOC, 3468, ""),
            ("1iNgOkDQiqNnZLGYwL43pbUG_rfCh0Dp10eeRD9S64bY", "Copy of Master Template - Roadmap & Estimate", SHEET, 23645, ""),
            ("1T6DEZVJ9To_v9sHDILxQwMltnraHTTBF", "Roadmap Presentation call.mp4", MP4, 163474317, ""),
            ("1k9afZ1l8tehVk_5qPp4wBBiILNHpdZ5S", "Career coaching platform.m4a", M4A, 35761967, ""),
        ],
        "errors": [("file:1CGkUNyvzBKotvu-RhBiP7oWSeBzvYcO8", GONE)],
    },
    242: {
        "source_folders": ["1DZXOw1i53HGnpmtInuudZ6AAlb4QP71a"],
        "files": [
            ("1IPvFIytiNl45khg-pnhXvZRJ0AsmrG4Q5lcmaYO8xSY", "LEE Thermal Energy Application | Web App Development - Roadmap & Estimations", SHEET, 38643, ""),
            ("1FBRXJciOMYqN_wmautNJiGI8SI0TjBVxdmmxsIpltGc", "AI Requiremets", DOC, 3347, ""),
            ("1usMPMgCZF42WcWTjLhLCoTtz9sd87k96ZJIzb68xRTE", "Requirements: ", DOC, 2082, ""),
            ("10NvXX44BgMi7-IQ4l_kJ-fuSK9yYkvfD", "AI Additons to the Platforms.mp4", MP4, 125774272, ""),
            ("1EzbNjD7hRcMrIQGni4trrWgWJ2TzrQHo", "Roadmap Presentation call.mp4", MP4, 66233621, ""),
            ("1TD88B6meGKHSAbOEuWzc2Dc6L2WQNFu2", "Discovery.mp4", MP4, 392692929, ""),
        ],
        "errors": [("file:1ygGFJ-uuGri3qWgidwaNb8QeGT2Hb2AE", GONE)],
    },
    243: {
        "source_folders": ["1IQ6o8sIf-1HBWqL_g4MNH7tIDaM7C8HP"],
        "files": [
            ("1FKDGTj7-Vgkv-rrJ9m2AE_2QOJd0FAIX", "Flow Diagram.pdf", PDF, 363262, ""),
            ("1tnt9lSDgUQ9dSBgrYoLbivNxIkWKIXjngDKFC2DZlpw", "1. AI_Powered Competitor Insights | Web App Development - Roadmap & Estimate", SHEET, 29608, ""),
            ("1fCQdpH9UdnHk-oPz_Gir6PT1waC0vwgypl85bxaPzKs", "Enhancing Competitive Insights Through AI-Driven Public Content Analysis - Solution Document", DOC, 20116, ""),
            ("1VjCp6XV9qQzn4uEP0uHsmMjjtYYXPu6_RUzWUtE8Oiw", "5 DEC - Email Communication with Brent", DOC, 7578, ""),
            ("1st5ZW_vcb4JOcBtFfZifnwW-KB-9Vy_8gdNkYoeyYWQ", "ServBetter~(New Features ) | Web Application Development - Roadmap", SHEET, 33235, ""),
            ("1ZWMEVZDu4pFo55JBwq--HbC-aSyMNr5T", "new -- requirements-06.25.24 (1).xlsx", XLSX, 109186, ""),
            ("1z4_q12AuK_XCfERVL1aiyNSnQSVyHQYH", "requirements-06.25.24.xlsx", XLSX, 101091, ""),
            ("16W3dlQR640Gmf8nafZ2CWkAR1v24z9bMbsvaZNvAIBw", "19 June - MOMs", DOC, 3540, ""),
            ("1LEhRIVCLNeAlEAq_nevyLKoz9pQUHvZMVV1w75CLUQ8", "28 June Meeting ", DOC, 1024, ""),
            ("1z9_rNoSLh_SlSAST74OQ4ydlwuNjx-VrQpV0cPJBDl0", "24 June MOms ", DOC, 1024, ""),
            ("1xJKiyu4adJvRIhFFIWLT5I1K4HRIInl1", "serv-20240621T202559Z-001.zip", ZIP, 100526726, ""),
            ("1Q74MO6X6qvSULPP6zbyIdV9aOWNLwSv3", "3 jan 2025  -- Brent_video1743642018.mp4", MP4, 268992107, ""),
            ("18IIZmmqFJcJR8PUnTmxUXqL2XM325gWz", "28 june 2024 video1031940428.mp4", MP4, 175757024, ""),
            ("1SXbMFTD8lXGxl3etSyeHI4AwavXu6GBx", "24_JUne_2024_video1285618942.mp4", MP4, 49117815, ""),
            ("11tieGxOayssNCdGQ0H1n2QRGd8iDbbQ2", "Brent_19_JUNE-2024_video1406800527.mp4", MP4, 158905085, ""),
            # subfolder: 2023
            ("16iophfRyJZqsxEY0wUEyuXw0Z_RRVBcc", "Dining Insight - Roadmap & Estimations.xlsx", XLSX, 13101, Y2023),
            ("1Tmjir_bycNS4kcTa3w8OCt0k4Y7S9kGS", "DI-Product Requirements v1.1 09012022.pdf", PDF, 470186, Y2023),
        ],
    },
    244: {
        "source_folders": ["1qDutpuwvPIN_J_9bbAGm9eaSGJA7UvsM"],
        "files": [
            ("1sLGxQ-p5Rz5ov7y3PKPO3lMi2vCNMgYwnryGOgANjd0", "Job Recruitment Platform - Roadmap & Estimate", SHEET, 24008, ""),
            ("1ji7icee17yqwJc2VPAAh-AwkKNQh_gXe", "Job Recruitment Platform - Mindmap.pdf", PDF, 1534889, ""),
            ("11KEVjdlzs6t-xpmGWb8i6aCTqulQA5TUlzY-cisHHd0", "Notes & Requirements", DOC, 5639, ""),
            ("1lpOsQDslDud6_W7zLlSNWHaS3NWFvoer", "Discovery.mp4", MP4, 301420369, ""),
            ("1dr46jdlOQkIfjp8bSbDbUibjhMMqjS66", "Roadmap Call - 6th March.mp4", MP4, 62480175, ""),
        ],
        "errors": [("file:1AJO3Smm9dbrULLI_1iSfkA6Wd8gq7akx", GONE)],
    },
    245: {
        "source_folders": ["1MDMUV4xMFtu461VPogES9Mg0mcWz8UXR",
                           "1lcKdZZr2yEKK_aCm-DxjC1oRxbpqaxrh"],
        "files": [
            ("1ItwNcwAFfN3Um1Fxvj5Iu0uRUtfo2JPF2PuQGimXxKI", "Fiber Intake Assessment Application | Hybrid Mobile App Development - Roadmap & Estimate", SHEET, 29821, "Engineering"),
        ],
        "errors": [("folder:1MDMUV4xMFtu461VPogES9Mg0mcWz8UXR", GONE),
                   ("file:1M19ibMmI-c-7VM5QF2AiqURDMQH8NdIR", GONE)],
    },
    246: {
        "source_folders": ["1pvc2lZRGi_SMht763iygZwhX7VZI99L7"],
        "files": [
            ("19Z_B3a9527qcQlkNI4jPR5cayRQNmClJlrPFjnqTEHk", "Integrating Google Sheets with Presidio - Solution Document", DOC, 21265, ""),
            ("1IS_S6MVwBto0O8fO4-fKKCF9hLxBvb0L_mrdjVoUdY0", "Notes ", DOC, 1024, ""),
            ("1ccDdkdOMnLaYvyVaMYuQT6koZ_FC9b6I", "Copy of Discovery.mp4", MP4, 83276680, ""),
        ],
    },
    247: {
        "source_folders": ["1CW92URCrvPahru73rt_bMmKQlUpHDdL1"],
        "files": [
            ("1iXX0PB54wX-zTPJ96Vr7Ifcck4x0f4gn2j0h5nDSPOA", "Multi-Vendor Marketplace - Solution Document", DOC, 18477, ""),
            ("1hFGpNLJVuVnSYv0g5MxCR9kiRAorQoh-OfCg36dF36s", "Requirements ", DOC, 3320, ""),
            ("1S8ueNFLyT6geY-5v_3TCDHSgOPg8fsqsTUmxdIy2vUY", "Notes", DOC, 3583, ""),
        ],
    },
    248: {
        "source_folders": ["1iiQez-eEfeYBbiGw-G9PWeFJDdnbrOkH"],
        "files": [
            ("1e3IqEP_U9su6pv61JQ4iTQTqNVrafOE7kl6lrEqsB34", "Evolve DTF Software | Web Application Development - Roadmap & Estimations", SHEET, 12923, ""),
            ("1Pu0H3xaiZIfqUr7Ls9sSD9fMW_46SOMjUog-riLFhzQ", "New Requirements - 26th Nov", DOC, 4137, ""),
            ("1HO5To9WZegoQzE2ynOV-EhPjNl72zfNm", "purelogics Roadmap for Evolve_DTF Software.xlsx", XLSX, 551644, ""),
            ("1v_683GwSVUq4cyQkmj_qv3HyUQmL6Vs1", "purelogics Roadmap for Evolve_DTF Software - Roadmap & Estimations.csv", CSV, 14928, ""),
            ("1WV2otXBBcc_sDauAvKF9LO0Ny-9IhUut", "ROADMAP VISUAL@2x.png", PNG, 894694, ""),
            ("1zGyv2KhoNqZX8uzjIM8K_AC4M2fVw6QS", "unnamed (9).png", PNG, 29239, ""),
            ("1uMRoKxT54ggpbdnMFC1mEWTlchI0VjQs", "Discovery call.mp4", MP4, 577253123, ""),
            ("1jwg53PMio06BnJawSRXTlpBnP3LWcDdr", "video1625433487.mp4", MP4, 100726781, ""),
            ("1xJ3fLcQ-jpbeo6k069iUzCRAC4fmofM7", "video2304662205.mp4", MP4, 463500362, ""),
            # subfolder: Novemeber 26, 2024
            ("1_C0TOefhpZ9FSjLuu8OrjG_In0f4au2WWT2OnqezcyA", "1. Evolve Dentistry - Roadmap & Estimate", SHEET, 19945, NOV26),
            ("1T4vnH2-eBQ6Tu4RhSZ6sYqMm9VdbGGNz", "2. Evolve Dentistry Mindmap.pdf", PDF, 916091, NOV26),
            ("1T8lZ_c3jmfBvqV1_L92PLBnsf2efB4rS", "3. Evolve Dentistry Wireframes.pdf", PDF, 4198798, NOV26),
            ("1Cf27hr0fiveg0ZFLAZQ-tLg-oVznmsEH0biGDDeGZzY", "Dentistry App | Design Proposal & Recommendations", DOC, 29205, NOV26),
            ("1cV9puU5U2uoObuTk-i8QWYYDEk2MnVL25amlSTq3iyw", "Copy of Solution Document - Template", DOC, 15555, NOV26),
            ("1n5EUOxDK-nigzQBbWQ_GBqi7NvWZ10dLWBAuJJLsius", "Additional Features", DOC, 3382, NOV26),
            ("1oQcaVmDe-rHRzx0lSlj4-O4XRgYf_0TLGeewgh1E4yk", "Updated Requirements", DOC, 9151, NOV26),
            ("1qvM03FL-PO1s3OI6zDBd0g6B5ZOfes4-", "Evolab Portal - Copy of Sheet2.csv", CSV, 5251, NOV26),
            ("1WvF9Oatwabqxa76ATVYdo7xM_mEyjwmj", "12 Dec call.mp4", MP4, 107476756, NOV26),
            ("1gipP6pMIpNfYhjG2PTgIbJnkNUJGBtWV", "Trimmed - 6th dec.mp4", MP4, 53420298, NOV26),
            ("1s8Ca3vi4xMNj3TySKxcOLg5wur6KFTza", "Roadmap presentation call 1.mp4", MP4, 140675515, NOV26),
        ],
    },
    250: {
        "source_folders": ["15XVlE4nc3M2MDCFoIP6mfD6nRFjGLstA"],
        "files": [
            ("1F0pfoYIGPjWCxTMHOz0PJ4fXD0BpNaJHxZN3tPGP8eQ", "AI Wellness Application | Web Application Development - Roadmap & Estimate", SHEET, 19829, ""),
            ("1529VaAT4yeqfQSRDfjsRjlhbYv_FnT50_wOv43jOp9c", "AI Use Cases", DOC, 14226, ""),
            ("18v8jMXOGeXnCt0TFqrNs2T75v88OL9QqMcRhGUO2wXs", "Requirement: ", DOC, 2163, ""),
            ("1Sg6HE2LqWnVDvMujLaayQkSQsBn95n0m", "Trimmed - AI Wellness Platform.mp4", MP4, 256862314, ""),
        ],
        "errors": [("file:1k9Cb6Z3sBdFEpmKm9fnVVUQyckEnPvfz", GONE)],
    },
    251: {
        "source_folders": ["1u0NMfDEqXDIPItpa6CuP18T3ewJ4be1y"],
        "files": [
            ("1jHspxMVpnelHEyi-ZY5PLT24JfrnzGxaZDCtr4dyBvA", "LMS for Health Education - Roadmap & Estimate", SHEET, 17924, ""),
            ("1LNTrxL884go-c1p3Btm7owoSdkIu68yzz6B7gTm-t0E", "Requirements", DOC, 2213, ""),
            ("1wu_W9k0NiPyHefbyMftEH-umlGF_x5P6", "video1897723238.mp4", MP4, 101812666, ""),
            ("1KrRYpIf-sVFYRizXS3bRHmvhk75FIxjB", "Trimmed Requirement - LMS.mp4", MP4, 473765837, ""),
        ],
        "errors": [("file:1KQrcjcSZPdkkzvp4PKj5uyxixmH_Cw15", GONE)],
    },
}

DEAD_FOLDERS = {245: [("1MDMUV4xMFtu461VPogES9Mg0mcWz8UXR", GONE)]}

EMPTY_FOLDERS = {
    233: [("1bAdYVquwPhWtcDRql8ZvSklrn0SiRu1E", "Engineering")],
    234: [("1Yv0TRvFuv4drvUJNp5OT78ERArHq9Tm2", "Engneering")],
}

SUBFOLDERS_TO_WALK = {}
