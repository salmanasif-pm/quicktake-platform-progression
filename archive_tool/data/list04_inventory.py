"""
Real Drive inventory for the 9 remaining List 04 cards, gathered read-only.

Recorded so the shipped classifier can be run over genuine data (and re-run
later) without re-listing every source folder. Each entry is
(file_id, name, mimeType, size_bytes, containing_folder_name); a containing
folder name of "" means the file sat at the top level of the card's linked
folder.
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
PDF = "application/pdf"
MP4 = "video/mp4"
GVID = "application/vnd.google-apps.vid"
DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
XLSM = "application/vnd.ms-excel.sheet.macroenabled.12"
ZIP = "application/x-zip-compressed"

# card idShort -> {"folders": [...], "files": [...], "note": str}
INVENTORY = {
    295: {
        "source_folders": ["1UX9a6irjn_Iv6347OoukophBnd6VbzPS"],
        "files": [
            ("1ATomNzck_qO5FDCDHJLSFZbeWM3oqzxFjwIDdR0d5fI", "Stephanie - Questions ", DOC, 8306, ""),
            ("19GZZI1P3IT8BdM66ZTiVVCTdmr0-248E", "Solution Call.mp4", MP4, 284314759, ""),
            ("1KAN2daIkmcZaeYuKKjZ7KjdNyADsYHWNzrWW02ub_-8", "Copy of Requirement", DOC, 5706, ""),
            ("1FRoNMQb7ykDFKAo2QPk5ypYjjRC2cHS8", "Copy of Intro call.mp4", MP4, 254556717, ""),
            ("1fc0h8LYoIlYfMu-UBkGdaUvWaTp1FcOE", "Copy of Copy of Campus Weekly Activity Report 2025.xlsx", XLSX, 15798, ""),
            ("1FJcbmAx2J_-qPAKwJGSkkqARBaArtWvY_6-0NmLcgO4", "Copy of Requirement doc for client", DOC, 2129, ""),
            ("1mNItLPxc5hmjn9PL-MvomYtS3BXuqAPQ", "Copy of Educator Feedback Summary Pain points.docx", DOCX, 37308, ""),
            ("14qJza1Vyo4JdyDvXvhHcy0hkuckwiFpjOU25_JIIruo", "Copy of Feedback", DOC, 2272, ""),
            ("1hFNP_MP1JKrJtcBX-AvKIDMvfGjD9oWi", "Copy of TitleTrack_Software_Spec_Phase5 Stephanie Krol.docx (1).pdf", PDF, 195825, ""),
            ("110aAkaHKBySqdykuoUjvLd_XyUfzedq3cEPufhRcf1U", "Copy of Readme", DOC, 1024, ""),
            ("1oc_9MgdnQawdNELxmgVxkVnCqzCg1bi8", "Copy of 19th Aug call.mp4", MP4, 285691309, ""),
            ("16E9cYwnH8JT1CXt2jg2bdUwWz971hsZp", "Copy of accreditation check off sheet.docx", DOCX, 351762, ""),
            ("1DPJA_vhTcPi5JkXW_dDAXbVDwo7o9i7Z", "Copy of Education Specialist OSE Report Checklist.docx", DOCX, 395158, ""),
            ("1ApwyNijaeGWrojGie950oiK6QWlMVd5r05A8FKjEeU4", "Requirement", DOC, 5434, ""),
            ("1GSIAENrVW0j5Mv2ANv7Y10A53wIxej-R", "accreditation check off sheet.docx", DOCX, 351762, ""),
            ("1h_JuEJC3lfnHn1p6GbSKnL0HOtYvksHU", "Copy of Campus Weekly Activity Report 2025.xlsx", XLSX, 15798, ""),
            ("1QamEVz3VdbiTNHQwhZVIJBUG6Z4ZvVoC", "Education Specialist OSE Report Checklist.docx", DOCX, 395158, ""),
            ("1fAulKSsAttuHnbGr8GfCza_C6TSA5IEh", "Educator Feedback Summary Pain points.docx", DOCX, 37308, ""),
            ("1JTrUyI1JV453cfv-HIw0mO6gvJb6ZsGm", "19th Aug call.mp4", MP4, 285691309, ""),
            ("1QXDugqlF8MynBi5KL4yhC5gajyGqRXk-cUzFzx4syog", "Readme", DOC, 1024, ""),
            ("1Xa7Guid24hRd5oj_I-zg9HPrODz3TZYY", "TitleTrack_Software_Spec_Phase5 Stephanie Krol.docx (1).pdf", PDF, 195825, ""),
            ("1tpIPG5Ztwex5x6-TXmoGbqQMiHWxTnsPiw1GJtY-EQI", "Requirement doc for client", DOC, 1968, ""),
            ("1uTod_4vDTS3kQuj4dbSsmtsn3Fwjn_WXMsAotYWpi1o", "Feedback", DOC, 2278, ""),
            ("1dtS_f0xY-De5M-Phug5H0nC8rnjDNQge", "Intro call.mp4", MP4, 254556717, ""),
            # subfolder: Latest Updates (2nd June 2026)
            ("1L6enqI64O_trMKKNE-vIW9X3Ky7Tv-x0", "EduCommand AI Level 1 School Review Overview FINAL.pdf", PDF, 149280, "Latest Updates (2nd June 2026)"),
            ("1KTYMj3S_VeUvOwu3ZAp1r4x7GjtNUS5-", "EduCommand AI Level 2 Funding Proposal Brief FINAL.pdf", PDF, 173578, "Latest Updates (2nd June 2026)"),
            ("1QTeqOGi6uAtJm8_M86MIoJ06K6hi_fhn", "EduCommand AI Level 3 Beta Architecture Materials FINAL.pdf", PDF, 164775, "Latest Updates (2nd June 2026)"),
            # subfolder: BA Team Deliverables
            ("1mrOWA8-D2TdQZRWOr2SZPFQfR0Lz2MebOKD7A38zq3s", "EduCommand AI | GoHighLevel-Based Institutional Command Platform - Roadmap & Estimate", SHEET, 50737, "BA Team Deliverables"),
        ],
    },
    448: {
        "source_folders": ["1dQJ15sNEltdW-LH-casuKG7ltchqrw5G"],
        "files": [
            ("1dIRo2QNMQHQeWdBjmc6D5CUGpRQeGwH0BUPBE9nO2Xw", "Questions and Answers - May 14, 2026", DOC, 12686, ""),
            ("1FosLAdGaQL2X2ZrKBt3PF09qO43iXIG50HdyCsGSVG8", "Care Plans for Life | Roadmap & Estimations", SHEET, 23431, ""),
            ("1gqghr7RpwdJ5GX7qpDAvMxcOkHaO9aP-VhseXEMwZeQ", "Meeting Recording", DOC, 1024, ""),
            ("1Nwmp_ZjwvX5m4pljtd1C5Yt_tIXO2_kV", "Care_Plans_for_Life_BA_Scope_Estimate_Workbook.xlsm", XLSM, 78292, "BA - DRAFT"),
        ],
    },
    452: {
        "source_folders": ["11zbFhO5DOk3rjxY4EBbOB_oH4vBiQcwc"],
        "files": [
            ("1Buv8FvAl4Lu9qLl4e2PnejRHABArX36lYAS3fHC9I8U", "Procore Lite Custom Version - Roadmap & Estimations", SHEET, 32857, ""),
            ("1xF93We3FCqZ_CrMrokKzzhlxTG1KgeNJ", "Kyle __ PureLogics - May 22 2026 (2).mp4", MP4, 166883797, ""),
        ],
    },
    447: {
        "source_folders": ["1PbqZA5RrXIOHn2Qc93gYlODWm-4mCAAQ"],
        "files": [
            ("1cCESJeMyG_AexRdUmTVh07B-vpKf09G9y8Bv3Q92Ils", "Great Kids Mobile App | Roadmap & Estimations", SHEET, 34323, ""),
            ("1_XXjWDbTweiEug0Iplo0jVjmBdKueS3j", "Copy of Great Kids, Inc. __ PureLogics - Apr 27 2026.mp4", MP4, 241990930, ""),
        ],
    },
    442: {
        "source_folders": ["13MGh1EZtDHs2rpHJG-7Xt79DoC_32tKj"],
        "files": [
            ("1JqP5jPF6jnIIb31Ykm2rn1UzK6OCIlgz6kYIgGcjXKQ", "Brightstead AI Agents - Roadmap & Estimate", SHEET, 29329, ""),
            ("17x_1pBcpFDLA_drx-kpv5dFLSxtvd8YYRQDbQlz5lvc", "Copy of ORG BRSTD AI Army- Roadmap and estimates", SHEET, 7030, ""),
            ("1Kr-NFst07jYwwnslW9Y6QWvaFHBz_srf", "Prekickoff - Brightstead Tech.mp4", MP4, 88416974, ""),
            ("1HsHMcVPLG7dwpC-o2p_TRtlApYQR05Z1", "BRSTD Agent Army Build.docx", DOCX, 70591, ""),
            ("16VfinxB9M31oli7t30PR1MlFsW7WSkoFMqeawreOFUo", "GrantAI Production readiness - Engineering Findings", DOC, 4416, ""),
            ("1SkRu7MyEOuiDRpAPiqWVMAcQFtpz7eZZ", "Brightstead_Phase2_L2_Qualification_Outreach_Roadmap.xlsx", XLSX, 24080, "BA DRAFT"),
            ("1r6ND44nOGaZ4ihXIvdZLwEcYo5ON7xfu", "Brightstead_Technologies_Phase_2_Jira_Tickets.pdf", PDF, 492792, "BA DRAFT"),
        ],
    },
    119: {
        "source_folders": ["1sBBnl4pOUTjCZvFb0jHYzoxW-8CGCdCQ"],
        "files": [
            ("1TdhH-cvgFrC_McPsKtVHxV1MSGs83zlB7x7A_HprQ_E", "video1015049405", GVID, 258215281, ""),
            ("1YbP2o0yzGV0ClMbBV3fyl1GcTskPrsioklfh7DS9tL8", "Questions to ask the bank / local partners ", DOC, 4708, ""),
            ("1a34hgBk876jTtLbQEKByKRMIWe0_OMpqmwyTBLMBeFQ", "Lumyn <> PureLogics - Feedback Discussion - March 30", DOC, 18059, ""),
            ("1AzSVaWCTNyHyBHULpZZA22THJCV9XDWu", "RainCheck Overview.pdf", PDF, 123593, ""),
            ("1IkSmKORAou8BqyVml0g4pwH06flYa835", "Lumyn __ PureLogics - Feedback Discussion  - Mar 30 2026.mp4", MP4, 291215394, ""),
            ("11Pc2XYmxqYzBYAgnGGY4U94MRXM9muDP", "video1015049405.mp4", MP4, 258214712, ""),
            ("1FDvrDHIA-VgyXcrQ5NauQsPpZy6kX4Ft", "FOR SOHAIB-3.5.2026.pdf", PDF, 112496, ""),
            ("18HT5WNO0lmgPiyiZ0KFLk8HMfaU8u4kZ", "Lumyn - USA-Ghana Remittance & Stability Layer 02102026.pdf", PDF, 168156, ""),
            ("1p8p0cdgBplemhl0i9fxobRShbATkE7MUZZKtd2BuomU", "Notes & Understanding", DOC, 6153, ""),
            # subfolder: Project "RainCheck"
            ("1rPcLrbTWjQm2ukIY7yN6M4C7uGy8ALzz", "welcome-hub-main.zip", ZIP, 449831, 'Project "RainCheck"'),
            ("1cIA318p-mUeSugGDTQASR583MDhlA89K", "Lumyn __ PureLogics - Feedback Discussion  - Mar 30 2026.mp4", MP4, 291215394, 'Project "RainCheck"'),
            # directly linked in the card description, external owner
            ("1FRwMUBvlokGDeig64w-pnn5M0Dj1Bg26HqmITkypFF0", "FOR SOHAIB-3.5.2026", DOC, 24851, ""),
        ],
    },
    436: {
        "source_folders": ["1M1RAb6C2eRod3zLG4FQuZADulHHlMGF_"],
        "files": [
            ("1HWDYA4Ptdpy0Be-8vrYKJDZx_ZEnXdiU", "Copy of Brian Kinney __ PureLogics - Mar 26 2026.mp4", MP4, 279928722, ""),
            ("13ewOD14sz1K3Y2tOMKuxOWBBJYbmJ7xsrLU-Ho5pRvg", "Brian Kinney <> PureLogics - March 26", DOC, 16320, ""),
        ],
    },
    116: {
        "source_folders": ["1ZP1_6Rhnbd40CSrWGy7z2OEousTNAY6H"],
        "files": [
            ("14rRZIlpPSApfDB1Qk7hwE7HOnwFQCm0jE_7I0MLSO0w", "Deliverables", DOC, 1024, ""),
            ("1XMFVapsM-H0ddd6IwtW_ECezm3077o61", "PureLogics Mail - Fwd_ Keebeck _ PureLogics follow up.pdf", PDF, 862142, ""),
            ("1xQC51Fd9ZDx8S8CsCMt-rWBh2w5YuazFqB1Sx67ZfBM", "Keebeck Unified Client Portal - Platform Access Questions", DOC, 156287, ""),
            ("1CpTk-P1iPrGAxbEvnqWXOwS8YEPzbOFr", "Engineering - Keebeck.mp4", MP4, 556697822, ""),
        ],
    },
    458: {
        "source_folders": ["1Z7cT9Gkc9xjcR546q7NXGallISTAnHb2"],
        "files": [],
        "error": ("folder:1Z7cT9Gkc9xjcR546q7NXGallISTAnHb2",
                  "Requested entity was not found (deleted or access revoked)"),
    },
}
