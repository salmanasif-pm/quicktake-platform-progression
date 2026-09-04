"""
Real Drive inventory for List 07 (`On Hold`) batch 07f: cards 164, 165, 167,
169, 170, 171, 172, 173, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217,
218, 219, 220 and 221.

Card 164 links one card-level file (`Copy of NT Sprint Portal Updates`) that
is NOT inside the card's folder, so it is inventoried with an empty
containing-folder alongside the folder's own contents. Its six
`Screenshot_..._Lingokids.jpg` captures are competitor-app screenshots: they
carry no diagram keyword and are skipped as ordinary imagery.

Card 167's `Client Portal Screenshots` holds six numbered portal captures,
excluded by folder name. Card 171's `DRAFT` and card 212's `DISCARDED`
subfolders are walked (they hold one real file each); the `2. Architecture
Diagram.jpg` inside `DISCARDED` is the superseded copy of the level-0 PDF and
the deduper keeps whichever the classifier reaches first - both are recorded.

Card 216 is the widest here: ten level-0 files plus a `Deliverables`
subfolder with seven more, including four flowcharts/diagrams. Its four
`Parkalot-*` PDFs are the incumbent product's own manuals, kept as source
documents because they are what the prospect shared.

`MindMapping.pdf` appears on cards 214, 216 and 220 and stays a source
document in each: `mindmap` counts only on an image.
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
PDF = "application/pdf"
MP4 = "video/mp4"
MOV = "video/quicktime"
PNG = "image/png"
JPEG = "image/jpeg"
BIN = "application/octet-stream"

SHOTS = "Client Portal Screenshots"
DRAFT = "DRAFT"
DISC = "DISCARDED"
DELIV = "Deliverables"

INVENTORY = {
    164: {
        "source_folders": ["1WPX7CYyUzh2G8seaZ-D8bhx5aaLo8-ZX"],
        "files": [
            ("16fTXg1cBiuFLMn3GtoVJfXqRV6P4lJpWuvjD2dUJBEk", "GrowingBrilliant - Roadmap & Estimate", SHEET, 29310, ""),
            ("1hT_lQ9JFo7fwsxCxIg6F79vZY67dxi85wJJjlkv50n8", "Copy of NT Sprint Portal Updates", DOC, 1241727, ""),
            ("12qQW2OkCH1jjhbTqIvk490NQam-AghCD", "Screenshot_20251028_220952_Lingokids.jpg", JPEG, 141861, ""),
            ("1iX2xSfQu-fN3TTEmR-Ny__PqkiKK-BwN", "Screenshot_20251028_221018_Lingokids.jpg", JPEG, 113587, ""),
            ("1ORh8w5YXbGMcbeCrPAAUbvOkxCtmYw9o", "Screenshot_20251028_220925_Lingokids.jpg", JPEG, 180968, ""),
            ("1BrJzxLXWyT1D8KRUXeL9sIeJbjCZuqbd", "Screenshot_20251028_220941_Lingokids.jpg", JPEG, 144906, ""),
            ("1pDIE6IQ2jp4_DVC_ff37CZbekDVKcZTd", "Screenshot_20251028_220930_Lingokids.jpg", JPEG, 201063, ""),
            ("1l4M_9cByv8lhER0OauNvE-pzzpwxdqwe", "Screenshot_20251028_220936_Lingokids.jpg", JPEG, 180905, ""),
        ],
    },
    165: {
        "source_folders": ["1bk4Gr2xFSifuGTFzyIKVOcOKevg2Dygh"],
        "files": [
            ("1fDaNTQcaJYb78hMtL81cBVgSkTO2sSz3", "Miro Board PDF.pdf", PDF, 875542, ""),
            ("1LV_Bo_C8CByGlslFitTglGL3MrrJ2Q0RmS-KtRN3ugY", "Read Me", DOC, 1024, ""),
            ("1l_druAK9J9Xo0xIERUUSWRTeMGV2izbz", "Recording - Terrence Murphy Companies.mp4", MP4, 57917287, ""),
        ],
    },
    167: {
        "source_folders": ["1PhamMYqgmobb7IjOPq1UZo48dzsScDBa"],
        "files": [
            ("1Nks28Qf1W-RZRsHr0cSU5lSuskYWEzjD", "PiQwell - Tech Recording.mp4", MP4, 79216116, ""),
            ("1TvUk51529rwGeEhdjb6vGm4tT63PRZFfjMc3UgHpRKU", "Piqwell Mobile Application - Roadmap & Estimate", SHEET, 27910, ""),
            ("1kdP4GTvQKS3URzeGVeCw5vEFZUN7O_gG5KDmU5etlXw", "Read Me", DOC, 1024, ""),
            # subfolder: Client Portal Screenshots
            ("1V-OPFT_LGTgE8il7DFcsuTm5VWBRYVb_", "01 Appointments 1.png", PNG, 144606, SHOTS),
            ("1zF7tF8Qs57nkDti8yW0Lig7UCWicDQjg", "02 Appointments 2.png", PNG, 135957, SHOTS),
            ("1OyCmmJX5VWbMItuZxOVpf4pD5m8OeRSx", "03 Documents.png", PNG, 133391, SHOTS),
            ("14wOzLoSfWAhLtJClWdEWMlKDYdMXLpSW", "04 Billing and Payments.png", PNG, 163491, SHOTS),
            ("1_xyb6KtwSHJLKqdRhg7sHl1eICNFKgzc", "05 Announcements.png", PNG, 169271, SHOTS),
            ("176C4uiHYZwWxnQhcEcJHp9MK5A2Nc3n4", "06 Contact.png", PNG, 145150, SHOTS),
        ],
    },
    169: {
        "source_folders": ["1paUxJnqMu3LXkMVoL6qnM14OVEqppShs"],
        "files": [
            ("1v-3aplzpyhUFCq7PrpiYyC9GCTNsaHnIt6m7x2Yomuk", "Conversational AI Agents - Comparison Document", DOC, 1475589, ""),
            ("1LeGXomYjwqwCnd3i7ytdssBeLOidtwG5EVdAPMkaTWw", "Endless Vitality - Roadmap & Estimate", SHEET, 19084, ""),
            ("1F4qYlQ3Lx-CUCQKU1PMS5QZEFqUNvJNq", "Endless Vitality - Tech Recording.mp4", MP4, 120612965, ""),
        ],
    },
    170: {
        "source_folders": ["1_F7UMXexejfUbuQJ6S1yKrFVdMdEqM4T"],
        "files": [
            ("1GqnimEkVkQTUCSOJFFt0OE4NIShUGrwz", "Tech Recording - IYA.mp4", MP4, 116627115, ""),
            ("1OnIguRQrhxaUdeSCrDBv0q5fjdaKPEw_", "IYA_Purelogics_SOW.pdf", PDF, 4260, ""),
        ],
    },
    171: {
        "source_folders": ["1MDSJ0vMuxqgAedGNBTv5982cAhwVHE92"],
        "files": [
            ("1A97r2xNMP17O76V7ORW7rgTNTDgtyxcq", "WellNuo - Recording 3.mp4", MP4, 392529586, ""),
            ("19FHuvaFTgQC4mMZ6K58aloIcZuwbv95C", "WellNuo - Recording 2.mp4", MP4, 945149186, ""),
            ("1LhOq2IefsoUXj8-5_VRWCEeVF9-SRfuTF5d4W2M0V60", "IOT-Based Activity Detection System - Understanding Document", DOC, 5323765, ""),
            ("13QUAu4PctHyp_8qNVVHuH06RBvD6TdWY", "Jupyter Notebook for Phase 1.ipynb", BIN, 8867130, ""),
            ("1Utyp6_UIOeKmK2g0GUG_duh5ZDSwVncr", "Room Labels.png", PNG, 234923, ""),
            ("1OAoQP8rcNvzm_a-2XdyHQX-o4SP9PQV1qJjdplvBucI", "SOW + Sample Data", DOC, 1024, ""),
            # subfolder: DRAFT
            ("1D19XYIoztpzrmjSBZL4KS3PPmAUOen-YTdwvPs5pM10", "Project plan (tentative)", DOC, 18775, DRAFT),
        ],
    },
    172: {
        "source_folders": ["1OJHhJJwRnPuUaqPIfznYRlvpSSjh0AkX"],
        "files": [
            ("1KXo5VxxEJll0oJ_XMYLQSS9-rzURukZh", "7(A)Funding - Recording 2.mp4", MP4, 268079546, ""),
            ("1NpUrIXJdbSjecop--z9rNyrJvC0g7HIr", "7(A) Funding - Tech Recording.mp4", MP4, 362826713, ""),
            ("1dcRxM0NAbQlrswaDp3G6C8QVEN7BUB-n4X1RUfVTyc0", "SBA Loan Exchange Platform - Roadmap & Estimate", SHEET, 81829, ""),
            ("168A5fBgPWcnCYNtgS-vIAXlvqdyQkN_dnF1dtwI0dMw", "Read Me", DOC, 1024, ""),
            ("10pRVufBftt8Hs3wLu1W2oQUhdBnMw-XIw3KHqJal9Wk", "SBA Loan Exchange Project- Questions", DOC, 1475596, ""),
            ("15xPJD0jpHkBDD3TwHOSNFY50O8gRPYuv", "SBA Loan Exchange Project Breakdown for Sharing.pdf", PDF, 458118, ""),
            ("1klOueC0_FFKfA7hTWbN1TX2hJWHT93Z6", "SBA Loan Exchange Proposal For Sharing (1).pdf", PDF, 1401336, ""),
        ],
    },
    173: {
        "source_folders": ["1vU2_hAv18EAFRPoHh2uGx_fwxht3ML52"],
        "files": [
            ("1pmx7PBGSTfnVV3_mqmKXHUf5LtwdAwsy", "Redpoint - Tech Recording.mov", MOV, 173548033, ""),
            ("1s-n_Y0kQe-czFGdg4NDbNanqMjqbvHLoICXC6dCiUq0", "Procurement Automation and Vendor Sourcing Platform - Roadmap & Estimate", SHEET, 19260, ""),
        ],
    },
    208: {
        "source_folders": ["162fLTdB9lAdfqnQ_-2lW6rzYUi1OogJQ"],
        "files": [
            ("1R7Odlgaffm4XCrKUt3U4fojB60VNYSlB", "Recording Workflow Automation.mp4", MP4, 88808370, ""),
            ("1QB6ay-nSRuMpjYCTzvXysbz-xW8wMvq-VP4qV9pxO0E", "HealthCare Workflow Automation and Integration - Solution Document", DOC, 17403, ""),
        ],
    },
    209: {
        "source_folders": ["1uRVfaqsrJLJjzGHKTs-F78CDY9VJFmvX"],
        "files": [
            ("1brslMRNeBjhaB22DfuCeKj_m6yWAlLil", "3. Architecture Diagram.pdf", PDF, 1984257, ""),
            ("1wbfLUf-YDJ5kiaTjvijVAxtnBTj0Qu09JxlDW0soYfo", "1. AI-Powered Dashboard Development - Roadmap & Estimate", SHEET, 20124, ""),
            ("1xelh-7pwM5OgNGS_qzIY_HYB6ru-a3zs", "2. Balsamiq Mockups.pdf", PDF, 483044, ""),
            ("15qjO_lsQ67fZc_4OQY9jqOy3AMA8THNk2aSNHnhIyWM", "AI Powered Healthcare Dashboard - Solution Document", DOC, 14313, ""),
            ("1LDrZETD9sqlQwh4dHchr2x9PIpmNvhovqkXY3TYjSP8", "Deliverables", DOC, 1024, ""),
            ("1BFuqksX7gi3ZjI07ZaUoQlgCDylMxdcG", "Recording - G S.mp4", MP4, 108289011, ""),
        ],
    },
    210: {
        "source_folders": ["17cs925PW7up54VUA4wPkETYsTVh1uJL_"],
        "files": [
            ("1J5DzteXte7fCgLsfFVN2VO38Ds_kFgVPyunS8SGjtLc", "Wellness Analytics Tool For Military Units - Roadmap & Estimate", SHEET, 19033, ""),
            ("1n_gRKThO8f8-4jBanybloghGy8DIYCxy", "Recording - J W.mp4", MP4, 119472803, ""),
        ],
    },
    211: {
        "source_folders": ["1lGlaP03WnlfWMmSA9sxzf1oajdYoQ0Js"],
        "files": [
            ("1g4M7Y21_8ds_yWaA8XGMNonaJk9MTO4c", "Ed-Tech - Recording.mov", MOV, 22494966, ""),
            ("1-_Vw5m9rH6fpGwB0ME3AaaR-V-sxZ0d6Lzts2Fnsaho", "Essay - OCR + AI Solution", DOC, 16457, ""),
            ("1wOyDDXDC53CO9Iy6jhG0jmOLhIHH9CS5rIqyVNoPJMA", "Essay OCR and AI Solution - Roadmap & Estimate", SHEET, 20379, ""),
        ],
    },
    212: {
        "source_folders": ["1mhIOJ0JwmtXGcPUGfLR5Cl6zYI7zAQdR"],
        "files": [
            ("1AX6yn1hF0Di2HA9BSjGJ8j5uZF50-7nQwkd-Ie_uFcc", "1. Invoice Processing Engine | Solution Document", DOC, 37754, ""),
            ("1uWbGCIqK1hwmCAF6HHPWz3_jqZ5IeAPP", "Engine - Recording.mp4", MP4, 145171400, ""),
            ("1Ds6uS3owG5P3iVB946K9Lw0hjSQxtWxC", "2. Architecture Diagram.pdf", PDF, 1389421, ""),
            ("1f8SQg3NtBO0f5T3npno5bev9fEmeadzNypG-T3CrtfA", "Data Engine - Roadmap & Estimate", SHEET, 17760, ""),
            ("1B-Y24VLm8MyvjNomnjm6PkKe9YOdzvJWb-8Dn0qA3Pw", "Requirements", DOC, 3567, ""),
            # subfolder: DISCARDED
            ("1O72Ti1j3lOu_le8qEruz6wqiPWP5gmtr", "2. Architecture Diagram.jpg", JPEG, 84195, DISC),
        ],
    },
    213: {
        "source_folders": ["1I8m6BMhhsKYB-LGR6h__nwNkfvcbDoSR"],
        "files": [
            ("17WwP4M7adhIXPCxp8_Jp1Nc5Nx7PBQif", "Process Automation Recording.mov", MOV, 452452966, ""),
            ("1Ul77IirhrUyu_PTXawAMGNyyFepYvtFFlZzR-uRdwTk", "Law Firm Process Automation - Proposal Document", DOC, 5933493, ""),
            ("1olVyicQRQnM4_EAUDDMVgMZx1TuRlRTh", "Flow Diagram for Client.pdf", PDF, 99072, ""),
            ("1rZgBu77h7KK9MwBS719bIeHG4owkVNuqxETyzaYD3q4", "Law Firm Process Automation - Roadmap & Estimate", SHEET, 33203, ""),
        ],
    },
    214: {
        "source_folders": ["1NJGuwsvOQDGseZMpgaM4Rddq9zzE5lPs"],
        "files": [
            ("126UvspJCO1mOvA2tTIDZWSrNzrEp03Lpgs0oF1hwbl8", "1. Learning Management System (LMS) Development - Roadmap & Estimate", SHEET, 33906, ""),
            ("1JhzwxbtCfoyM-X0Sc9hZzQDRHYwqUcj-", "2. MindMapping.pdf", PDF, 890755, ""),
            ("1eMgZnIXU6ew8kQI29j2NLbdHtHxBVUM7", "3. Student Flow Diagram.pdf", PDF, 634501, ""),
            ("1VdCB-TvMqZJV0SBG2fvV1CWBNxU57o7d", "4. Teacher Flow Diagram.pdf", PDF, 481111, ""),
            ("1HoB16qoGEMl-z2BNNCJ6A713KB8z1QTu", "Recording - 15 Aug 2024.mp4", MP4, 153894159, ""),
        ],
    },
    215: {
        "source_folders": ["1Pcb42bhkOwu-UcsCfp1hbV71Ns3YiNss"],
        "files": [
            ("1mAQ3NsKS2oFwtLvN3OPH2fwCetrqurQq", "Project Phases Diagram.pdf", PDF, 6167720, ""),
            ("1oHwy5oYS4GXfkyngbo6MIAF9_sLOADfA7l2NVjkbDQM", "Jewelry Warranty Management System | Solution Document", DOC, 28942, ""),
            ("1P_6ajL5gSSH9Lp5Wmu3fWO8EjPS600vj", "Recording - L M.mov", MOV, 101728063, ""),
            ("12e5mGqzAbxol79XyYgYmNspRoTXPXmzw", "Problem Statement.pdf", PDF, 275054, ""),
            ("1GMeQOzIZctaPvkElrrSyTz84LwnAtM4tE0UxBBl2KMs", "IT System Upgrade - Roadmap & Estimate", SHEET, 17752, ""),
        ],
    },
    216: {
        "source_folders": ["1dVRGcdWAFyb5UxPX3soH7q20RYQzk933"],
        "files": [
            ("1c4_LH0BRW4XrW5lyKJ3YkplQDD5kNh6d", "Flowchart - Parking System.pdf", PDF, 68834, ""),
            ("1ni4ZDcbE4VEdjVZuZ31MCdJgUT_jTUCn", "Mind Map - Parking Systems.pdf", PDF, 90359, ""),
            ("1iW96d18YM61_zBgWxhKdD_na3JO5HO8n", "Roadmap & Estimate 2.mp4", MP4, 172470352, ""),
            ("1TyiQzjRLwt7wKWbXfaorR75jDnWDHAVt", "Roadmap & Estimate.mp4", MP4, 161198460, ""),
            ("1g0TKlyWcclF78KqLxMQn6IUNKNaYtHaw", "Parkalot-Admin-Guide-Complete.pdf", PDF, 3507974, ""),
            ("1Du0LfusDBgeuKO7zywlBUywuT0matBNV", "Parkalot-How-to-setup-your-parking_ (1).pdf", PDF, 3732758, ""),
            ("1qb8zyU4ebwstIXzu-G5-bZhI8oOnrBU7", "How-to-use-Parkalot-on-mobile_-1 (1).pdf", PDF, 2850368, ""),
            ("1X7-7qsbYm-CRf-y4_HeMCJ5Kkqj-wpgk", "Parkalot-User-Guide-Complete.pdf", PDF, 1912998, ""),
            ("1lf_GbPs7Gj1XuQh2VDL8r-bO7xVUu2O_6bK7CsfmQb0", "Solution Document - Template (BD)", DOC, 20217, ""),
            ("1V8pyxXEX-WIgVtbcm4WLoqXDyokr7EQg", "Recording - 16 Aug 2024.mp4", MP4, 71555627, ""),
            # subfolder: Deliverables
            ("13Ax2N03S09VKULeJRfrRh2M9wsrU-LgH2YYtvSyO_CQ", "1. Parking Management System - Roadmap & Estimate", SHEET, 35270, DELIV),
            ("1cR5U372RlKz0Az590RwXUdgl6suWRJKB", "2. Wireframes.pdf", PDF, 1570935, DELIV),
            ("18IyT6sjpph_wGic1pA3dbaU7WXAkDwcC", "3. Employee Flowchart.pdf", PDF, 424366, DELIV),
            ("1AadNvg2HIlvF5_4WEsjqaxGFb0gCYNCT", "4. Company Admin Flowchart.pdf", PDF, 641125, DELIV),
            ("1iKH161BkO90DqPmyGfh9BWFyuHFwmRLR", "5. MindMapping.pdf", PDF, 417590, DELIV),
            ("11ZcClf1hs-ORvlM8UWv0jGX242pcGzSt", "6. Architecture Diagram.pdf", PDF, 226757, DELIV),
            ("1UNngCQuOGOqZ9mZitktZgg39DYN0j4eb", "User Flow Diagram.pdf", PDF, 1338192, DELIV),
        ],
    },
    217: {
        "source_folders": ["1Jm1XhvZCCMEqrVozMMCLQfAmfPxW03bz"],
        "files": [
            ("1Onlc1wDUCc3n3hSTrp1RHzltgupPexN4", "User Flow Diagram.pdf", PDF, 1136287, ""),
            ("1aIGfi9aG7Gjlw4XFNUL5zfRXgZl1cDjhFQGNt1WCF0s", "Excel Tool Transformation - Roadmap & Estimate", SHEET, 18880, ""),
            ("1zgIwd7GHRS8PLiKxHN8h7SDLGFk6wbrr", "Recording 2.mp4", MP4, 157839585, ""),
            ("1bGLipJbunocv-T9W7Mnddofvf45BXM5v", "Excel Tool Recording.mp4", MP4, 215980793, ""),
        ],
    },
    218: {
        "source_folders": ["1xbLaJIrp1Nhkog3QxmmJY7C0Ye2X9HS9"],
        "files": [
            ("1El_uwCtoMcqyxwPJQli38VyhAYOMgachh2UTsUaaQYw", "Mowgo Mobile App Revamp", DOC, 21979, ""),
            ("1iJ7ld1x7y3_wQuQTsSnjLdsJhvZQ8nKP", "Recording.mp4", MP4, 77184337, ""),
        ],
    },
    219: {
        "source_folders": ["1H0HeRzJSfLHiJtvROraTPaEliPJsYt4b"],
        "files": [
            ("1mns38XBzco53LlkdqNdj9-FIv_TTQzCXHVYbaoHWMis", "Pausitive Health Application | Mobile App Development - Roadmap & Estimate", SHEET, 44856, ""),
            ("1LespoFwPv3dTHNSgnL6fix2lIGIiYV2cHRLBzX1qeMw", "ALTERNATIVE: AI-First Model", DOC, 6123, ""),
            ("12zdrK22SUWX9T55sYZDywRcFz2YZfQOH6ayIc16TA1w", "MVP Features", DOC, 4372, ""),
            ("1qSxlHtIHc4gzd8eFOixWfPAghJXszE9F", "Discovery Recording1.mov", MOV, 49872139, ""),
            ("13i5mYdRCI0LOdtMmt50PTI6F7vytm7_M", "pausitive health - Project Overview.pdf", PDF, 116530, ""),
        ],
    },
    220: {
        "source_folders": ["1LBNqiOxU1V9GNhSGKp7Q5hs5CD_JSaBy"],
        "files": [
            ("1iog3_BUZ8F36AZwA1QXr9f18jGF2h76s", "MindMapping.pdf", PDF, 613071, ""),
            ("1V6biOaQsVDG941qf0TSvq7nvAU5mpCAULd8WchBemPE", "Open-Source Intelligence (OSINT) Software - Roadmap & Estimate", SHEET, 28168, ""),
            ("1uavV_J3odvp3qlThivnM_gf3wFRm2Gsw", "Scope of Work/Requirements.pdf", PDF, 74748, ""),
        ],
    },
    221: {
        "source_folders": ["1jnuQcPfBe66x6SGgNb6RhQGoPNr8Grxn"],
        "files": [
            ("1u0jf7aIEzHlyg_5sOcic-GcA81w5DvjYssyBHI1dOlQ", "AI-driven Retrieval-Augmented Generation (RAG) - Proposal Document", DOC, 6159839, ""),
            ("1nminwVnKXVjH-zbmgxcjlPw2hOmhDB9Vikx46MHdoNc", "AI-driven Retrieval-Augmented Generation (RAG) - Solution Document", DOC, 324816, ""),
            ("1rwr59eWx57ytxOIgofhXEMUMPCynalE_", "AI-driven Retrieval-Augmented Generation (RAG) (Diagrams).pdf", PDF, 887097, ""),
            ("1BvMIPv7vnoGNtlEN1ia2IA2iIuf3QGx8", "Recording.mp4", MP4, 450160558, ""),
        ],
    },
}
