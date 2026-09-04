"""
Real Drive inventory for List 07 (`On Hold`) batch 07k - the last seventeen
cards on the list: 406 - 421, 440 and 446.

The first grouped listing (cards 406 - 415) came back empty, so those nine
folders were probed one at a time: four are gone. The second chunk (416 - 446)
listed cleanly. Two subfolder listings followed.

  DEAD_FOLDERS   cards 407, 408, 409 and 410. None of the four links a file
                 either, so all four archive as a card.md and nothing else.
  EMPTY_FOLDERS  card 411's `Engineering` - readable, no children.
  DEAD_FILES     six card-level file links answer "Requested entity was not
                 found"; recorded per card in `errors`.
  NOT_WALKED     card 440's `BA Deliverables/DRAFT`, at level 2.

Card 419 (`Unifier - M`) is another under-reporting case: its folder lists
three recordings and nothing else, yet `08 July 2024` and `AI-Powered Jupyter
Plugin - Roadmap & Estimate` both report that folder as their parent. Only the
union with the card's own file links finds them.

Card 406 (`The Super Bill`) links a project root whose sole child is an
`Engineering` subfolder holding the roadmap - the one card on the board whose
deliverable sits a level below the linked folder with nothing beside it.
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
SLIDES = "application/vnd.google-apps.presentation"
PDF = "application/pdf"
MP4 = "video/mp4"
MOV = "video/quicktime"
PNG = "image/png"
JPEG = "image/jpeg"
DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
XLS = "application/vnd.ms-excel"
HTML = "text/html"
EML = "message/rfc822"

GONE = "Requested entity was not found (deleted or access revoked)"

ENG = "Engineering"
DOCU = "Documentation"
SALES = "Sales"
DELIV = "Deliverables"
BAD = "BA Deliverables"

INVENTORY = {
    406: {
        "source_folders": ["1zxcZWEa0qWFFsxS-UWmflF-Ipnzy5JR6"],
        "files": [
            ("167tYNW6XhbzmakkyeWHEwqjwMdWseVWiLrMBAxRb1ZU", "The Super Bill | Design Work (WebFlow Animations + Figma) - Roadmap & Estimations", SHEET, 5128, ENG),
        ],
    },
    407: {"source_folders": [], "files": [],
          "errors": [("folder:1g7Mon5CTgFK3iUchxOJ-T2u6I2lVpVGT", GONE)]},
    408: {"source_folders": [], "files": [],
          "errors": [("folder:1o1vQSX6hhrxK06lEIfq0qeez_T3qs8j-", GONE)]},
    409: {"source_folders": [], "files": [],
          "errors": [("folder:1VfpI4H2llf9VTY1KWoXul_o3JF4vIqxH", GONE)]},
    410: {"source_folders": [], "files": [],
          "errors": [("folder:1tETSyU45cRfjMtUfPhMqXhgGtGWXpVis", GONE)]},
    411: {"source_folders": ["1D_YJgJUMMxlyMGTj70bAL-W4tj0V7rGA"], "files": []},
    412: {
        "source_folders": ["1QusSbFtMBO0fv_cP0mo6f0O57YUFXYd9"],
        "files": [
            ("1IOOq-8gd9KNtUTcTuqhOKu282_sMimRr", "Trimmed Requirements - Setup Sheets Software.mov", MOV, 3045562866, ""),
            ("1VPRAllwJmWeJOSQmVJF8W7k3ysdbbcNl", "Trimmed version - Machine Setup Software.mp4", MP4, 61031972, ""),
            ("15sS0LibErbr3uWyvTOPGRK3yNEZE5du138fFOBCk9pA", "Machine Setup Form | Web App Development - Roadmap & Estimate", SHEET, 52926, ""),
            ("1Dwd8KzZ-PO-iaSYLcsZH3P5ObvY8yXLx6Yau88lVgxY", "Setup Sheet | Question & Queries", DOC, 14399, ""),
            ("1xaXTSSV35WiUIH41ygKq7ww8fps7WiVn", "Setup Sheet DATABASE Example.xlsx", XLSX, 275933, ""),
            ("1TERR_nE1ZUERJMi-8RmL81eYvQDoQJdmKMMmPfN0q6g", "Parker Hennifin |  WorkFlow & Kickoff Document", SLIDES, 799365, ""),
            ("1L3xHwdHfSfFeduy84PN9K_Y-5TBRPGfY", "Setup Sheet Scope of Work.docx", DOCX, 199901, ""),
            ("1qjNMy4L0zaUALTbOAJX30lnIq9pptjqE68UNHfJBtfE", "Requirements 14 oct", DOC, 1024, ""),
            ("1Lh_FoFCVrGKuVgMruyDpYT9BKwNieVVq", "Setup Sheet Form.pdf", PDF, 202010, ""),
        ],
        "errors": [("file:1wymfkd1iilaKV1mlpfiO1F1t_-0HbxZ7", GONE)],
    },
    413: {
        "source_folders": ["1eiYL2eIT0XgB4wMOiUTUf7Sd-W830Gd9"],
        "files": [
            ("1C_CP3iST3fF8BCi_FEhzNnZavb5m-40D", "trimmed version - AI.mp4", MP4, 258308252, ""),
            ("1bgvDWz_HDlgCseova614GqA74Nb3rkIp", "Roadmap call.mp4", MP4, 326129274, ""),
            ("1NJ7iFWX7NNEsZ3KuMwkFF8UdANmQH-ndZkqIGFr0UaA", "AI Trading System - Roadmap & Estimate", SHEET, 18515, ""),
            ("1kazzRQncd-eK7agpg8OYxCb45xvO2EJ5xC3NIvOwgoI", "Requirements", DOC, 2155, ""),
            ("1GQkolHZXM_8YQDEqnEq0FzLJylyFa_9Y", "GPU Based Cloud Ballpark Cost.pdf", PDF, 847252, DOCU),
            ("1dcvCyZKxtQEq48JI0rBxBasdqqpeBXzI", "CPU Based Cloud Ballpark Cost.pdf", PDF, 862096, DOCU),
            ("1VynsxjhTtPphgd6CPBWCmDbvX8wGU-XA", "GCP Flowdiagram.pdf", PDF, 164908, DOCU),
            ("14z5S6OZ7-QSv2plgXQ3X3lr1jVarVvOg", "overall_comparison.html", HTML, 9271, DOCU),
            ("1SPQUHeIYHF57ia5VTt8Yl9bNM9dHmblE", "overall_cpu_comparison.html", HTML, 10932, DOCU),
            ("1NAd9weDDZ5WZS7b77SP4JiPSa6n8leZu", "AWS Flow Diagram.pdf", PDF, 172013, DOCU),
            ("1ztbb1-nqD7f1_H5dB5P42AHVYZwUG4S7", "Azure Flow Diagram.pdf", PDF, 167734, DOCU),
        ],
        "errors": [("file:112TnJQas3UamZyNYiCYjLVmOFV3awtF_", GONE)],
    },
    415: {
        "source_folders": ["1yFnRwSm-Vg4n6beCqHP3zNqJu5ph_PK9"],
        "files": [
            ("1P59CZ2XAHnb4gWHeSxkg1R3Ex_t0VOh0", "Discovery 1.mp4", MP4, 115413066, ""),
            ("1iUV71d1C6LJWIs9PYUWlmGLQMSpLkHWb", "Discovery 2.mp4", MP4, 132322944, ""),
            ("12t4k5NvPPbgWBhk_3aoZZuugW4cX36y7pWokwb-Fo3Q", "AI-Powered ChatBot Development - Roadmap & Estimate", SHEET, 20111, ""),
            ("1kxZBXv3dYGbtXohOYlEs0vFa-bkEnANC1aT30HKZCdg", "Requirement", DOC, 2443, ""),
        ],
        "errors": [("file:1k8j0MxeNiYoMWlMSRcFs5fc9eTbHl-hc", GONE)],
    },
    416: {
        "source_folders": ["1WURsCj57Ny-Kw8iqPnw_XCsBfewSLxI_"],
        "files": [
            ("1tOdDuT7geSUlhoiWGRKVyxeUkbD_eiUC", "11 sep call.mp4", MP4, 243059857, ""),
            ("1VLPkAsN116DzhtDsqtG953r9Pe7Pf4s3", "18th sep call.mp4", MP4, 67800245, ""),
            ("1MhbtOeGLwRrwuayH9ABYkXf_DJJW4oFka7Z4PPngl8s", "5. Northstar Web App", SHEET, 13118, ""),
            ("1rXTe-3P2HX6XNmF-6PXxVI5x15ikQ-plSGm902T39ho", "6. WPSS Implementation timeline", DOC, 12493, ""),
            ("14d93GoiGug1WFl_3sMdmUqmNQzDWnFLHx04RxihQuE0", "3. Answers", DOC, 2853, ""),
            ("1XOadreeRS9g4Oxf4xqk7FDV6_f8FLDAo6W4dpsSoexc", "Actionable Plan for WPSS Implementation", DOC, 6933, ""),
            ("1lKP6DefY7m4r34GaPXTFml-lAsdKcMgxQviDuSNFF4Y", "1. Employee Tracking System - Solution Document", DOC, 20044, ""),
            ("1sfo9pT4PbTn5oNHhaKaCXKPnCQmRY1pKke7B5uOSK3k", "2. WPSS Solution", DOC, 300729, ""),
            ("1i8iudiuC-sudbOFtaW30D0v4ZgKupq9Ge4DlFjDvlB4", "Copy of WPSS _ Draft", DOC, 300729, ""),
        ],
    },
    417: {
        "source_folders": ["10kYz5BjZ2sLAfPf0YdX3ENLXtOXsOI2A"],
        "files": [
            ("1KslYJeEDBBI-WGO_lqtkHoAqkjD6L74Z", "Workflow doc.png", PNG, 568751, ""),
            ("1hKaZG-MlKIiDPmsVnHqog4p--QFel_V1", "image0 (1).jpeg", JPEG, 479584, ""),
            ("1qpFlBLE-1oBNKE20MXbmb-Yvyh5Da5gLx7eJKNbzPpA", "3PL Shipping Notifications - Solution Document", DOC, 18749, ""),
            ("1pORlzSs0chhbk7mHFSjk04VPyHGo0BkW", "Whole World Botanicals Shipping Confirmation.eml", EML, 42738, ""),
            ("1IugPUkGsZ9ukhgnrYR88NZNwx8kd3ACZ", "wholeworldbotanicals-ftp-4280877.xls", XLS, 33280, ""),
            ("191-H2F52YATT1-vI5OyTILZWPLio8RbxBvZj9v2E-fQ", "Intial Requirement", DOC, 1024, ""),
        ],
    },
    418: {
        "source_folders": ["1Cqz9PvmFP6tVzi15q1QkDQllB1mtDAHr"],
        "files": [
            ("14DaePDLnixhjBSQlyV2mlthK3ZOLK8gwDo77wkZxB-E", "Farragut ERP System Development - Project Proposal Document", DOC, 5873152, ""),
            ("1iqw-rJ_st0wWH-oS3dcIpL_o1mosee_TMZtEGgYJRVQ", "Requirement", DOC, 5037, ""),
            ("1L0za6QdtbvBcdefC7vQstYr29CnHzA3pkDT9VDcmtvs", "Copy of Master Template - Roadmap & Estimate", SHEET, 17755, ""),
            ("1qkHwksFLlpxio1CPuIrxo19mrKvjlBKX", "ERP_Pricing_Sheet.xlsx", XLSX, 49716, ""),
            ("1QnPrLI-opyEuAAINlnwlRp_71t4N7kWT", "Notes Sohaib .docx", DOCX, 45894, SALES),
            ("1A2EGjmn-2XzqjbXW-TzZ8d5is4phIOfo", "FY25_ERP.pdf", PDF, 2908473, SALES),
        ],
    },
    419: {
        "source_folders": ["1XZeseg-X0AY8kwlXk4D8Yb4j2R8wNtLn"],
        "files": [
            ("1CiygRjrxIzKxY4So5QSJ4ncWHn2VX_7n", "video1123964973.mp4", MP4, 228554500, ""),
            ("11nQi-C_p6dvNxNVm7b0gHajknCuHiXvI", "Trimmed - Call.mp4", MP4, 64979299, ""),
            ("1ST1b4T8XJ4kFGDzZZWj1FaaipmET4srJ", "Trimmed call - 1st aug.mov", MOV, 92468918, ""),
            ("1yIIsmvSvocC6mpAFP1WQOMDb-vPHrjJtf8INL6rFN-Q", "08 July 2024", DOC, 3812, ""),
            ("1arfp6oJK72Nc5_F95ONOQNkEEY0ZqziCUNFgek96LIM", "AI-Powered Jupyter Plugin - Roadmap & Estimate", SHEET, 15594, ""),
        ],
        "errors": [("file:1Jip7-HjEn7dbxui4UWw7aXSoa3pJ5gju", GONE)],
    },
    420: {
        "source_folders": ["1qe8_dFDMTw9NtW-6v1L9JwFlHB61asXG"],
        "files": [
            ("1ZzVwx48PAEnDFXFjl1bZFHHd9qHiJPFU", "1. Discovery - 26th Aug.mp4", MP4, 249337913, ""),
            ("11em2s_sWvm8nMbfim8aEcrEvkujOanNL", "2. 20 Sep call.mp4", MP4, 124929565, ""),
            ("1XFGxwSBpJXX_ChKHfGdRpVwvbNEjx5JF", "3. 11 Oct call.mp4", MP4, 414715449, ""),
            ("1Tgijo34aUdBISX8kBYp7_Awm7O1tdA1r7XjCj52ZJ4o", "Mental Well-being Web App - Solution Document", DOC, 17773, ""),
            ("1cPYXdxR-GHt5dqcZSGZ5cya9LrzEq3VeK9ZUAsiU7BU", "Updated requirements 20 sep", DOC, 2953, ""),
            ("1lzcW9ElMKWR4fq1DquklNRkJndblgu4AVKCXpcBJ9vM", "Requirements:", DOC, 2588, ""),
            ("1K2P1y1s8rYoiaEkOceks_tR1VtNZJwoxQMbaj6VcpAY", "1. Mental Well being Application | Web App Development - Roadmap & Estimate", SHEET, 19982, DELIV),
            ("1MEu2gYq7qnM3Lpv46qWGGKBTXK9Q77qK", "2. Wireframes.pdf", PDF, 2167205, DELIV),
            ("1yJAKhQbH64dsktHJ1ZT14UsyipzxRWuM", "3. MindMapping.pdf", PDF, 1216132, DELIV),
            ("1xUZXej2cs1rRxBpUrHXvEC6vPJjkxr2d", "4. Patient Flow Diagram.pdf", PDF, 728020, DELIV),
        ],
        "errors": [("file:1rGCUBjMb8pxXgrD1XwJ04aKeAp73VwVh", GONE)],
    },
    421: {
        "source_folders": ["1ts9UpDNRlGdkba673rmeSzAaQUDTwHdL"],
        "files": [
            ("1lS8MC0A-c3L2LOVPmOLKXgNqPnU9CmDs", "Trimmed - RFID Tracking Software.mp4", MP4, 283729490, ""),
            ("1cvtlG_unvuXgRuSjBpk18W0KWw1ZlWnsesp0M4Qtne0", "RFID-Based Inventory Management and Tracking System for Small Businesses - Solution Document", DOC, 18867, ""),
            ("1nmPKkYToDZAcRsIRvH9tPd5j_Pm_p38H5VueqyiRc4k", "Requirements", DOC, 3031, ""),
        ],
        "errors": [("file:1Xfbo9NAHUlPu6xoQ38aaDJHVlCI18A23", GONE)],
    },
    440: {
        "source_folders": ["16WKBPW_zIa_4qoSuWGWvYRujXiIV1JM6"],
        "files": [
            ("1MngeTXB68HvnjiMw2nPjzkPW9FnGTjhJLzbH94poiAM", "Trua Senior Living Locators - Franchise Systems Discussion (PureLogics) - April 17", DOC, 20902, ""),
            ("1O6Qko7PwZHcWYImjWyxf0yNokHEdGatq", "Trua Senior Living Locators - Franchise Systems Discussion (PureLogics) - Apr 17 2026.mp4", MP4, 248267044, ""),
            ("1nmUsV1XMIxFyZXuoCvOaW6JBVGrbkCSbn-QJw1oeZKk", "Franchise Training Portal - Roadmap & Estimate", SHEET, 41180, BAD),
        ],
    },
    446: {
        "source_folders": ["1JgD238TnhWCJhHUnupbvMRiBQUX7mbVG"],
        "files": [
            ("1ZSJYpTNz6xx51QF7qaypa9JUuj3lFnwSk2XGgt5sflc", "Northcoast Helicopters - Roadmap & Estimations", SHEET, 24782, ""),
            ("1I4RFsj09Vtj4CT-6v6WmiGgz4EhLjsnU", "Homepage Screen.png", PNG, 57402, ""),
            ("1GTvvrkF0RdvC_ZgpvfOCFmkA907kbzds", "Flight Duty Time Screen.png", PNG, 51126, ""),
            ("1VsFVtly2TL6lbxSS4TwhIhfrc56esF9R", "Flight Duty Time Screen # 2.png", PNG, 105852, ""),
            ("134KgJeeiuUqzJy-ramNCIjJKBEprkwhXQ0gdCC8EEMA", "Meeting ", DOC, 10185, ""),
        ],
    },
}

DEAD_FOLDERS = {
    407: [("1g7Mon5CTgFK3iUchxOJ-T2u6I2lVpVGT", "Engineering")],
    408: [("1o1vQSX6hhrxK06lEIfq0qeez_T3qs8j-", "Engineering")],
    409: [("1VfpI4H2llf9VTY1KWoXul_o3JF4vIqxH", "Engineering")],
    410: [("1tETSyU45cRfjMtUfPhMqXhgGtGWXpVis", "Engineering")],
}

EMPTY_FOLDERS = {
    411: [("1D_YJgJUMMxlyMGTj70bAL-W4tj0V7rGA", "Engineering")],
}

SUBFOLDERS_TO_WALK = {
    406: [("1JoULvzVBwDRe7XVpx5snUkaaRv8p6qpf", ENG)],
    413: [("1qRaWhyUOx0DaNQw4SPSZ_XCk-iHhZj9U", DOCU)],
    418: [("1Chw73FARMUACxISGb7pu6U3-YG8x3ks3", SALES)],
    420: [("157G2WArO6_8cKqxc5zssx2Qv2N9gAsNW", DELIV)],
    440: [("1L-70_nzgVXbXQ3P0dC4CSTYyW4qsFX04", BAD)],
}

NOT_WALKED = {
    440: [("1z1SUsfU_sf9S0NhI00db1kIVuxy5TAsE", "BA Deliverables/DRAFT")],
}
