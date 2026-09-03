#!/usr/bin/env python3
"""
Unit tests for the archive's classification rules (spec section 7).

These run without credentials or network access. The two reference standards
from the spec are encoded as tests: card 414 (Heart ID) must yield 11 diagrams
with 32 app screenshots excluded, and card 460 (Diamond Resources) 9 diagrams.
"""

import unittest

import classify as C
from archive_trello_to_drive import normalise_card, render_card_md
from classify import card_folder_name


def gdoc(name, size=50000):
    return {"id": name, "name": name, "mimeType": C.GOOGLE_DOC, "size": str(size)}


def png(name, size=250000):
    return {"id": name, "name": name, "mimeType": "image/png", "size": str(size)}


def binfile(name, size=100000, mime="application/octet-stream"):
    return {"id": name, "name": name, "mimeType": mime, "size": str(size)}


class TestSanitise(unittest.TestCase):
    def test_strips_illegal_characters(self):
        self.assertEqual(
            C.sanitise_name('A/B\\C:D*E?F"G<H>I|J'), "ABCDEFGHIJ")

    def test_collapses_whitespace_and_trims(self):
        self.assertEqual(C.sanitise_name("  Foo   \n bar  "), "Foo bar")

    def test_truncates_to_limit_keeping_meaningful_title(self):
        out = C.sanitise_name("X" * 300, limit=120)
        self.assertEqual(len(out), 120)

    def test_card_folder_name_keeps_prefix(self):
        name = card_folder_name(295, "Riley Infinity - EdTech Software")
        self.assertEqual(name, "295 - Riley Infinity - EdTech Software")

    def test_card_folder_name_with_illegal_chars(self):
        # A real board name: the pipe must not become a path separator.
        self.assertEqual(
            card_folder_name(1, "HOE | Ahmed's Review"),
            "1 - HOE  Ahmed's Review".replace("  ", " "))

    def test_never_empty(self):
        self.assertEqual(C.sanitise_name("///"), "untitled")
        self.assertEqual(C.sanitise_name(None), "untitled")


class TestUrlDiscovery(unittest.TestCase):
    def test_extracts_folder_ids(self):
        text = ("see https://drive.google.com/drive/folders/1UX9a6irjn_Iv6347OoukophBnd6VbzPS "
                "and https://drive.google.com/drive/u/0/folders/1abcdEFGHijklMNOP")
        self.assertEqual(
            C.extract_folder_ids(text),
            ["1UX9a6irjn_Iv6347OoukophBnd6VbzPS", "1abcdEFGHijklMNOP"])

    def test_extracts_doc_ids_of_every_kind(self):
        text = ("https://docs.google.com/document/d/1docIDdocIDdocID/edit "
                "https://docs.google.com/spreadsheets/d/1sheetIDsheetID/edit#gid=0 "
                "https://docs.google.com/presentation/d/1slideIDslideIDs/edit "
                "https://drive.google.com/file/d/1fileIDfileIDfile/view")
        self.assertEqual(
            C.extract_file_ids(text),
            ["1docIDdocIDdocID", "1sheetIDsheetID", "1slideIDslideIDs",
             "1fileIDfileIDfile"])

    def test_folder_link_is_not_mistaken_for_a_file(self):
        text = "https://drive.google.com/drive/folders/1UX9a6irjn_Iv6347Oouko"
        self.assertEqual(C.extract_file_ids(text), [])

    def test_extract_urls_dedupes_and_strips_trailing_punctuation(self):
        text = "see https://a.example/x. and https://a.example/x, plus https://b.example/y)"
        self.assertEqual(C.extract_urls(text),
                         ["https://a.example/x", "https://b.example/y"])

    def test_no_links_yields_nothing(self):
        # Card 452 (Seaver Construction) has no Drive links at all.
        self.assertEqual(C.extract_folder_ids("Plain text, no links."), [])
        self.assertEqual(C.extract_file_ids("Plain text, no links."), [])


