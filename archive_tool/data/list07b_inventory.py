"""
Real Drive inventory for List 07 (`On Hold`) batch 07b: cards 19, 20, 22, 23,
26, 28, 34 and 37.

Scope calls recorded here:

  NOT_WALKED   card 34 attaches three source-code trees exported from git
               (`redicare_api-develop`, `redicare_web-develop`,
               `redicare_reactanative-main`). A code export is not a sales
               artefact and each holds hundreds of level-2+ files, so they are
               named in the manifest and deliberately not walked - the same
               call made for the earlier repo dumps in Lists 05 and 06.

  EMPTY_FOLDERS  card 28's `Sample Files ` holds no files at all: its only
               child is the level-2 folder `fwdmeetingreminderpurelogicsandmatthalpert`,
               which the one-level recursion does not reach.

Diagram calls: card 26's `... (Diagrams).pdf`, card 28's `... Solution
Diagram.pdf` and `Flow Diagram.pdf`, and card 34's `... Project Phases
Diagram.pdf` are final diagrams. Card 37's `transaction diagram flow.png`
is one too (its title says .png, its mime is image/jpeg - the classifier keys
off the title extension, which is what a reader sees); its four sibling PNGs
(`Saas overview`, `User buying-1`, `User selling-2`, `User registration-3`)
carry no diagram keyword and are skipped as ordinary imagery.
"""

DOC = "application/vnd.google-apps.document"
SHEET = "application/vnd.google-apps.spreadsheet"
PDF = "application/pdf"
MP4 = "video/mp4"
DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
CSV = "text/csv"
PNG = "image/png"
JPEG = "image/jpeg"

