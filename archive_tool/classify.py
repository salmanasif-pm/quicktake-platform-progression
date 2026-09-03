"""
Pure classification / naming / discovery helpers for the Trello -> Drive archive.

No I/O and no Drive or Trello calls live in this module: everything here is a
deterministic function over plain dicts, so the rules in spec section 7 can be
unit-tested without credentials or network access.
"""

import re
import unicodedata

# --- Drive mime types -------------------------------------------------------

GOOGLE_FOLDER = "application/vnd.google-apps.folder"
GOOGLE_DOC = "application/vnd.google-apps.document"
GOOGLE_SHEET = "application/vnd.google-apps.spreadsheet"
GOOGLE_SLIDES = "application/vnd.google-apps.presentation"
GOOGLE_DRAWING = "application/vnd.google-apps.drawing"

GOOGLE_NATIVE_COPYABLE = {
    GOOGLE_DOC,
    GOOGLE_SHEET,
    GOOGLE_SLIDES,
    GOOGLE_DRAWING,
}

# --- extension groups (spec section 7) --------------------------------------

COPY_EXTS = {
    "docx", "doc", "xlsx", "xlsm", "xls", "pptx", "ppt",
    "pdf", "txt", "csv", "md", "rtf", "odt", "ods",
}
VIDEO_EXTS = {"mp4", "mov", "avi", "mkv", "webm", "m4v", "wmv", "flv"}
AUDIO_EXTS = {"m4a", "mp3", "wav", "aac", "ogg", "flac", "wma"}
ARCHIVE_EXTS = {"zip", "rar", "7z", "tar", "gz", "tgz", "bz2", "xz", "jar", "war"}
SQL_EXTS = {"sql", "dump", "bak", "mdb", "sqlite", "db"}
IMAGE_EXTS = {"png", "jpg", "jpeg", "svg", "webp", "gif", "bmp", "tif", "tiff"}

# Diagram-eligible extensions per spec: images plus pdf.
DIAGRAM_EXTS = {"png", "jpg", "jpeg", "svg", "webp", "pdf"}

OVERSIZE_LIMIT = 50 * 1024 * 1024          # 50 MB
STUB_LIMIT = 1024                          # Google Docs <= 1 KiB are placeholders

# --- diagram / screenshot signals -------------------------------------------

DIAGRAM_KEYWORDS = (
    "diagram", "workflow", "work flow", "user flow", "userflow",
    "system map", "systemmap", "architecture", "process flow", "data flow",
    "dataflow", "integration", "wireframe", "gantt", "flow",
)

# `architecture` and `integration` are ordinary words in document titles
# ("Level 3 Beta Architecture Materials FINAL.pdf", "Heart ID Integration"),
# so on paged formats they are too weak to mean "diagram" on their own. On a
# raster/vector image they still are: a PNG called `Architecture.png` is a
# diagram. Paged formats therefore need one of the strong signals below, or a
# diagram-ish containing folder.
WEAK_DIAGRAM_KEYWORDS = ("architecture", "integration")
PAGED_EXTS = {"pdf"}

DIAGRAM_FOLDERS = {
    "diagrams", "diagram", "individual diagrams", "workflows", "workflow",
    "architecture", "system maps", "system map", "final diagrams",
}

# Folders whose contents are raw reference imagery, never final diagrams.
EXCLUDED_IMAGE_FOLDERS = {
    "screenshots", "screen shots", "application screenshots", "app screenshots",
    "app's screenshorts", "apps screenshorts", "app screenshorts",
    "raw", "game images", "images", "reference images", "photos",
}

# Filenames that are screenshots / camera dumps rather than deliverables.
EXCLUDED_NAME_PATTERNS = (
    re.compile(r"^screen\s*shot", re.I),
    re.compile(r"^screenshot", re.I),
    re.compile(r"^img[_\-]?\d", re.I),
    re.compile(r"^pxl[_\-]?\d", re.I),
    re.compile(r"^dscn?[_\-]?\d", re.I),
    re.compile(r"^photo[_\-\s]", re.I),
    re.compile(r"^whatsapp\s+image", re.I),
    re.compile(r"^image[_\-\s]?\d+$", re.I),
    re.compile(r"^\d{8}[_\-]\d{6}", re.I),      # 20240131_115959.jpg
    re.compile(r"^capture\s*\d*$", re.I),
)