class TestSkipRules(unittest.TestCase):
    def test_video_and_audio_skipped_at_any_size(self):
        for n in ("call.mp4", "demo.mov", "x.avi", "y.mkv", "z.webm"):
            self.assertEqual(C.classify_file(binfile(n, 1000))[0:1], ("skip",),
                             "%s should skip" % n)
            self.assertEqual(C.classify_file(binfile(n))[2], "video")
        for n in ("call.m4a", "vm.mp3", "rec.wav"):
            self.assertEqual(C.classify_file(binfile(n))[2], "audio")

    def test_archives_and_sql_skipped(self):
        self.assertEqual(C.classify_file(binfile("src.zip"))[2], "archive")
        self.assertEqual(C.classify_file(binfile("db.sql"))[2], "sql/db dump")

    def test_oversized_non_document_skipped(self):
        big = binfile("blob.bin", size=60 * 1024 * 1024)
        action, _dest, reason = C.classify_file(big)
        self.assertEqual(action, "skip")
        self.assertIn("oversized", reason)

    def test_oversized_pdf_deliverable_is_still_copied(self):
        big_pdf = binfile("Solution Document.pdf", size=80 * 1024 * 1024,
                          mime="application/pdf")
        action, dest, _ = C.classify_file(big_pdf)
        self.assertEqual((action, dest), ("copy", "sources"))

    def test_empty_google_doc_stub_skipped(self):
        action, _dest, reason = C.classify_file(gdoc("Untitled document", size=512))
        self.assertEqual(action, "skip")
        self.assertIn("empty stub", reason)

    def test_google_doc_just_over_stub_limit_is_copied(self):
        self.assertEqual(C.classify_file(gdoc("Requirements", size=2048))[0], "copy")

    def test_junk_files_skipped(self):
        for n in (".DS_Store", "Thumbs.db", "desktop.ini", "~$draft.docx",
                  "part.tmp"):
            self.assertEqual(C.classify_file(binfile(n))[0], "skip", n)

    def test_native_doc_without_size_is_not_treated_as_stub(self):
        # Drive v3 omits `size` for some native files; absence must not mean empty.
        f = {"id": "x", "name": "Discovery Notes", "mimeType": C.GOOGLE_DOC}
        self.assertEqual(C.classify_file(f)[0], "copy")


class TestCopyRules(unittest.TestCase):
    def test_google_native_types_copied(self):
        for mime in (C.GOOGLE_DOC, C.GOOGLE_SHEET, C.GOOGLE_SLIDES):
            f = {"id": "1", "name": "Estimate", "mimeType": mime, "size": "9999"}
            self.assertEqual(C.classify_file(f)[0:2], ("copy", "sources"))

    def test_office_and_text_documents_copied(self):
        for n in ("Proposal.docx", "Estimate.xlsx", "Macro.xlsm", "Deck.pptx",
                  "Scope.pdf", "notes.txt", "leads.csv", "readme.md"):
            action, dest, _ = C.classify_file(binfile(n))
            self.assertEqual((action, dest), ("copy", "sources"), n)


