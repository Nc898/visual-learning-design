# Visual Learning Design

A Claude skill that designs and reviews teaching material using **Richard Mayer's cognitive theory of multimedia learning**, a research-backed framework for combining words and pictures so that people understand them.

Ask Claude for a lecture deck, an explainer video, an Instagram carousel, or an interactive lesson, and the skill steers it toward what the research supports:

- the parts are named before the mechanism
- narration explains while the visual is on screen
- labels sit on the diagram
- there's no decorative clutter and no music under the voice
- the piece ends with a question that makes the learner think

It works for:

| | |
|---|---|
| **Slides** | Live lectures, narrated decks, self-paced decks |
| **Video** | Explainers, lecture video, narrated animation, screencasts |
| **Short-form & social** | TikTok, Reels, Shorts, carousels, threads, stories |
| **Web apps** | Interactive explainers, simulations, e-learning modules, in-app tutorials |
| **Demonstrations** | Software walkthroughs, procedure demos, worked examples, product tours |
| **Other** | Infographics, textbook figures, handouts, games, VR, AI tutors |

It also **reviews existing material**: give it a deck, a script, or a page, and it returns fixes ranked by expected learning impact.

## Install

### Claude Code (plugin)

```bash
claude plugin marketplace add Nc898/visual-learning-design
claude plugin install visual-learning-design@nc898-plugins
```

Or, inside a session, run `/plugin marketplace add Nc898/visual-learning-design` and install the plugin from the `/plugin` panel. To get updates later, run `claude plugin update visual-learning-design`.

### Claude Code (personal skill, no plugin)

Copy `plugins/visual-learning-design/skills/visual-learning-design/` into `~/.claude/skills/`.

### Claude.ai

Download `visual-learning-design.skill` from the [latest release](https://github.com/Nc898/visual-learning-design/releases/latest) and upload it under **Settings → Capabilities → Skills**.

## Use it

You don't need to name the skill. Ask for teaching material the way you normally would, and it triggers:

> "I'm teaching my 9th grade bio class how vaccines work, 10 minutes, presenting live. Make me the slideshow with speaker notes."

> "Script a 45-second TikTok explaining why the sky is blue. Include what's on screen at each moment."

> "Write an Instagram carousel teaching compound interest to 20-somethings new to investing."

> "Review this onboarding video script. Why aren't new users getting it?"

In Claude Code you can also call it directly with `/visual-learning-design:visual-learning-design`.

**What you get back:** the deliverable, a short **design rationale** (each key decision and the principle behind it), and the assumptions it made about your audience. Learner level and pacing change the design, so say up front if your audience is expert or the piece is self-paced.

## How it works

The skill follows a six-step process:

1. Profile the learner: goal, prior knowledge, whether the pace is set by the presenter or by the learner, and the medium.
2. Inventory the essential content.
3. Choose a representation for each idea by its function.
4. Apply the principles.
5. Apply the playbook for the medium.
6. Check the actual draft before handing it over.

It reasons about three kinds of mental load, and the principles are grouped the same way:

| Load | Principles |
|---|---|
| **Reduce** load caused by poor design | coherence (cut the extras), signaling, redundancy, spatial and temporal contiguity |
| **Manage** load caused by complex material | segmenting, pre-training, modality |
| **Encourage** the learner's own effort to make sense of it | personalization, voice, embodiment, image, immersion, generative activity |

Each principle comes with its effect size and the conditions where it weakens or reverses. For example, cutting on-screen text matters less when learners set their own pace or are reading in a second language. That way the skill adapts to the situation instead of applying rules blindly.

### Draft checker

`skills/visual-learning-design/scripts/check_draft.py` checks the countable rules in Markdown slide outlines, carousels, and video scripts. It needs only the Python standard library:

```bash
python check_draft.py slides.md
python check_draft.py tiktok.md --seconds 45
python check_draft.py carousel.md --json
```

```
[WARN] runtime: 157 spoken words, about 63 s at 150 wpm (target 45 s)
[WARN] hook: first beat doesn't pose the learning question; make the hook the question itself
[FAIL] music under narration: 1 line(s) put music or a sound bed under the explanation ...
```

It checks:
- on-screen words per slide, with the headline counted
- headline length, and headlines that are just topic labels
- alt text and speaker notes
- narration runtime
- on-screen text that repeats the narration
- whether the opening poses a question
- whether the ending asks the viewer something
- music under the narration

It exits with code 1 when anything fails, so you can use it in CI. The skill runs it on its own drafts, which matters because models misjudge their own word counts. In testing, every agent reported "about 115 words" for scripts that actually ran 133–157.

## Does it help?

These are informal tests: one run per prompt, each graded against six checks taken from the principles.

| Prompt | With skill | Without skill |
|---|---|---|
| Live 9th-grade slideshow on vaccines | 5/6 | 4/6 |
| Instagram carousel on compound interest | 6/6 | 3/6 |
| 45-second TikTok on why the sky is blue | 6/6 | 3/6 |

The biggest gains were on social media. Without the skill, Claude suggested upbeat music under the voiceover, opened with a gimmick instead of the question, and ended on "follow for more". With the skill, runs take about twice as long and use about 15–20% more tokens.

The test cases live in [`plugins/visual-learning-design/evals/`](plugins/visual-learning-design/evals). With Claude Code v2.1.269 or later, you can rerun them from the plugin directory:

```bash
cd plugins/visual-learning-design
claude plugin eval . --allow-tools Write,Edit,Bash
```

## Evidence and limits

The principles and effect sizes come from Mayer's *Multimedia Learning* (3rd ed., 2021) and his 2023 summary chapter. Related work covers cognitive load theory, animation, video engagement, assertion-evidence slides, and short-form video. Full citations are in [`references/sources.md`](plugins/visual-learning-design/skills/visual-learning-design/references/sources.md).

Keep these limits in mind:
- **Lab conditions.** Most of the evidence comes from short lab lessons with college students learning how something works. Effects in real courses are smaller but point the same way.
- **Social and short-form.** The evidence here is thin and correlational, and it measured likes, not learning.
- **Accessibility comes first.** The skill always keeps captions, transcripts, and alt text. The redundancy effect is small, and it never justifies removing access features.

The popular "12 principles" summary, such as the [Digital Learning Institute article](https://www.digitallearninginstitute.com/blog/mayers-principles-multimedia-learning) this project started from, is a subset. This skill uses Mayer's current 15 plus closely related cognitive-load effects: worked examples, expertise reversal, and transient information.

## Repository layout

```
.claude-plugin/marketplace.json          marketplace listing (nc898-plugins)
plugins/visual-learning-design/
├── .claude-plugin/plugin.json           plugin manifest
├── evals/                               test cases for `claude plugin eval`
└── skills/visual-learning-design/
    ├── SKILL.md                         workflow, principles table, conflict rules
    ├── scripts/check_draft.py           draft checker
    └── references/
        ├── principles.md                each principle: mechanism, evidence, boundaries
        ├── slides.md · video.md · web-apps.md · demonstrations.md
        ├── social-and-short-form.md · other-formats.md
        ├── audit-checklist.md           full review checklist
        └── sources.md                   citations
```

## Contributing

Issues and pull requests are welcome. Better boundary conditions, new medium playbooks, and test cases are especially useful. When you change the skill, rerun the evals and the draft checker on a sample draft.

## License

MIT. This project isn't affiliated with Richard Mayer, Cambridge University Press, or the Digital Learning Institute. The skill summarizes and cites published research in its own words.
