"""
Real Drive inventory for the fifth List 05 batch (cards 41, 82, 202, 205, 206).

Entries are (file_id, name, mimeType, size_bytes, containing_folder_name).

Scope notes:

* Card 41 is a live 18-month engineering project. `Deliverables` holds 24
  `Sprint-NN` folders and `Engineering` a nested integration plan - all level 2,
  outside the spec's one-level recursion, so not walked. `Call Recordings` is a
  recording archive (all skippable by the spec's rules) and `GoogleTakeout` is
  somebody's personal Google Takeout export with no files of its own; both were
  deliberately left alone. See NOT_WALKED.
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
SLIDES = "application/vnd.google-apps.presentation"
PDF = "application/pdf"
MP4 = "video/mp4"
MOV = "video/quicktime"
MKV = "video/matroska"
DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
PPTX = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
ZIP = "application/zip"
ZIPC = "application/x-zip-compressed"
TXT = "text/plain"
MD = "text/markdown"
CSV = "text/csv"
PNG = "image/png"
JPG = "image/jpeg"
VTT = "text/vtt"
M4A = "audio/x-m4a"

GONE = "Requested entity was not found (deleted or access revoked)"

INVENTORY = {
    41: {
        "source_folders": ["1SHRzslEwud9zYHY7rvakKOEE1xFsH3Q5"],
        "files": [
            ("1KdzzDcqRIwoBpjAg0mcf1ZKw7YUtPweF", "Updated MacOS Plugins.xlsx", XLSX, 98339, ""),
            ("1C4BCW7tDwEDs9DqE3l09Pt5gOnn0sHLEO_9oXCsK4fo", "LAB Sprints High Level Plan", SHEET, 2276, ""),
            ("1PEUoWTlzh7ppuFDiTaX2pWO-9Rl65dcf", "Sprint_1 Work Breakdown.xlsx", XLSX, 128334, ""),
            ("1AV9PWhfSSrCpvYW873cYnEqrTQorxdlp", "Roadmap Coverage & Gaps Summary.xlsx", XLSX, 7082, ""),
            ("1ctb5haezValzVkX_67IaoXO_xi8m66xw", "RECON ITR Plugins Requirements.pdf", PDF, 180478, ""),
            # subfolder: Dev Team
            ("1eBoeo6FO7Ii49qKYinD8fF5IG0z00YbH3i_ivgv3wWQ", "Risk Register", SHEET, 2209, "Dev Team"),
            # subfolder: Requirements
            ("1wf7LOKvHQ6UOP-kCiDpfr8teqjVLCx01", "MacOS Plugins.xlsx", XLSX, 19029, "Requirements"),
            ("1sgXqvsQcowmDs6G0Pz6A37jdDMRxjJps9fHSLv0zbls", "RECON System - Roadmap & Estimate", SHEET, 134679, "Requirements"),
            ("1sLthBiruL0DfrQ06Uf1y2Vma2lgHMWMH", "Project VIC 2.0 Integration (Round-Trip) [SUPERSEDED].docx", DOCX, 996964, "Requirements"),
            ("1AIUxLaMqgXOC6AAPNLDyynm_5-inxsiF", "MEETING PACK - LAB Lockdown (for tomorrow with Pure Logics).md", MD, 54609, "Requirements"),
            ("1jrdbTwa_VYKJFOIhfhYduSh_y_y9xh4a", "RECON LAB v2.0 - Lockdown Plan (Pure Logics).md", MD, 44409, "Requirements"),
            ("1QUtiesD6CiWgBxEwQUF-5MNi2DMqg6oK", "Engineering Brief_ RECON LAB Offline Vision Strategy.docx", DOCX, 1019345, "Requirements"),
            ("1Kns1HbMzyySHRQJigV1AY2jFeVlJU3li", "RECON ITR — Recovery Mode File Preview.pdf", PDF, 138045, "Requirements"),
            ("1bLAvOVfv-a7d1v-ycTzqeHKz3d8pw3LB", "Updated MacOS Plugins.xlsx", XLSX, 33608, "Requirements"),
            ("1LwCRjNzXdIblspLQk6JbzQwIrGZkwN_O", "iLEAPP/aLEAPP integration plan suggestion.pdf", PDF, 229822, "Requirements"),
            ("1d0Ug2M400_iMqyjLPUndXQPm_UCkR9CD", "RECON ITR Updater Design Requirements (1).pdf", PDF, 531617, "Requirements"),
            ("1Q_Z7T0heMJIS_DJkRYNmrknksWwNwcbP", "ITR Migration from C++ to Swift - Henry - Architecture Diagram.pdf", PDF, 3067947, "Requirements"),
            ("1l20L5kGeI6tEEv4NLJcGsZrWIhmvBkEpy9b-2rVLe_E", "Sumuri - Kick Off Document ", SLIDES, 4166790, "Requirements"),
            ("10M5_m80KIgXBDbX-9lpGElYAPavFsORZ", "Licensor - Software Requirements Document.pdf", PDF, 208672, "Requirements"),
            ("1xIYz6QwFyoJO9-WPDxDa-9Dw59eDX4RQ", "Figma RECON Redesign.zip", ZIP, 30945, "Requirements"),
            ("1ShYPZlUrvTp9FwnVoptyUfmowzmu_irK", "Muhammad Ahmed_F45224-1823.zip", ZIP, 651, "Requirements"),
            ("1RO7_xtc0KXiOLE-PRGfGMQQzkeBpjPXB", "recon_itr_manual.pdf", PDF, 23403942, "Requirements"),
            ("1sllyzOFxIsn-QLRFXVcBobsAd6TJi24J", "RECON ITR Plugins Requirements Updated.pdf", PDF, 223393, "Requirements"),
            ("18Jjo91BOzr07OjuVL72Tb2tdAKY0hoHu", "RECON ITR Updater Design Requirements (1).pdf", PDF, 531617, "Requirements"),
            # subfolder: Internal
            ("1mOoch9dCC2KtiUU86eqWwSWJfUqVWui5BsCzMkf6P38", "RECON Estimates Variance", SHEET, 15754, "Internal"),
            ("1tcqaHPZ8Bbs98Qdv2Wd7yeONC9Sl34BXDa4EAlXFAss", "Plugins Parity Verification", SHEET, 4083, "Internal"),
            # subfolder: PMO
            ("1YENVV9eTRSw9MczzA9RKRd9LPW3P9MHs", "Project Workbook.xlsx", XLSX, 530532, "PMO"),
            ("1-C_6ganBuGnNOAdC59zJKraerNOwOAfI", "Project Charter (2025) - RECON System macOS Project.docx", DOCX, 72420, "PMO"),
            # subfolder: BA
            ("1J3FNz-yUf-FvCOQJoWy2hniaruLWIT7W3hIAl6gxulY", "RECON ITR Platform – Future Roadmap and Strategic Maintenance Plan - Solution Document", DOC, 1478195, "BA"),
            ("1hrZ1-swe9XxT3HnUikw8MRK1Ltwclhzc", "Support Plan - Steve Whalen.docx", DOCX, 10961, "BA"),
            ("1kP4XzZzvXG9HXFAtkCKnmkMsAPdOY8WYAusrddKIqJo", "Copy of RECON System - Roadmap & Estimate", SHEET, 78943, "BA"),
            ("186MtkCjtM8Zqhm_3WnjJtJ_TEJXLUWCuMqbsWqt4yVQ", "[new] - Technical Business Requirements", SHEET, 74186, "BA"),
            ("1vD2448HiPRxBoDxI9ucorWdbYzRNxWirJRbX6dCJ05w", "Recon ITR MacOS Application - Roadmap & Estimate", SHEET, 19692, "BA"),
            ("1DMtDd6EDLNmTzVnFCPdjHob4xwm6Ar4SoqdsWO2cvz0", "Recon ITR MacOS Application - Solution Document", DOC, 1476346, "BA"),
            ("1lvACQhUG3z2fQptNFlgqjieCxwlmki7h", "RECON ITR Requirements Review - 2025_01_31 10_12 CST - Transcript (1).pdf", PDF, 147384, "BA"),
            # subfolder: Deliverables (24 Sprint-NN folders below it are level 2)
            ("1-DIQpcbeg2IK69nXlnlv8fPO0pOIOGWZ", "ReconLab-v1.0(31).zip", ZIP, 579850509, "Deliverables"),
            # subfolder: Engineering
            ("1_Oiq2YHxWjc0YPbamczaz9dCevmwbmec", "Plugin_Language_Evaluation_v1.xlsx", XLSX, 59113, "Engineering"),
            ("175i40yhlnhuqLlJ63ZFYRI07casO6NjZ", "Plugin Architecture for Recon-ITR and Recon-LABS_v1.docx", DOCX, 605914, "Engineering"),
            # subfolder: QA Documents
            ("1zIMgVBjB1e5GK1iy9CF1ek1ntHzbxOrVjN7VGIYGc0k", "RECON System macOS App- Test Management Sheet", SHEET, 254852, "QA Documents"),
            ("1dyElaYWM0NZ5cp7PD6VNmRnDZvfI4run2z9GcedCsdk", "Test Plan- Recon System ", DOC, 17127, "QA Documents"),
            ("1feYni1EVjMEaDMhLY91nu9lpbnmlB56_qAcp3POziT8", "Parity ITR vs Swift ITR", SHEET, 6796, "QA Documents"),
            ("1pXFQ7z9bNYzVvGojemfyIVPSanjjfv-kdr3acECzWz8", "Signatures", SHEET, 3819, "QA Documents"),
            ("1IX7JjFvHzog775B8__lutSRgG4ocmpdI1RP0U8omKD0", "Plugins comparison document New vs Existing", DOC, 6809754, "QA Documents"),
            # subfolder: Supporting Documents
            ("1z9YhdoyNvxyPEBYp6lXGbhqtii5c01yW", "iLEAPP_Plugin_Filtering_Tech_Notes.docx", DOCX, 233738, "Supporting Documents"),
            ("1na537xXfVpSZP3-xULaQ5mvDojtRueid", "RECON SYSTEM Migration from C++ to Swift - Architecture Diagram V2.pdf", PDF, 1564581, "Supporting Documents"),
            ("1XR_qqvJEBwkdOTYFh1u3Mvaggsp4xUzl", "RPK-Image Classification & Objectionable Content Detection in RECON LAB (Without Third-Party APIs)-250625-161423.pdf", PDF, 438687, "Supporting Documents"),
            ("1HAp8HXIpAIncbD3W5XPqJVdGCgx5p0hN", "Embedding Python App in a Swift Project.docx", DOCX, 363953, "Supporting Documents"),
            ("1m17CPnpxy1Pj4a2la554oLsp8m7YWCGd", "NotebookLM Mind Map (1).png", PNG, 5454523, "Supporting Documents"),
            ("10KbpBahwrxDL1Bub_tq9OD5gfNmiwEwm", "Architecture for Recon-ITR and Recon-LABS_v1.docx", DOCX, 642789, "Supporting Documents"),
        ],
    },
    82: {
        "source_folders": ["1Vut4AX2L5vL_wOxVIesbG6-6bUMlg9Ad"],
        "files": [
            ("10WiKz-EB4yO1EgZhJoh2sZ9ck1vUQodX", "Copy of RECON System macOS Apo Work Items Status.xlsx", XLSX, 16496, ""),
            # subfolder: CaP - Phase 2
            ("1EvfmhoVP2L4dX7bp0XREOaROLBRCSSGg_A-GKRfpetI", "CaP - Product - Roadmap & Estimate", SHEET, 37055, "CaP - Phase 2"),
            # subfolder: Documents
            ("1XYN4xUxhHVIGwSpkfQQRFJcE-XyqpwP0qc3RNefxDzU", "CaP SES Integration", DOC, 1613850, "Documents"),
            ("1_Tzz8s2bURsAEHQtkXQYoxDMId0FwNgQQ5HWcBE5yzI", "CaP Build Documentation", DOC, 1483891, "Documents"),
            ("16eIc-VFLOiQtDOZ6CiF72V5edvjO5aZr", "OLD - User Manual \u2013 Catch-A-Predator (CAP) Application.docx", DOCX, 2056113, "Documents"),
            ("16GZXZlijdZ3lrRokEbDj35uVfaPt3Igm", "OLD - CAP hash salting and security algorithm.docx", DOCX, 26471, "Documents"),
            ("1tKJSbeS-BfItP8pQ447sM1kZW6owyog2", "OLD - SES (Simple Email Service) \u2013 History & Logs for CAP.docx", DOCX, 228606, "Documents"),
            ("16iGRzsEbKigOGSiOtPr2qlw2WeZ1NUfJH6W2cPcatCE", "CaP User Manual", DOC, 3701555, "Documents"),
            ("1oGjuQrLJm1OUCbpTCR-mV45markg3tHs", "SES (Simple Email Service) \u2013 History & Logs for CAP.pdf", PDF, 171678, "Documents"),
            # subfolder: QA
            ("1swB1_ZiMTBWdxswr_pHtpGhUYuNQlHKhDGWxZ32mNxM", "Copy of Catch a Predator - Test Management Document", SHEET, 62848, "QA"),
            ("1gAaVU-ZGcw1qGORYfTWws6gUN81n61gMRffDKZeGO_k", "Catch a Predator - Test Management Document", SHEET, 62891, "QA"),
            ("15KcmCxGC52NzAqotaLKHgEKA2qpsmELn7nUzVCOVlkU", "Copy of Catch a Predator - Test Management Document", SHEET, 58027, "QA"),
            ("1syHh77C60IOygtHZupQM-djj_OTTovojSlFOElPRK3Q", "Catch a Predator - Test plan", DOC, 12672, "QA"),
            # subfolder: PMO
            ("1R1MUTS_6F9vzyZYzSZ_keLwXkHs46P0h-Lugdjuqtyw", "Workbook - Catch a Predator", SHEET, 151703, "PMO"),
            ("1A8O_LL2EKm5wLcYs4SsWIyCcFj6d9thJizp2WSy3hM0", "Project Closure Report - Catch a Predator", DOC, 22835, "PMO"),
            ("1YjTTwU8a6DDuPQ0d41L8uuuo-b3myn92A3c7QWIRVxc", "Sprint Breakdown and Completion Status", SHEET, 5868, "PMO"),
            ("1VvL1c0mGQ2rHmz8m-AXkD-A2d6mYKUCdEsAggsGByQc", "Project Charter - Catch a Predator", DOC, 35753, "PMO"),
            ("1N9C5dSarjK63cm9XCa0e8PpbzyagQPQRekM7TNYPb6c", "Catch a Predator | Windows App Enhancement - Roadmap & Estimate", SHEET, 16281, "PMO"),
            # subfolder: Requirements
            ("1bULp_FDsbHrbqRhCldqDeKkVIMoC4A45EFop2eJirDY", "BMF-Connect-BRD", DOC, 1607160, "Requirements"),
            ("1iSUZwEsMTc1GoeCPEwFE2M1RWWonxfn53S1woalvObY", "Pre Kick Off Video", DOC, 1024, "Requirements"),
            ("1wzfrPNmKFkbsT6F85clieIX5oeViTrM9sypmLLz4-JI", "Catch a Predator - Project Understanding Document", DOC, 1608643, "Requirements"),
            ("1o_qun_dcgVjEmZiaifrydOF8g3PfbTXFzd26dst24Fg", "Read Me", DOC, 1024, "Requirements"),
            ("11lrO5-EsaGy8ZacgGyEpdKKkc1kTIwc_", "System Workflow Diagram.pdf", PDF, 32390, "Requirements"),
            ("1JWIfOJirDtaSNXgCDWq5QUodlfBbDcv6vXJo_j_aCGQ", "Catch a Pred - Steve - Engineering", "application/vnd.google-apps.vid", 902544113, "Requirements"),
            ("16cpfscWtoRA1JfF-eCnIhqFl31BAVlRp", "Business Requirements Document (BRD).pdf", PDF, 138940, "Requirements"),
            ("1twc0mv7oiwToPIG2kA0wqjn3_OrXWzAS", "Catch a Pred - Steve - Engineering.mp4", MP4, 902543553, "Requirements"),
            # subfolder: Supporting Documents
            ("1evapBOVW89ZUc9BVA2_Y89-qI6tNxC6F", "Result Page.png", PNG, 116092, "Supporting Documents"),
            ("1GKoG6IjjPkDh0VekcyNMFyNwH7ZDBRpB", "Error.png", PNG, 327370, "Supporting Documents"),
            # subfolder: Email Backup
            ("1iU01ThLgT6ZEDLS1xRZPxPLBZzjsLdUV", "CaP-Emails.zip", ZIP, 296005, "Email Backup"),
            # subfolder: Prospect's Codebase
            ("1mMQEyVOMfByZwdYxPjaOgjt-vpMPxycM", "SUMURI-ITSM Source Code and Executables-20250911T093020Z-1-001.zip", ZIPC, 408804247, "Prospect's Codebase"),
            ("1KczHTXkvWZF7k2crRFPkdQTdFygowzLx", "CAP Final Download.zip", ZIPC, 778030203, "Prospect's Codebase"),
            ("1dMhuVn_bCeQv1un3-H414-uREd1lDNhp", "CAP BOC Build-20250911T093029Z-1-001.zip", ZIPC, 639890497, "Prospect's Codebase"),
        ],
    },
    202: {
        "source_folders": ["1CxvqCkQvfjqYGnVQNTIMNGfMue58ayLJ"],
        "files": [
            ("1wkfAK0t45TcsxhC4gUeNLOjqHCK3klfH", "Risk calc job descriptions Ver 2.xlsx", XLSX, 80963, ""),
            ("1LntEjAAO8sNrPUOUf6RSYP8_S1TLMBHG", "Minerva - Tech Recording.mov", MOV, 355659286, ""),
            ("1X9ZXSI4j9JP6TUg1yFolM-ueh0-li893", "Minerva Medical Group - Recording 2.mp4", MP4, 916599308, ""),
            ("1-pu9_KAtJpPUu98MOfp1_pImUXACpDGy", "Minerva - Recording 3.mp4", MP4, 63964627, ""),
            ("1hHtExrO698pGOXWYIAghawUaHrYqloxp", "Minerva - Prekickoff (27th Nov, 2025).mp4", MP4, 111252954, ""),
            ("18z4RpclhfxAwSNUDCSDmHJVOUkqxsTQ8njuPV7UAQDk", "Industrial Health and Risk Management System (IHRMS) - Roadmap & Estimate", SHEET, 29278, ""),
            ("14-EumfYBnekWGUvksN9w-vhVSSIDrZYi", "Risk_Weights_Template .xlsx", XLSX, 137023, ""),
            # subfolder: Phase 1.3
            ("1HwtDKUFPGDKUCcNT86zCk6Hu1Ie4B50M99nGoPNEVGQ", "IHRMS Phase 1", DOC, 9528, "Phase 1.3"),
            # subfolder: Quality Assurance
            ("1JJzirZJvgcer0jT5DdSBr00XUykl2IuO", "Minerva Medical Group IHRMS.xlsx", XLSX, 313042, "Quality Assurance"),
            # subfolder: TPM folder
            ("1BrgBI038FmPOenZInj-5RKV5yDJjVs63xOxvH45H_lw", "Database Schema & Entity Relationship Specification (IHRMS)", DOC, 13198, "TPM folder"),
            ("1dfY1RYPelno5Bx4FDJlpM9-YXKLmNdVw8TZOUTHNoO0", "Risk Scoring engine", DOC, 15944, "TPM folder"),
        ],
    },
    205: {
        "source_folders": ["1-EjvI0QHlBzyImiOX_fDBjI7TErzFfjT"],
        "files": [
            ("1ndxyWFVdYZ6ZZWEDto_wyFjqgXDRD13v", "We Advisors - Relaw.ai Questionnaire Management Workflow.pdf", PDF, 80536, ""),
            ("1sdji8SZQcviRHDfhyn9gNl3mq6ugTmSYEfxkUkQCkxY", "Email - June 10, 2025", DOC, 7512, ""),
            ("1T3d09GHp400_prRTz015PFjGBFLDEBrKALuVySfYt5c", "Optimized Infrastructure & Services Plan - We Advisors App", DOC, 14029, ""),
            ("1UUXYXz5IjAzFTlZglBSWITBBz9s62fx9", "AWS Infrastructure, Monitoring & Security \u2013 Current Status and Improvement Plan.pdf", PDF, 127845, ""),
            ("1aEk8IfbWxoL0OwKaIckl9IRU_pmqU1LEq-hmWaynygg", "SEC Compliance Checklist", DOC, 33183, ""),
            ("1Diu7dtSgKDRWCPAU1VWYxrz-IN9IJuRnAW3AMEJLqxw", "Security Features", SHEET, 2090, ""),
            ("1kPHctAb7IL9KJPVSdQc3P_sMhsfdXgl2TGCOI4IjLHQ", "Project Handover sheet", SHEET, 5841, ""),
            ("1QbG_9ocgvDD4GpZb6pCbXWa2CTY6kzky", "Database Schema as of 19 August 2026", PNG, 3095662, ""),
            ("1PyausQ78cq8Z4umYxQOFQZXqe5l9ZugYDCyv45HNJeI", "RetirementAlchemist_User_Manual_Professional", DOC, 11548464, ""),
            ("1KAi-GB3V0u0VrqYpdJzrn92MAkcwaY__", "RetirementAlchemist_User_Manual_Professional pdf.pdf", PDF, 13118128, ""),
            ("1ObRlxJPnVjOj3jOcDT4BOEW30vS-magjOl5JwKtCfUk", "Work Done Report", SHEET, 10016, ""),
            ("1CfW_kWQi6-txwB600D7mFIA-_F_RxXOPkMH7xi6X7Ow", "We Advisors - Roadmap & Estimate", SHEET, 76487, ""),
            ("19hs4TytuqQa8Euf7H-ZMloTxUlSZeI6H_lhhHwmloM0", "Project transition Moeez -> Junaid Tariq", SHEET, 3397, ""),
            ("1j8dd_UX-wBMfhBcxLD2JJjs5dK3Ijd5UbD_itKnUC7k", "We Advisors - Weekly Progress Report", SHEET, 30158, ""),
            ("19Y2gyxqRXakHmOMwZLoomephy6dLw8BLJfKZV2QjUFo", "Meeting Schedules with Terry for November", SHEET, 1024, ""),
            ("121pfAI_Vw3qiTP7-0jJmMrZePodjCLS07LQKRHcwr1I", "To Do's for Terry", SHEET, 2094, ""),
            ("1MfCjH2jS6F_p0WMWka8fazvFQG-XP5hF", "Recording 2.mp4", MP4, 1033082318, ""),
            ("1qBbvuEPPyyIiMO7NvvHlZ6sWdMaZheuL", "Recording 7.mp4", MP4, 148972669, ""),
            ("1JgXO6BqU6JEL6xEnDkkdh5Cwbqa05STK", "We Advisor - Recording 8.mov", MOV, 187736626, ""),
            ("1e4yC9owKpd3bBhE66rdTvIgzRXtvfksa", "Terry - Engineering Rcording.mp4", MP4, 411307567, ""),
            ("13lwxPNCF-B_oQZ3EhveictmH5QIE81CW9IhRpSJNTkQ", "Calculator Fields Summaries", SHEET, 214554, ""),
            ("1ghcjGozPt8ebZ4R_Qg0Bd26STIoMj66_NS0gIXDPszE", "Figma Designs", DOC, 1024, ""),
            # subfolder: PDF Templates
            ("1bxKrt0wcmvAfrCV1ZDRnm0GN6tMHGXuM", "Tax_Map_v1_Modern.pdf", PDF, 32895, "PDF Templates"),
            ("1SI6G5_7lLQxYZTTitRvJmvjn7L8dx0Ns", "Tax_Map_v2_Premium.pdf", PDF, 53978, "PDF Templates"),
            # subfolder: Wishlist Implementation
            ("1ZGQol1zMI16UXbX2tT-J4SWw72uksGmvW399kFbIJcg", "We Advisors Wishlists - Roadmap & Estimate", SHEET, 35152, "Wishlist Implementation"),
            # subfolder: Brad Feedback (feedback screenshots)
            ("1XLVcaRPhUtdpbIrlyOQC8eWCwWRQjWQC", "F.png", PNG, 124777, "Brad Feedback"),
            ("1ulPHGXimfRgodldDEF_L3MXsRC1G3_Ev", "G.png", PNG, 21543, "Brad Feedback"),
            ("1Xv9U4NWinuJALMA0bJR29p0w3GOH7oKC", "C.png", PNG, 63058, "Brad Feedback"),
            ("1O6n6uQ_VtXDP2A2L6Bn-9D6Ks7VZR9yr", "A.png", PNG, 18741, "Brad Feedback"),
            ("1eAbipEZYlN10SGXXT9InV5dPW76zTkNe", "B.png", PNG, 49820, "Brad Feedback"),
            ("185K9iICveQRK9DZ_RdjAqYGC-PyKr4eG", "D.png", PNG, 45589, "Brad Feedback"),
            ("1y7DBcojfcJPJVawDYqyA-O9Fp9wbf2KI", "H.png", PNG, 217272, "Brad Feedback"),
            ("1lD1DZUHN-HQj4HECciQsvc3qa5fBB_Yh", "E.png", PNG, 174272, "Brad Feedback"),
            # subfolder: Tax overlay (Internal Research)
            ("1r_0PuRA_3T4SBDPh9qZ6tfdkJiahtIvi", "TaxOverLay.mp4", MP4, 16268341, "Tax overlay (Internal Research)"),
            ("1FAOEJD3lHiAR8DxuXAujgCo6MUHipOQL", "TaxOverLay R&D.pptx", PPTX, 24855332, "Tax overlay (Internal Research)"),
            ("1jMpaLzO4NWIY6zkvnghpGC8wVMLZh0bL", "Mindmap of Tax OverLay Version 1.png", PNG, 1139167, "Tax overlay (Internal Research)"),
            # subfolder: Calculator
            ("14vuYcA6u-5wtK30lDxqAnDRwSQHVx_s_fAZwMiBIKnY", "Roadmap & Estimate", SHEET, 25212, "Calculator"),
            ("1UrC0sG79criNQrk6sXzBM-xWJCiWx-22XGyaOgjdECY", "We Advisors Calculator Project Workbook", SHEET, 122039, "Calculator"),
            ("1Zcn0Jtliv1V_8BXkHhHSlBG4QezfY6JLLRcNaUCmXZQ", "Story Cards & Sprint Plan", SHEET, 19496, "Calculator"),
            ("1ginaOkJDO1iCgRhRwdMqsdNEkWKxU2D8BLs-wM6IJBU", "Estimated Fixed Income & Comparisons", SHEET, 17186, "Calculator"),
            ("1C1JcUegxXxeKPhwEg2H1BGmqtk19IAM65yY5enrc5xo", "Estimated Fixed Income Requirement Specification Document", DOC, 8169, "Calculator"),
            ("1Wb_D2F2Oh0x2B4EC2rlhhb9FcXe5Wq7WMRvkLky1Uyc", "Untitled spreadsheet", SHEET, 1024, "Calculator"),
            ("1ZXfPfJsSdDmtXsMnyV4Nlxy40jR47XrCDi7aF9WHutc", "Monthly working", SHEET, 1024, "Calculator"),
            ("1656IvdRg8DbmI_RKHtl-zLvE1S41BGeh", "Weekly Task Report.xlsx", XLSX, 33943, "Calculator"),
            ("1KDEpqpHkaDrjfn-vDEMfmDZD_tyfrEY6VHG0f19U6tA", "Project Handover Document", DOC, 14432, "Calculator"),
            ("1eOdPzoDVRSMGpgFoG4B1ycIYrgvNqV0K", "P4PShop MVP Closure Report.docx", DOCX, 357744, "Calculator"),
            ("1H5PbzrVzBrQUPcHPaofyakRuyLkRVTrA0bnplSRjxsQ", "Solution Document", DOC, 30787, "Calculator"),
            # subfolder: Requirements
            ("11gAYASp9ywRfWACXgTkm8scepbDaPI5ylUHzFud3iCo", "Brad Recent Email", DOC, 10267, "Requirements"),
            ("1_1F-tYKOn0txEqLWlkm6YRmTNHMro9P1", "Tax Overlay Guide.docx", DOCX, 143479, "Requirements"),
            ("1K-DHklYvhFd7DC7zKJJaePtAPm091lXT", "TaxOverlay.WealthMap.MappingandAllocationMarch2026.xlsx", XLSX, 14517, "Requirements"),
            ("1wFy1D-VP3lQuG-gE2BNNDBhYJ5SiiARCu8c4wRCJXww", "Untitled document", DOC, 2219, "Requirements"),
            ("1-ryhoMHy8e6VSnSAxdgTwmCdNclGVDZyXITCqussDfU", "User With Mulitple Roles and Companies", DOC, 5034, "Requirements"),
            ("1dOQj6SR-uowfEDF0gbLYZ-vcnz9ZByQEUVwHGawXbGQ", "Wealth Map Phase 1", DOC, 7167, "Requirements"),
            ("1ovTRdcsrVEzBL4Uluwy4QuqGzggIbao_-wkyU3R16Pw", "Wealth Map Phase 2", DOC, 3431, "Requirements"),
            ("1lVJTVT6UY8Ezgd-85Nl7ct4sGaIydbXBr0JedkfJJ6g", "Wealth Map Model Allocation Permisisons Flow", DOC, 2308, "Requirements"),
            ("1ERV9uF1iTVSJ7vAbdR2hnPKMdEMqNBfvndM2IAsfd_w", "Email Template", DOC, 1024, "Requirements"),
            ("17ZO3xs2xeuFbD88YbLWzGIUtSnBu-UQ0LK8F9cxquyM", "Wealth Map", SHEET, 8061, "Requirements"),
            ("1TBJiIb-ykcDGHhEpyF4ASb7_eWUYD0yQeriX66lP1zA", "Questionnaire Edit and Clone", DOC, 3266, "Requirements"),
            ("1EQK_33jUUOatbnJtDWF8bhOID_9YGDZa6Q-lyoz7yAY", "Input Mapping with Questionnaire", SHEET, 2348, "Requirements"),
            ("1_waABvRqjHfc4LNcNTSM2CLOQBzf8VIu", "Sample Client Before.After June 2025.xlsx", XLSX, 231526, "Requirements"),
            ("10kX3nq1JhGiyRjGrcWKGSpkkR3qw1RRD", "Sample Clients Income Calculator Last Updated 06-05-2025 (1).xlsx", XLSX, 315506, "Requirements"),
            ("16zGBtpNNDBYBnOME44Gzz9j5RBrcd12mYx_PqTUgmtk", "Public Questionnaire", DOC, 2088, "Requirements"),
            ("1TI-lZGu7WLijK9bPUeo6TQ2OPf3V5O3yaf-_8eGMQZk", "Dashboard ", DOC, 13415, "Requirements"),
            ("1uWMRUqzccegMuOeIusb641-lV8VnpslesRY0VMvYcZg", "Advisor Assistant", DOC, 2273, "Requirements"),
            # subfolder: Email templates
            ("1FDeDOqbu0JFKucq4I_f0BLU96I-kg2CH", "Advisor Options for Email Copy (2).docx", DOCX, 15923, "Email templates"),
            ("196zyWV-BlsQvc83jb9MRoofl00oaa1ps", "Client Options for Email Copy (3).docx", DOCX, 15951, "Email templates"),
            ("1WcCpJFT_O_rcqxWKlU_Sby1ouCr5Rusq", "Company Admin Options for Email Copy (1).docx", DOCX, 15937, "Email templates"),
            # subfolder: QA Docs
            ("11UhKhQLHj_XARytio5GyWW71f7KaopUU", "TMS We Advisors.xlsx", XLSX, 430424, "QA Docs"),
            ("1jRcPWW0Jj60-mn0SLM_J4hGo5k6s8Rwj", "Test Management Sheet - WeAdvisors .xlsx", XLSX, 430424, "QA Docs"),
            ("1LnA28K0K_BunFaW2QHcMjNQP5DG6rfXZ", "Retirement Alchemist Testcases.xlsx", XLSX, 127421, "QA Docs"),
            # subfolder: PMO
            ("1WYaBkNwHoOTXpr22pelqHUqO0t39wmFa9-0B7jkJdU4", "We Advisors Workbook", SHEET, 152205, "PMO"),
            ("1u390TepWK6-jXBFcl4vxzV0zyfwinSem39pZBKP1I6k", "We Advisors | Story Cards & Sprint Plan", SHEET, 44893, "PMO"),
            ("1k-syI_egwikTGaim_qFqXmcor-sulfUWs-Xfj3ZwPr0", "PL-PMO-T-007-Project Charter", DOC, 39564, "PMO"),
        ],
    },
    206: {
        "source_folders": ["1ATu9B-oegm2pH-xAT5UdXqQ7oZqvP-um"],
        "files": [
            ("1lXQWnhRUKyb3Xj7tfcwA8DxMD3gVYIDa", "24/7 Call-a-Doc - System Walkthrough.mp4", MP4, 6221000, ""),
            ("1sm-oKHKF_NM_Przs3b6GERoRbOVxwC3xeo3tUUgsPms", "24/7 Work Progress", SHEET, 1024, ""),
            ("1VN9tXxOrFUz76glw43bklhb9O0F_GFlX", "247CAD-SystemOverview.docx", DOCX, 11575, ""),
            ("1h_jPll-M-1yzIoFgiGykhE4AStPR1wcB", "247CAD- Roadmap & Estimate.xlsx", XLSX, 51225, ""),
            ("1AY7AXN-_IOdkNowZC0vHBIbM4PBV3Yqf81CpXSkXzQU", "24/7 Call-a-Doc Project Roadmap", DOC, 7272, ""),
            ("1LgCb5anU2_mSeNmeUNMWYYLbKwqsnNjZmnn8RRBqGPE", "Copy of Dev Estimation", DOC, 19308, ""),
            ("1FoL71tK8MO6Svqj3LKji4ApdVCyScQa3bVWx6Ml-tk8", "247CAD - WorkFlow & Kickoff Document", SLIDES, 434412, ""),
            ("1aRvIjmS1RcARin4LzW1FIDjpUSXHhUJUuIfISajq3_c", "Dev Estimation", DOC, 18464, ""),
            # subfolder: 24/7 Call-A-Doc (Updated)
            ("1b0tED6-FImu51Thx1HP3XRy0d1WTfcYQtBsppoRo088", "24/7 Call-A-Doc - Roadmap & Estimate", SHEET, 20399, "24/7 Call-A-Doc (Updated)"),
            ("19QpHkIMfAm1YbyD4uFty_n9a0fs_FImg", "24_7 Call-A-Doc.pdf", PDF, 67324, "24/7 Call-A-Doc (Updated)"),
            # subfolder: Original Repositories
            ("1tAKRS4D31q6Ge_MjEl6T9gFG1TnHFTgX", "Orignal 247 COD Repository ASPX.rar", "application/x-rar", 1963334636, "Original Repositories"),
            ("1qZcjDuM1GrQ_Ut98v7s5tx8DBllh4A5S", "WebSites.rar", "application/x-rar", 269058400, "Original Repositories"),
            # subfolder: Internal Meeting
            ("1uZKTYopEk6f5piMSt3L9AK-ZxAwi-Sbe", "video1332897272.mp4", MP4, 23495025, "Internal Meeting"),
            # subfolder: 247CAD-Documentation
            ("1pxxZ8tiS5--rziNbFhGHOvHIfM4p0tKK", "Member Enrollment Overview.docx", DOCX, 10055, "247CAD-Documentation"),
            ("1ZSPN0JAP9hyKuPBE9-9IHDc6ZwjIPg2-", "247CAD-DevelopmentOverview.docx", DOCX, 11863, "247CAD-Documentation"),
            ("1Zvnk_tC5NIMSl4wBnPRw28UBje52MiC9", ".DS_Store", "application/octet-stream", 6148, "247CAD-Documentation"),
            ("1lZiyzKtGOFACyFl2IUoVLigIvGo3kPxO", "247CAD-SystemOverview.docx", DOCX, 18618, "247CAD-Documentation"),
            ("1oeh6qCTZ-TY1OzL6DUimYmQyN4cbMidx", "SQL Server Agents.xlsx", XLSX, 11356, "247CAD-Documentation"),
            ("15MH2UDa4Cg477O1un-DbP0OdPfVDPl1v", "Description of Disaster Recovery Plan.docx", DOCX, 39140, "247CAD-Documentation"),
        ],
    },
}

NOT_WALKED = {
    41: [
        ("1nicZCUpO3iWz3imBKa1qu8UTGlGdJpi0", "Call Recordings",
         "recording archive - videos only, all skipped by the spec"),
        ("1IJTw4Kiigu5ilM5Z-wZih7lBL2WWzqNa", "GoogleTakeout",
         "personal Google Takeout export (Mail, Photos, Keep, ...) - "
         "8 subfolders, no files of its own, not a project deliverable"),
        ("1FdiyddxiiHq-aYpJggLZi25_NImrALYa/Sprint-*", "Deliverables/Sprint-NN",
         "24 sprint folders at level 2, outside the one-level recursion"),
        ("1MQgFXloPgivS3Aez0uyi0gwKKiXAWy0y/Integration Plan for ITR and LAB",
         "Engineering/Integration Plan for ITR and LAB", "level 2"),
    ],
    82: [
        ("1pbMyEe5AXechGXeMQ1QDSlhVu7A_A40q/DataFile", "Supporting Documents/DataFile", "level 2"),
        ("1pbMyEe5AXechGXeMQ1QDSlhVu7A_A40q/Dummy Images",
         "Supporting Documents/Dummy Images", "level 2"),
    ],
    202: [
        ("1LRLlFvIEpHMWYBfzlIB6bY22S38AE1yT", "SPM 1 recording", "recording archive"),
        ("1HpBaWP0KYVzwB_nQWMDsSDQxCIJBJERV", "SPM 2 recording", "recording archive"),
        ("1yMDoB1_ZE6tKx4DT-TVgEPVYPP5-SywZ", "Daily Stand Up recordings",
         "recording archive"),
        ("1YfTfT2CmrXTjUuSc1mtRFGlJ492tTO_A", "Demo",
         "holds only two level-2 sprint-demo folders, nothing at level 1"),
        ("1VoBb2GOzKTHQbVdaqWLLnm25Pb4Wrcbj/*", "TPM folder/{Test CSVs, Future planning}",
         "level 2"),
    ],
    205: [
        ("1DpNHKUrLy-x3mbZsbm0NjrQ1kPCHqYy6", "Meetings",
         "17 monthly meeting-recording folders, nothing at level 1"),
        ("1uQiRKfws3VoJU_ZMxOIMaSD4zXHKp_dZ/Tax Overlay",
         "Requirements/Tax Overlay", "level 2"),
        ("1dsKhMghckc1aX_ULtH3xZFQhkKLS7pl4/CRs", "PMO/CRs", "level 2"),
    ],
    206: [
        ("1lYUhqZIbFPkLCmu53PVraMplfuHqp6f6", "247 Call-A-Doc Mobile App",
         "one level-2 folder, nothing at level 1"),
        ("1jGNy73q1qIFMA3DEnDXJe0iOwNcjG8iM", "Database Backup",
         "two level-2 folders of database dumps, nothing at level 1"),
        ("1oOzoUtLaQG0qcpVNNND9NIY0_FFHgy2f/*",
         "247CAD-Documentation/{Eligibility & API, Config Screenshots, SQL Scripts}",
         "level 2"),
        ("1X1UPz1lrB-RAsH8U1ZR0oQQLUZNSNjpp/WebSites",
         "Original Repositories/WebSites", "level 2"),
    ],
}