# Cache / temp / system junk.
JUNK_NAME_PATTERNS = (
    re.compile(r"^\.ds_store$", re.I),
    re.compile(r"^thumbs\.db$", re.I),
    re.compile(r"^desktop\.ini$", re.I),
    re.compile(r"^~\$", re.I),
    re.compile(r"^\._", re.I),
    re.compile(r"\.tmp$", re.I),
    re.compile(r"\.crdownload$", re.I),
    re.compile(r"\.part$", re.I),
)

# --- URL discovery (spec section 7 steps 1-2) -------------------------------

RE_DRIVE_FOLDER = re.compile(
    r"https?://drive\.google\.com/drive/(?:u/\d+/)?folders/([A-Za-z0-9_-]{10,})"
)
RE_DOCS_FILE = re.compile(
    r"https?://docs\.google\.com/(document|spreadsheets|presentation|drawings)"
    r"/d/([A-Za-z0-9_-]{10,})"
)
RE_DRIVE_FILE = re.compile(
    r"https?://drive\.google\.com/(?:file/d/|open\?id=|uc\?id=)([A-Za-z0-9_-]{10,})"
)
RE_ANY_URL = re.compile(r"https?://[^\s<>\)\]\"'}]+")

_ILLEGAL_NAME_CHARS = re.compile(r'[/\\:*?"<>|]')
_CONTROL_CHARS = re.compile(r"[\x00-\x1f\x7f]")
_WS = re.compile(r"\s+")


# --- naming -----------------------------------------------------------------

def sanitise_name(name, limit=120):
    """Strip Drive/OS-illegal characters, collapse whitespace, trim to `limit`."""
    if not name:
        return "untitled"
    name = unicodedata.normalize("NFC", str(name))
    name = _ILLEGAL_NAME_CHARS.sub("", name)
    name = _CONTROL_CHARS.sub(" ", name)
    name = _WS.sub(" ", name).strip().strip(".").strip()
    if len(name) > limit:
        name = name[:limit].rstrip()
    return name or "untitled"


def card_folder_name(id_short, card_name, limit=120):
    """`<idShort> - <sanitised card name>`, keeping the title meaningful."""
    prefix = "%s - " % id_short
    return prefix + sanitise_name(card_name, limit=max(20, limit - len(prefix)))


def ext_of(name):
    if not name or "." not in name:
        return ""
    return name.rsplit(".", 1)[-1].lower().strip()


def base_name(name):
    """Filename without its extension."""
    if not name:
        return ""
    return name.rsplit(".", 1)[0] if "." in name else name


# --- discovery --------------------------------------------------------------

def extract_folder_ids(text):
    """Drive folder ids referenced in free text, in first-seen order."""
    return _dedupe(RE_DRIVE_FOLDER.findall(text or ""))


def extract_file_ids(text):
    """Directly-linked Drive/Docs file ids in free text, in first-seen order."""
    out = [fid for _kind, fid in RE_DOCS_FILE.findall(text or "")]
    out += RE_DRIVE_FILE.findall(text or "")
    return _dedupe(out)


def extract_urls(*texts):
    """Every http(s) URL across the given texts, deduped, first-seen order."""
    found = []
    for t in texts:
        if not t:
            continue
        for u in RE_ANY_URL.findall(t):
            found.append(u.rstrip(".,;:!)]}>\"'"))
    return _dedupe(found)


def _dedupe(seq):
    seen, out = set(), []
    for x in seq:
        if x and x not in seen:
            seen.add(x)
            out.append(x)
    return out


# --- size helpers -----------------------------------------------------------

def file_size(f):
    """Bytes for a Drive file dict, tolerating v3's absent `size` on native docs."""
    for key in ("size", "fileSize", "quotaBytesUsed"):
        v = f.get(key)
        if v not in (None, ""):
            try:
                return int(v)
            except (TypeError, ValueError):
                continue
    return None


