import re

CHECKBOX_RE = re.compile(r"^\s*[-*+]\s+\[([ xX])\]", re.MULTILINE)
HEADING_RE = re.compile(r"^(#{1,6})\s+", re.MULTILINE)
TAG_RE = re.compile(r"\{\{\s*progress(?:_(section))?\s*\}\}")

def get_color_class(pct: int) -> str:
    if pct < 30:
        return "is-low"
    if pct < 80:
        return "is-mid"
    return "is-high"

def render_bar(checked: int, total: int, label_prefix: str = "") -> str:
    pct = round((checked / total) * 100) if total else 0
    color_cls = get_color_class(pct)
    prefix = f"{label_prefix} : " if label_prefix else ""
    return (
        f'<div class="mkdocs-progress">'
        f'<div class="mkdocs-progress-bar {color_cls}" style="width: {pct}%;"></div>'
        f'<span class="mkdocs-progress-label">{prefix}{checked}/{total} ({pct}%)</span>'
        f'</div>'
    )

def get_section_slice(markdown: str, tag_pos: int) -> str:
    headings = list(HEADING_RE.finditer(markdown))
    prev_heading = None
    for h in headings:
        if h.start() < tag_pos:
            prev_heading = h
        else:
            break

    if not prev_heading:
        return markdown

    level = len(prev_heading.group(1))
    start = prev_heading.end()
    end = len(markdown)

    for h in headings:
        if h.start() > tag_pos and len(h.group(1)) <= level:
            end = h.start()
            break

    return markdown[start:end]

def on_page_markdown(markdown, **kwargs):
    if "{{ progress" not in markdown:
        return markdown

    scope_md = markdown.split("<!-- progress-stop -->").pop(0)
    all_matches = CHECKBOX_RE.findall(scope_md)
    global_total = len(all_matches)
    global_checked = sum(1 for m in all_matches if m.lower() == "x")

    def replace_tag(match):
        is_section = match.group(1) == "section"
        if not is_section:
            return render_bar(global_checked, global_total, "Avancement global")

        section_text = get_section_slice(markdown, match.start())
        sec_matches = CHECKBOX_RE.findall(section_text)
        sec_total = len(sec_matches)
        sec_checked = sum(1 for m in sec_matches if m.lower() == "x")
        return render_bar(sec_checked, sec_total)

    return TAG_RE.sub(replace_tag, markdown)