# Web apps and interactive learning

Covers learning web apps, interactive explainers ("explorable explanations"), simulations, e-learning modules, in-app tutorials, scrollytelling, and charts that teach.

**Default profile:** usually *learner-paced* and text-led. That changes the weights:

- Redundancy and modality relax. Printed text is fine.
- **Spatial contiguity, segmenting, signaling, and generative activity** carry most of the load.
- When the app has narration or auto-playing animation, the system-paced rules return for that component.

## Structure: segment the lesson

- **One idea per view.** A view is a screen, a step, or a scroll section, whichever unit fits. It should hold one cause-and-effect link, one step, or one comparison. End each view with a clear next action ("Continue", "Try it", "Next: what happens when…").
- **Show progress and position** (for example, "Step 3 of 7" plus a step list). The visible structure is a signal.
- **Pre-training view first:** a labeled diagram of the parts, or "Meet the controls". Let experts collapse it or skip it ("I know these, skip ahead").
- **Recommended path, open navigation.** Novices follow the default path. Experts can jump using a table of contents or step list (see learner control in principles.md).

## Layout: keep words with their pictures

- **Label inside the graphic** with leader lines. Avoid legends and keys, numbered parts explained in a separate list, and captions below a long figure.
- **Sticky figure with stepping text** (scrollytelling). The graphic stays in view while short text steps scroll past, and each step changes the graphic's state *as it becomes active*. This is temporal and spatial contiguity at once. Check that the text step and the graphic state never drift out of sync, including on fast scrolls and at narrow widths.
- **Linked highlighting.** Hovering or focusing a term in the text highlights the matching part of the diagram, and the reverse. Give each concept one consistent color everywhere it appears: prose, diagram, code, and equation.
- **Feedback beside the input** it responds to. A toast in a far corner or a results page breaks contiguity.
- **Instructions on the same screen as the task.** Don't make the learner remember the directions from the previous screen.
- **Mobile:** stacking columns can separate a label from its graphic. Use inline labels, a sticky figure, or a figure placed directly above its own explanation. Check that a learner at 375px can read each label next to its part.

## Interactivity: make it generative, not busywork

The goal of an interaction is to make the learner select, organize, and integrate. An interaction that does none of these, like "click to reveal the next sentence", is extraneous.

- **Predict, then reveal.** Ask the learner to commit to a prediction ("Which bulb gets brighter?") before running the simulation or showing the answer. Then explain the gap between the prediction and the result.
- **Manipulate to discover** (enacting). Provide sliders and toggles on the essential variables, with immediate visible effects.
- **Implicit scaffolding**, from PhET's simulation research. Steer exploration through the design itself instead of instructions:
  - Start with few controls, and add the rest as the lesson advances.
  - Choose sensible default values.
  - Constrain ranges so every state teaches something.
  - Make cause and effect visible right away.
  - Show readouts next to the thing they measure.
- **Completion tasks.** Give a partially worked example and ask the learner to fill in the missing steps. Fade the support across exercises, and adapt the fading to how the learner performs.
- **Self-explanation prompts** after key steps: "Why did the current drop?" Offer a short free-text box or a multiple-choice "best explanation" item.
- **Concept-map or ordering drags** for organization: put the steps in order, or connect each cause to its effect.

## Practice and feedback

- Put a short retrieval check at the end of each segment, and space a few cumulative questions across the lesson.
- **Explanatory feedback.** Say *why* an answer is right or wrong, and point back to the relevant part of the graphic, highlighting it again.
- Use task-focused wording. Leave out confetti, streak shaming, leaderboards, and generic praise: they draw attention away from the task and toward the learner's ego or the game layer.
- Adapt the difficulty to performance. Learners who answer correctly skip worked steps, and struggling learners get more examples (this follows from expertise reversal).

## Motion and animation

- Animate only *changes the learner must learn*. Leave out ambient motion, parallax, auto-rotating carousels, and animated backgrounds (coherence).
- **Give every teaching animation controls:** play/pause, step forward and back, scrub, replay, and speed. Default to step-through for complex processes, and keep a persistent key-frame summary visible.
- Keep motion *congruent* (direction and timing match the concept) and *apprehensible* (slow enough to see; around 300–800 ms for a state change; longer for multi-part processes, or make them step-able).
- Respect `prefers-reduced-motion`: swap continuous motion for discrete state changes, keeping the information and dropping the movement. WCAG 2.2.2 (Pause, Stop, Hide) and 2.3.3 (Animation from Interactions).

```css
@media (prefers-reduced-motion: reduce) {
  .process-anim { animation: none; }
  .process-anim[data-step] { transition: none; } /* jump between states */
}
```

## Words on screen

- Use conversational second person ("Drag the slider and watch your current change"). Keep sentences short and words plain.
- **Define technical terms where they first appear** (inline definition or hover/focus tooltip). Keep a persistent glossary for re-reference.
- Headings work as signals. Make each one state the point ("Resistance limits current") rather than the topic ("Resistance").
- When the app includes narration, the narration explains and the screen shows labels and key terms only. Offer captions and a transcript.

## Charts and data visualizations in lessons

- Use **direct labels** on the lines or bars instead of a legend (spatial contiguity).
- **Annotate the takeaway** on the chart itself: an arrow and a short note at the point that matters (signaling). Make the title the claim ("Deaths fell after chlorination"), not the variable names.
- Remove chartjunk: 3D effects, heavy gridlines, decorative icons, and gradients (coherence).
- Reveal complex charts in stages: axes and one series first, then the comparison (segmenting).
- When you use several linked views, connect them explicitly with hover-linked highlighting and shared color (multiple representations).

## Interface chrome is extraneous load

- Keep the lesson the visual focus. Quiet the navigation and branding, and leave out hero images, sidebars of unrelated links, and auto-playing media.
- Avoid stock photos and decorative illustrations. Use visuals that explain.
- Let gamification serve the learning (practice volume, spaced review). Avoid gamification that competes with it (points for clicking through).

## Accessibility (non-negotiable, and mostly aligned with the principles)

- Write alt text that states the graphic's *function and takeaway*, not its appearance ("Diagram: current flows from the battery's + terminal through both bulbs in series"). For complex interactive graphics, also provide a text description or data table.
- Make every interaction keyboard-operable. Use visible focus. Make sure linked highlighting works on focus as well as hover.
- Announce feedback with `aria-live="polite"` and place it next to the input.
- Offer captions and transcripts for any audio or video. Never convey information by color alone; pair color with a label or pattern.
- Use contrast of at least 4.5:1 for text and 3:1 for essential graphic parts.

## Build checklist (web-specific)

- [ ] Every view teaches one idea and ends with a clear next action.
- [ ] Every label sits on or beside its part, including at 375px width.
- [ ] Every animation is controllable, congruent, and respects reduced motion.
- [ ] Every interaction makes the learner predict, manipulate, explain, or retrieve.
- [ ] Feedback explains why, and sits next to the response.
- [ ] Experts can skip pre-training and worked steps.
