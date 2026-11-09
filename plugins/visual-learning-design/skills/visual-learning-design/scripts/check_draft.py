#!/usr/bin/env python3
"""Check a Markdown draft of teaching material against the countable rules of
the visual-learning-design skill.

Handles three kinds of draft:
  slides    a slide outline with "## Slide N" sections
  carousel  a social carousel with "## Slide N" sections and alt text
  video     a video or short-form script written as a Markdown table with a
            voiceover/narration column

Usage:
  python check_draft.py DRAFT.md [--type auto|slides|carousel|video]
                                 [--budget N] [--wpm N] [--seconds N] [--json]

Exit code: 0 when nothing FAILs (WARNs allowed), 1 when something FAILs,
2 when the file can't be parsed.

The checker reads the format the skill's playbooks ask for:
  ## Slide 3: <working title>
  **Headline:** <the slide's takeaway sentence>
  **On screen:**
  > the literal text that appears on the slide, one line per element
  **Visual:** <description of the graphic, not counted>
  **Speaker notes:** <what the presenter says, not counted>
  **Alt text:** <carousel only>

Drafts in other formats still get checked, but word counts are marked
"estimated" because descriptions may be counted as on-screen text.
Only the Python standard library is used.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field

# ---------------------------------------------------------------- parsing --

UNIT_RE = re.compile(r"^#{2,4}\s+(?:slide|frame|card)\s*(\d+)\b(.*)$", re.I)
FIELD_RE = re.compile(r"^(?:[-*]\s+)?\*\*([^*]+?)\*\*\s*:?\s*(.*)$")
FIELD_VOCAB = ("headline", "title", "assertion", "on slide", "on-slide", "on screen", "on-screen",
               "slide text", "text", "body", "subtext", "subtitle", "callout", "question", "bullets",
               "visual", "build", "speaker notes", "notes", "presenter notes", "script", "alt",
               "caption", "timing", "layout", "design", "graphic", "image", "chart", "diagram")
DESCRIPTION_CUES = re.compile(r"\b(diagram|labell?ed|arrow|icon|sketch|drawn|draw|shows?|showing|"
                              r"appears?|left|right|below|above|beside|next to|layout|graph|chart)\b", re.I)
LITERAL_RE = re.compile(r"\*\*([^*]+)\*\*|\"([^\"]+)\"|“([^”]+)”")
WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’$%.,\-]*")

HEADLINE_LABELS = {"headline", "title", "headline text", "slide title", "assertion"}
ONSCREEN_PREFIXES = ("on slide", "on-slide", "on screen", "on-screen", "slide text",
                     "text", "body", "subtext", "subtitle", "callout", "question",
                     "caption on slide", "bullets")
NOTES_PREFIXES = ("speaker notes", "notes", "presenter notes", "script")
ALT_PREFIXES = ("alt text", "alt-text", "alt")

PROMPT_RE = re.compile(r"\b(predict|guess|your turn|test yourself|quiz|try it|try this|"
                       r"explain|comment|answer|sketch|write|check yourself|which|why|how)\b", re.I)
VIEWER_PROMPT_RE = re.compile(r"\b(your turn|comment|guess|predict|try it|try this|test yourself|quiz|"
                              r"answer|explain|sketch|what do you think|which would|pause)\b", re.I)
MUSIC_RE =re.compile(r"\b(music|soundtrack|instrumental|song|trending (?:sound|audio)|beat|lo-?fi)\b", re.I)
UNDER_RE = re.compile(r"\b(under|underneath|behind|background|throughout|bed|beneath)\b", re.I)
NEGATION_RE = re.compile(r"\b(no|not|without|avoid|never|don'?t|skip|cut|mute|nothing)\b", re.I)


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def clean_literal(text: str) -> str:
    """Strip Markdown and placement notes so only displayed words remain."""
    text = re.sub(r"\([^)]*\)", " ", text)          # (on the navy block), (small)
    text = re.sub(r"\[[^\]]*\]\([^)]*\)", " ", text)  # links
    text = re.sub(r"[*_`>#|]", " ", text)
    text = re.sub(r"^\s*[-•]\s*", " ", text, flags=re.M)
    text = re.sub(r"\b(title|subtitle|text|question|caption|label)\s*:", " ", text, flags=re.I)
    return text


def norm_label(label: str) -> str:
    label = re.sub(r"\([^)]*\)", "", label).strip().rstrip(":").strip().lower()
    return label


@dataclass
class Unit:
    number: int
    heading: str
    fields: list[tuple[str, str]] = field(default_factory=list)

    def get(self, prefixes) -> list[str]:
        out = []
        for label, body in self.fields:
            if any(label == p or label.startswith(p) for p in prefixes):
                out.append(body)
        return out


def parse_units(md: str) -> list[Unit]:
    units: list[Unit] = []
    current: Unit | None = None
    label, buf = None, []

    def flush():
        nonlocal label, buf
        if current is not None and label is not None:
            current.fields.append((label, "\n".join(buf).strip()))
        label, buf = None, []

    for line in md.splitlines():
        m = UNIT_RE.match(line)
        if m:
            flush()
            current = Unit(int(m.group(1)), m.group(2).strip(" :—-"))
            units.append(current)
            continue
        if current is None:
            continue
        if re.match(r"^#{1,3}\s", line) or re.match(r"^---+\s*$", line):
            flush()
            if re.match(r"^#{1,3}\s", line):
                current = None
            continue
        f = FIELD_RE.match(line)
        if f and norm_label(f.group(1)).startswith(FIELD_VOCAB):
            flush()
            label, buf = norm_label(f.group(1)), [f.group(2)]
        elif label is not None:
            buf.append(line)
    flush()
    return units


def split_headline_and_body(unit: Unit) -> tuple[str, str, bool]:
    """Return (headline, on-screen body, exact) for a slide unit."""
    headline = " ".join(unit.get(HEADLINE_LABELS)).strip()
    bodies = [b for lab, b in unit.fields
              if lab not in HEADLINE_LABELS
              and any(lab == p or lab.startswith(p) for p in ONSCREEN_PREFIXES)]
    body = "\n".join(bodies)
    quoted = [ln for ln in body.splitlines() if ln.strip().startswith(">")]
    exact = bool(quoted)
    if exact:
        body = "\n".join(quoted)
    if not headline:
        m = re.search(r"^\s*[-*]?\s*title\s*:\s*(.+)$", body, re.I | re.M)
        if m:
            headline = m.group(1)
            body = body.replace(m.group(0), "")
    if not headline and quoted:
        first = quoted[0]
        headline, body = first, "\n".join(quoted[1:])
    if not exact and DESCRIPTION_CUES.search(body):
        # A prose description of the slide: count only the bold or quoted
        # strings, which are usually the literal labels it names.
        literals = [next(g for g in m.groups() if g) for m in LITERAL_RE.finditer(body)]
        if literals:
            body = "\n".join(literals)
    return clean_literal(headline).strip(), clean_literal(body), exact


def parse_tables(md: str) -> list[tuple[list[str], list[list[str]]]]:
    tables, lines = [], md.splitlines()
    i = 0
    while i < len(lines) - 1:
        if lines[i].strip().startswith("|") and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            header = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            rows, j = [], i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                rows.append([c.strip() for c in lines[j].strip().strip("|").split("|")])
                j += 1
            tables.append((header, rows))
            i = j
        else:
            i += 1
    return tables


def classify_columns(header: list[str]) -> dict[str, int]:
    roles: dict[str, int] = {}
    for idx, h in enumerate(header):
        hl = re.sub(r"\([^)]*\)", "", h).lower()
        if "narration" in hl or "voiceover" in hl or "voice-over" in hl or "spoken" in hl \
                or re.search(r"\bvo\b", hl) or (re.search(r"\baudio\b", hl) and "visual" not in hl):
            roles.setdefault("narration", idx)
        elif "caption" in hl:
            roles.setdefault("captions", idx)
        elif "text" in hl or "label" in hl:
            roles.setdefault("onscreen", idx)
        elif "visual" in hl or "on screen" in hl or "on-screen" in hl or "shot" in hl:
            roles.setdefault("visual", idx)
        elif "time" in hl or hl in {"#", "beat"}:
            roles.setdefault("time", idx)
    return roles


def find_script_table(md: str):
    for header, rows in parse_tables(md):
        roles = classify_columns(header)
        if "narration" in roles and len(rows) >= 2:
            return header, rows, roles
    return None

# ----------------------------------------------------------------- report --


@dataclass
class Result:
    level: str          # PASS, WARN, FAIL, INFO
    check: str
    detail: str


class Report:
    def __init__(self, kind: str, path: str):
        self.kind, self.path, self.results = kind, path, []

    def add(self, level, check, detail):
        self.results.append(Result(level, check, detail))

    @property
    def failed(self):
        return any(r.level == "FAIL" for r in self.results)

    def text(self) -> str:
        out = [f"Draft check: {self.path}  (type: {self.kind})", ""]
        for r in self.results:
            out.append(f"[{r.level}] {r.check}: {r.detail}")
        counts = {lvl: sum(r.level == lvl for r in self.results) for lvl in ("FAIL", "WARN", "PASS")}
        out += ["", f"{counts['FAIL']} fail, {counts['WARN']} warn, {counts['PASS']} pass"]
        return "\n".join(out)

    def json(self) -> str:
        return json.dumps({"path": self.path, "type": self.kind, "failed": self.failed,
                           "results": [r.__dict__ for r in self.results]}, indent=2)

# ---------------------------------------------------------- shared checks --


def music_check(md: str, rep: Report):
    hits = []
    for sentence in re.split(r"(?<=[.!?])\s+|\n", md):
        if MUSIC_RE.search(sentence) and UNDER_RE.search(sentence) and not NEGATION_RE.search(sentence):
            hits.append(sentence.strip()[:120])
    if hits:
        rep.add("FAIL", "music under narration",
                f"{len(hits)} line(s) put music or a sound bed under the explanation, e.g. \"{hits[0]}\". "
                "Coherence: remove it, or keep sound to before or after the narration.")
    else:
        rep.add("PASS", "music under narration", "no music under the explanation")

# ------------------------------------------------------------ slide checks --


def check_units(units: list[Unit], md: str, rep: Report, budget: int, carousel: bool):
    n = len(units)
    if carousel:
        lvl = "PASS" if 5 <= n <= 10 else "WARN"
        rep.add(lvl, "slide count", f"{n} slides (aim for 5-10, one idea per post)")
    else:
        rep.add("INFO", "slide count", f"{n} slides")

    over, estimated, short_heads, long_heads, no_head = [], False, [], [], []
    for u in units:
        head, body, exact = split_headline_and_body(u)
        estimated |= not exact
        hw, bw = len(words(head)), len(words(body))
        total = hw + bw
        if not head:
            no_head.append(u.number)
        elif hw < 4:
            short_heads.append(f"{u.number} (\"{head.strip()}\")")
        elif hw > 12 and not carousel:
            long_heads.append(f"{u.number} ({hw} words)")
        if total > budget:
            over.append((u.number, total))

    note = " (estimated: no '> ' on-screen block found, so descriptions may be counted)" if estimated else ""
    if over:
        worst = max(t for _, t in over)
        lvl = "FAIL" if worst > budget * 1.3 and not estimated else "WARN"
        listed = ", ".join(f"{num} ({t})" for num, t in over)
        rep.add(lvl, "on-screen words", f"over the ~{budget}-word budget, headline included: slide {listed}{note}. "
                "Move definitions or explanation to speaker notes or narration, or split the slide.")
    else:
        rep.add("PASS", "on-screen words", f"every slide within ~{budget} words, headline included{note}")

    if no_head:
        rep.add("WARN", "headlines", f"no headline found on slide {', '.join(map(str, no_head))}")
    if short_heads:
        rep.add("WARN", "headlines", "looks like a topic label, not a takeaway sentence: slide "
                + ", ".join(short_heads))
    if long_heads:
        rep.add("WARN", "headline length", "over ~12 words (won't fit two lines): slide " + ", ".join(long_heads))
    if not (no_head or short_heads or long_heads):
        rep.add("PASS", "headlines", "every slide has a sentence headline of a usable length")

    if carousel:
        per_unit = sum(1 for u in units if u.get(ALT_PREFIXES))
        m = re.search(r"^#{2,4}\s*alt[ -]?text.*$", md, re.I | re.M)
        section = 0
        if m:
            tail = md[m.end():]
            nxt = re.search(r"^#{1,4}\s", tail, re.M)
            tail = tail[:nxt.start()] if nxt else tail
            section = len(re.findall(r"^\s*(?:\d+[.)]|[-*])\s+\S", tail, re.M))
        have = max(per_unit, section)
        lvl = "PASS" if have >= n else "FAIL"
        rep.add(lvl, "alt text", f"{have} of {n} slides have alt text")
    else:
        missing = [u.number for u in units if not u.get(NOTES_PREFIXES)]
        if missing:
            rep.add("WARN", "speaker notes", f"missing on slide {', '.join(map(str, missing))}")
        else:
            rep.add("PASS", "speaker notes", "every slide has speaker notes")

    tail_text = " ".join(" ".join(b for _, b in u.fields if not _.startswith(ALT_PREFIXES))
                         for u in units[-3:])
    if "?" in tail_text and PROMPT_RE.search(tail_text):
        rep.add("PASS", "learner prompt", "the last slides ask the learner to answer, predict or apply")
    else:
        anywhere = any("?" in b and PROMPT_RE.search(b) for u in units for _, b in u.fields)
        rep.add("PASS" if anywhere else "WARN", "learner prompt",
                "a prompt appears earlier in the deck" if anywhere
                else "no question asking the learner to predict, answer or apply (generative activity)")

    if carousel:
        last = " ".join(b for _, b in units[-1].fields) if units else ""
        only_cta = re.search(r"\b(follow|save|share)\b", last, re.I) and "?" not in last
        if only_cta:
            rep.add("WARN", "ending", "last slide is only a save/share/follow call to action; end with a recap "
                    "and a question the viewer answers")

# ------------------------------------------------------------ video checks --


def check_video(md: str, rep: Report, wpm: int, seconds: int | None):
    found = find_script_table(md)
    if not found:
        rep.add("FAIL", "script table", "no Markdown table with a voiceover/narration column found")
        return
    header, rows, roles = found
    nar_i, vis_i, txt_i = roles.get("narration"), roles.get("visual"), roles.get("onscreen")

    def cell(row, i):
        return row[i] if i is not None and i < len(row) else ""

    narration = [re.sub(r"[*_\"“”]", "", cell(r, nar_i)) for r in rows]
    total_words = sum(len(words(x)) for x in narration)
    est = total_words / wpm * 60
    detail = f"{total_words} spoken words, about {est:.0f} s at {wpm} wpm"
    if seconds:
        lvl = "PASS" if abs(est - seconds) <= seconds * 0.25 else "WARN"
        rep.add(lvl, "runtime", f"{detail} (target {seconds} s)")
    else:
        rep.add("INFO", "runtime", detail)

    if vis_i is None:
        rep.add("WARN", "visual per line", "no visual column; pair every narration line with what is on screen")
    else:
        bare = [str(k + 1) for k, r in enumerate(rows) if cell(r, nar_i).strip() and not cell(r, vis_i).strip()]
        rep.add("WARN" if bare else "PASS", "visual per line",
                f"narration without a visual in row {', '.join(bare)}" if bare
                else f"all {len(rows)} rows pair narration with a visual (temporal contiguity)")

    if txt_i is not None:
        repeats, long_lines = [], []
        for k, r in enumerate(rows):
            spoken = " ".join(w.lower() for w in words(narration[k]))
            raw = cell(r, txt_i)
            literals = [next(g for g in m.groups() if g) for m in LITERAL_RE.finditer(raw)]
            segments = literals or re.split(r"<br>|/|·|\n|\bthen\b", raw)
            for seg in segments:
                seg = clean_literal(seg)
                sw = [w.lower() for w in words(seg)]
                if len(sw) > 10:
                    long_lines.append(str(k + 1))
                if len(sw) >= 6:
                    grams = [" ".join(sw[j:j + 3]) for j in range(len(sw) - 2)]
                    hit = sum(g in spoken for g in grams) / max(len(grams), 1)
                    if hit >= 0.7:
                        repeats.append(str(k + 1))
        if repeats:
            rep.add("FAIL", "redundant on-screen text", "on-screen text repeats the narration in row "
                    + ", ".join(sorted(set(repeats), key=int)) + ". Keep labels and key terms; let narration explain.")
        else:
            rep.add("PASS", "redundant on-screen text", "on-screen text doesn't duplicate narration sentences")
        if long_lines:
            rep.add("WARN", "on-screen text length", "an on-screen line runs over ~10 words in row "
                    + ", ".join(sorted(set(long_lines), key=int)))

    first = cell(rows[0], nar_i) + " " + cell(rows[0], txt_i)
    rep.add("PASS" if "?" in first else "WARN", "hook",
            "opens with a question" if "?" in first
            else "first beat doesn't pose the learning question; make the hook the question itself")

    end = cell(rows[-1], nar_i) + " " + cell(rows[-1], txt_i)
    ok = "?" in end and VIEWER_PROMPT_RE.search(end)
    rep.add("PASS" if ok else "WARN", "ending prompt",
            "ends with a question for the viewer" if ok
            else "ending has no question for the viewer to answer (\"follow for more\" isn't one)")
    music_check(md, rep)

# ------------------------------------------------------------------- main --


def detect(md: str) -> str:
    if find_script_table(md):
        return "video"
    if parse_units(md):
        return "carousel" if re.search(r"carousel|alt[ -]?text|instagram|linkedin", md, re.I) else "slides"
    return "unknown"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("path")
    ap.add_argument("--type", default="auto", choices=["auto", "slides", "carousel", "video"])
    ap.add_argument("--budget", type=int, help="on-screen words per slide (default 25 slides, 40 carousel)")
    ap.add_argument("--wpm", type=int, default=150, help="speaking rate for runtime estimate")
    ap.add_argument("--seconds", type=int, help="target video length in seconds")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:  # Windows consoles default to a legacy code page
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    try:
        md = open(a.path, encoding="utf-8").read()
    except OSError as e:
        print(f"can't read {a.path}: {e}", file=sys.stderr)
        return 2
    kind = detect(md) if a.type == "auto" else a.type
    rep = Report(kind, a.path)
    if kind == "video":
        check_video(md, rep, a.wpm, a.seconds)
    elif kind in ("slides", "carousel"):
        units = parse_units(md)
        if not units:
            print("no '## Slide N' sections found", file=sys.stderr)
            return 2
        budget = a.budget or (40 if kind == "carousel" else 25)
        check_units(units, md, rep, budget, kind == "carousel")
    else:
        print("couldn't tell the draft type: use '## Slide N' sections or a narration table, "
              "or pass --type", file=sys.stderr)
        return 2
    print(rep.json() if a.json else rep.text())
    return 1 if rep.failed else 0


if __name__ == "__main__":
    sys.exit(main())