class TestDiagramRouting(unittest.TestCase):
    def test_keyword_pngs_are_diagrams(self):
        for n in ("Detailed Workflow Diagram.png", "User Flow.png",
                  "System Map.svg", "Architecture.jpg", "Data Flow.webp",
                  "Integration Diagram.pdf", "Wireframe.png", "Gantt.png"):
            action, dest, _ = C.classify_file(png(n))
            self.assertEqual((action, dest), ("copy", "diagrams"), n)

    def test_screenshots_excluded_even_with_diagram_like_extension(self):
        for n in ("Screenshot 2026-01-02 at 10.11.12.png", "Screen Shot 5.png",
                  "IMG_2941.PNG", "PXL_20240101_101010.jpg",
                  "20240131_115959.jpg", "image12.png", "Capture.png"):
            action, _dest, reason = C.classify_file(png(n))
            self.assertEqual(action, "skip", n)
            self.assertEqual(reason, "image is not a final diagram")

    def test_folder_context_promotes_generic_names_to_diagrams(self):
        action, dest, _ = C.classify_file(png("1.png"), folder_name="Diagrams")
        self.assertEqual((action, dest), ("copy", "diagrams"))

    def test_individual_diagrams_folder_routes_to_subfolder(self):
        action, dest, _ = C.classify_file(png("3.png"),
                                          folder_name="Individual Diagrams")
        self.assertEqual((action, dest), ("copy", "individual_diagrams"))

    def test_excluded_folder_beats_diagram_keyword(self):
        # A file called "flow.png" inside App Screenshots is still raw material.
        action, _dest, _ = C.classify_file(png("flow.png"),
                                           folder_name="App Screenshots")
        self.assertEqual(action, "skip")

    def test_all_excluded_folder_spellings(self):
        for folder in ("Screenshots", "Application Screenshots", "App Screenshots",
                       "App's Screenshorts", "Raw", "Game Images"):
            action, _d, _r = C.classify_file(png("Workflow Diagram.png"),
                                             folder_name=folder)
            self.assertEqual(action, "skip", folder)

    def test_google_drawing_is_a_diagram(self):
        f = {"id": "d", "name": "Sketch", "mimeType": C.GOOGLE_DRAWING,
             "size": "40000"}
        self.assertEqual(C.classify_file(f)[0:2], ("copy", "diagrams"))

    def test_slides_named_as_diagram_route_to_diagrams(self):
        f = {"id": "s", "name": "Process Flow Deck", "mimeType": C.GOOGLE_SLIDES,
             "size": "40000"}
        self.assertEqual(C.classify_file(f)[1], "diagrams")

    def test_plain_slides_stay_in_sources(self):
        f = {"id": "s", "name": "Client Proposal", "mimeType": C.GOOGLE_SLIDES,
             "size": "40000"}
        self.assertEqual(C.classify_file(f)[1], "sources")

    def test_weak_keyword_on_pdf_stays_in_sources(self):
        # Real card-295 file: a document, not a diagram deliverable.
        for n in ("EduCommand AI Level 3 Beta Architecture Materials FINAL.pdf",
                  "Integration Requirements.pdf"):
            action, dest, _ = C.classify_file(binfile(n, mime="application/pdf"))
            self.assertEqual((action, dest), ("copy", "sources"), n)

    def test_weak_keyword_on_image_is_still_a_diagram(self):
        for n in ("Architecture.png", "Integration.svg"):
            action, dest, _ = C.classify_file(png(n))
            self.assertEqual((action, dest), ("copy", "diagrams"), n)

    def test_strong_keyword_on_pdf_is_a_diagram(self):
        action, dest, _ = C.classify_file(
            binfile("Integration Diagram.pdf", mime="application/pdf"))
        self.assertEqual((action, dest), ("copy", "diagrams"))

    def test_weak_keyword_pdf_in_diagrams_folder_is_a_diagram(self):
        action, dest, _ = C.classify_file(
            binfile("Architecture.pdf", mime="application/pdf"),
            folder_name="Diagrams")
        self.assertEqual((action, dest), ("copy", "diagrams"))

    def test_native_google_video_skipped_as_video(self):
        # Real card-119 file: 258 MB native video with no extension.
        f = {"id": "v", "name": "video1015049405",
             "mimeType": "application/vnd.google-apps.vid", "size": "258215281"}
        self.assertEqual(C.classify_file(f)[2], "video")

    def test_mime_type_alone_never_decides(self):
        # Same mime type, opposite outcomes: only name/folder differ.
        diagram = C.classify_file(png("Workflow Diagram.png"))
        shot = C.classify_file(png("Screenshot 1.png"))
        self.assertEqual(diagram[0], "copy")
        self.assertEqual(shot[0], "skip")


