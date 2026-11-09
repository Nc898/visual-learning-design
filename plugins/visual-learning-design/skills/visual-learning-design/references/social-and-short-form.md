# Social media posts and short-form video

Covers vertical short video (TikTok, Instagram Reels, YouTube Shorts, LinkedIn video), static posts (single image, carousel or document posts), text threads (X, Threads, Bluesky, LinkedIn), and stories.

## What's different about this context

Social feeds break several assumptions the lab research made, so start by adjusting your learner profile:

| Lab assumption | Feed reality | Design consequence |
|---|---|---|
| Learner chose to study | Learner is scrolling, and can leave in about a second | The first frame must state a question or claim the learner cares about (relevance as signaling) |
| Sound on | Often muted: roughly 69% of US viewers watch sound-off in public (Verizon Media/Publicis, 2019) | The piece must work **sound-off complete, sound-on better** |
| Prior lessons | No guaranteed prior context; each post may be someone's first | Each post pre-trains its own terms, or links clearly to part 1 |
| Large screen, controls | Small vertical screen. Platform UI covers the edges. Autoplay and auto-loop | Large type, one focal point, essential visuals in the safe zone |
| Goal: transfer | Goal is usually one idea, remembered and recognized later | Teach **one** idea per post. Use a series for more |

Likes and views are **not** learning measures. In a study of 34 educational TikToks (Zhang et al., 2023), the videos that used more of Mayer's principles, especially social cues, got more likes. **Coherence was the principle applied least often (29% of videos)**. The dominant failure in this genre is clutter, not a lack of hooks. For learning, saves, shares, and comments that contain correct answers are better proxies than likes.

## Short-form vertical video

### Structure (15–60 seconds for one idea; series for more)

**Spoken-word budget: about 2.5 words per second** (150 wpm): roughly 40 words for 15 s, 75 for 30 s, 110 for 45 s, and 150 for 60 s. Every beat below has to fit inside that total, so the mechanism usually gets 50–60% of it. Count with `scripts/check_draft.py --seconds N` before you hand the script over. Models consistently undercount their own scripts. In testing, scripts reported as "about 115 words" actually ran 133–157. When you're over budget, cut words, not beats: trim the side note first, then shorten the setup lines.

1. **Hook (0–2s): the learning question or a misconception**, spoken *and* on screen ("Why does ice float when almost every other solid sinks?"). A hook that *is* the question to be answered draws attention to the right content. Hooks unrelated to the lesson (shock clips, "wait for it", trending gags) are seductive details. They buy a second of attention and cost understanding.
2. **Name the parts (2–6s), only what's needed:** label the one or two key elements on screen as they're introduced (pre-training, compressed).
3. **One mechanism, shown while it's said (most of the runtime):** the visual changes on the word that names the change (temporal contiguity). Show the thing itself, a quick diagram, or a hand sketch, rather than only a face talking.
4. **Payoff and recap (last 3–5s):** a one-line answer on screen as text, which doubles as the sound-off takeaway.
5. **Generative prompt:** "Comment your guess before part 2", "Try it: which would sink?", "Explain it to someone in one sentence". Put it on screen *and* in the caption.

### Words: sound-off complete, sound-on better

- **Narration carries the explanation** (modality). **On-screen text carries the skeleton:** the hook question, key-term labels, step names, and the final answer. A muted viewer should get the gist. A listening viewer should get the full explanation.
- **Captions:** burned-in captions are the platform norm, and many viewers depend on them (deaf and hard-of-hearing viewers, muted viewers, second-language viewers). The redundancy cost is small (*d* = 0.10), and the research found it fades for short text and second-language viewers. So:
  - Use **phrase-level chunks** (3–6 words) that are short and synced to speech. Avoid long sentences and full paragraphs.
  - **Place captions away from the thing being explained.** A caption bar sitting on the diagram breaks the visual.
  - **Emphasize only the key term** (color or weight) as a signal. Bouncing word-by-word animation, emoji on every line, and multiple colors are extraneous load.
  - Or, instead of burning in, turn on the platform's auto-captions, and correct them.
- **Labels go on the object** they name (spatial contiguity), not in a caption bar.

### Visuals and pacing

- **Frame the essential visual in the center safe zone.** The bottom ~20% (caption and audio label) and the right edge (like, comment, share buttons) are covered by platform UI. Check one frame with the UI overlay before publishing.
- **One focal point per moment**, high contrast, text large enough to read on a phone at arm's length: roughly 5% of frame height or more for key text.
- **Cut at idea boundaries, not on every beat.** Rapid jump cuts every second can keep attention, but they break *apprehension*: the learner can't perceive a change that vanishes before it registers. Hold each key visual long enough to be read.
- **Green screen or "creator in front of a diagram":** point at the part you're naming, look at it, and draw on it (embodiment). A face *beside* a diagram the creator never references is the image principle's static talking head.
- **Authentic creator presence helps:** a conversational, relatable, real person talking to one viewer (personalization, voice). Humor helps when the joke *is* the concept (a memorable analogy). Irrelevant jokes are seductive details.

