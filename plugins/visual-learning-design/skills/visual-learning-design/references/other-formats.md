# Other formats

Covers infographics and posters, figures in textbooks and documentation, handouts, educational games, VR/AR, audio-only material, and AI tutors or avatars.

## Infographics and posters

The learner sets the pace and reads printed words, so **spatial contiguity, signaling, and coherence** dominate.

- **Give it one clear reading path.** Number the sections, or use arrows or a strong visual flow (top to bottom, left to right). The path itself is a signal of the structure.
- **Headline = the takeaway**, as a sentence.
- **Labels sit on the graphic.** Put each number next to the thing it measures.
- **Cut the infographic clichés:** decorative icons for every bullet, ornamental illustrations, pictogram filler, and gradient backgrounds. A good test: if an icon were removed, would any meaning be lost?
- Visualize the *relationships* (process, comparison, hierarchy, cause and effect). Text set in colorful boxes isn't a graphic.
- **Accessibility:** provide a text-equivalent version or detailed alt text, and don't rely on color alone.

## Figures in textbooks, documentation, and articles

- **Put each figure next to the text that discusses it**, on the same page or screen, and refer to it explicitly ("In Figure 2, notice the valve…").
- **Make the caption state the takeaway.** "Figure 2. Closing the valve raises upstream pressure", not "Figure 2. Valve diagram."
- **Label the parts directly** with leader lines. Avoid keys.
- For processes, use **numbered static key frames** that match numbered steps in the text, rather than one dense diagram.
- In technical docs, put code next to its explanation, and diagram the architecture before the API details (pre-training).

## Handouts and job aids

- Make handouts and job aids *references* for later performance: numbered steps, labeled screenshots, checklists, a glossary. They can be text-dense, because the reader controls the pace.
- Don't print the slides as the handout. Slides designed for a speaker don't explain themselves.
- Guided notes, with key words left blank for learners to fill in during the session, add a light generative activity.

## Educational games and gamification

Mayer's "value-added" studies of games (*Computer Games for Learning*, 2014) found that several features improve learning *within* a game: **modality** (narrated rather than printed instructions), **personalization** (conversational wording), **pre-training** (learn the key concepts before playing), **self-explanation prompts**, and **explanatory feedback or coaching**. Adding a narrative theme did not reliably help.

- **Tie the core mechanic to the learning goal.** The action the player repeats most should be the thing being learned. When it isn't (quiz questions sitting between platformer levels), the game layer is a seductive detail.
- **Use reflection breaks**, such as a "Why did that work?" prompt after a level, to turn play into generative processing.
- **Give explanatory feedback on failure**, not just "try again".
- Keep the visual and audio polish from competing with the learning signals. During learning-critical moments, mute the music and make the relevant state visually dominant.
- **Gamification** (points, badges, streaks): reward practice volume and spaced review, not clicking through. Use leaderboards sparingly, because they shift attention to ego.

## VR, AR, and 3D immersive learning

**Immersion principle:** immersion does not automatically produce better learning. Immersive VR has been shown to raise presence and enjoyment while *lowering* learning, because of extra cognitive load (Makransky, Terkildsen & Mayer, 2019).

- Choose VR or AR only when the task is truly spatial, embodied, situational, or impossible or unsafe to do in reality. Otherwise build a 2D or desktop version.
- Apply coherence aggressively. Immersive scenes are full of detail. Strip the environment down to what the task needs, and make the essential objects visually dominant.
- **Signal inside the 3D scene:** highlight, glow, or outline the object being discussed, and have an agent or narrator point at it.
- **Segment with generative breaks.** Pause the experience and prompt a summary or explanation. Summarizing after each VR segment restored learning in Parong and Mayer (2018).
- **Pre-train outside the headset**, covering both the concepts and the controls. Learning the controls in VR adds essential load.
- Narrate rather than float text panels in the scene (modality), and keep any labels attached to their objects.

## Audio-only (podcasts, audio lessons)

The multimedia principle says words alone are weaker than words plus pictures, so add a companion visual when you can (a diagram in the show notes, a one-page visual summary).

When it must be audio only:
- Signal heavily with words: outline at the start, numbered points, recap at the end.
- Segment with chapters.
- Define terms before you use them (pre-training).
- Invite imagining ("Picture a pipe narrowing…"), which is a generative activity with *d* = 0.65.
- Keep it conversational, and keep music out from under the explanatory speech.

## AI tutors, chat-based learning, and pedagogical agents

- **Personalization and politeness:** conversational, encouraging, focused on the task.
- **Voice over image:** if the agent speaks, voice quality matters more than whether an avatar is shown. If an avatar is shown, it should be *embodied*: gesture, gaze toward the content, expressions. Otherwise leave it out (image principle).
- **Make the learner generate.** Ask the learner to explain, predict, or attempt before the tutor explains. The tutor should prompt self-explanation and give explanatory feedback rather than hand over finished answers.
- **Pair text explanations with diagrams** when the concept has spatial or causal structure (multimedia principle). Render the diagram inline next to the explanation (spatial contiguity).
- **Adapt to the learner:** gauge prior knowledge early, and fade hints and worked steps as the learner shows competence (expertise reversal).
- **Segment long explanations** into short turns with a check between them, rather than one long reply.