class TestDedupe(unittest.TestCase):
    def test_copy_of_dropped_when_original_present(self):
        files = [gdoc("Requirements.docx", 5000),
                 gdoc("Copy of Requirements.docx", 5000)]
        kept, dropped = C.dedupe_files(files)
        self.assertEqual([C.file_name(f) for f in kept], ["Requirements.docx"])
        self.assertEqual(len(dropped), 1)
        self.assertIn("duplicate of Requirements.docx", dropped[0][1])

    def test_meaningfully_different_sizes_keep_both(self):
        files = [gdoc("Scope.docx", 10000), gdoc("Copy of Scope.docx", 40000)]
        kept, dropped = C.dedupe_files(files)
        self.assertEqual(len(kept), 2)
        self.assertEqual(dropped, [])

    def test_trivial_size_difference_is_still_a_duplicate(self):
        files = [gdoc("Scope.docx", 100000), gdoc("Copy of Scope.docx", 100200)]
        kept, _ = C.dedupe_files(files)
        self.assertEqual(len(kept), 1)

    def test_numbered_copy_suffix_treated_as_duplicate(self):
        files = [gdoc("Notes.docx", 8000), gdoc("Notes (1).docx", 8000)]
        kept, dropped = C.dedupe_files(files)
        self.assertEqual([C.file_name(f) for f in kept], ["Notes.docx"])
        self.assertEqual(len(dropped), 1)

    def test_stacked_copy_prefix_reduces_to_original(self):
        # Real card-295 shape: Drive stacks the prefix on repeated copies.
        self.assertEqual(
            C.canonical_name("Copy of Copy of Campus Weekly Activity Report.xlsx"),
            "campus weekly activity report.xlsx")
        files = [gdoc("Campus Weekly Activity Report.xlsx", 15798),
                 gdoc("Copy of Campus Weekly Activity Report.xlsx", 15798),
                 gdoc("Copy of Copy of Campus Weekly Activity Report.xlsx", 15798)]
        kept, dropped = C.dedupe_files(files)
        self.assertEqual([C.file_name(f) for f in kept],
                         ["Campus Weekly Activity Report.xlsx"])
        self.assertEqual(len(dropped), 2)

    def test_stacked_copies_with_no_original_keep_exactly_one(self):
        files = [gdoc("Copy of Copy of Report.xlsx", 15798),
                 gdoc("Copy of Report.xlsx", 15798)]
        kept, _ = C.dedupe_files(files)
        self.assertEqual(len(kept), 1)

    def test_copy_kept_when_no_original_exists(self):
        files = [gdoc("Copy of Orphan.docx", 8000)]
        kept, dropped = C.dedupe_files(files)
        self.assertEqual(len(kept), 1)
        self.assertEqual(dropped, [])

    def test_unrelated_files_all_kept(self):
        files = [gdoc("A.docx"), gdoc("B.docx"), gdoc("C.docx")]
        kept, dropped = C.dedupe_files(files)
        self.assertEqual(len(kept), 3)
        self.assertEqual(dropped, [])

    def test_riley_infinity_shape(self):
        """Card 295: a Latest Updates subfolder of `Copy of X` beside originals."""
        originals = [gdoc("Discovery %d.docx" % i, 20000 + i) for i in range(5)]
        copies = [gdoc("Copy of Discovery %d.docx" % i, 20000 + i) for i in range(5)]
        kept, dropped = C.dedupe_files(originals + copies)
        self.assertEqual(len(kept), 5)
        self.assertEqual(len(dropped), 5)
        self.assertTrue(all(not C.is_copy_named(C.file_name(f)) for f in kept))


class TestReferenceStandards(unittest.TestCase):
    """The two worked examples the spec gives as the correctness bar."""

    def test_card_414_heart_id(self):
        # 1 combined diagram, 10 in Individual Diagrams, 32 app screenshots.
        candidates = [(png("Detailed Workflow Diagram.png"), "")]
        candidates += [(png("%d.png" % i), "Individual Diagrams")
                       for i in range(1, 11)]
        candidates += [(png("Screenshot 2026-01-%02d at 09.10.11.png" % (i + 1)),
                        "Application Screenshots") for i in range(32)]

        diagrams, individual, skipped = [], [], []
        for f, folder in candidates:
            action, dest, _ = C.classify_file(f, folder)
            if action == "skip":
                skipped.append(f)
            elif dest == "individual_diagrams":
                individual.append(f)
            elif dest == "diagrams":
                diagrams.append(f)

        self.assertEqual(len(diagrams), 1, "one combined overview diagram")
        self.assertEqual(len(individual), 10, "ten individual diagrams")
        self.assertEqual(len(diagrams) + len(individual), 11, "11 diagrams total")
        self.assertEqual(len(skipped), 32, "32 app screenshots excluded")

    def test_card_460_diamond_resources(self):
        candidates = [(png("System Architecture Diagram.png"), "")]
        candidates += [(png("Flow %d.png" % i), "Diagrams") for i in range(1, 9)]
        candidates += [(png("IMG_20%02d.PNG" % i), "Raw") for i in range(12)]

        copied = [f for f, folder in candidates
                  if C.classify_file(f, folder)[0] == "copy"]
        self.assertEqual(len(copied), 9, "9 diagrams for card 460")