def file_name(f):
    return f.get("name") or f.get("title") or ""


def is_google_native(f):
    return str(f.get("mimeType", "")).startswith("application/vnd.google-apps.")


# --- diagram routing --------------------------------------------------------

def _matches(patterns, text):
    return any(p.search(text or "") for p in patterns)


def is_excluded_image(name, folder_name=""):
    """True when an image is raw screenshot/reference material, not a deliverable."""
    if (folder_name or "").strip().lower() in EXCLUDED_IMAGE_FOLDERS:
        return True
    return _matches(EXCLUDED_NAME_PATTERNS, base_name(name))


def has_diagram_keyword(name, strong_only=False):
    low = (base_name(name) or "").lower()
    keywords = DIAGRAM_KEYWORDS
    if strong_only:
        keywords = tuple(k for k in DIAGRAM_KEYWORDS
                         if k not in WEAK_DIAGRAM_KEYWORDS)
    return any(k in low for k in keywords)


def is_diagram(f, folder_name=""):
    """
    Classify a copy-worthy file as a final diagram.

    Filename and containing-folder name decide this, never mime type alone:
    final diagrams and raw screenshots are both PNG.
    """
    name = file_name(f)
    mime = str(f.get("mimeType", ""))
    folder_low = (folder_name or "").strip().lower()

    # Raw imagery is never a diagram, whatever it is called.
    if is_excluded_image(name, folder_name):
        return False

    # Google Drawings are diagrams by construction.
    if mime == GOOGLE_DRAWING:
        return True

    # Everything inside a diagram-ish folder is a diagram.
    if folder_low in DIAGRAM_FOLDERS:
        return True

    ext = ext_of(name)
    if ext in DIAGRAM_EXTS:
        return has_diagram_keyword(name, strong_only=ext in PAGED_EXTS)

    # Slides that are explicitly a diagram deliverable.
    if mime == GOOGLE_SLIDES:
        return has_diagram_keyword(name, strong_only=True)

    return False


def is_individual_diagram_folder(folder_name):
    return (folder_name or "").strip().lower() in {
        "individual diagrams", "individual diagram",
    }


# --- the main per-file decision --------------------------------------------

def classify_file(f, folder_name="", oversize_limit=OVERSIZE_LIMIT):
    """
    Decide what to do with one Drive file.

    Returns (action, destination, reason) where action is "copy" or "skip" and
    destination is "sources" | "diagrams" | "individual_diagrams" | None.
    """
    name = file_name(f)
    mime = str(f.get("mimeType", ""))
    ext = ext_of(name)
    size = file_size(f)

    if mime == GOOGLE_FOLDER:
        return ("skip", None, "folder")

    if _matches(JUNK_NAME_PATTERNS, name):
        return ("skip", None, "cache/temp/system file")

    # Drive stores some recordings as a native video type with no extension.
    if ext in VIDEO_EXTS or mime.startswith("video/") or mime.endswith(".vid"):
        return ("skip", None, "video")
    if ext in AUDIO_EXTS:
        return ("skip", None, "audio")
    if ext in ARCHIVE_EXTS:
        return ("skip", None, "archive")
    if ext in SQL_EXTS:
        return ("skip", None, "sql/db dump")

    is_doclike = (
        mime in (GOOGLE_DOC, GOOGLE_SHEET, GOOGLE_SLIDES)
        or ext in {"pdf", "docx", "doc", "xlsx", "xlsm", "xls", "pptx", "ppt"}
    )

    # Empty Google Docs stubs.
    if mime in (GOOGLE_DOC, GOOGLE_SHEET, GOOGLE_SLIDES, GOOGLE_DRAWING):
        if size is not None and size <= STUB_LIMIT:
            return ("skip", None, "empty stub (%s bytes)" % size)

    # Oversize, unless a clear doc/sheet/pdf deliverable.
    if size is not None and size > oversize_limit and not is_doclike:
        return ("skip", None, "oversized (%.1f MB)" % (size / 1048576.0))

    if is_diagram(f, folder_name):
        dest = ("individual_diagrams"
                if is_individual_diagram_folder(folder_name) else "diagrams")
        return ("copy", dest, "diagram")

    # Images that are not diagrams are raw material.
    if ext in IMAGE_EXTS:
        return ("skip", None, "image is not a final diagram")

    if mime in GOOGLE_NATIVE_COPYABLE:
        return ("copy", "sources", "google native document")

    if ext in COPY_EXTS:
        return ("copy", "sources", ".%s document" % ext)

    if is_google_native(f):
        return ("skip", None, "unsupported google type (%s)" % mime)

    return ("skip", None,
            "not a document type (.%s)" % ext if ext else "no file extension")


