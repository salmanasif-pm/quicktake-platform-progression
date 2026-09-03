"""
Real Drive inventory for the fourth List 05 batch (cards 109, 424, 431, 433).

Entries are (file_id, name, mimeType, size_bytes, containing_folder_name).

Scope notes, recorded because these three cards are large live project folders:

* Card 424's diagrams sit one level deeper than the spec's one-level recursion
  reaches - `Latest Deliverables/User Flow Diagrams` and
  `Latest Deliverables/System Workflow Diagrams`. Both were walked anyway,
  because separating final diagrams is the spec's second priority and these are
  plainly diagram deliverables: 11 PDFs between them.
* Card 431's `DSU Meetings` holds 90+ dated subfolders (the listing paginates)
  and `Internal DSU Meetings` 9 monthly ones. They are meeting-recording
  archives - videos, audio and VTT captions, all of which the spec skips - so
  they were deliberately not walked. Noted in NOT_WALKED below.
* Level-2 folders under card 109's `Post kick-Off Documentation` (Sprint
  Documents, Misc, Milestones Planning) and its `Deliverables/Codebase
  Analysis` are outside the spec's one-level recursion and were not walked.
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
ZIP = "application/x-zip-compressed"
TXT = "text/plain"
VTT = "text/vtt"
M4A = "audio/x-m4a"

GONE = "Requested entity was not found (deleted or access revoked)"

INVENTORY = {
    109: {
        "source_folders": ["1qZ8vEoG0eH7l5Jd4ly0fdJwSMIfusgUG"],
        "files": [
            ("1XeNZwIgFwLYDiZ29eF9xWIR_9vIs5cnXqDV8nHCTwx0", "Credentials", DOC, 1024, ""),
            ("1IlcnDFDr43ZNW4ZazlbEIKk1OlEQPlRiChMlCkyhM6c", "MARSS-System-LIfeCycle_OverView", DOC, 3808, ""),
            ("1GTOoAtgBxNQDnx74uIYO6L4uiP57niiG", "Request for Proposal (RFP)- Peer-to-Peer Healthcare Ecosystem App Development_1766059523864.docx", DOCX, 335752, ""),
            ("1dh2nsauoYxJ6trInMFoZFMsfSdyE3eXBVSVwzLls4oA", "Read Me", DOC, 1024, ""),
            ("1_OwoJjfdH0ekX3Q_c2gybaf2nvpe1Xdt", "MARSS-System-LIfeCycle_OverView.pdf", PDF, 221929, ""),
            ("1jXMwmnHpbWzoU3-AMCVrcd8hUp10D8IY", "Dr. Jason - Nov 28 2025 (1).mp4", MP4, 154016062, ""),
            ("1BoyZXSfMilm1p6nQhHW3mPcuDOOPpA0X", "Kick Off - MARSS Analytics - Mar 24 2026.mp4", MP4, 215072378, ""),
            ("1JS3xG1WyM1u7phfqiK8WRvrTpPBq2sfHzLPXXBvtoR4", "Kick Off Transcript", DOC, 20023, ""),
            ("1A9lm0oHwXXRL00RyFx6-lppwkyDFmVgZ", "Marss-blockChain-blockchain-dev.zip", ZIP, 28696434, ""),
            ("1HQbewihlXw0dmkJVOER2GNIWVt0Lxn5q", "Marss-blockChain-F-blockchain-dev.zip", ZIP, 45434849, ""),
            ("1_HKp5oRMzcq952qSoJFDuxuz0v-6Fnd6", "Jason - Proposal Discussion - Jan 9 2026.mp4", MP4, 287735336, ""),
            ("1i9NIU_dnMyiz8PaIHdsc_Cs4xyXETJ52NaBG2CGe5UA", "MARSS Analytics Pure logics", DOC, 4858, ""),
            ("1vZfzQXiKxL60c_Qhaz-A-xfF5Rs96QX4imTT226iS0c", "Blockchain Healthcare Claims MVP - Understanding Document", DOC, 5300824, ""),
            ("1drE5J4etuvTrUz7UQMxYCYvogm2ZNSzt", "MARSS Analytics Pure logics.pdf", PDF, 190589, ""),
            # subfolder: PMO
            ("1_SnJpKyOVxahK4GBC-zUbz21pVV8pcOW_xmpXqY3JDs", "MARSS Analytics Workbook", SHEET, 52190, "PMO"),
            ("1Gl9kffBvZG1fzBG3tXuVyvVRScjBL2lA", "MARSS Project Charter.docx", DOCX, 52221, "PMO"),
            # subfolder: MVP_DEMOS
            ("1X4w8k0uq4NOOjV0xTlW-XC5KpQQvJfew", "Demo video (copy).mkv", MKV, 59414467, "MVP_DEMOS"),
            # subfolder: Post kick-Off Documentation- 24 April
            ("1yjcE_Q9_2qSDlYqrMuxhtMe9a4ShNeWWmLVEnKvXoWE", "marss_mvp_plan", DOC, 12527, "Post kick-Off Documentation- 24 April"),
            ("1tV1aWp4sAI54c1I7LY18op5kr_etZ5OV", "marss_mvp_plan.pdf", PDF, 394738, "Post kick-Off Documentation- 24 April"),
            ("1K0dWOyvzQyPLNfnI2W0rKqtZky45R1jd", "marss_v2_phase_3_document.pdf", PDF, 209077, "Post kick-Off Documentation- 24 April"),
            ("1Lv2-1VyluealbcIVIkBHDm3CSHpIYhPG", "marss_v2_phase_4_document.pdf", PDF, 210147, "Post kick-Off Documentation- 24 April"),
            ("10dQDPIR7hf_sUbrVEBPIJ9ISiH31Zkns", "marss_v2_phase_2_document.pdf", PDF, 205841, "Post kick-Off Documentation- 24 April"),
            ("1Xw0tDyt3yY7wGODmcUnRBTuToivzIjeT", "marss_v2_phase_1_document.pdf", PDF, 244971, "Post kick-Off Documentation- 24 April"),
            ("1uZyABprWQrJ3Qvbb0zMExjYaDMSeh_eM", "marss_mvp_role_workflows.pdf", PDF, 195165, "Post kick-Off Documentation- 24 April"),
            ("1i0NubGugVtw3b9C9mw_xLSDhpkJWy4x9", "marss_v2_task_breakdown.pdf", PDF, 712969, "Post kick-Off Documentation- 24 April"),
            ("1f8xKYieah_YB7MXVwoNM5coIyrUgvmRO", "marss_mvp_task_breakdown.pdf", PDF, 356714, "Post kick-Off Documentation- 24 April"),
            ("1rMVa2KVF_1vzBnJ92oyo61b-YmmLlsiq", "marss_v2_schema_diagram.pdf", PDF, 535617, "Post kick-Off Documentation- 24 April"),
            ("1-xvrjRgcXdY6Pef2UNBB523QxVWWWKGy", "marss_v2_actor_flow_diagrams.pdf", PDF, 360986, "Post kick-Off Documentation- 24 April"),
            ("1p9mWJiRM_RxOAMaAOn3J-sTkBfBMl9wu", "marss_v2_implementation_plan.pdf", PDF, 567601, "Post kick-Off Documentation- 24 April"),
            ("1d3WjcJ-19ref292wSlzCeDwXVUotKPpw", "marss_v2_master_blueprint.pdf", PDF, 708812, "Post kick-Off Documentation- 24 April"),
            ("1jP3B-pM-2i8aNs6MicCi2cspW-IW4X9e", "marss_mvp_jira_tickets.pdf", PDF, 361652, "Post kick-Off Documentation- 24 April"),
            ("1S-j-kbgaUS35J5WyfxpRAkZYyyOd3X0_", "marss_v2_client_overview.pdf", PDF, 174520, "Post kick-Off Documentation- 24 April"),
            # subfolder: Deliverables
            ("1TwdeNSxQLvCTOH-MsT4SlfQvY9256__wjrg2BE3EE5k", "MARSS Analytics  - Peer-to-Peer Healthcare Ecosystem App Development", DOC, 12610966, "Deliverables"),
            ("1znb1emV-Qbtcx1SJyjWD7bvchW-zmwOV7AxdJDO48b8", "MARSS Analytics  - Technical Addendum", DOC, 5420204, "Deliverables"),
            ("1WsDO-MzYk7HQCbosvPS7Fz_2A1AxseJg", "IoT Handshake Sequence Diagram.pdf", PDF, 40174, "Deliverables"),
            ("1RX0G6b_CYHswe0CNJ8_qnA8syq23rNxD", "Provider User Flow Diagram.pdf", PDF, 340840, "Deliverables"),
            ("1C5TL7yutvko0aPVUSUWrDiXb0oOd-atZ", "System Architecture Diagram.pdf", PDF, 488067, "Deliverables"),
            ("1rSfeEpx7yQwQ7xtyhGWX8oENAdvyz4Ij", "System Admin & Automated Adjudication Flow.pdf", PDF, 305407, "Deliverables"),
            ("1lms9CRqjetqNo0HYtAE_ivrtFyH_Gum8", "Patient User Flow Diagram.pdf", PDF, 254061, "Deliverables"),
        ],
    },
    424: {
        "source_folders": ["1o_oQ0N8iO7WIeb3dCVyhlJyh7I-rXyd2"],
        "files": [
            ("1x4ax3XmmNyga5AK4m759-HbpXWu5aH2M", "Sales team meeting - 9th May.mov", MOV, 6638048120, ""),
            ("10S1PyScYZBDb_Va6PP-Fqs9J9ApoVDa9", "Course development team - 19th May.mov", MOV, 10895770685, ""),
            ("1WLcm7AYNhNNTnRyqKAm4L8xz8u3aLq2Q", "Operations Team - 8th May.mov", MOV, 5287934816, ""),
            ("1uh4THyNhAYl56szIdoXIBY6IvJF5l36y", "video1426559700.mp4", MP4, 211094877, ""),
            ("1cMdjcztgaUL3ZJSPtjcKt6wXz15P9RVE", "Finance Team Meeting 2025-05-14 at 6.03.31 PM.mov", MOV, 4771193925, ""),
            ("1xYSgBbaIdCdB60n-3FM6d-a6A8Tglb19", "Call on 29th April.mov", MOV, 12417475550, ""),
            ("1SQplk95bxp1xfVGx_XSA5-fiJXsu3cgC", "Call recording HR module 4th June.mov", MOV, 6914554842, ""),
            ("1jlzyvI8KuVjAOG5BKV1dSRcilx681d0Q9xON74Xxeek", "COMPLETE REQUIREMENTS - ALL TEAMS", DOC, 17156, ""),
            ("1Vjww-CpQr35fEZ5AL0BoPNUEeSiEP5fWQED-dIOtIcE", "HR Team NOTES", DOC, 2829, ""),
            ("1cGBZj-5tWT7MCK4Us_6JPBIpSPz1h2HxGHNPiiNyJa0", "Notes from 27th May", DOC, 3881, ""),
            ("1Mwoqt8sK3i-6Y1LgQLIlehpbKwfeHpF14t6LmV10eo4", "Operations team notes - 8th may", DOC, 5289, ""),
            ("1s8PKrPBc1sBp3vDCBIJYEwCukDh7WFc92xV4z3CNyWE", "Notes from Course & Development team - 19th May", DOC, 5455, ""),
            ("1g7h_lQiimtoHkyvIjDdx9QPD2VmarBDhrY8ZAf7JjRM", "Finance Team Notes - 14th May", DOC, 4446, ""),
            ("1UMftuDD_bLetluHKEaRdZBwA9t-7PRopM8MtQupSMNU", "Sales Team notes - 9th May", DOC, 4199, ""),
            ("12vk9vTygVsnVSXHVN8WZuPG3or9n_xXPfdL2-vkCalw", "JAATO - ITMS Understanding Document", DOC, 1597529, ""),
            ("140-5_NP2V-GrPMp-TtbcqMkhuuGIf98h", "Translated - FPA Rapportage JAA TO V1.0 301021.pdf", PDF, 5725237, ""),
            ("1xvbEpw48x_H2SjryBKTwm1iB2WTV5392", "Workflow Diagram.pdf", PDF, 37216, ""),
            ("1MzkHaoYWh58gbP7M9mnntMIb2rw2fqG9", "JAATO - Workshop 5 april (1).pdf", PDF, 229039, ""),
            ("1yNGtEqd5ZXyeRbz4x9lBHs1hKIupVcu9", "FPA Rapportage JAA TO V1.2 091221.xlsx", XLSX, 140020, ""),
            ("1thldI2_sdPY-JPK5YFA3tx-bfR19t7YP", "FPA Rapportage JAA TO V1.0 301021.pdf", PDF, 615704, ""),
            ("1DqXFgWhenPX5eHEiCL3vZqskgGOhuRfi292iJB_Wl5g", "Notes from 29th April call", DOC, 2511, ""),
            ("131jndO0krKZspziVjpCpap1Vj772vSQx0sRDaIsBJWs", "Questiuonaire - JAA Training", DOC, 13357, ""),
            ("1UaOzKWpuEV8LkIpELXxQ3bUarP7miLJlzBYCkDnGifo", "Copy of Untitled document", DOC, 23860, ""),
            # subfolder: Latest Deliverables
            ("1myvtql0NFBfdHZQL-xwZgy-nFbZDMeWPBXn864c2tE4", "JAA TO ITMS App Development - Updated Roadmap & Estimate", SHEET, 60379, "Latest Deliverables"),
            ("13LFHsVYIEFC4wUJ_8pRlh2SbIKMQBNqz", "Unified System Workflow Diagram.pdf", PDF, 61043, "Latest Deliverables"),
            # subfolder: Internal Meetings
            ("1Je4XifMg2Z-FiU-gkAuyDzoVFaRXVNkx", "video1971416304.mp4", MP4, 23903519, "Internal Meetings"),
            # level-2 subfolder: Latest Deliverables / User Flow Diagrams
            ("1VCAF3XgtRcESHJUqqNeej_6tbE1FeqIu", "1. Participant Flow Diagram.pdf", PDF, 21946, "User Flow Diagrams"),
            ("153CMJ6puEoiG6gBxb5ZpqSUDVoOHR6g4", "2. Trainer Flow Diagram.pdf", PDF, 14868, "User Flow Diagrams"),
            ("19p-ot_EddBqbaQ0Iz6D7vFnmHCplPHW8", "3. Course Development Team (R&D Team) Flow Diagram.pdf", PDF, 18036, "User Flow Diagrams"),
            ("1ulGOtXbFnxoYH8-IM8JpHAdqqd4mJUlX", "4. Operations Flow Diagram.pdf", PDF, 16749, "User Flow Diagrams"),
            ("1_EQjbijc0I6Sgl3DImYLFCu_7ueVNW1Y", "5. Finance Team Flow Diagram.pdf", PDF, 21083, "User Flow Diagrams"),
            ("1lXWPwdfHex3S-0Vgexp84L4vXdGHl1Uz", "6. Sales Team Flow Diagram.pdf", PDF, 17575, "User Flow Diagrams"),
            ("13pMeLIIyXt4bUO_9ozplwhE_EqsswzCt", "7. Admin Flow Diagram.pdf", PDF, 15323, "User Flow Diagrams"),
            # level-2 subfolder: Latest Deliverables / System Workflow Diagrams
            ("1Eckfbvf7TeSwX3ZoephDREpUAgWR0g1t", "Course Development Team (RnD Team) System Workflow Diagram.pdf", PDF, 51997, "System Workflow Diagrams"),
            ("1IXrgQfRi_PZYwURaXT1CXkXa1Z5pu4ZD", "Finance Team System Workflow Diagram.pdf", PDF, 39084, "System Workflow Diagrams"),
            ("1GQJg8t-YAbsPTb_5qCJ3TVHAqOAXjHR4", "Operations Team System Workflow Diagram.pdf", PDF, 44415, "System Workflow Diagrams"),
            ("1v8J2XiCElMTanZI1QMIaRqrss6Ow7FkK", "Sales Team System Workflow Diagram.pdf", PDF, 35433, "System Workflow Diagrams"),
        ],
    },
    431: {
        "source_folders": ["1e1NBfuYNLKuET2DwDZtGB5oe5fPdhaNV"],
        "files": [
            ("1NRwa89mYZ5oUJO-yiY30Cc4UGCigZYw3NQKrTo3tbTk", "Homegauge - New Workbook - Staff Augmented", SHEET, 44582, ""),
            ("1JOTd4S1lAWqiUDltCw8o-adPfl3fKnI01UOYYRn8sLM", "InfluencerMarketingHub |  WorkFlow & Kickoff Document", SLIDES, 796102, ""),
            ("1cwPJ90nmnyIzFJkqyzTdl2BN25tKxxO6DfKvH3opGoo", "HomeGauge - Roadmap & Estimate", SHEET, 29807, ""),
            ("1dODQaeBBrMfaIePZkXWULiYdAuSEqKbqcXvEak1w6gs", "Workbook - HomeGauge (Depreicated)", SHEET, 58832, ""),
            ("1J-cx_ncvT_XB44xHC2KKcEMKdjyYKnfqCuJAPdrU0nY", "Team Charter - Home Guage", DOC, 8407, ""),
            ("1WM90YZzvcS_N5LnQsP16DJTf3bvr61sZDap_GOKI33Y", "Project Charter - Home Guage", DOC, 86535, ""),
            ("1RXeTM45v-2EnYTH7XcdwryDT3oFnn4bbJyaB6Iv4pj4", "Homegauge Meeting Links", SHEET, 10164, ""),
            ("1WHpYtxrZY0cvbpmvn_Vq5i9iDivz7k_-RWL0_PV_BAU", "HomeGauge Transformers 2025.05.10", SHEET, 11183, ""),
            ("1PxCKPmPTngGEUICetG1HGmxGr65vUrkk10w2P0jSs68", "HomeGauge Transformers 2025.05.09", SHEET, 11523, ""),
            ("176J063NSUeAHmxXD-1dedDF6h0w6qaNN", "Kickoff call .mp4", MP4, 134694246, ""),
            ("1FQHG0_Mzupf4hSk9cUtzvaW8vWyuHlhv", "11st Call - 13th Aug.mp4", MP4, 168976731, ""),
            ("1I48YaDub5Ka-F9Lrm6Etz8-ObutoiMDM", "Trimmed version - Requirements.mp4", MP4, 23949783, ""),
            ("1YbSulhX4LO7n0XJoGmoOhKuKoFl_o_Nq", "17th Sep call.mp4", MP4, 84877576, ""),
            ("1bQ2xpUcKNe-xAJB2IcvvpePyjYtnavbG", "Tech Debt - Product.mp4", MP4, 85826643, ""),
            ("1SFkgeBmy0tNhheY5ZYajC6GwDxd_PF1HSxxJYLc15is", "Aleyant |  WorkFlow Document", SLIDES, 800065, ""),
            ("1P3zeGAvqSx0DFX9rGO3OYioKwg3Gn4KIdU7shRWvRHQ", "Requirements", DOC, 1637, ""),
            ("16yulyUR5-iutaEtTmYMgVYcsD78Zt-ej0PXEBNPBhmM", "DETAILS", DOC, 14830, ""),
            # subfolder: Internal meeting 17th OCT
            ("1qVbRqWeOfamgH_7YGqv46T6hG1HS8YAU", "17th OCT 2025 internal meeting.mp4", MP4, 25963259, "Internal meeting 17th OCT"),
            # subfolder: 22nd October, 2024
            ("1fVbK7EYUJ3Max89Ng1crlYMzQrEo6qsQ", "video1636322255.vtt", VTT, 94128, "22nd October, 2024"),
            ("1iXcNmSBPCQq7KLSaZeRaUddz7_E-IcuZ", "recording.conf", TXT, 127, "22nd October, 2024"),
            ("1pyaTxMaf7c6pDRLWsh3jza7gIbdDWhJF", "audio1636322255.m4a", M4A, 48164354, "22nd October, 2024"),
            ("1RfLOwECkYHVra8FlsvfIeO7pV6wO0_zw", "video1636322255.mp4", MP4, 173421603, "22nd October, 2024"),
            ("1nd95zqMhOVIpFGIFi0PGQqBiNRMgGUF3", "chat.txt", TXT, 701, "22nd October, 2024"),
            ("1zrKh-O2PkWCmqIkaHzHRCOJSHWPYr_LZ", "closed_caption.txt", TXT, 69087, "22nd October, 2024"),
            # subfolder: PL's Product Development Process & Approach
            ("1M6VMuHDPwuRy0K9_jjlr1I1kEhsc5a4JSOKzpYE7dbw", "2. Process Governance - Checklist", SHEET, 4241, "PL's Product Development Process & Approach"),
            ("1B0lO6Rg9_aTUzfGWZ8zyFMBAteSG-ucGF5_z5vhjDXY", "1. Process & Approach ", DOC, 55525, "PL's Product Development Process & Approach"),
        ],
    },
    433: {
        "source_folders": ["1bIV1njBfHrAPh7fLaPKXQlma-hDjPCkX"],
        "files": [
            ("1N0LyqQSKTD_0kPwaS5UltudUSwa3dOiFl5vYt6U11qY", "OEM Auto Parts Marketplace - Roadmap & Estimate", SHEET, 20281, ""),
            ("1Dn3xZChxw5HOJYryx1HTtrKc5qkSQiw6", "Solution call.mp4", MP4, 183159161, ""),
            ("1CqPqnfGyWFeVphQ3oPGjZMngTM4aGPIt", "opddp1.docx", DOCX, 13856, ""),
            ("1bt-h9-Ib72rjpngD5XHUZceNm8m_1I7g", "OPD SAMPLE EXEL TEMPLATE.xlsx", XLSX, 11431, ""),
            ("1mCqOkTiXpO2y3CR8u0CWc0ut_ZKKCb3s", "OPD EMAIL ANSWERS 1.docx", DOCX, 143033, ""),
            ("1HGwrF3HMyDp1AkGZAhPfZ9oAy_aBTOLbAeEfAq1i5qU", "Notes from 21st OCT call", DOC, 7509, ""),
            ("1EcSwWoPLUNvQTrJsTerFa44D3gWeRcRXUewDrmaKsII", "Questions", DOC, 13369, ""),
            # subfolder: Admin Guide
            ("144UqDLOW3xBEMwqyVtwIsuaqZKTYDJSuyIewwO7szzo", "OBSO Parts Depot - WordPress Admin Panel Guide", DOC, 19158, "Admin Guide"),
            # subfolder: Documents for live website
            ("1tm4cKI5TFc3tA-ASpEs2xyhzQvkDWetmWQee90spEdE", "PRIVACY POLICY (ObsoPartsDepot", DOC, 10613, "Documents for live website"),
            ("1EDWeXCd9kNirATHdRGWenMWxC14cRATB029x7zuEBaw", "TERMS & CONDITIONS (ObsoPartsDepot", DOC, 11092, "Documents for live website"),
            # subfolder: Meeting recordings
            ("1GgJZa-x8PJ2F6pAx244Wb0mkNTnqZ-X5", "GMT20251124-180113_Recording_1920x1080 (1).mp4", MP4, 56519912, "Meeting recordings"),
            ("1WI-lofhQ7OG4ZUpvpZX1mO899lPKCCeS", "GMT20251120-180004_Recording_1920x1080.mp4", MP4, 70656929, "Meeting recordings"),
        ],
        "errors": [("file:15xKnVqDo0iS7AJR3o__09n_J4O45Oymr", GONE)],
    },
}

# Subfolders deliberately not walked, with the reason.
NOT_WALKED = {
    109: [("Pre Kick-Off Engineering", "listing returned empty"),
          ("Post kick-Off Documentation/Sprint Documents, /Misc, "
           "/Milestones Planning", "level 2, outside the spec's one-level recursion"),
          ("Deliverables/Codebase Analysis",
           "level 2, outside the spec's one-level recursion")],
    424: [("Prospect's System Screenshots",
           "excluded by rule - raw screenshot folder")],
    431: [("DSU Meetings", "90+ dated subfolders of meeting recordings "
                           "(listing paginates); contents are video/audio the spec skips"),
          ("Internal DSU Meetings", "9 monthly subfolders of meeting recordings"),
          ("Credentials", "listing returned empty")],
    433: [("QA", "listing returned empty")],
}
