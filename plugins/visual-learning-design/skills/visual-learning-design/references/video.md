# Video

Covers explainer videos, lecture videos, narrated animations, screencasts, micro-learning clips, and AI-generated or AI-narrated video.

For vertical short-form video in social feeds (TikTok, Reels, Shorts), read [social-and-short-form.md](social-and-short-form.md) too. It adjusts these rules for sound-off viewing, hooks, and platform UI.

**Default profile:** *system-paced and transient*. Every principle applies at full strength here, especially temporal contiguity, modality, redundancy, coherence, and segmenting. Pause, scrub, and chapter controls move the experience part-way toward learner-paced, so provide them.

## Plan the video as a two-column script

Write the **audio** and the **visual** side by side, one row per beat. This format enforces temporal contiguity: every spoken line has a named visual on screen *at that moment*, and every visual has a reason to exist.

| # | Audio (narration) | Visual (on screen now) | On-screen text | Principle check |
|---|---|---|---|---|
| 1 | "Your phone's battery has two sides. Let's meet them." | Labeled cell: anode, cathode, electrolyte | "anode", "cathode" | Pre-training, personalization |
| 2 | "When you charge it, lithium ions move *this* way…" | Ions animate from cathode to anode, arrow highlight | none | Temporal contiguity, signaling |
| 3 | "Pause and predict: what happens when you unplug it?" | Frozen frame, question card | "Predict: which way do the ions go?" | Generative activity, segmenting |

How to write and check the script:

- Write the narration to be *heard*: short sentences, second person, one idea per sentence. Read it aloud.
- **On-screen text** is limited to labels, key terms, numbers, and step names, two or three words each. Never put the narration's own sentences on screen (redundancy).
- Check the script before any production. If a row has no meaningful visual, either find one that explains (a representational or transformational graphic, not decoration) or cut the row. If the visual changes but nothing is said about it, the change is unexplained motion.

## Length and segmenting

- **Aim for about 6 minutes or less per video.** In MOOC data from 6.9 million sessions, median engagement was close to 100% for videos under 6 minutes and fell sharply for longer ones (Guo, Kim & Rubin, 2014; summarized in Brame, 2016). Split long lessons into a series.
- Inside a video, add **chapter markers** at the boundaries between ideas, and **pause points** with a question about every 3–5 minutes. Questions inserted into lecture video reduce mind-wandering and improve test scores (Szpunar et al., 2013).
- Open each video with a single sentence of purpose: "By the end you'll be able to…".

## Make words and visuals arrive together

- **Narrate what's on screen now** (temporal contiguity). Don't explain first and then play the animation silently, or show the animation and then explain it afterward.
- **Signal visually, synchronized with the spoken word:** arrows, spotlight or dim the rest, zoom into a region, a cursor highlight, circling or underlining as you speak.
- **Signal verbally:** an outline at the start ("three steps"), pointer words, and vocal stress on key terms.
- **Keep labels beside their parts**, not in a lower-third caption bar (spatial contiguity).

## Cut everything that doesn't explain (coherence)

- **No background music** under narration. Music and sound effects measurably hurt learning from narrated animations (Moreno & Mayer, 2000). A short sting on the title card is the most you need.
- No unrelated b-roll, generic stock footage, or cinematic flourishes. Keep logo animations very short (under 3 seconds).
- Use clean, plain backgrounds. Leave out animated textures, busy sets, and an open desktop with notifications.
- Cut dead air, filler, and false starts. Keep deliberate pauses after key points.
- **AI-generated video:** check every generated clip against the script row it serves. Generators tend to produce attractive but decorative or inaccurate visuals. Decorative visuals are seductive details, and inaccurate ones are worse.

## The instructor on screen

- A **talking head alone** does not explain. Prefer the instructor **drawing or annotating while explaining**: Khan-style tablet drawing, or a lightboard. It is both more engaging (Guo et al., 2014) and better for learning (embodiment; Fiorella & Mayer, 2016).
- When you show the instructor, **cut between face and content**, or show a small inset during a brief intro. Avoid a permanent static picture-in-picture (image principle).
- An on-screen presenter should **point at the content, look at it, and gesture** (embodiment). A presenter or avatar that just stands still adds nothing.
- **For procedural demos, use a first-person (over-the-shoulder) camera**, not a camera facing the instructor (Fiorella et al., 2017). See [demonstrations.md](demonstrations.md).

## Voice

- Use a warm, enthusiastic, conversational human voice, or a high-quality modern neural TTS voice. Avoid flat or robotic synthesis (voice principle).
- **Pace:** natural speech. Slow down for dense content, novices, and second-language audiences. Faster speaking rates correlated with engagement in MOOC data, but speed only helps when learners can keep up. Offer a playback-speed control.
- Choose personalization in the wording: "your", "let's", "you'll notice".
- Get the audio quality right: a good mic, no echo, consistent levels. Bad audio is extraneous load on every second of the video.

## Generative activity around video

- **Before:** two or three guiding questions to watch for.
- **During:** pause-point questions, a prediction prompt before a reveal, or "sketch what you think happens next".
- **After:** a short quiz with explanatory feedback, a one-sentence summary prompt, or a problem that applies the idea. Video embedded in an assignment helps more than video watched on its own.
- When the platform supports it (an LMS, an interactive player), embed the questions in the video itself.

## Accessibility

- **Closed captions** (toggleable, accurate, synced) on every video: WCAG 1.2.2 for prerecorded audio. These are an access track. Keep them separate from the burned-in on-screen text the redundancy principle warns against.
- Provide a **transcript**, which also serves as a reference copy for re-reading (this addresses the transient-information effect).
- **Audio description** when essential information is visual only (WCAG 1.2.5). The best fix is to narrate what matters about the visuals in the main track.
- Avoid flashing above 3 per second (WCAG 2.3.1).

## Production checklist (video-specific)

- [ ] A two-column script exists, and every row pairs audio with an explanatory visual.
- [ ] On-screen text is labels, key terms, and numbers only, never the narration's sentences.
- [ ] No background music or unrelated footage.
- [ ] Each video is about 6 minutes or less, with chapters and at least one pause-point question.
- [ ] It opens with a purpose statement and pre-training of the key parts.
- [ ] The instructor (if shown) draws, points, or gestures. No static talking-head overlay.
- [ ] Captions, transcript, and a speed control are available.