# --- duplicate suppression (spec section 7) --------------------------------

RE_COPY_PREFIX = re.compile(r"^(?:copy of|copia de|copie de)\s+", re.I)
RE_COPY_SUFFIX = re.compile(r"\s*\((?:\d+|copy)\)\s*$", re.I)


def canonical_name(name):
    """
    `Copy of Foo.docx`, `Copy of Copy of Foo.docx` and `Foo (1).docx` all
    reduce to `foo.docx`. Drive stacks the prefix on repeated copies, so it is
    stripped repeatedly rather than once.
    """
    b, e = base_name(name), ext_of(name)
    b = b or ""
    while True:
        stripped = RE_COPY_PREFIX.sub("", b, count=1)
        stripped = RE_COPY_SUFFIX.sub("", stripped, count=1).strip()
        if stripped == b:
            break
        b = stripped
    return (b.lower() + ("." + e if e else "")).strip()


def is_copy_named(name):
    b = base_name(name) or ""
    return bool(RE_COPY_PREFIX.match(b) or RE_COPY_SUFFIX.search(b))


def copy_depth(name):
    """
    How many copy markers a filename carries.

    Used to pick the primary of a duplicate group: `X` beats `Copy of X`, which
    beats `Copy of Copy of X`. Ranking by this rather than by modified time
    matters because Drive stamps the newest time on the *copy*, so "newest"
    would otherwise keep the most-derived name.
    """
    b = base_name(name) or ""
    depth = 0
    while True:
        stripped = RE_COPY_PREFIX.sub("", b, count=1)
        if stripped != b:
            depth += 1
            b = stripped
            continue
        stripped = RE_COPY_SUFFIX.sub("", b, count=1).strip()
        if stripped != b:
            depth += 1
            b = stripped
            continue
        return depth


def sizes_differ_meaningfully(a, b, rel=0.02, absolute=1024):
    """True when two byte counts look like different generations, not one file."""
    if a is None or b is None:
        return False          # cannot tell -> treat as same, prefer the original
    if a == b:
        return False
    return abs(a - b) > absolute and abs(a - b) > rel * max(a, b)


def _neg_time(value):
    """Sort key that puts the newest timestamp first among equal copy depths."""
    s = str(value or "")
    return tuple(-ord(ch) for ch in s)


def dedupe_files(files):
    """
    Drop `Copy of X` when X is present and the two look like the same file.

    Returns (kept, dropped) where dropped items are (file, reason) pairs.
    Files whose sizes differ meaningfully are both kept: they are different
    generations rather than duplicates.
    """
    groups = {}
    order = []
    for f in files:
        key = canonical_name(file_name(f))
        if key not in groups:
            groups[key] = []
            order.append(key)
        groups[key].append(f)

    kept, dropped = [], []
    for key in order:
        group = groups[key]
        if len(group) == 1:
            kept.extend(group)
            continue

        # Fewest copy markers wins; ties broken by the newest modified time.
        primary = sorted(
            group,
            key=lambda f: (copy_depth(file_name(f)),
                           _neg_time(f.get("modifiedTime"))),
        )[0]
        kept.append(primary)

        p_size = file_size(primary)
        for f in group:
            if f is primary:
                continue
            if sizes_differ_meaningfully(file_size(f), p_size):
                kept.append(f)          # different generation, keep both
            else:
                dropped.append((f, "duplicate of %s" % file_name(primary)))
    return kept, dropped
