"""
Real Drive inventory for List 07 (`On Hold`) batch 07h: cards 252 - 275.

Three grouped `parentId = ... or ...` listings covered all 25 linked folders
and every one came back non-empty, so all 25 are readable. Twelve subfolders
were then walked one level down (`SUBFOLDERS_TO_WALK`).

The under-reporting seen in 07g recurred, and again only the union with the
card's own file links recovered the files:

  card 254  `Project Management System (PMS) | Web Application Development -
            Roadmap & Estimate` reports parentId 1ORedyoV..., the folder the
            card links, yet the folder listing does not mention it. Its
            `Copy of ...` twin does, so the pair only becomes visible - and
            dedupe-able - through the union.
  card 264  both `Requirement - 6 Aug` and `AI Chatbot for Compliance
            Assurance Website -  Roadmap and Estimations` report parentId
            1F90tB2E..., which lists one mp4 and nothing else.

  DEAD_FILES     fifteen card-level file links answer "Requested entity was
                 not found"; recorded per card in `errors`.
  EMPTY_FOLDERS  card 254's second linked folder (1sFlFZce...). It was in a
                 listing that returned rows for its siblings, so it is
                 readable and, as far as a listing can show, empty.
  HELD_BACK      card 272's `Creds` subfolder holds one sheet, `ICC
                 Credentials/Logins`. It is a live credentials store, not a
                 deliverable, so it is deliberately NOT copied and not
                 listed in `files`; see HELD_BACK below.

Card 272 (`Icenhower - Additional AI features`) links the old ICC delivery
project folder, whose five subfolders are a full project record: `PMO`,
`QA`, `Documents`, `Meetings` (eight kickoff/DSU recordings, all skipped as
video) and `Creds`. `PMO/Dashboards` and `PMO/Internal` sit at level 2 and
were not walked, per the one-level rule.

Card 259's folder is the School Responder project - the card is the
ColdFusion UI/UX revamp of it - which is why its files carry that name.
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
SLIDES = "application/vnd.google-apps.presentation"
PDF = "application/pdf"
MP4 = "video/mp4"
PNG = "image/png"
JPG = "image/jpeg"
WEBP = "image/webp"
DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
M4A = "audio/x-m4a"
PAGES = "application/x-iwork-pages-sffpages"

GONE = "Requested entity was not found (deleted or access revoked)"

DSC = "Documents shared by client"
AS = "App Screenshots"
MBS = "Mockups by Sohaib"
FSD = "Final scope by David"
UXR = "High level UX review and recommendations"
VFA = "Video from Amy"
PMO = "PMO"
QA = "QA"
DOCS = "Documents"
MEET = "Meetings"

INVENTORY = {
    252: {
        "source_folders": ["1OyaoaydTFJ2Ls1_QEjUCFDqOd4XOR8j7"],
        "files": [
            ("1JvLvrrIoF1PWIPo18ZZYAi6BnWUkcKIq", "Flow Diagram.pdf", PDF, 700201, ""),
            ("1wVQKUa3tKUMqhI5fY-WlFWHO8E7WCZWOYYgW2hF9qJk", "Meetings Minutes from Drip Masters <> PureLogics with Sohaib on January 06, 2025", DOC, 2692, ""),
            ("1lsF1g2vizk5KZX9ETEWy_MNFxw6jOzVQ", "Discovery .mp4", MP4, 301799062, ""),
            ("1cOvID1UXalqdCHI37hpKeQPH8HO2kjSD", "Roadmap call.mp4", MP4, 136955569, ""),
            ("1sYOnKulUg873GuhXkSpFZYHkTfieoNkuCnGZp_ZlDyk", "Additional Notes", DOC, 1024, ""),
            ("1ScqcPdLFtfFwckc9jRmp39bU7pffMBzWHG9X6HvNRHE", "REQUIREMENTS", DOC, 7681, ""),
            ("1WcNySo6hmxkbipexy4lIhM1BDOZ7hX_TGl2jQyiRZc4", "Comprehensive HR Management System | Hybrid Mobile App Development - Roadmap & Estimate", SHEET, 19343, ""),
            ("1iGknirM1V2uACbdCeUtkgzgy4EzyhaDy", "RN Subcontactor Paperwork.pdf", PDF, 731526, DSC),
            ("1ruwA1CvVbyWd6aTYDZt-PtbdSLv3YXzM", "Judi Caruso INS 2023 CEUs.pdf", PDF, 601395, DSC),
            ("1Ai_46WLtVhi1-B-DqLveZaCpAw_3Sg1O", "TB Survey_Annual_fillable_V2.pdf", PDF, 280067, DSC),
            ("1A8izixtwbe4zqKzyeS_Jj2e45TVcmz1H", "JC BLS Exp Jan 20 2025.pdf", PDF, 879763, DSC),
            ("1AmUqTKo_TY2YbWpnFgumNBhMUXJIAuFS", "JC Auto Ins Exp Feb 1 2025.pdf", PDF, 86979, DSC),
            ("11Iwd6z39MukLH0VPI12C_izmE6kiTaGr", "JC Vax & Imm (ALL, Flu 2022 & COVID).pdf", PDF, 2090567, DSC),
            ("1cECxw8Raa4B04vtJfglFGFxgYVji72L0", "RN license Judi July 2023.pdf", PDF, 269101, DSC),
            ("1N3Ea-Xwa_lXPXqgVfniSFciRFY09ZtWY", "Job Searching Platform _  WorkFlow & Kickoff Document (1).pdf", PDF, 632283, DSC),
            ("1UROKNRxLUB0K8X2hjvUNwvnxXofP_X2J", "JC NSO Ins Exp 6 16 2025.PDF", PDF, 166285, DSC),
            ("1G8ypVWwHFmT8NU-HFFOenfQdxQN3RVwc", "Judi Immunization Record.pdf", PDF, 74468, DSC),
        ],
        "errors": [("file:1xSl3sMzIre-Rmh9sOnad8CC42gnnHPvu", GONE)],
    },
    253: {
        "source_folders": ["1rp7KGAu5PauDxtIYAb8UCGwjb7yB_jFM"],
        "files": [
            ("1xp0rwp2N3efysCKvYSVOYPqYjh8T5o8alwssK5qKBKk", "The AI-Powered Cultural Soundscapes Experience - Solution Document", DOC, 18161, ""),
            ("1IvEoWseto7pddmelZFohrptVwCRE8F4nAkscYjpmtmE", "Cyber Secuirty ", DOC, 4379, ""),
            ("1zxsIIQt5Q2XGrGYPGtkLXKLEiEN8WS_YTRQ95Mxm1IU", "Initial findings for AI Project", DOC, 4735, ""),
            ("1II1YKwqXaRdaypImiptK_PjiJZrmYP4Z", "Amazon Music Resonance_ Cultural Soundscapes Experience.pdf", PDF, 91141, ""),
        ],
    },
    254: {
        "source_folders": ["1ORedyoV_ZNZNRfk60Ut-31g2B2BLRsIO", "1sFlFZceJ5ihuJLzuHGB6aa85NYgcssS5"],
        "files": [
            ("1Su0hFaSWHiE5nThX0KYeoI3MoXmDV46Y", "video1847649514.mp4", MP4, 102657166, ""),
            ("1qrlpSrgAl7ydhoX0j0kMyu8CQv8WRMv1", "Trimmed - Poject Management.mp4", MP4, 246114540, ""),
            ("16_ebnJJ2_0vgqFbg_SG2VeaTUfRrJNW9I2NfINJICaE", "Copy of Project Management System (PMS) | Web Application Development - Roadmap & Estimate", SHEET, 32535, ""),
            ("1AyuU2u4U-w2xqb7NaSZDN8w0K7yOnXrFUnk4jbVkCys", "Project Management System (PMS) | Web Application Development - Roadmap & Estimate", SHEET, 30106, ""),
        ],
        "errors": [("file:1WpTrFZf2zieRpFL3mVGB2s--iACKRc3r", GONE)],
    },
    255: {
        "source_folders": ["1oFUwvzfsLtBM4406sx6gZtFhwcVROzr6"],
        "files": [
            ("1TDQYDNKBvaosjieNF4kMofk8vs5tOTaBm1FVnDgR0I4", "Property Management System - Roadmap & Estimate", SHEET, 20061, ""),
            ("1SZAZjDfVoRCOANyiVrqZZ6MIflDC42sX", "2nd Roadmap Discussion call.mp4", MP4, 99254931, ""),
            ("1PEupuZ2SMqwYe-trB2PNNwTDDtxZPSCa", "Trimmed - Mobile App call Ionic.mp4", MP4, 111270532, ""),
            ("1ApFbPcfq72R7aRAVJB6DHSeMPTO_4ae9", "Trimmed - Roadmap DIS AJAR.mp4", MP4, 88884591, ""),
            ("1jh7iqCnjNp77LRaOtDtEsyVinA672VqaaGNs6talaaE", "Notes & Requirements - 17th March", DOC, 3424, ""),
            ("15MUUXBkng8SbnZjPfBUNK_KqhCI8X2eQOUmSswAp3Sc", "Flutter vs Ionic Comparison Document - Solution Document", DOC, 1476373, ""),
            ("1LE1e8XnsarK7sHRWnQqhrEhqknDKbE_gpb8MnlVsGYg", "Notes & Requirements 11th March call", DOC, 7954, ""),
            ("1XKjP5bAXggzczPiuLLB0L2iE2uqNi8pV", "Screenshot 2025-03-12 143133.png", PNG, 291746, AS),
            ("1dLMVBmpt_sUKeRtVy7BlviVArC1c1kmq", "Screenshot 2025-03-12 143049.png", PNG, 234478, AS),
            ("1lnw-_XnK2WJ4tcbH6m3gYzJSH7mDTLXa", "Screenshot 2025-03-12 143145.png", PNG, 302731, AS),
            ("1jn7l_e_tducQCx2j59AakCXeYwNMOoeK", "Screenshot 2025-03-12 143255.png", PNG, 181988, AS),
            ("1KStGLED4i9pTeny0YLIor-EKVkWMVPRp", "Screenshot 2025-03-12 141811.png", PNG, 200259, AS),
            ("1xY6958yrnxxL9eunhKIEx5bMyjY5Y3Uq", "Screenshot 2025-03-12 141741.png", PNG, 299780, AS),
            ("1CI9eLdkHaN3p4t3xWfN4LBvIIJb8zrS7", "Screenshot 2025-03-12 141843.png", PNG, 197032, AS),
            ("19MnHrbH14sVe5X9wnAA2B9TEl9fHGEo1", "Screenshot 2025-03-12 141858.png", PNG, 280486, AS),
            ("1FamETrqq-eXzO9gSd_b2OpSEcFJ9CQ9U", "Screenshot 2025-03-12 142054.png", PNG, 117784, AS),
            ("19sI-5SmGkY5x2pacPKXkkKMu-oLENR-b", "Screenshot 2025-03-12 141954.png", PNG, 162863, AS),
            ("18Ij2gwsA90QbhwG99g7YUHml1IFl5q_i", "Screenshot 2025-03-12 142951.png", PNG, 222526, AS),
            ("1Jpp2DmJP6g7PHAhPQX-fv9aSgFy6EaDk", "Screenshot 2025-03-12 142923.png", PNG, 195427, AS),
            ("1ZghfxUd9ALzZZHGkm2pP2sFauvPBehC0", "Screenshot 2025-03-12 141801.png", PNG, 231240, AS),
            ("1x5_Mg8fp29e9Nh7S1DtlnKaOhReikaJC", "Screenshot 2025-03-12 142218.png", PNG, 246802, AS),
        ],
    },
    256: {
        "source_folders": ["1selND2iqKFV57Q_c6Wd5Fu8UmKDylfuC"],
        "files": [
            ("1-sy7qbNZp07vDsyIzfmM3AmIHByZZZ9d", "Discovery call - 14th march.mp4", MP4, 237626490, ""),
            ("1UKoayMVqHdDeXnPn2v-5NYmzligeaRtwlVxfa5O6_Ek", "AI-Driven Fitness Application - Solution Document", DOC, 1487815, ""),
            ("1qQ9OoqlYSaRzhGMPXzzfHm6hD1NEofpzG0jN4EebCi0", "Notes & Requirements", DOC, 3885, ""),
            ("11wG3tbm5xU4OH8TFpbyyDFbGsJW1wDVxWzApUqG_MDM", "Copy of Master Template - Roadmap & Estimate", SHEET, 24277, ""),
            ("1TTpmq80gnijGec8J9PyAy_wXJMwsoZyy", "DALL·E 2025-03-13 22.22.25 - An AI-powered motion tracking system analyzing a person's posture through a webcam on a laptop. The screen displays real-time skeletal tracking with p.webp", WEBP, 324800, ""),
            ("1_s2b1-GEYE7Bx-WH-dk7kzua8yxvcIoU", "DALL·E 2025-03-13 22.26.31 - A realistic depiction of a young athlete recovering from an ankle injury with the help of an AI-driven rehabilitation app. The app provides personaliz.webp", WEBP, 369850, ""),
            ("1uMPKl7U1QdkwA8ApcUuSsVV3f7VHn3XR", "DALL·E 2025-03-13 22.22.21 - A futuristic AI-powered physical therapy app interface on a smartphone screen. The app displays real-time motion tracking with a human silhouette corr.webp", WEBP, 334636, ""),
            ("1AguwuVH0bkrINHdodEEDsVXbPf8hBtf7", "DALL·E 2025-03-13 22.24.54 - A realistic depiction of a patient with a knee injury using an AI-powered physical therapy app on a tablet. The app provides real-time movement analys.webp", WEBP, 362938, ""),
            ("1QjIlpc2z6cDEs1NYuifF_7pswUkh9tka", "DALL·E 2025-03-13 22.25.48 - A realistic scene of an elderly patient recovering from a shoulder injury using an AI-powered rehabilitation device. The device provides real-time fee.webp", WEBP, 304866, ""),
            ("1BLAkVPM-Q4vhFcYymo9Oww2lCJpbrH_Q", "Flow Diagram.png", PNG, 1734111, MBS),
            ("1oiRR9W38l0-gGwhp8f2U4cGcOjsbn9QU", "Flow Diagram 1.png", PNG, 1870684, MBS),
            ("1oG0IVx3ebE0ze9EOUfCUotdN0JBmjS4R", "Flow Diagram 3.png", PNG, 1919699, MBS),
        ],
        "errors": [("file:17C01JNbQTT9JoUPj1DcbTMFj4cpWthfn", GONE)],
    },
    257: {
        "source_folders": ["1OXJUu714sUcg00iLaYldxnEvHf3i3jOH"],
        "files": [
            ("1xnkHyOKMbi9vDKNrT-B1mGvAkeC1ojcjhxU_-7PmKFI", "Copy of Master Template - Roadmap & Estimate", SHEET, 24283, ""),
            ("1bYkdrXa15KCZKzOw0k1mxzgN-T95KQBJ", "2nd Call - 28th March.mp4", MP4, 194596835, ""),
            ("1fbIzT0tXzvRXLMKsDJyqsQCN66WC7Ud_", "Trimmed - Smart AI System.mp4", MP4, 167168644, ""),
            ("1ljRpA2-WwEpRf_j7mJNKxLiVWQgb2QSNwAC6XSkQiA8", "AI-Powered Computer Vision System - Solution Document", DOC, 1488022, ""),
            ("1_MU9t1zVISvRiha6uyfTiTJ4zDGr7Xglpt2vnYn-2RY", "Maximin Management - Hardware Cost - Solution Document", DOC, 1476377, ""),
            ("1WjZmODLUi2l86DDcZtKSX0i12h2OzIXLPaO9CTBwpEs", "Notes & Requirements 28th March", DOC, 10786, ""),
            ("1a_0qQLvkjkRXoVekh_UU_9tvF-VA391TiUGV9ERsYSw", "Hardware Cost", DOC, 5220, ""),
            ("1K4zDRtHtWkxvwL6S9d7TgDzPbXGNNeycyt-7kMcbLM8", "Notes & Requirements", DOC, 3211, ""),
        ],
        "errors": [("file:1zOn0MygyIAkAzy8slq4fDBbEWV79X74k", GONE)],
    },
    258: {
        "source_folders": ["12dQLAuwi-rWU9rAcyVdQfCsT39JMEGrd"],
        "files": [
            ("1l3bR0wt9-3lpCcqfT-BwqOt9SIb_lrNC", "Trimmed version - Welcome Walks 2.mp4", MP4, 62441425, ""),
            ("1s35Wavr4LBpZ2vbvNjjXl2vR_MqC96hYIQ0NwIdAbdM", "GPS Integration In WordPress - Solution Document", DOC, 1476381, ""),
            ("12gNA23yu6sVg4_WUN6jrh5041X9EYX41ab8URUyJeHA", "Notes & Requirements", DOC, 3035, ""),
        ],
        "errors": [("file:1vuljncV6gcO2t4OBxOexIh9cdtoNjaOP", GONE)],
    },
    259: {
        "source_folders": ["1Mvs32YzY7Nml6I57aJrtI99gvNFpgq6a"],
        "files": [
            ("1pqAhme9MfHFsJ4jKIils6zW8JSZBs3pVMRdDnda9w7A", "ColdFusion Platform - UI/UX Revamp Plan - Solution Document", DOC, 44916, ""),
            ("110nK65oXkbmQ4RJFiLvtKaFMWvtoBFLY", "Meeting on 24th Feb.mp4", MP4, 143408872, ""),
            ("1Z8W2G2v0USwxuM2toEmgyB21AGkAfT-G", "Discovery.mp4", MP4, 85302203, ""),
            ("1BEVMMS8eQFq4uPvYKcMdRExQW0jAjk1s", "Second Discussion meeting.mp4", MP4, 148726678, ""),
            ("1J1tK_DvzjpljJPZFZQuQUd0T_q7g9QzhAxJn1st0qCo", "Notes & Requirements - 24th Feb", DOC, 5071, ""),
            ("1Z-Gu5QRpePD3-k0wwg8CVwAMl6Oq-7S0bJ0e1RijhhI", "SchoolResponder |  WorkFlow & Kickoff Document", SLIDES, 796494, ""),
            ("1O4rc33P9mG3J1abKGiWuRO6ZTSWh8SIXiDNFWxq-97I", "Notes from 13th Feb meeting", DOC, 6823, ""),
            ("1_BJ1bgu58CqibqUZuc91vrQZ3LpxydHSOQsJW-y1Ps4", "Notes & Requirements", DOC, 3190, ""),
            ("1tahZN1NMGpdCBFCJKkdrr0JVDG2UVind", "Advanced Reporting and Menus RESPONDER 13mar25.pdf", PDF, 199524, FSD),
            ("1UA2_TkyEMOSXwRhC3V2nb4iopp3OzlVncA-qMJ-CN9U", "School Responder-UI/UX suggestions", DOC, 4789, UXR),
            ("1vblN8U-uhSqL9jsroN1c5SpcRSbE7Aq7", "01 Check in About Me.png", PNG, 117358, AS),
            ("1vtb_AA7Kgav38DTY8BA3_RKgAwoZTcur", "02 Tips About Others.png", PNG, 116445, AS),
            ("1ubJoLS31ZEvBUtW_31hOlefAvgJgpleC", "03 Staff Report.png", PNG, 119175, AS),
            ("1vUkg5Nlg6lvYy7LFqxFv9kr-k_7sHRri", "04 Incident List.png", PNG, 96009, AS),
            ("1ALkwDiGbjTIZi2_6btd-un_yjLTal-_k", "05 Chat a.png", PNG, 107919, AS),
            ("1uzsNuKpGd-FdHj3j96mcmcrOz26iCE8W", "06 Chat b.png", PNG, 109235, AS),
            ("17oFWivbKljTd0yLdKKLxPAhNSMsX4Ggc", "07 Contacts.png", PNG, 323265, AS),
            ("16JSpj_2cBIuoVt1P0D7QUAZUMysKSCrN", "08 Events.png", PNG, 130449, AS),
            ("13XoOvCrkgZ8MYiv1FPjT9nuL2Brqh681", "09 Occurences.png", PNG, 326259, AS),
            ("1N2teeyrf0DiyOcs1vfFw1WrKnIiOKaUK", "10 Activities.png", PNG, 115001, AS),
            ("12FOtXm0jSLKPzNQnYdQUY6IuPabW5zAI", "11 Escalation Matrix.png", PNG, 293473, AS),
            ("1DpwaLMK7ccnCcdcliGlAUwPIxKxFLvY7", "12 Reporting.png", PNG, 98896, AS),
            ("1NAuLMu8jGjpRJytcq4uB3koPlqFWj3LL", "13 Incident Report by Type.png", PNG, 120278, AS),
            ("1tdNqn6ADnrXwRNfY1gcIrREoxAVIYAxj", "14 Incident Report by Date.png", PNG, 120676, AS),
            ("1S10C2MHwCAId4ZHy7AAajb80E5x8wL6W", "15 Saved Incident Reports.png", PNG, 122406, AS),
            ("1lbu78bu8lpsfHCX_-tvIZQvCZztBXkF6", "16 Comms.png", PNG, 103416, AS),
            ("1X4uCYM1a43tydjgLVF7c52VDPtZnD89w", "17 Oversight.png", PNG, 97369, AS),
            ("1VIPRQ5PgPo1F59vfmcXQijapHL3Rvg5n", "18 Checkins.png", PNG, 177942, AS),
            ("1Rx5NjZKh-TPtp5u3EYCWInQAxlUBwPaE", "19 Tips.png", PNG, 390645, AS),
            ("1WlAEu1Uf-mxGSRRUH4TFNvtujVhZ3cU4", "20 Staff Reports.png", PNG, 173417, AS),
            ("12rc2s4bWY3KG_2Q03iSgdvSJnRjraT2u", "21 Answers.png", PNG, 116216, AS),
            ("1SGvgHLZqGJMg-Wy1K2PULzS7BoZ6E3wr", "22 Champions.png", PNG, 104172, AS),
            ("1PFZ7Tdcr4TaOXJT_QuxWkMtTQIoLnnf0", "23 Admin.png", PNG, 118142, AS),
            ("19l2sG7-SZ7e8Q150eSvDW2HSbf1LKNPE", "24 Hurry.png", PNG, 113021, AS),
            ("1saABI_DmDPRmCBTYwYKIty4RBB3LivI5", "25 Profile.png", PNG, 95536, AS),
        ],
        "errors": [
            ("file:1Df9L50rw5oO2fpnD_1FmnNRU68gA_v2AmNbibGQxD7M", GONE),
            ("file:1SOlcyDb9mt150mXxivo2hMnN-oupSm7M", GONE),
        ],
    },
    260: {
        "source_folders": ["18tMBu4Jlp0sOb0Zzt86R8u1vMZjhJeSO"],
        "files": [
            ("1hgceoe02JrQZ1RA7pXa-jgYs1-yzoL_Di4WfEwkGHRE", "Referance Document - Warehouse Product Scanning App - Solution Document", DOC, 1603572, ""),
            ("12NHdyawpxcC4G-cWLyVi2oCN2ZhG95B_", "Wireframe presentation Meeting - 14th March.mp4", MP4, 231779011, ""),
            ("17PhxlqTeahrNf8GdAoIVsRj5AFQ4H_Ee", "Trimmed - US Medclinic 17th March.mp4", MP4, 55132699, ""),
            ("17e2idzbTvyCU1R1p_fTpndUstyfUseYnanL6-XjpGpM", "Custom EMR Development - Roadmap & Estimate", SHEET, 24008, ""),
            ("11UPOeJiIhe-udi6AVaTs1d-e0EQPD7cy", "Workflow Diagram Sohaib.pdf", PDF, 15102, ""),
            ("1wZ5mHPlBWG8v9skmo0u3_SNm5zx0ZYw_Cdmzmt5lAk4", "Custom EMR - Workflow Document", DOC, 1684069, ""),
            ("15zWqLloPIrsuX4wEzGrwRJyl2ggFIStV", "Workflow Diagram.pdf", PDF, 743225, ""),
            ("1Tc433vezDfbHw6MCB50Ltf2MpRkDLtewxpVLF3Oeid0", "Notes & Requirements 17th MARCH Call", DOC, 2869, ""),
            ("1GGGr4J4lmxHU1zIpWezYXBKZnlmzbt9r", "Screenshot 2025-03-17 at 11.27.21 PM.png", PNG, 468331, ""),
            ("11sHtNj_cNLqk6gmWB2umiTwZjqQbH6EO", "Sample ArchitectureAndConfig.docx", DOCX, 680955, ""),
            ("1fqhsIA7eTL3aLbyNMb2lkwwvKXjDyl5jUUzsmerNh-k", "Custom EMR System Architecture Document", DOC, 295705, ""),
            ("1Kx9Yt27t_05NQmbtvgPZazNkbOKH8Pmy", "Trimmed version - USmedClinic 4th March mp4", MP4, 85288801, ""),
            ("1tZtyyrb8vJhMmmlpZ9y5OuathpRvwM9S", "Recent Call on 4th March .mp4", MP4, 246402878, ""),
            ("18f92SGsvjfhOBxHd4cHHczUIyq0WFUx3", "MVP presentation call - 10th March.mp4", MP4, 160599469, ""),
            ("1_G38XTpVaUvT3Vk_yrnenU0X4FO7uWf1lEdkvpdXAnk", "Notes from 10th March call", DOC, 4510, ""),
            ("1pUr94RpaiILiyyGJxLVFa1cowzrfs6hVe7KmIO0q41s", "ERD Diagram", DOC, 231471, ""),
            ("16MaYBYNic4BEUwelo-ZGoPpGFGNWDvO_0RMAyIEcT3Y", "Notes & Requirements from 4th March Meeting", DOC, 7136, ""),
            ("1DWx9JyjXCpjvXIu6ALARK_c44D-FSQD-", "Custom EMR Solution - USmedClinic (Diagrams).pdf", PDF, 9944579, ""),
            ("1fLfb7dKCP0ahjfe-iF9dRN44Ga7TP_y3ZLgjeSe6PDU", "Notes and requiremnets", DOC, 7752, ""),
        ],
    },
    261: {
        "source_folders": ["1dZFF4zpvfAuHlLLFrTF9Av7T3jKrlGbV"],
        "files": [
            ("1gnZgPQI52C48h4dkViCJbW-oYfG_pe0gaqSzazgaSsw", "Equityzen.com - Solution Document", DOC, 1476345, ""),
            ("1UV_ESVNzOpRggFT06NAmvsKOPq_1ymmJ", "Shiv_ Platform Requirements (SJ updates) (2).docx", DOCX, 22488, ""),
            ("18wl3Jaj56KoWslrPzN4mwX96uBcLPjJDbdurqroEC7Y", "Solution Document - Equityzen.com", DOC, 7677, ""),
        ],
    },
    262: {
        "source_folders": ["1e0PP8oGYqts8rCScbMlUsLOmsjmbwO2K"],
        "files": [
            ("1i5E0Aatc7Dxm3VxxaQZ5oag9rgZFRUR2Fft0fsdRgC4", "No Code or Low Code Tools", DOC, 17881, ""),
        ],
    },
    263: {
        "source_folders": ["1BC81KUCqOT82Eg7Pb8ArUgLCk8WGhvcH"],
        "files": [
            ("1YFXl8EplM85DgYLilx-qatUS2Gh-c4tL", "Requirements - AI Platform.mp4", MP4, 50300153, ""),
            ("1wfQ05knEaFC3FSXFa5Bc35Ct13RX6TBD0v6mvHmFWCQ", "Magellan College Counseling | AI-Powered Platform - Solution Document", DOC, 19618, ""),
            ("11uojWZn9CbRE35XadY2R8T3e_4Bk8teLEpPawyO7nvs", "Requirements", DOC, 1850, ""),
        ],
        "errors": [("file:1OQd48Er5wPu1uRfRlbkwypSa_NYCTcli", GONE)],
    },
    264: {
        "source_folders": ["1F90tB2EuS2tOep1dUB-wcgB52QJsjubY"],
        "files": [
            ("1HbtBL9wrTU_Bz1CGrobKFQtLG0z-3zkN", "Trimmed - 6 Aug.mp4", MP4, 70604887, ""),
            ("17MgyePAjoG_NzE-J2QQROng4bCQiH3b8EhCL2LQR-4o", "Requirement - 6 Aug", DOC, 1024, ""),
            ("1sqEOOA5ynuFJqoC1PAvP5dKwC5PyzCJP6AUGxKZhDGE", "AI Chatbot for Compliance Assurance Website -  Roadmap and Estimations", SHEET, 15797, ""),
        ],
        "errors": [("file:1YgxSw-z5i1VbXPKPGylZBf7aYKPHe0vv", GONE)],
    },
    265: {
        "source_folders": ["1qvIIEUka2qcwhJcuNCydF5CP7zNFQN4B"],
        "files": [
            ("1BOayx4dNqtn1_lJ2OTHBXpyUNimmnswg", "Trimmed Version - Dream Canada.mp4", MP4, 239369825, ""),
            ("1NC0jfqaOpYK-8qZhqAY0JYks4LiXank4", "MindMap | AI-Driven Skill Evaluation Tool.pdf", PDF, 69226, ""),
            ("1WEw5ae0yKPrF97eTN5H6iUtEMyaL5g-Ua1JyK1hdsp4", "LMS Automation Platform - Roadmap & Estimate", SHEET, 24281, ""),
            ("1OZidqyvXz4-UwO8MmSikGVSD-Wj3Xryhh8xkYfDVtvI", "Notes & Requirements", DOC, 5590, ""),
        ],
        "errors": [("file:1dUyU71B2dLmP3_Hhw4-scm_EKp0A6YGt", GONE)],
    },
    266: {
        "source_folders": ["1CoEfDTYpMfgVirQxfnJg4exfz53m0K3b"],
        "files": [
            ("1yo51xy_D2OvQ911MRrUX7bEORmEBGwPhxmJAdzCFzh0", "Astrology Application | Web App Development - Solution Document", DOC, 1488620, ""),
            ("1azvuApvPMt9pmRIrpxOZafmy1pMnrPAB", "Trimmed - Astrology Call.mp4", MP4, 56370882, ""),
            ("1REtl586IyM1DwZ39beH7UataOp_FMW--pD6D6fc-ebc", "Additional Details from Prospect - 25th March", DOC, 7266, ""),
            ("1wiG0Vplwlm9Bg1lDs1Ox8Ff2zoUkoxkOwzhzH_QETqw", "Notes & Requirements", DOC, 4741, ""),
        ],
        "errors": [("file:1sEbsILlftg8wz8vXB7uFsaLsbHqzZ2Ck", GONE)],
    },
    267: {
        "source_folders": ["1UXPk2wzfqlBPbyhbDi8iLicVRJdG2Vai"],
        "files": [
            ("1_O0NunglU57d4bl9Ato71jrEQfqg8R1k", "Workflow .png", PNG, 1954765, ""),
            ("1opFm9xiEcKLNQ7RmfYtY4akV83kC0w_y", "raw.png", PNG, 1747577, ""),
            ("1Cxp7NbdwNS2KGF7tMwIUUOka6NZ7v2ae901BW1sCHtA", "Copy of ProjectName - Solution Document", DOC, 1476489, ""),
            ("1UQDkrhLHc3wXe5tKfEhn1WlUs6QmLrVe", "Trimmed Version.mp4", MP4, 40681585, ""),
            ("14FJtupe_UyOWYQq8AsCq8Vrw_N12rGKuMu4ZEGHl-ck", "Notes & Requirements", DOC, 4053, ""),
        ],
    },
    268: {
        "source_folders": ["18HuK-bAxmvecibyccJPJTWVaFtfbhyN0"],
        "files": [
            ("1SyM3q4-gvRXcKZgbsuFkvXi0DcVq8YiV", "Introductory call.mp4", MP4, 131210630, ""),
            ("1slYlDdkRv3BHICW5AVS_D_1w8QW3yh3C", "Keen Keepers - AI Aavatar platform - Architecture Diagram.pdf", PDF, 562337, ""),
            ("1eQ9GVpnoYyQE2h701wKqVK1qGmE1N_a3", "Keen Keepers - AI Aavatar platform - Gantt Chart.pdf", PDF, 70612, ""),
            ("1Tq0cnw42wIZIV4Ras4MyCdH6VLmmu0PL", "Keen Keepers - AI Aavatar platform - Team and Tech Stack.pdf", PDF, 29742, ""),
            ("1fL6rCOEVFx_VWlU2aFXAZSjO12yYCqxn", "Keen Keepers - AI Aavatar platform - Ballpark Time Estimate.pdf", PDF, 38740, ""),
            ("1BIe5KtZL2VdvaBOBo5yzazZ2fz6VUN19", "Keen Keepers - AI Aavatar platform - Mindmap.pdf", PDF, 47804, ""),
            ("1KSFy4YkWzl55Ama2UkHzK1qnUxMDVi_cjuzRpirCd8k", "Notes & Requirements", DOC, 4387, ""),
            ("1OkMEp7eBMfbhwIGn47n_Oo3faissEogknlnWs41FtEs", "Copy of Master Template - Roadmap & Estimate", SHEET, 25901, ""),
        ],
        "errors": [("file:1BtF3fpeBgi5rZEBjdE091xPJ8-ayWbNl", GONE)],
    },
    269: {
        "source_folders": ["1SDrncdntUNFsTzHPikqDuWtZkBr64YpD"],
        "files": [
            ("1dE1my2pwoXhTnCdGbcbaI3t8aX4f_0FI", "1 May meeting.mp4", MP4, 188859769, ""),
            ("1OFkPEPwnBSHkl3NWeGft8B0qNJgB--Yt_EaIxaD-PpM", "AI Mindfulness and Wellness Platform - Roadmap & Estimate", SHEET, 36457, ""),
            ("12W7TPxaw6s9nFiOQqsNgYGejFQ41IdVJcnORvzF8kKE", "Meeting with 1 May", DOC, 2797, ""),
            ("1p_hX_LtgNvqhtRMDspncjkMk8bVyBLcKtxNuT9bybN0", "Notes & Requirements", DOC, 6014, ""),
            ("17vtUS3ydehNg6vaEkDAmWPdZ3h8Sg085", "Workflow.png", PNG, 1201853, ""),
            ("1TChTcgkYBsG1PS2m-5HJs88hAXvFzhtE", "Workflow.png", PNG, 1647584, ""),
            ("14sDdL6V5NhkosWo4BZ5ldcW89Nc9qdrp", "GMT20250418-165756_Recording.m4a", M4A, 43986197, VFA),
        ],
    },
    270: {
        "source_folders": ["14lALCIrJ3tb7cbhfCHwkHihUHx8e_lc8"],
        "files": [
            ("1YLpH5LEY-pnqDFPUljFWtDwJJC6f_iGtT7QK6o4iFa8", "Jawlah - Proposal Document", DOC, 6048591, ""),
            ("1CzZ7JlxEeD3M0_WJ9ecwVfmWFuBPuSjV", "Solution Document call.mp4", MP4, 121211065, ""),
            ("1tTgpRMhuznHb_sUY4L-477ieDDl_CirP", "Intro Call.mp4", MP4, 50498327, ""),
            ("1Lc5_6FvoGLw_QyItco3YO7eST7WKN0uHKucu4OVeVAQ", "Notes from 12th May call", DOC, 2651, ""),
            ("1M_oEf0bqZpxuh0bMGkcFXf-KnNle_D4H8bwwH_1lc3o", "Notes", DOC, 4003, ""),
            ("1MVinZgIRCjlj584aj9-XRjKlW6gAYksg", "Ticketing System.pdf", PDF, 287698, ""),
        ],
    },
    271: {
        "source_folders": ["1OuB9BtLrlq0h8Lg6HF9_hubzdMTxzE2_"],
        "files": [
            ("1JfR0ly0MszTggUjEcx5_QCDOpzt6Tyqy", "Discovery.mp4", MP4, 37275104, ""),
            ("14AvVFmjQ_yru_WaxtP-DulgxsFTGbRqu", "IMG-20250328-WA0006.jpg", JPG, 103245, ""),
            ("1re4ahnEdVc-D55lJh4WkHlZyhQc7Qc0w", "IMG-20250328-WA0005.jpg", JPG, 56791, ""),
            ("1uBB_AZcYlxAXCP_v-pJRm5ZYLK_OU0LDszHD7RD_oDY", "Basic Features - Timia Capital - like Project", DOC, 1476376, ""),
        ],
        "errors": [("file:15kBc853UIGjivKmDjiUStNbN4WRLqj_5", GONE)],
    },
    272: {
        "source_folders": ["1dfBK8VByhO_YsyI1kog4O4PwTeUtNGem"],
        "files": [
            ("1ecLk87oHYybArcrxgzATgbxOQRD7TjppKYZYc1jGmFU", "Icenhower Coaching & Training - Roadmap & Estimate", SHEET, 11087, ""),
            ("1-C2oVyKU24BIpuzcK2hVTDXBUjHey0UhbMUZCbBC3Nk", "The Real Estate Trainer Application Enhancement Suggestions - Solution Document", DOC, 18051, ""),
            ("1QeSWBm7bcAmNlode-diswr3SpDdVLnwk2AKsW8aTqx0", "Copy of Master Template - Roadmap & Estimate", SHEET, 17813, ""),
            ("1HzxMsnUTIATytgLcA0kGV0BohmbR5vsfLQ4Pk1HzX7g", "ICC Application - Kickoff", SLIDES, 32494, ""),
            ("1D_69CdEcef4MfrAvgMu3FuijMh6B2FFv", "ICC Application Wordpress Project.xlsx", XLSX, 992506, PMO),
            ("1f9mNkXanXIXFRj5CfqoOBka8a6zBkmZ_", "ICC - Issue Log.xlsx", XLSX, 68532, PMO),
            ("1bz8FqgVs0qhe31sIx2XlPWtp6h0kTmWa", "ICC - Project Charter.docx", DOCX, 37458, PMO),
            ("1gFu8ICkz2vM7CCoDl74EOInX4_T6Koh7uegeTRcG6ik", "Templates", SHEET, 1670, PMO),
            ("1lT93BGDLQDLA1kaBKZCyvou1UVsCGRqC", "Communication Matrix.xlsx", XLSX, 63085, PMO),
            ("1zihe1Q-gdvK57_a_i6E2EfozakUcyUsPGX3jXJxyANk", "ICC - Change Request Log", SHEET, 5149, PMO),
            ("1qIqw-4HZPBSXDw9iN7buuy3z_SH5fkwm", "ICC application sanity checklist.xlsx", XLSX, 24249, QA),
            ("1CVoDqvcMKtxP1UkCnjRHb_IUIX70DfOl", "Test report dec 23.xlsx", XLSX, 9649, QA),
            ("1FzdvB_6VHD6gF4X_XFwZ2gd5gDFI5wmY", "All tasks and issue sheet oct23 (ICC application).xlsx", XLSX, 22696, QA),
            ("1VtpJHB9NgG3mRz1jcovDoXAVtn4JplDY", "All tasks and issue logs sep23 (ICC application).xlsx", XLSX, 20423, QA),
            ("165l9wMe5mENTHaxp8p8crH-7UM7k1KiS", "All tasks and issue logs aug23 (ICC application).xlsx", XLSX, 17736, QA),
            ("1j1-adJakIZtPZbv3ze4qUFqq66ADLOxJ", "ICC application (Test plan).docx", DOCX, 1025023, QA),
            ("152rx0SA-KmBYcU8o6SsT2R4TFzAHQ75_", "ICC application test scenarios.xlsx", XLSX, 51690, QA),
            ("1QmXbc8sK7ErjLJoTwNnC88OjCXRB9dcA3sT5yzFIrSE", "ICC Task List", DOC, 1177237, DOCS),
            ("1dwB_lIoevmHzYTg_bFSujr5l-cUStDCO", "Kickoff Meeting June-05-2023.mp4", MP4, 99770604, MEET),
            ("1Ea1HUkmsYVBnF-QCcvQH7KHKmq0CyihZ", "June-07-2023.mp4", MP4, 141338811, MEET),
            ("1-qhDD6cnO7OfZtvj_Gb5XyKshcTeuUr8", "June-09-2023.mp4", MP4, 49226021, MEET),
            ("1KhbYjPp4VwxZpq1VlBopdECqh0x6hCIX", "June-16-2023.mp4", MP4, 43703139, MEET),
            ("1cP4fFYawVPnJKqh2IHWTuHp3J-Zx208B", "June-21-2023.mp4", MP4, 45645448, MEET),
            ("1aoyZIMP7hz4JHOLdGae2J72YwY2okQpW", "June-23-2023.mp4", MP4, 40183625, MEET),
            ("1VBSZtMmY69C215zd5S5qZVCrcYUwFxj3", "Nov-13-2023.mp4", MP4, 62304566, MEET),
            ("1r6ae7iSpLfGLw43QR_N0D5U4R-Z8rtTK", "08-Jan-2024.mp4", MP4, 33655024, MEET),
        ],
    },
    273: {
        "source_folders": ["1oaYSSr_sU-AETu57kA3AkVulvcQxepV3"],
        "files": [
            ("1xa_SIM0k0cUxVMY52IPUB8D0UHZZbrgc", "Data from Prospect's Provided Table in TrackVia.pages", PAGES, 977764, ""),
            ("1C8I1xS5dO_4TwRjajvFnFbArdP-wwJpe", "PM Virtual Agent AI Chatbot Demo.mp4", MP4, 7434662, ""),
            ("1Snhqt0ikSbcE-OCVOgQvxGrR94Z_eobl-njCVhf8kZE", "AI Chatbot for Field Employees - Roadmap & Estimate", SHEET, 20386, ""),
            ("1pDUSEVh64GGJhEutqCV6ZB7EWq1ZRS25", "Trimmed version - API Call 26th March.mp4", MP4, 105294859, ""),
            ("1t5penC8g73l50W7tcJM9jdqicjImP5Mn", "Trimmed version - AI Chatbot.mp4", MP4, 179789525, ""),
            ("1mF49UObhT3Jl6j-T4wEMJSBv5KNpzRU_5zJEUWCMfww", "Requirement - 11th April", DOC, 2927, ""),
            ("1IXtx2aWsuijisvoRpNjtIpcJBLveCZ8vD396_-Phpq8", "Notes & Requirements", DOC, 3334, ""),
            ("1uwmMx6aGTY67hNV4RQ3VJs6m-3JwKLKZ", "image001 (1).png", PNG, 16172, ""),
            ("19UkOQALecyvLvm8_TrK64WpVXjzVtFY4", "image002.png", PNG, 14526, ""),
            ("1ND9TFr9YQCzNs4SsVwKu1tn9zps55u6rR_AEhzvXplA", "Notes & Requirement from our 26th March call", DOC, 5640, ""),
        ],
        "errors": [("file:1GhX8eNqXawpOMBYrKRg5EyCYUPf-SEuL", GONE)],
    },
    274: {
        "source_folders": ["14lt9Hd3a3smJqvZWaNVKQr37Z02gBBTc"],
        "files": [
            ("1mm1d3XhFKXG60lgqGJ9ZOBxr05OE2ng5", "Mission Benefits AI Automation Project.pdf", PDF, 215395, ""),
            ("1RjR7EAlw-yyp9jvJV-7ax2nBpzEotBEa", "Flow Diagram.pdf", PDF, 24276, ""),
            ("1ElLpbM_1-bX7E6HqlPyOlqWOhxG-wbhM", "Architecture Diagram.pdf", PDF, 605820, ""),
        ],
        "errors": [("file:1DUxIc7u2Up6nGXNP8Mhm2VuJMjW083_C1s7kZK-wpsM", GONE)],
    },
    275: {
        "source_folders": ["1ML6XC2ZH2r4LBC0Ow_vrNt9sQYzjXMuh"],
        "files": [
            ("1gpc2tMYT2ms0b-GPbNNlqqerBqo5PO19", "Second call.mp4", MP4, 21402226, ""),
            ("1FdoCe09t1omfCY7mULAE4iMhvzHZNKR2YiUeFEr0Ltg", "Otter summary", DOC, 1024, ""),
            ("10mv_o-1XV1OBUw4L-W7UNQXD6TeZOU46KomT8fyivFM", "Notes & Requirements", DOC, 5133, ""),
        ],
    },
}

EMPTY_FOLDERS = {
    254: [("1sFlFZceJ5ihuJLzuHGB6aa85NYgcssS5", "second linked folder")],
}

# Files found by discovery and deliberately NOT copied, with the reason.
HELD_BACK = {
    272: [("1GNCmDwO8CfHmNkV45hLRSEiA0f4fFG7JbnGzTbVi89E",
           "ICC Credentials/Logins",
           "live credentials store, not a deliverable")],
}

SUBFOLDERS_TO_WALK = {
    252: [("1ZgCIYMePoGB2wKFLwmhJ_GIqPedDlcX7", DSC)],
    255: [("1qFB1CtNI8MD0WIRRjtepeQIeYvHpwXbr", AS)],
    256: [("1ry6rcCjakTjsXPtTAmZM7DgDlTIK_Lfs", MBS)],
    259: [("1poGhyWZOxoYyF3Uj5SdDtlaW5rVhp-5D", FSD),
          ("14eTePQv00fFE2e_hAH2tZ4wpQ1vixpi_", UXR),
          ("1wcUL1MIexcpL0hkKHt37ZTRSz7LxJX-b", AS)],
    269: [("1BpD5zw_lY7qgNLZx5QNATQ8e5b6v28Iq", VFA)],
    272: [("1M8YG8k82WrjQDFrKQc3UfO0GZqlRpfZ2", PMO),
          ("127a6wuqVRF8BSM0HN2GYAoDD-fpQ2Ark", QA),
          ("1YvretGWQ6FZROA4EA5N_MQrt7En3pyNt", DOCS),
          ("1y5gbWsyIjyj_Bs6bIf12XqCk3mzMz3AU", MEET),
          ("1krCwwiO_u352P_FaR4ni2Z01aQF9_UWF", "Creds")],
}

# Level 2, not walked (one-level rule): PMO/Dashboards, PMO/Internal.
NOT_WALKED = {
    272: [("1RAzHjj88kG13Jnh8nRqehHapg9jynnNG", "PMO/Dashboards"),
          ("1wfO_24hJwaqgr0UK6M5_O7xhIqe5Ayz4", "PMO/Internal")],
}