### Music and trending audio

Background music under explanatory narration hurts learning (coherence). Platforms reward trending sounds, so treat this as a negotiation, not a ban:
- Best: no music under the explanation. A sound can play over the hook or the outro.
- Acceptable: very low-volume, lyric-free music, ducked under the voice.
- Avoid: lyrical tracks, beat drops timed against the narration, and trending audio *instead of* narration with all teaching in text.

### Series and segmenting

- Number episodes on screen and in the title ("Part 2/5: why ice floats"). Pin or link the playlist.
- Open each part with a 2-second recap of the previous one, because many viewers arrive in the middle.
- If an idea needs more than ~60–90 seconds, it's two ideas. Split it.

### Accuracy and trust

Short-form video spreads errors fast. Name a source in the caption for any factual claim, and keep the simplification honest ("roughly", "in most cases"). Correct mistakes in a pinned comment or a follow-up video.

## Static posts

### Single image post

- **One idea per image.** The headline is the claim as a sentence, and the body is a labeled visual: a diagram, an annotated chart, or a before/after.
- **Readable at feed size.** Check it at about 400px wide: the headline and the key labels should still be legible.
- **Put essential words in the image, next to their parts.** The post caption sits far from the image and is often truncated, which is split attention. Use the caption for context, the source, and the generative prompt.

### Carousel / document posts

The swipe makes carousels **learner-paced segmenting** by design, so printed text is fine here (modality relaxes).

| Slide | Job | Principle |
|---|---|---|
| 1 | The question or claim that names the payoff ("5 steps from sunlight to sugar"), plus a visual teaser of the diagram | Signaling, relevance |
| 2 | Labeled diagram of the parts that every later slide reuses | Pre-training |
| 3 to n−2 | One step per slide. **Reuse the same diagram** and highlight the active part on each slide (progressive build) | Segmenting, signaling, spatial contiguity |
| n−1 | Recap: the whole diagram with every step labeled, the complete mental model on one slide | Organization |
| n | Retrieval or apply prompt ("Which step uses the light? Answer in comments"), plus "save this" | Generative activity |

- Aim for 5–10 slides, and **keep text short per slide** (roughly 40 words or fewer). Put the words on the diagram, not in a block beneath it.
- Keep the layout consistent across slides: headline position, diagram position, colors. The only change between slides should be the content that changes.
- Slide progress ("3/8") and a visual continuation cue (the diagram running off the right edge) signal structure.

### Text threads (X, Threads, Bluesky, LinkedIn)

- **Post 1 states the payoff** and the count ("How vaccines train your immune system, in 6 posts 🧵"). Then put one idea per post, numbered.
- **Attach the visual to the post that discusses it** (spatial and temporal contiguity), not all images at the end.
- Use pointer words ("First… Because of that…") to make the causal chain explicit.
- End with a one-post recap and a question that prompts retrieval or application.
- LinkedIn and other long single posts: short paragraphs, a bolded or first-line claim, and one image that explains rather than a stock photo.

### Stories (ephemeral, tap-through)

They auto-advance (system-paced) but can be tapped (learner-paced). Put one idea per frame and keep text minimal. Hold dense frames longer, or tell viewers to tap and hold. Use interactive stickers (quiz, poll, "guess first") as built-in generative activities. Reveal the answer on the next frame with an explanation.

## Accessibility on social platforms

- **Alt text on every image and carousel slide**, written as the takeaway. Most platforms have a custom alt-text field, and auto-generated alt text is poor.
- Captions on every video, corrected rather than raw auto-captions.
- **CamelCase hashtags** (#CellBiology) so screen readers can parse them. Use emoji sparingly, and not as bullets, since screen readers announce each one.
- Keep contrast at least 4.5:1, and don't use color as the only cue.
- Avoid rapid flashing (WCAG 2.3.1). Some short-form effects exceed 3 flashes per second.

## Checklist (social and short-form)

- [ ] Teaches exactly one idea, or is clearly numbered as part of a series.
- [ ] The opening frame or slide states the learning question or claim, and the hook is the lesson itself.
- [ ] A muted viewer gets the gist from on-screen text and visuals. Narration carries the full explanation.
- [ ] Captions are phrase-level, synced, and kept off the explained visual. Only key terms are emphasized.
- [ ] Every visual changes as it's named. Cuts happen at idea boundaries.
- [ ] Essential content sits inside the platform safe zone and is legible at phone size.
- [ ] No music under narration (or ducked and lyric-free). No irrelevant gags or b-roll.
- [ ] The creator, if on screen, points at, looks at, or draws on the content.
- [ ] Carousels reuse one diagram across slides and end with a recap plus a retrieval prompt.
- [ ] There's a generative prompt (guess, comment, try, explain).
- [ ] Alt text, corrected captions, camelCase hashtags, and a source for factual claims.