class TestCardNormalisation(unittest.TestCase):
    def test_mcp_snapshot_shape(self):
        raw = {
            "name": "CTLG - Workflow Automation",
            "desc": "See https://drive.google.com/drive/folders/1abcdefghijklmn",
            "webUrl": "https://trello.com/c/2L4A2YBR/462-ctlg-workflow-automation",
            "url": "https://trello.com/c/2L4A2YBR/462-ctlg-workflow-automation",
            "list": {"name": "Done, (Waiting on Decision)"},
            "labels": [{"name": "Salman Asif", "color": "blue"}],
            "due": "2026-09-01T19:49:00.000Z", "dueComplete": True,
            "lastActivityAt": "2026-09-03T13:39:14.264Z", "closed": False,
        }
        c = normalise_card(raw)
        self.assertEqual(c["id_short"], 462)
        self.assertEqual(c["list_name"], "Done, (Waiting on Decision)")
        self.assertEqual(c["labels"], ["Salman Asif"])
        self.assertTrue(c["due_complete"])

    def test_live_api_shape(self):
        raw = {
            "idShort": 295, "name": "Riley Infinity - EdTech Software",
            "desc": "", "shortUrl": "https://trello.com/c/AbCdEfGh",
            "closed": False, "dueComplete": False, "due": None,
            "dateLastActivity": "2026-08-01T00:00:00.000Z",
            "labels": [{"name": "BA"}],
            "attachments": [{"name": "spec", "url": "https://x.example/a.pdf",
                             "bytes": 100}],
        }
        c = normalise_card(raw, "Done, (Waiting on Decision)")
        self.assertEqual(c["id_short"], 295)
        self.assertEqual(c["url"], "https://trello.com/c/AbCdEfGh")
        self.assertEqual(len(c["attachments"]), 1)


class TestCardMarkdown(unittest.TestCase):
    def _card(self, desc=""):
        return normalise_card({
            "name": "Seaver Construction - Procore-like Construction Platform",
            "desc": desc,
            "webUrl": "https://trello.com/c/XyZ/452-seaver-construction",
            "list": {"name": "Done, (Waiting on Decision)"},
            "labels": [], "due": None, "dueComplete": False, "closed": False,
            "lastActivityAt": "2026-08-01T00:00:00.000Z",
        })

    def test_contains_required_sections(self):
        md = render_card_md(self._card("Body text."), [("A.docx", "https://l")],
                            [("big.mp4", "video", 900000000)])
        for needle in ("# Seaver Construction", "(#452)", "- **Card:**",
                       "- **List:**", "- **Status:**", "- **Last activity:**",
                       "- **Labels:** none", "## Description",
                       "## Linked URLs found in description/attachments",
                       "## Files copied", "## Files skipped"):
            self.assertIn(needle, md, needle)

    def test_description_is_verbatim(self):
        desc = "Line one\n\n- bullet *not* rewritten\n\nhttps://x.example/a"
        md = render_card_md(self._card(desc), [], [])
        self.assertIn(desc, md)

    def test_no_files_renders_none_markers(self):
        md = render_card_md(self._card("no links here"), [], [])
        self.assertIn("## Files copied\n\n_(none)_", md)

    def test_skipped_file_size_rendered_in_mb(self):
        md = render_card_md(self._card(), [], [("v.mp4", "video", 52428800)])
        self.assertIn("(50.00 MB)", md)


if __name__ == "__main__":
    unittest.main(verbosity=2)


class TestPrimarySelection(unittest.TestCase):
    def test_fewest_copy_markers_wins_over_newest(self):
        # Real card-295 shape: Drive stamps the newest time on the copy.
        original = dict(gdoc("Report.xlsx", 15798), modifiedTime="2025-08-19T00:00:00Z")
        copy1 = dict(gdoc("Copy of Report.xlsx", 15798), modifiedTime="2025-08-21T00:00:00Z")
        copy2 = dict(gdoc("Copy of Copy of Report.xlsx", 15798), modifiedTime="2025-08-22T00:00:00Z")
        kept, dropped = C.dedupe_files([copy2, copy1, original])
        self.assertEqual([C.file_name(f) for f in kept], ["Report.xlsx"])
        self.assertEqual(len(dropped), 2)

    def test_numeric_suffix_original_beats_copy_prefix(self):
        a = dict(gdoc("Spec.docx (1).pdf", 195825), modifiedTime="2025-08-21T12:33:12Z")
        b = dict(gdoc("Copy of Spec.docx (1).pdf", 195825), modifiedTime="2025-08-21T14:12:30Z")
        kept, _ = C.dedupe_files([b, a])
        self.assertEqual([C.file_name(f) for f in kept], ["Spec.docx (1).pdf"])

    def test_copy_depth_counts_markers(self):
        self.assertEqual(C.copy_depth("Report.xlsx"), 0)
        self.assertEqual(C.copy_depth("Copy of Report.xlsx"), 1)
        self.assertEqual(C.copy_depth("Copy of Copy of Report.xlsx"), 2)
        self.assertEqual(C.copy_depth("Report (1).xlsx"), 1)


