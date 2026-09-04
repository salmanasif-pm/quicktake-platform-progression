"""
Real Drive inventory for List 07 (`On Hold`) batch 07j: cards 301 - 405
(the list jumps from 313 to 393; there is no 311 or 403 on it).

Every card here links exactly one folder, and every folder is named
`Engineering`. The grouped `parentId = ... or ...` listing came back EMPTY for
all three chunks - the `or`-query trap - so all 24 folders were probed one at a
time with `get_file_metadata` first: six are gone, eighteen resolve. The
eighteen live ones were then listed in two grouped queries, both non-empty.

  DEAD_FOLDERS   cards 303, 397, 398, 399, 402 and 404.
  EMPTY_FOLDERS  cards 395, 396, 400, 401 and 405 - all readable, all with no
                 children. With no live card-level file links either, those
                 five plus the six dead-folder cards archive as a card.md and
                 nothing else: eleven of the twenty-four.
  DEAD_FILES     nine card-level file links answer "Requested entity was not
                 found"; recorded per card in `errors`.
  NOT_WALKED     card 301's `DB Credentials` subfolder is deliberately not
                 walked - a credentials store, not a deliverable - and card
                 393's three level-2 subfolders are past the one-level rule.

Card 393 (`Project Take Over - Himiko`) is the whole batch's weight: a
handover record with six subfolders (five walked, one - `5th Feb - Handover
details from Carnellia` - holding only further subfolders). `mongodb.zip` in
`2nd Feb Meeting` is a 56 MB database handoff dump; the classifier skips it
as a non-document type, which is the right outcome for an archive.
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
PDF = "application/pdf"
MP4 = "video/mp4"
JPEG = "image/jpeg"
ZIP = "application/zip"

GONE = "Requested entity was not found (deleted or access revoked)"

FEB9 = "9th Feb - Himiko & Erick Meeting"
REBUILD = "Rebuild & Valid Execution Plan"
FEB2 = "2nd Feb Meeting"
JAN31 = "more details - 31 jan"
SHOTS = "Screenshots"

INVENTORY = {
    301: {
        "source_folders": ["1s5n2PcK8bwxr5MbfY-h4fMLG5sQCop8w"],
        "files": [
            ("1LtFE-hI9TQxtp4O4V1zYRXhseP1RG-XoTCJSMcYNpIw", "Like Car Care - Features Coverage Document", DOC, 1481889, ""),
            ("1oimf0VXYbFgXkn1ABhETFvvBXO2rJYH2eKgZqbdcAco", "LinkCarCare - Web App Enhancement", DOC, 1488808, ""),
            ("1HjTfvnNmFEsU05YNukKAaT8RlF6PWWclu0BI1KOCxoM", "LinkCarCare - Web App Enhancement - Updated", DOC, 1479108, ""),
            ("1TbVlDpG3xyjw4W-zDoFLRR-TBR8zaExG", "video1262814218.mp4", MP4, 61794644, ""),
            ("1oDiaW1HOr6v-rbGAzjEgsViUwO2Dib8mYkkHIlkYi38", "Notes", DOC, 6193, ""),
            ("1dUou6Dj5aq2cl5MKYgX5T5738_s4hflv", "MYRON_video1888203803.mp4", MP4, 114099395, ""),
        ],
    },
    302: {
        "source_folders": ["1ZPb76HbbYYTh4cM6JLnoWEg-1NJN8EgT"],
        "files": [
            ("18RRDQo5ScF9by8z1bXudomx8FvBCdCZK", "video1593465727.mp4", MP4, 224791885, ""),
            ("1L48N60poWGK1MQnFpcdoKjpp-uejZv5TBsCzYIWwez8", "Chefee Robotics (AI Ingredient Evaluating Platform) - Roadmap & Estimate", SHEET, 19665, ""),
            ("1GmBHvg_GKxqO-P9O5gt0dImXfZ6b4f4dQAIfv_luWWg", "Notes", DOC, 8446, ""),
            ("1xspp9knYDD-hMWdcrbEPTd1hZE3wrj-m", "Ingredient_Datasheet_Filled_chefee.pdf", PDF, 18962, ""),
        ],
        "errors": [("file:1VS3zhrhxu3U-utwOoyCijaPGmCY-RiOR", GONE)],
    },
    303: {
        "source_folders": [],
        "files": [],
        "errors": [
            ("folder:1XHSmkgc1JQNlVda7aVVaUedzTzrZHO12", GONE),
            ("file:1K14bRE_5LuBHBMi2Bt5oQ9vGS8ZD21kLxc7DAS_cEeA", GONE),
            ("file:1_Ih7VWHMAakB10yv61c_nKWmP6nCxDjm", GONE),
        ],
    },
    304: {
        "source_folders": ["1c-7QTVz76dKEmseAmHXSOmBbZcGQzbVg"],
        "files": [
            ("1qWLqcBgrB59HxtHb4Orta4bEyOqTBqMi", "Trimmed - 1.mp4", MP4, 122089122, ""),
            ("1i3c1v_UOvo6Vk5quePADHsIjbdA4Wk0a", "Trimmed - 2nd .mp4", MP4, 86478113, ""),
            ("1_MSLl_QBYsGjmp_APqDcqma0_fA6OpHf", "Extracted pages from 122023_Final_041423.pdf", PDF, 1663142, ""),
            ("1L_wwqQ95jHpUlKLEtj1xNsDJO1kQEg7wwmsEdQz3n5Q", "Read Me", DOC, 1024, ""),
            ("1Y-GNLbWi_VTcBAtJWmvDMrHuyTJ3O6DR_49n2PkLXNI", "Requirements", DOC, 7444, ""),
        ],
        "errors": [("file:1Z55qrYzJM3lZaCXjAEqNv5lhjI9r3gVR", GONE)],
    },
    305: {
        "source_folders": ["1XKFO21TXQtA4CCIdeokIDj0_slUi8EXO"],
        "files": [
            ("1lTMPf_n2nNxH9IC0c6cv7jAnYAkP7Mfi", "Follow up meeting.mp4", MP4, 141388030, ""),
            ("1W-w7fNNLxqadSj38Ko2IJQ915ivifg4O", "Intro call.mp4", MP4, 197761817, ""),
            ("1n7cjeEYhnBfFvW-FIJXogJ9ALRQL3gP2qJPd6eEMOjQ", " Solution Document - Concreate", DOC, 1676349, ""),
            ("1HHsJ9komQIIT8C28vQpNFgr-k7JqziIceuuQ_S_P-YE", "ROI plan", DOC, 19747, ""),
            ("1kKxLMUI1WBVPZtpULKqYglUEY6dOtei_lT58CIqPta8", "Industry Comparison", DOC, 3627, ""),
            ("1Z5ehYmyPN6dmw5uMJjccYTmNxxTOHPP_Qg0QKqVcvwA", "Read Me", DOC, 4267, ""),
            ("1ig_vovAAXyL-NE2e6med2XguDet4CtcmNV5jGAbNKxU", "Follow up meeting notes", DOC, 3263, ""),
            ("1tHMGOsF_gtlG_n3tCbvMP-JwkjIehA56Eq8hub1SAUU", "Notes ", DOC, 5563, ""),
        ],
        "errors": [("file:1NKAHJ1w1ietVhOOViy-MEoP1Hf-kwFjW", GONE)],
    },
    306: {
        "source_folders": ["1AYJM6PV3N2y1iy8xAwxNEy2wsppg9VRS"],
        "files": [
            ("1iDuPvwdun9IBYubr6Y7oKq3DGYufkKQ9_an4e37TKtg", "Healthcare-focused event platform - Roadmap & Estimate", SHEET, 29306, ""),
            ("1WV4tc36_QWUGgXB5Cs7GVe4OoZ6bBFvlHIRxVZ7EAU8", "Healthcare-focused Event Platform - Solution Document", DOC, 1476539, ""),
            ("1ZvdyhPfGMWoSuhu0jTJ2wolOeY23jWYC", "Trimmed - call 1.mp4", MP4, 122065982, ""),
            ("1_PMmtxrma5QlDfiCo79UC2Mt60E-FJFbcV6ZO4b5IYo", "Notes 20th Aug", DOC, 6238, ""),
        ],
    },
    307: {
        "source_folders": ["1yS9mSS1LSW4LbzG45dHUdF9elyclGpgL"],
        "files": [
            ("1DbIEdKMEnP0djdmeRMZmy_d64ND9TTU0", "Intro call.mp4", MP4, 179501444, ""),
            ("1vwsWLn8_PVGD0MWR2YsguFUpKL_rooTorY4ancg8b2o", "Multi AI-Agent System Implementation - Understanding Document", DOC, 1475591, ""),
            ("1fhuo7QxUhCxulOrhFz7E80oeVjjAstO5qYvJtSHLejQ", "Notes & Requirements", DOC, 8565, ""),
        ],
        "errors": [("file:1m1bGTpXOwMKwjGSv7IAlYrTp7UP7qVPE", GONE)],
    },
    308: {
        "source_folders": ["1g-ZdJAFiTGqEO6Ggc3nhdWQkiRgahNOt"],
        "files": [
            ("1YM92rQCf1OCG3_kKkAgXan2YH8M627eI3OrPZXwhTlU", "N8N Project Automation - Roadmap & Estimate", SHEET, 29306, ""),
            ("15Gsk0rXzoEbmaGEcLvOsmDjZzYYHp7cc", "Trimmed call - Rob.mp4", MP4, 71497109, ""),
            ("1muOuiGQzwk0GsKgRTGOfnbV_Vw0eIkdX-ZyQuN_ZMEU", "Notes", DOC, 10004, ""),
        ],
        "errors": [("file:1kmeyDaDH_VIsU1vq7vRqXO9eeAFiN8S9", GONE)],
    },
    309: {
        "source_folders": ["1LGXBuWTRZtInOIAcoXm4XI-biYhE2IER"],
        "files": [
            ("1N13Fpy90yhboK8IfD5cF12LcHl6RvO5WWX0CyVfiP_k", "Vision-Language Model Solution for EEG Analysis - Understanding Document", DOC, 5314262, ""),
            ("1mClVJBtdNBRJX-_0QPhGcO5DQloI4oywMOKmjq8uu3w", "Notes from 20th NOV", DOC, 8158, ""),
            ("1BuWwKcfdEtrWOS2wKfGydZjHiZwjxT2z", "20th Nov - Trimmed - call with shari.mp4", MP4, 146787324, ""),
            ("1XcfRM6jnAnQo1szFoOu0g5X93Ft-u9OL", "video1263326694.mp4", MP4, 171317672, ""),
            ("1k2br0D3Dw5L2Y0V17scDZSbiFB73nF14B8pw1HzHq5E", "Notes", DOC, 1024, ""),
        ],
    },
    310: {
        "source_folders": ["1sdmOVrZV3ca3nMnNH3YFhxCLJXeNi2NM"],
        "files": [
            ("1Yv3gP_qvdzsAFCrFTM0PJpsjTXGrT1vT1rpf6VRC1T8", "Notes", DOC, 5231, ""),
            ("1x98r9Sf6tTZGv_01obd75xgjD9jDQr9J", "video1545130625.mp4", MP4, 171296992, ""),
        ],
    },
    312: {
        "source_folders": ["1fq8z16hsZvzS3ilCR2Ffd9WRVabFNfxd"],
        "files": [
            ("1pr1DHZVfloUXljkcJBXmCL7BoxBxDo4FzRoQ6mtJr5A", "RDL Architects Checklist Development - Roadmap & Estimate", SHEET, 29397, ""),
            ("1Kfmj7W4d4UJW5jkWvHqJztouMUYo72qcPVAJ-y_IWUE", "Notes ", DOC, 7064, ""),
            ("1GoA-mVREbJaVdg6jCG8xh9K_pV85lbPW", "Intro call.mp4", MP4, 193951320, ""),
        ],
    },
    313: {
        "source_folders": ["1qzw-drO7TfKj1_QYP7FruHcSQgOqb2q9"],
        "files": [
            ("13wJ5UbECAUfyuAT5SJYbpCq0GTCJtjZ_8giN4jMXbuY", "Copy of ProjectName - Solution Document", DOC, 1476538, ""),
            ("11S7n9VLBZpzST5X1_FjtZLTcV_0esM2Er6WhnP8X050", "Requirements", DOC, 7730, ""),
            ("15z1LQtAXKCi1oRR5MkdfqEk4xDX2GpJRQ3dcrL_2EaY", "Untitled document", DOC, 6328, ""),
        ],
    },
    393: {
        "source_folders": ["1WdSmiZOYMAwazXGqNJQ4qtEQ0Sq21eH3"],
        "files": [
            ("1TdWevHEE-q_nPNjwFjrKcbFiMtn1GtzV6ivzu8poO_g", "PartnerPro Application - Roadmap & Estimate", SHEET, 18510, ""),
            ("1SZZzVlHQ8bQ_Yd_MzA3c9bhNLomLa-HOeUIetBIyUP0", "Himiko Project - Project Takeover Plan", DOC, 5056, ""),
            ("1G_IXhCB38rm9a7R9zZOaGv9HN1qYj6LybFA7hwIW-4k", "Carnelllia - Understanding Document", DOC, 5300825, ""),
            ("1rIrK0cxMmDFmEogRLSEEZkNLFqqshCbeBhHP-8RPt2Y", "BOT NOTES", DOC, 9424, ""),
            ("19iVEvEe1fwp1eXAlW4CNimudr9POzZ2DLOeL3FLTUKg", "Requriements", DOC, 6447, ""),
            ("1MWOrvGdjX7aSTUvnlSHS-HnfHrVw7LLi", "Carnelllia_video1927371929.mp4", MP4, 39525449, ""),
            ("1HXd1HTalDHMNGleHDIR6CooEkksGMR5R", "Meeting w_AYRE Demo - 2026_02_10 11_59 EST - Recording.mp4", MP4, 1031883821, FEB9),
            ("1G2TmGwUSWYCi8WBHAvHvnkExolk9y0t9", "Meeting w_AYRE Demo - 2026_02_10 11_59 EST - Notes by Gemini.pdf", PDF, 140786, FEB9),
            ("1GpKxKFkecdYgbS_mqGyghqP2nKxvL_lGQ5cLep8Un34", "Access to PARTNER PRO DEMO", DOC, 1024, FEB9),
            ("1qZP67mKYb1sNX87op3L86ttYrh82tjF06YiXRQzZRa4", "Notes from our 9th Meeting", DOC, 4261, FEB9),
            ("1zvn2xrPbeB71SVIAESGXBzpV28R_4eBTwbFVRoPEBMg", "IWriteOffer - Feature Roadmap", DOC, 9508, REBUILD),
            ("1UjUc6tflDpdqQtrabFYjW9Dskwzg5o7ioySkofnrR-o", "IWriteOffer - Engineer-Led Discovery Questions (Internal)", DOC, 6921, REBUILD),
            ("1Ru4Hrx7B_cySRr1NJrfSr5an5U0mjpQ9gB38SstshWw", "Rebuild & Validation Execution Plan ", DOC, 9324, REBUILD),
            ("19IZAaBZybXM3zj_LtHyTDVcKN82xHQaV1YB5qmjfx5k", "Rebuild & Validation Execution Plan - Himiko", DOC, 5187187, REBUILD),
            ("1F0lISgI77LnTi2-lcYxfdWN2b-ImVnnjl9MNIX9Utg4", "PROJECT MIGRATION & TAKEOVER", DOC, 10045, FEB2),
            ("16lukmxPX78V0sp_bRCYIKpXZei9MLjyu8x6yLeXBR0Y", "PROJECT MIGRATION & TAKEOVER", DOC, 11021, FEB2),
            ("19rnCTWqE7rT5cOkT4EHMqcfSHn6RZw3DZnV-AWHA6ps", "Notes from 2nd Feb Call", DOC, 8033, FEB2),
            ("1MJswUWOwcSs1oHWZ0hHgC1mwU0WfX8O2", "Technical Migration call.mp4", MP4, 201224499, FEB2),
            ("1TkMK9eUjhrefrgLvwoYTPoz4RUxJSogK", "mongodb.zip", ZIP, 56214464, FEB2),
            ("1ZOYEQ2FlhWU249-YCoHlCb9d5XewNz4Q", "Our Understanding_ AYRE.pdf", PDF, 74657, JAN31),
            ("1frJX0WjKGmGwO3cyCrF_bry0IyklDINlsn8xi_gTVys", "Monday Migration Kickoff & Project Handover", DOC, 3060, JAN31),
            ("1EpluOZI4m-z7BO9U62TfmGzR3_yheTuA", "WhatsApp Image 2026-01-29 at 08.32.59.jpeg", JPEG, 121045, SHOTS),
            ("1ZDZt6YLfirFZsemw4cZWYHUGRXkEkb_n", "WhatsApp Image 2026-01-29 at 08.33.05.jpeg", JPEG, 103351, SHOTS),
            ("1AUfusyXi1z84qGgpFfArzqWFXhRQosk3", "WhatsApp Image 2026-01-29 at 08.54.23.jpeg", JPEG, 193719, SHOTS),
            ("1_Mhpi23ZtLwKCEzLHZomltiaBCUT4UJ2", "WhatsApp Image 2026-01-30 at 07.39.08.jpeg", JPEG, 104018, SHOTS),
            ("1WyFu0xDpkizfiNNfBlgcKbNBy9xmjBj_", "WhatsApp Image 2026-01-30 at 08.07.23.jpeg", JPEG, 185619, SHOTS),
            ("1WhnjGCF-yn_VtWVKVyHKtV0bI9_x_rVX", "WhatsApp Image 2026-01-30 at 08.42.15 (1).jpeg", JPEG, 103362, SHOTS),
            ("18koptrUWQRbLqpSJ6tK9WRSg6T0m_HMQ", "WhatsApp Image 2026-01-30 at 08.42.19 (1).jpeg", JPEG, 103722, SHOTS),
            ("1N9x8zW0igIKCdlXolbjRuIXnI3Qz_7i_", "WhatsApp Image 2026-01-30 at 08.42.22 (1).jpeg", JPEG, 100564, SHOTS),
            ("1sLzBKlWKOHI7eWPsnfitr4iCv_pHqOnk", "WhatsApp Image 2026-01-30 at 09.00.51.jpeg", JPEG, 99494, SHOTS),
            ("1BICD8Z0YZAAfPYn2FjM6AZewC0m6pqEw", "WhatsApp Image 2026-01-30 at 09.00.55.jpeg", JPEG, 97776, SHOTS),
        ],
    },
    394: {
        "source_folders": ["1t64HUgm7FQX-nEII6bzZcmbLNiPj6g32"],
        "files": [
            ("1pjd3nGY8RREMylxW6MizwaWHTdzl3qFk", "Discovery.mp4", MP4, 235904949, ""),
            ("1d8nhj0EfEKWfn24RhyeIUMyelTl8dKN5Thw0KZxIMZA", "Health & Wellness App - Roadmap & Estimate", SHEET, 23983, ""),
            ("1Iwo2pv7uas-FqG8ajqoS0g9AdjkYRRYNgqWbfg_v698", "Competitor Analysis", DOC, 9464, ""),
            ("1CGkny0cnLMo1VLgSFKt5JAsu9bAC_2JLDJHcWcQI8A8", "Notes & Requirements 11 Feb Call", DOC, 4612, ""),
        ],
        "errors": [("file:1JflsxRcEuO9XvL_1V2icreU0cLeIijlO", GONE)],
    },
    395: {"source_folders": ["13zFrIbPcFuBl3Xf2cqoTz2SthIrXIVqs"], "files": []},
    396: {"source_folders": ["1mTJKtJc5PdE4zC7awU7JiWXapf2H8BlL"], "files": []},
    397: {"source_folders": [], "files": [],
          "errors": [("folder:1I-UIg9_romFEE6WJMqtjpCoGqctRMkKn", GONE)]},
    398: {"source_folders": [], "files": [],
          "errors": [("folder:11e7QgyHF8bFV3So2NrRftoVKXqhpX3KG", GONE)]},
    399: {"source_folders": [], "files": [],
          "errors": [("folder:1lXuF0ErlWMK-xKMwXte1KljL1e7m_U0z", GONE),
                     ("file:1A-pQfVLQk_11kVqAWo9XBqKTh0DDSphx", GONE)]},
    400: {"source_folders": ["1_zGyI5KMikCo9FCh3Tu7PM964nertAQz"], "files": []},
    401: {"source_folders": ["1WFnQOasJslE1vuDpvUQDpyN3bej0IGUW"], "files": []},
    402: {"source_folders": [], "files": [],
          "errors": [("folder:1CccDPyMW47HFYWIka55fk0gjDWKvGnlu", GONE)]},
    404: {"source_folders": [], "files": [],
          "errors": [("folder:1CQPBlolnkdDvVlCpcKZ17ncfyTtyV1sW", GONE)]},
    405: {"source_folders": ["10H1QQ8MkZEkYA9KucDDTvkctagDbab7c"], "files": []},
}

DEAD_FOLDERS = {
    303: [("1XHSmkgc1JQNlVda7aVVaUedzTzrZHO12", "Engineering")],
    397: [("1I-UIg9_romFEE6WJMqtjpCoGqctRMkKn", "Engineering")],
    398: [("11e7QgyHF8bFV3So2NrRftoVKXqhpX3KG", "Engineering")],
    399: [("1lXuF0ErlWMK-xKMwXte1KljL1e7m_U0z", "Engineering")],
    402: [("1CccDPyMW47HFYWIka55fk0gjDWKvGnlu", "Engineering")],
    404: [("1CQPBlolnkdDvVlCpcKZ17ncfyTtyV1sW", "Engineering")],
}

EMPTY_FOLDERS = {
    395: [("13zFrIbPcFuBl3Xf2cqoTz2SthIrXIVqs", "Engineering")],
    396: [("1mTJKtJc5PdE4zC7awU7JiWXapf2H8BlL", "Engineering")],
    400: [("1_zGyI5KMikCo9FCh3Tu7PM964nertAQz", "Engineering")],
    401: [("1WFnQOasJslE1vuDpvUQDpyN3bej0IGUW", "Engineering")],
    405: [("10H1QQ8MkZEkYA9KucDDTvkctagDbab7c", "Engineering")],
}

SUBFOLDERS_TO_WALK = {
    393: [("1idE_AzcRknpNljfVwhja-UdVqLv_TRS_", FEB9),
          ("1UjpCpO4XCqpfoZxIA0Fhtd4iY-vowRnM", "5th Feb - Handover details from Carnellia "),
          ("1QAS8t9PPXOfylJmhXtVFzwxjnAMlWo7K", REBUILD),
          ("1uo69ey3hNKFr6fnkLBisrV2yswKl3ouR", FEB2),
          ("16LRnD6Gwoj7r2ZATapM2Uw8fB3895SrZ", JAN31),
          ("1PJnY0h5nT1avaoq3X9Iu2gwa9eryfYHm", SHOTS)],
}

NOT_WALKED = {
    # A credentials store, deliberately left alone.
    301: [("1GKyvbKtFTcNh0enHUYLjoLNZ8RDHFUgG", "DB Credentials ")],
    # Level 2, past the one-level rule.
    393: [("1yGJHPnZe1y-4uZc6k7QCWz8OOSHjLo98", "5th Feb .../5th Feb Carnellia Meeting"),
          ("1wupjfSQGm5fTF3BAPSjJLZheEw3McAy7", "5th Feb .../App Demo"),
          ("16Qky3Tc8-cHpRW4i1t3J9RwN_2oJmoSA", "5th Feb .../MongoDB Handoff Code")],
}
