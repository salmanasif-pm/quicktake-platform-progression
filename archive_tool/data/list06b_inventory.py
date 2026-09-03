"""
Real Drive inventory for the second List 06 (`Closed Lost`) batch.

Cards 74, 75, 76, 81, 83, 85, 89, 90, 91, 92 and 97.

Four source folders no longer exist (deleted or access revoked), confirmed by
files.get returning "Requested entity was not found" rather than by an empty
listing - an empty listing alone cannot tell the two apart. Cards 83, 91 and
92 have no other source, so they are a `card.md` only; card 76's second
folder is intact. All four are logged in errors.csv.
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
PDF = "application/pdf"
MP4 = "video/mp4"
DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
ZIPC = "application/x-zip-compressed"

GONE = "Requested entity was not found (deleted or access revoked)"

DEAD_FOLDERS = {
    76: ["1NlJY5DwTEQ1ihqZG7bHxRb08KLaksQdu"],
    83: ["1Nw7u0lHRsyV5yig67_L0hoinACvNpRYR"],
    91: ["1mcNfe2Ju_lvof-iRIxUkdPCLVpWPPuIc"],
    92: ["1NA4MQFBzhEaZl7bi6npSmJsFYNNsDZBX"],
}

INVENTORY = {
    74: {
        "source_folders": ["1HsBwfXv2pz9TM3ZYoBjH8jA2reeA6rrj"],
        "files": [
            ("1irDUeCda2nn_s9De8tdecAakyCEUqJL3", "MCP meeting  - Aug 8 2025.mp4", MP4, 76584110, ""),
            ("1C_Hb1n8NwFP9ocgl8WESLzPDooS9Jy_p", "Architecture Diagram.pdf", PDF, 315768, ""),
            ("1GaamMwHOp6Nh_E5XuO0R6iZfLXDu4sLM", "Copy of Tim Miner - Aug 4 2025.mp4", MP4, 68074695, ""),
        ],
    },
    75: {
        "source_folders": ["1SKqV1Sq1oal_w--95XND8FIh6vQNlELA"],
        "files": [
            ("1uYT4QHqUUb3XSd09-MRLw7Il6JM9QWDHcf8-ds1GqkI", "Read Me", DOC, 1024, ""),
            ("1ZZUxwJtWY1PFBKL1vJBEad91yAZi3uxAj_U8up0LQMs", "PWA Application - Julie ", DOC, 3788, ""),
        ],
    },
    76: {
        "source_folders": ["1rZEj5XMlPniI1GASROkVlt9F0BrOdfH2"],
        "files": [
            ("1RdtvGQqENe-llQObPmwrZdUrjNEIYOF0", "14th October - Danny <> PM Meeting ", MP4, 225858017, ""),
            ("1D5LV5KLwV353knCZWqoGrt7S1f-6EaXk", "PureLogics Final FVI Scope - Aug 26 2025.mp4", MP4, 270094097, ""),
            ("16sfPEjMcsMdRLIjGBExMWNoN1-qgh-OlgGMoN3fnU3A", "Canvas Diagram and Description", DOC, 312748, ""),
            ("1hEfpllov5XQMV8mvRz6tGYjSCylXAyEmOyDZOSKSCqc", "MoMs", DOC, 44526, ""),
            ("19uV5C5ErCBrxCvjA5s24WO4ZKF1hLZlg", "Meeting - 12th Aug 2025.mp4", MP4, 39728168, ""),
            ("1RUOpsyBdwiTd6xnx-BvB4pk4QauJzitT_g0jmys4TlE", "Read Me", DOC, 1024, ""),
            ("1YQnL3OVHlvWMbe7TBW0qBubLNoTadfqbf2ghaPJkU8A", "MVP - 3os ", DOC, 5441, ""),
            ("1cKYTmbDu6P4PBEQK8U3kvaoc3TBlW_vz_ANnFCAdS7g", "Link to Recording", DOC, 1024, ""),
            ("1b2BQ0Os5EJmSK1aYzTrOkQwzWPwsHoIIy6ImP0UOQ3w", "MVP - 3os ", DOC, 5441, ""),
            ("1QeWBNcefjcMUifujq2rZ8fbmKmroGsfytwqnAW-iib0", "\U0001f527 Engineering Requirements Document (Quote‑Ready)", DOC, 8566, ""),
            ("1RcDXfOk-jaQ3vBGIrPD8qkM6QH2oBZ7m", "video1119362356.mp4", MP4, 160603827, ""),
        ],
    },
    81: {
        "source_folders": ["1FqsS0kzQ686pS7NkQoNe-CevuFWuwTQf"],
        "files": [
            ("1Vz5PPTGzjn92RMpMZG4TbdJzH82kkaQkdhyoYe3pzcI", "Read Me", DOC, 1024, ""),
            ("1MDzAYi79rrNeYoL9PQ6K70r691p0HUNh", "TrueFuels - Next Steps  - Sep 10 2025.mp4", MP4, 178123778, ""),
            ("1N0TI2Ds7kWSEhoCkaaP8NKvznO7cKHS7sdk3L_uU6vA", "Smart Reordering Engine – Feature Listing & User Flow (TrueFuels)", DOC, 7119, ""),
        ],
    },
    83: {"source_folders": [], "files": []},
    85: {
        "source_folders": ["144UoeHDIxxqz0QzIz30SiKo3KcqEJCD7"],
        "files": [
            ("1z3cARm29uiomdqZR-AwUCnjMRBhREdYx7eCKPX5PHa4", "AAP Patient Education App: Vendor Exit Strategy & AWS Migration", SHEET, 33861, ""),
            ("1eC1B_Ygv0f2rJ5zVuyHQtytfMo7Y8gcu", "Additional app spec info.docx", DOCX, 328182, ""),
            ("1lENGAdZuelZJveq7kfuXKZUiit4aIpql", "AAP_App+API_2026-02-04 1.zip", ZIPC, 35024486, ""),
            ("1OZMgSKmCt-80EOsnHevzK1WEE_VMNqv0", "AAP Patient Education App Product Specification.docx", DOCX, 2589703, ""),
            ("1cZYFmNbvgRyHB0TF6VmKCSmBkWhcwGVn", "AAP - Solution Call  - Jan 13 2026.mp4", MP4, 139461595, ""),
            ("1o7xb0KvUFzADQFh2VfGD0Myk2vTXMw47SfBOk9IEhpk", "AWS Handover & Training Plan - Solution Document", DOC, 1476540, ""),
            ("1pxafVkUWYatbht_gEEENcDJPmqehZhSDwIT7Gdw7gk8", "AAP Patient Education App AWS Migration Plan - Solution Document", DOC, 1580864, ""),
            ("1iH7XfEpH_TgsDjZYqWC9WVD7KQgIrnuDO6CCdY4VIac", "AWS Handover and Training Plan - Solution Document", DOC, 1476218, ""),
            ("18nPjHB_5VSDkJfmRZaISgBURT4CzkjaFS6F28LpJIGQ", "AWS Training  Plan - Solution Document", DOC, 1476536, ""),
            ("1xTlwJLDnwiYY6REpC3UoR60lQ2fI87wgrJeNtwvHeIE", "AAP Patient Education App On-Premises Migration - Question & Queries", DOC, 1475587, ""),
            ("15BtdBIvA31EMvn25FGHQHMEYupmj4pD5", "Architecture Diagram.pdf", PDF, 59210, ""),
            ("1kqj2ocSFqK4gIBZq35JZxAd0JGvgD3rT", "AAP - Hosting Discussion  - Sep 18 2025.mp4", MP4, 109154387, ""),
        ],
    },
    89: {
        "source_folders": ["1D-7wCGR3hQqYf17f9DC7MQGqsJovgBvD"],
        "files": [
            ("1yvUpLwOakGyEnKNA1CD6H_l6hx6OyjGRbbUbPeUy56w", "Technical Questions - Solution Document", DOC, 1512180, ""),
            ("1UkDNAcSJG780qh6S5CKYdzOabe0QAuUp", "Technical Questions.docx", DOCX, 21660, ""),
            ("1a48lHsE1glE7qvryGFVGqFFTmLiMAz6D", "FERZ X PURELOGICS - Oct 9 2025.mp4", MP4, 67461564, ""),
        ],
    },
    90: {
        "source_folders": ["1jsXHvHqJRgXTFEhx5fgBMyFsSeQGyhMV"],
        "files": [
            ("1UPOo-OSnnLcd60zAY15oic7f3x1kXSkEG-sF3ZTGC9s", "Read me", DOC, 1024, ""),
            ("1DuMOFaChu8fQZYWzPNcHZFj_F94SRTId", "Pamela <> Purelogics - Deeper Discovery - Oct 20 2025.mp4", MP4, 121211725, ""),
            ("1Tb7tIaTkA_5aH9WY51DVT1oQo1BLYceh", "Shelby Soto and Pamela Nygaard - Oct 9 2025.mp4", MP4, 51319365, ""),
        ],
    },
    91: {"source_folders": [], "files": []},
    92: {"source_folders": [], "files": []},
    97: {
        "source_folders": ["1PJ33Aof0BirOomzdIVjweAvZ56vLTZjB"],
        "files": [
            ("1RPWkhNopACspkctUcl4QMzUXJYAfV_5V", "Ryan __ Purelogics - Follow Up Meeting - Nov 13 2025.mp4", MP4, 134863054, ""),
            ("16TC8AsyPAQjUxS4ILtaHZpjvRugunqxI7j19JORriiY", "AI Tutor/ChatBot - Roadmap & Estimate", SHEET, 29309, ""),
            ("1tHZYGJDqAogj78YbJOWc2m-6vonMoHEk", "Little Mountain Learning Academy X PureLogics - Oct 28 2025.mp4", MP4, 278928841, ""),
        ],
    },
}