class TestQueueSelection(unittest.TestCase):
    """Selection against the real 368-card snapshot, no credentials needed."""

    @classmethod
    def setUpClass(cls):
        import json, os
        from archive_trello_to_drive import normalise_card
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "data", "trello_snapshot.json")
        with open(path) as fh:
            cls.cards = [normalise_card(c) for c in json.load(fh)]

    def test_snapshot_has_every_card(self):
        self.assertEqual(len(self.cards), 368)
        self.assertTrue(all(c["id_short"] is not None for c in self.cards))

    def test_all_list_names_are_mapped(self):
        from archive_trello_to_drive import LIST_TO_FOLDER
        unmapped = {c["list_name"] for c in self.cards} - set(LIST_TO_FOLDER)
        self.assertEqual(unmapped, set())

    def test_skips_the_32_already_done_cards(self):
        from archive_trello_to_drive import build_queue, ALREADY_DONE
        queue, skipped = build_queue(self.cards, skip_done=frozenset(ALREADY_DONE))
        self.assertEqual(skipped, 32)
        self.assertEqual(len(queue), 336)
        self.assertFalse(set(ALREADY_DONE) & {c["id_short"] for c in queue})

    def test_manifest_completions_also_skipped(self):
        from archive_trello_to_drive import build_queue, ALREADY_DONE
        pilot = {295, 448, 452, 447, 442, 119, 436, 116, 458}
        queue, skipped = build_queue(
            self.cards, skip_done=frozenset(ALREADY_DONE),
            done_by_manifest=frozenset(pilot))
        self.assertEqual(skipped, 41)
        self.assertEqual(len(queue), 327)
        self.assertFalse(pilot & {c["id_short"] for c in queue})

    def test_remaining_queue_is_lists_05_06_07(self):
        from archive_trello_to_drive import build_queue, ALREADY_DONE, LIST_TO_FOLDER
        pilot = {295, 448, 452, 447, 442, 119, 436, 116, 458}
        queue, _ = build_queue(self.cards, skip_done=frozenset(ALREADY_DONE),
                               done_by_manifest=frozenset(pilot))
        counts = {}
        for c in queue:
            counts[LIST_TO_FOLDER[c["list_name"]][0]] = \
                counts.get(LIST_TO_FOLDER[c["list_name"]][0], 0) + 1
        self.assertEqual(counts, {"05 - Closed Won": 28,
                                  "06 - Closed Lost": 80,
                                  "07 - On Hold": 219})

    def test_list_filter_selects_by_number(self):
        from archive_trello_to_drive import build_queue, parse_list_filter, ALREADY_DONE
        queue, _ = build_queue(self.cards, want_lists=parse_list_filter("05"),
                               skip_done=frozenset(ALREADY_DONE))
        self.assertEqual(len(queue), 28)
        self.assertTrue(all(c["list_name"] == "Closed Won" for c in queue))

    def test_card_filter_selects_exact_ids(self):
        from archive_trello_to_drive import build_queue
        queue, _ = build_queue(self.cards, want_cards={295, 452})
        self.assertEqual(sorted(c["id_short"] for c in queue), [295, 452])

    def test_queue_is_ordered_by_list_then_card(self):
        from archive_trello_to_drive import build_queue, ALREADY_DONE, LIST_TO_FOLDER
        queue, _ = build_queue(self.cards, skip_done=frozenset(ALREADY_DONE))
        keys = [(LIST_TO_FOLDER[c["list_name"]][0], c["id_short"]) for c in queue]
        self.assertEqual(keys, sorted(keys))

    def test_empty_pending_list_contributes_nothing(self):
        self.assertEqual(
            [c for c in self.cards if c["list_name"] == "BA Team (Pending)"], [])
