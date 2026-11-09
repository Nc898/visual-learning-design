---
name: visual-learning-design
description: Designs and audits teaching material with Mayer's cognitive theory of multimedia learning (coherence, signaling, redundancy, contiguity, segmenting, pre-training, modality, personalization, embodiment, generative activity). Use whenever you build or review something meant to teach or explain — a learning web app, interactive explainer or simulation, tutorial or onboarding walkthrough, demo, slide deck or lecture, explainer video or narration script, short-form video (TikTok, Reels, Shorts), educational social post, carousel or thread, infographic, course module — including requests like "make this easier to understand", "explain X visually", or "help students get this".
---

# Visual learning design

You are designing for **understanding**: whether the learner can use the idea later to solve a problem they have not seen (transfer). Recall and looking good come second. Everything here comes from Richard Mayer's cognitive theory of multimedia learning (CTML) and the research around it. Treat its principles as strong defaults with known boundary conditions, not as laws.

## The model you design against

Three assumptions about the learner's mind:

- **Dual channels.** People have an auditory/verbal channel and a visual/pictorial channel. Printed words come in through the *eyes*, so on-screen text competes with graphics for the visual channel. Spoken words do not.
- **Limited capacity.** Each channel holds only a little at a time.
- **Active processing.** Learning happens when the learner *selects* relevant words and images, *organizes* each into a coherent model, and *integrates* the models with each other and with prior knowledge.

Learning time draws on three kinds of processing. These three words are how you reason about every design decision:

| Load | Caused by | Your job |
|---|---|---|
| **Extraneous** | Poor design: clutter, split attention, out-of-sync media | **Reduce** it |
| **Essential** | How complex the material is *for this learner* | **Manage** it |
| **Generative** | The learner's effort to make sense of the material | **Foster** it |

Overload happens when extraneous plus essential processing exceeds capacity. Once you have cut extraneous load and managed essential load, the remaining risk is a learner who *can* think hard but has no reason to. Generative design fixes that.

## Workflow

### 1. Profile the learner and the situation

Write down one line for each:

- **Goal**, stated as something the learner can *do* ("predict what happens to current when resistance doubles"), not "understand X".
- **Prior knowledge**: novice, intermediate, or expert in *this* topic. This is the strongest moderator. Most principles are strongest for novices, and some reverse for experts (*expertise reversal*).
- **Pacing**: *system-paced* (video, live talk, auto-advancing animation) or *learner-paced* (scrollable page, self-paced deck, simulation). Pacing decides how strictly redundancy, modality, and coherence apply.
- **Medium, length, language** (is the material in the learner's second language?), and **accessibility needs**.

Done when every line is filled in. When something is unknown, assume a novice, system-paced if the piece has audio, and say in your output that you assumed it.

### 2. Inventory the essential content

List the key **elements** (named parts, terms, actors) and the **relations** between them (causal chain, process steps, comparisons, structure). Content that is neither an element nor a relation the goal needs is a candidate for cutting. The element list also becomes the pre-training material.

Done when every planned piece of content is tagged essential or cut, and the elements list exists.

### 3. Choose representations

For each essential idea, choose a graphic by its **function**:

- **Representational**: what it looks like
- **Organizational**: how the parts relate qualitatively (concept map, hierarchy)
- **Relational**: quantitative relationships (chart)
- **Transformational**: change over time or a process
- **Interpretive**: an invisible or abstract mechanism made visible (cause and effect, a model)

*Decorative* is not a function. A visual that only adds mood is extraneous load.

Use **animation** only when change over time is the thing to be learned (a process, a motion, a procedural-motor skill), and give it controls. Otherwise prefer a sequence of static key frames. Animation is *transient*: each frame disappears before the learner can compare it with the next one.

For **words**, decide by pacing. In system-paced pieces, spoken narration carries the explanation and the screen shows graphics plus brief labels. In learner-paced pieces, printed text is fine, but it must sit inside or beside the graphic it explains.

Done when every visual has a named function and every stream of words has a modality (spoken or printed) and a location.

### 4. Apply the principles

Go through the table below one load at a time, in order: extraneous, then essential, then generative. Read [references/principles.md](references/principles.md) when a boundary condition might apply (expert learners, learner-paced material, second-language learners, technical terms, long lessons), or when you need to justify a trade-off to the user. It also covers the closely related cognitive-load effects: worked examples, expertise reversal, transient information, and practice with feedback.

### 5. Apply the medium playbook

Read the file for the medium you are making. When a piece spans several media (a web app with an embedded video, a recorded talk with slides), read each relevant file.

| Making… | Read |
|---|---|
| Web apps, interactive explainers, simulations, e-learning modules, in-app tutorials, scrollytelling, lesson data visualizations | [references/web-apps.md](references/web-apps.md) |
| Slide decks, live lectures, narrated or self-paced slideshows | [references/slides.md](references/slides.md) |
| Explainer and lecture videos, narrated animations, screencasts, micro-learning, AI-generated video | [references/video.md](references/video.md) |
| Demonstrations (live or recorded), software walkthroughs, procedure demos, worked examples, product tours | [references/demonstrations.md](references/demonstrations.md) |
| Short-form vertical video (TikTok, Reels, Shorts), social posts, carousels, threads, stories | [references/social-and-short-form.md](references/social-and-short-form.md) |
| Infographics, textbook or documentation figures, handouts, games, VR/AR, audio-only, AI tutors and avatars | [references/other-formats.md](references/other-formats.md) |

**Markdown draft format.** When the deliverable is a Markdown slide outline, carousel, or video script, write it in the format the draft checker reads:

- **Slides and carousels:** a `## Slide N: <working title>` section for each slide, containing:
  - `**Headline:**` the takeaway sentence
  - `**On screen:**` followed by `> ` lines holding the literal on-screen text, exactly as it will appear
  - `**Visual:**` a description of the graphic
  - `**Speaker notes:**` for a presented deck, or `**Alt text:**` for a carousel
- **Video and short-form scripts:** one Markdown table with the columns `Time | Voiceover | Visual | On-screen text`, one row per beat.

### 6. Check the real artifact

For Markdown slide outlines, carousels, and scripts, first run the draft checker. It's `scripts/check_draft.py` in this skill's base directory and needs only the Python standard library:

```bash
python <skill-dir>/scripts/check_draft.py draft.md --seconds 45   # --seconds: the brief's target length
```

For a video with a target length, pass `--seconds`. Without it, the checker reads a length like "~45 sec" from the title.

It counts what can be counted: on-screen words per slide (headline included), headline length, alt text, speaker notes, narration runtime, on-screen text that repeats the narration, the hook, the closing viewer prompt, and music under the narration. Fix every FAIL. Fix every WARN too, unless a boundary condition justifies it. Your own word counts drift, so trust the script's.

Then run [references/audit-checklist.md](references/audit-checklist.md) against the actual output: the rendered page, the slides, or the two-column script, not your plan. Fix every item that fails before you hand anything over. Done when the checker shows no FAIL and every checklist item passes or doesn't apply. This check is for you. Keep the checklist, the checker output, and their marks out of the deliverable.

## Principles at a glance

Figures are Mayer's (2021) medians: Cohen's *d*, with positive tests out of total tests. An effect above about 0.4 is educationally meaningful. The figures come mostly from short lab lessons with novice college students, so use them to rank priorities, not to promise outcomes.

| Principle | Do this | *d* (tests) | Weaker or reversed when |
|---|---|---|---|
| **Multimedia** | Use words *and* relevant graphics, not words alone | 1.35 (13) | Graphics are decorative; the learner is an expert |
| *Reduce extraneous* | | | |
| **Coherence** | Cut interesting-but-irrelevant words, images, sounds, and music (seductive details) | 0.86 (18/19) | Learner-paced; high working memory; the extra material is dull rather than seductive |
| **Signaling** | Cue the structure and the essentials: headings, outlines, arrows, highlights, vocal stress | 0.70 (26/28) | Experts; simple material; overused cues (if everything is highlighted, nothing is) |
| **Redundancy** | Don't put the narration's full text on screen next to narrated graphics | 0.10 (8/12) | Learner-paced; short or reworded text; second-language learners; no graphics. Small effect, so it never justifies removing access captions |
| **Spatial contiguity** | Put printed words next to the part of the graphic they describe | 0.82 (9/9) | Experts; simple lessons |
| **Temporal contiguity** | Narrate a thing *while* it is shown, not before or after | 1.31 (8/8) | Short or learner-paced lessons |
| *Manage essential* | | | |
| **Segmenting** | Break the content into meaningful chunks the learner advances through (a "continue" control) | 0.67 (7/7) | Simple or slow-paced material |
| **Pre-training** | Teach the names and characteristics of the key parts before the explanation of how they work | 0.78 (10/10) | High prior knowledge; simple or learner-paced material |
| **Modality** | Explain graphics with spoken words rather than printed text | 1.00 (18/19) | Technical terms, formulas, or code; second-language learners; learner-paced; material that must be referred back to |
| *Foster generative* | | | |
| **Personalization** | Write conversationally: "you", "your lungs", "let's" | 1.00 (13/15) | Experts; long lessons; forced chumminess |
| **Voice** | Narrate with an appealing human voice or a high-quality modern TTS voice, never a robotic one | 0.74 (6/7) | Negative social cues elsewhere (a stiff avatar) |
| **Embodiment** | An on-screen instructor or agent gestures, points, looks at the content, draws as they explain | 0.58 (16/17) | Paired with a machine voice |
| **Image** | A static face or avatar on screen adds little and can distract. Show a person only when they *do* something | 0.19 (4/7) | (It is a "don't bother" principle) |
| **Immersion** | Don't assume VR or 3D beats a well-designed 2D desktop version | no reliable gain | The task is truly spatial or embodied |
| **Generative activity** | Prompt the learner to summarize, map, draw, self-explain, self-test, teach, or enact during learning | 0.71 (37/44) | No guidance or training in the activity; the activity overloads novices |

## Resolving conflicts

The principles collide with each other and with other goals. Resolve the common collisions this way:

- **Accessibility vs. redundancy.** Captions, transcripts, alt text, and audio description are access requirements (WCAG 1.2.x, 1.1.1), and the redundancy effect is small. Provide captions as a **closed, learner-toggleable** track. Burned-in full-sentence on-screen text is what redundancy is about. Make sure deaf and hard-of-hearing learners can follow every essential idea through text plus visuals.
- **Engagement vs. coherence.** Build interest from *relevance* (a real problem the learner cares about), social cues (conversational voice, a human who explains and draws), and generative activity, not from decoration, stock photos, music, or fun-fact sidebars. Short lessons pay the highest price for seductive details.
- **Platform norms vs. the principles** (social feeds). Make posts work with the sound off, so on-screen text carries the skeleton and narration carries the explanation. Burned-in captions are acceptable when they're short phrase chunks placed away from the visual being explained. Make the hook the learning question itself, not a gimmick. Keep trending audio away from the narration.
- **Brand vs. coherence.** Keep branding to a title or end card and a quiet palette. Logos, mascots, and slogans on every frame are extraneous load.
- **Novices vs. experts in one audience.** Design the main path for novices, and let experts *skip* support: collapsible pre-training, optional worked steps, a "jump to practice" link. Fixed scaffolding slows experts (expertise reversal).
- **Brevity vs. completeness.** When the material is long, *segment* it rather than cut essential relations. Cut only what step 2 tagged as non-essential.
- **Talking head vs. the image principle.** A brief face at the start builds social presence. After that, show the content, and bring the person back only when their hands, gaze, or drawing carry information.

## Output

**When building:** deliver the artifact, then a short **design rationale** of 3–8 bullets. Each bullet names a decision, the principle behind it, and the load it targets. List every assumption from step 1. Leave out an audit table or checklist results. When something couldn't be checked from where you are (contrast or legibility of art not yet rendered), say so in one line after the rationale.

**When auditing existing material:** report findings ranked by expected learning impact (use the effect sizes and the learner profile). Each finding gives the *location* (slide 4, 01:32, the `#chart` section), the *problem*, the *principle and load*, and a *concrete fix*. Group the findings by load. Finish with the two or three highest-leverage changes.

Cite principles by name when you explain your choices, so the user learns the vocabulary. Keep the effect sizes honest: say "strong lab evidence" or "small effect", and don't promise a percentage improvement.