INVENTORY = {
    19: {
        "source_folders": ["1SdJ659vOZKF77crEjqadHRwuQKEw33zy"],
        "files": [
            ("1No-BlMZ6HNY-EzcK1YPAOz5S9HCEGi9lKPfmS0y3NzM", "Migration for Revolv - Roadmap and Estimate ", SHEET, 17810, ""),
            ("1Mb9u_bMQkmALViPkQmh7vwr1N3UenohGv-khA4aR4To", "Scaling MVP to SaaS Solution - Solution Document", DOC, 18962, ""),
            ("1htSnZ-fd5yQDbJe9MywcwUwOGErAP0_ULuj6x5NqLWA", "Antoine's Migration ", DOC, 6614, ""),
            ("1s91fOeAsHiIaPg4-HHQ8hEreLpMg2znl", "video1686779420.mp4", MP4, 58633061, ""),
        ],
    },
    20: {
        "source_folders": ["17bI0bW_-HxsdUxkWv423X-wURul3E4hI"],
        "files": [
            ("1_J9jUx8KfL7phk3imQOGfIbY0QDx31C9HIvCb97cy2Q", "Crawler Development - Solution Document", DOC, 19818, ""),
            ("1Pbs5w0FMY-iEsjaW7u1sSsWHHB1AMY7rby6wI8jsR8Y", "Web Crawler - Roadmap & Estimate", SHEET, 17432, ""),
            ("1jDSbIp4c3Abu7R-Kda7xQhK6gfqTnPi_psLeHCGbNcs", "Simons Crawler ", DOC, 6095, ""),
            ("1EThoDnFQNIAUlF4KHtL5gH908olaAAyI", "video1787168312.mp4", MP4, 58444973, ""),
            # subfolder: Internal Meetings
            ("1Beigo4DiKHoznebrTC3ouK71NVFcp9vU", "01 Meeting with Engineer.mp4", MP4, 25312130, "Internal Meetings"),
            ("1di6c2KaSCE6eewrqcve1_J5a_tBgRKL_", "02 Meeting with Engineer.mp4", MP4, 10040737, "Internal Meetings"),
        ],
    },
    22: {
        "source_folders": ["1RdkGaMZhnVNba-yQFiMUg1MTtxL4Ytv8"],
        "files": [
            ("1cUOm-ehs_xi0NwbgO2BnrnJNBIhFoU5rmqXvi7CXjac", "Hollie CRM | Web App Development - Roadmap & Estimate", SHEET, 36638, ""),
            ("1PNrYVgmlGT7uDoBPKM_xBqzI2kvfkWe5YdYR-aI_q-E", " Hollie CRM | MVP", SHEET, 24877, ""),
            ("1mUmmmcuWYODZF94ggEaAuY1GwWCNNTjXGN281x3PuPc", "Technical Requirement Document - Biking CRM", DOC, 4061, ""),
            ("1vnzOU10CR6acCps6J5eg0JcYKc3uR3ts", "Hollie CRM - Engineering.mp4", MP4, 118988531, ""),
        ],
    },
    23: {
        "source_folders": ["1eRJlX1lmUcgIixH0cYnjGWPesloum5jv"],
        "files": [
            ("1r-SZUjFb4M5hQ1Wbal-bWDGMdqMmRhvf", "Investment Information LLM - Project Phases.pdf", PDF, 2715434, ""),
            ("1Mxit1BseGLHVdlrEZXM3GIymbqrtUFy0", "Engineering.mp4", MP4, 108513291, ""),
            ("1CG2NliYGkUFwUUcyqwAa9QnOXYEkHUYX", "Engineering - Quantera.mp4", MP4, 150296291, ""),
            ("1-GbddDDvXzIgXUMRREw873lybRNBmKXB", "Quantera Updated Requirements - Engineering .mp4", MP4, 18578327, ""),
            ("1U83LH6oXBwcLnaBSa2itdpT0q2h4DlEJ70rKrqusaN8", "Investment LLM - Roadmap & Estimate", SHEET, 19393, ""),
            ("1Xb9jOl0ujdOGXl539zGCwKQ0ka4saNOmhHi2hZ8CIwc", "Technical Requirements Document - API Consolidation", DOC, 6304, ""),
            ("1Iu8e8JFuz3ePjOvaVpOZTtYLoqwFU1To", "Key task list.pdf", PDF, 20650, ""),
            ("1PwXtu5SMul1ks-8BAgBh6o2wLjzgbunzP23hn4VUFwA", "technical-requirements (2)", SHEET, 2270, ""),
            ("1orYJA8_kLhFqXMuM_9veXcudIxVqwnxd", "technical-requirements (2).csv", CSV, 3547, ""),
        ],
    },
    26: {
        "source_folders": ["1cWsBFLJm-uHi5QhawOYNO7o_poONstqm"],
        "files": [
            ("13GbFaBqmp-LKaBsoDwT459_qIhAsziBd", "Inventory Management System - Minerals (Diagrams).pdf", PDF, 1109288, ""),
            ("1H8DnRhVcw9qqZ-qC2vrlC99B0fnRwSivIMPTgMXUiwk", "Inventory Management System - Solution Document", DOC, 19932, ""),
            ("1_S6Q9pUJbGp1v5PIp-7036wsz3DqUBaJ", "Fibras-test-data.xlsx", XLSX, 136027, ""),
            ("1xUWZI-n20eY7eBp6bUYz1wCN76ecKIUT", "video2774823691.mp4", MP4, 46212453, ""),
            ("1c_cg6hcnB-IQggjYqKq2WAfks9xNaNGuxD1ekepdx34", "Copy of Master Template - Roadmap & Estimate", SHEET, 23645, ""),
            ("1Ci9m_qHnp4SHP4Mb-tVzIxC0y7XaP5b9", "Example-Data.xlsx", XLSX, 67000, ""),
            ("19hwNW6u-EoOyfiK7Na0HJ3hFUR3o5XaSrWd8Uov9Deo", "Inventory Management System - Requirement Document", DOC, 4168, ""),
            ("1JgKPnX7G_RuPLzb8LLSlmUX0wVzONO-j", "Untitled video - Made with Clipchamp (2).mp4", MP4, 345795488, ""),
        ],
    },
    28: {
        "source_folders": ["17v8TS7MDl51uAcAvM4pYFwdcUYka4OfD"],
        "files": [
            ("19rQh3LMod4LxdIq1OPu08IhSALZ6ON36", "Cancer Cure DB - MH - Solution Diagram.pdf", PDF, 1429246, ""),
            ("1B4nfZghp8T3eM1WvXXt0wi1GA6eZGjBZ", "Engineering - Matt Halpert.mp4", MP4, 80500281, ""),
            ("1ipzhXJuZNu-lUVI5UH529FzjV6aUSoRk", "Flow Diagram.pdf", PDF, 2008363, ""),
            ("1WBNRCk3PkANIvHYC6rN6aF99tbjcl8W2Kl9BjLc7SG0", "Technical Requirements Document - Cancer Database", DOC, 4705, ""),
            ("1vVNX38DFDp1iLbhSMlVfM0WLnX4eI2-f", "video1800360771.mp4", MP4, 218112181, ""),
        ],
    },
    34: {
        "source_folders": ["17SlTblVzzPZGVwU2GpkMyHYrx11Oj30k"],
        "files": [
            ("1d-DAPOgM4j4KOEMK737lk1dGARJEDv7y", "Redicare - Project Phases Diagram.pdf", PDF, 6171104, ""),
            ("11WeKAo-NyuTjz8E-u7ZbqKuhQWxB9Co6", "video1943133023.mp4", MP4, 129376114, ""),
        ],
    },
    37: {
        "source_folders": ["1YnJuvqCzKESjMM-n9h4jb6TQ1GX1F2LQ"],
        "files": [
            ("1yxsaA2jWSfbhpEFX68CCfiOF2fPIhEVqmRDiIal6DgY", "Real Estate SaaS Platform - Roadmap & Estimate", SHEET, 24277, ""),
            ("1Y6e3RGrkCGrWuuyjFbjUxKnI1xEdkyxa", "Real Estate - March 21 Engineering.mp4", MP4, 288960679, ""),
            ("1UdxOEcfpqGpbPg1Uh9HGSULwur07-pc6", "BRD-3.docx", DOCX, 38326, ""),
            ("1UdHgD4WkWktrjFzP6W8jTmkKdh4Hj6DRDxXctDl_QN4", "Real Estate Platform", DOC, 8392, ""),
            ("1A19vD-5ig5q-dp0Kwz5lLGYrzrxVUXXHDyMjYwflyjE", "Core Features & Functional Modules - Real Estate SaaS App", DOC, 5923, ""),
            ("1_DJlUbziS8hA6FJZCvAQ_Kia-m4kJUQi", "Crux questions answers -.docx", DOCX, 487528, ""),
            ("1rCl3rPQhPQwjpT9denIxBuahssrN8H4M", "Saas overview.png", PNG, 198381, ""),
            ("1fR-uYoZTBj6f6BGqQzmeib6lJwhgxFgb", "User registration-3.png", PNG, 255401, ""),
            ("1GQKOJ-p3y_66JYQjphHMaPpgLUGoADSg", "User buying-1.png", PNG, 241568, ""),
            ("1m3SR8XlxaVLxQBnHwnyHD4sKunGZ--9M", "User selling-2.png", PNG, 214978, ""),
            ("19s1Cx1tKnsu7lamr_adoFub8hF7iDXbx", "transaction diagram flow.png", JPEG, 46585, ""),
            ("1Deiha1d-3M7d5lf88yD8r3J_yUCCGCT1", "FAQs.docx", DOCX, 487379, ""),
            ("1-zk6P19Vk5NVM5NIWw9XCk3rxsLLEFaq", "Real Estate App - Engineering .mp4", MP4, 31505446, ""),
        ],
    },
}

NOT_WALKED = {
    34: [
        ("1UmkuIeWBiffKl909gRbFRjGelO2xRs8w", "redicare_api-develop"),
        ("1-9kH1dncw3aXrrepRpj2tV7e6U0kVOKV", "redicare_web-develop"),
        ("1ldcNlzuHXHqlFIhrR6o1SAP1R4GoGGSO", "redicare_reactanative-main"),
    ],
}

EMPTY_FOLDERS = {
    28: [("1xwTulFcj5jliZW7sHmG1NRO70MnQHPPy", "Sample Files ")],
}

SUBFOLDERS_TO_WALK = {
    28: [("1zFdURg8gMH3JE_0wSBbQNhSqHEWuE7v_",
          "fwdmeetingreminderpurelogicsandmatthalpert (level 2, under Sample Files)")],
}
