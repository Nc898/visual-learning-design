# Audit checklist

Run this against the **actual artifact**: the rendered page at desktop and mobile width, every slide, or the two-column script plus the rendered frames. Work through every item and fix what fails. When you're checking your own build, the marks are working notes: they stay out of the deliverable (see Output in SKILL.md). When the user asked you to review existing material, report failures as described in "Reporting findings" below. Use the learner profile from step 1 of SKILL.md to decide which boundary conditions apply.

For a large artifact, audit a representative sample in full (the opening, the most complex segment, and one practice segment), then scan the rest for repeats of the failures you found.

## Rapid audit: highest-leverage checks

When time is short, run these five first. They cover the largest effects.

1. **Temporal contiguity** (*d* 1.31): narration and the visual it describes happen at the same moment.
2. **Modality / redundancy** (1.00 / 0.10): in system-paced pieces, narration explains and the screen shows labels, not the narration's sentences.
3. **Personalization** (1.00): conversational, second-person wording.
4. **Coherence** (0.86): no seductive details, decoration, or background music.
5. **Spatial contiguity** (0.82): every label is on or beside its part, and feedback is beside its answer.

## Foundation

- [ ] **Goal** is stated as a learner performance, and the piece visibly serves it.
- [ ] **Multimedia:** every essential relation has an explanatory visual, not just words.
- [ ] Every visual has a function (representational, organizational, relational, transformational, interpretive). None is purely decorative.

## Extraneous load (reduce)

- [ ] **Coherence:** no seductive details (fun facts, tangents, unrelated stories or clips).
- [ ] **Coherence:** no background music or ambient sound under explanation, and no decorative stock imagery.
- [ ] **Coherence:** branding, logos, chrome, and ambient animation are minimal and stay out of the content area.
- [ ] **Signaling:** the structure is visible (outline, headings stating the point, progress indicator, pointer words).
- [ ] **Signaling:** essential elements are cued (arrows, highlight, zoom, vocal stress), and cues are sparing, with one focal point at a time.
- [ ] **Redundancy:** no verbatim on-screen copy of the narration. Captions are available as a closed, toggleable track.
- [ ] **Spatial contiguity:** labels are on or beside their parts, with no legends or keys that need cross-referencing. This holds at mobile width.
- [ ] **Spatial contiguity:** feedback sits beside its response, instructions sit on the same screen as the task, and each figure sits next to the text that discusses it.
- [ ] **Temporal contiguity:** each visual appears or changes as it is named, never before or after its explanation.

## Essential load (manage)

- [ ] **Segmenting:** one idea per segment, with boundaries at meaningful points.
- [ ] **Segmenting:** the learner controls advancing (continue, next, chapters, pause). Videos are about 6 minutes or less.
- [ ] **Pre-training:** the key parts and terms are introduced with labels before the explanation of how they work, and experts can skip that introduction.
- [ ] **Modality:** for fast or system-paced graphics, the explanation is spoken. Printed words are used where they help: technical terms, formulas, code, second-language learners, or learner-paced reading.
- [ ] **Transient information:** long or complex animations and narration have replay, step, or scrub controls, or a persistent summary.
- [ ] **Animation:** motion is used only for change the learner must learn. It is congruent and slow enough to perceive, and it respects reduced motion.
- [ ] **Worked examples:** novices see a modeled example before solving, and support fades over the following tasks.

## Generative processing (foster)

- [ ] **Personalization:** conversational second person, plain words, polite tone.
- [ ] **Voice:** a natural, warm human or high-quality TTS voice, with clean audio.
- [ ] **Embodiment / image:** any on-screen person or agent points, gazes, gestures, or draws. There is no static talking head or avatar overlay.
- [ ] **Generative activity:** each segment ends with or contains a prompt to predict, explain, summarize, map, draw, or retrieve, with guidance or scaffolding.
- [ ] **Feedback:** explains why, focuses on the task, and links back to the relevant visual.
- [ ] **Immersion** (if VR, AR, or 3D): justified by a spatial or embodied task, stripped down to the essentials, with generative breaks.

## Learner fit

- [ ] Support fits the profiled prior knowledge. Experts can skip or collapse scaffolding (expertise reversal).
- [ ] Second-language learners get printed key terms and a slower pace.
- [ ] Novices get a recommended path instead of unguided navigation.

## Social and short-form (if posted to a feed)

- [ ] Teaches one idea. The opening frame or slide states the learning question, not an unrelated gimmick.
- [ ] Works with the sound off: on-screen text gives the gist, and narration gives the full explanation.
- [ ] Essential content sits in the platform safe zone and is legible at phone size.
- [ ] The medium checklist in social-and-short-form.md passes.

## Accessibility

- [ ] Captions (closed) and a transcript for all audio. Audio description, or narration, covers visual-only information.
- [ ] Alt text states the takeaway. Complex graphics have a text or table equivalent.
- [ ] Color is never the only carrier of meaning. Contrast is at least 4.5:1 for text and 3:1 for essential graphic parts.
- [ ] Interactive elements are keyboard-operable with visible focus. Feedback is announced (`aria-live`).
- [ ] Nothing flashes more than 3 times per second, and motion can be paused or reduced.

## Reporting findings

For each failure, record: **location**, **what's wrong**, **principle (load)**, **fix**, and **impact** (high, medium, or low, judged from the effect size and the learner profile). Sort by impact. Lead with the two or three fixes that would most change what the learner understands.

Example:

> **High · Slide 6 · Redundancy + Modality (extraneous/essential).** The full narration paragraph is printed under the diagram, so attention splits between reading and the graphic. **Fix:** cut it to three labels on the diagram ("p-layer", "n-layer", "electron flow →") and move the paragraph to speaker notes.
