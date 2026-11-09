# Demonstrations

Covers live and recorded demos, software walkthroughs, procedure and lab demos, worked examples (math, code, writing), and product tours or onboarding flows that teach.

A demonstration is a **worked example**, a model of expert performance. For novices, studying a worked example beats solving the problem cold. The demo's job is to make the expert's *invisible reasoning* visible, then hand the task over to the learner.

## Shape of a teaching demo

1. **Goal and end state first.** Show what the finished result looks like and why it matters ("Here's the dashboard we'll build; it answers which region is behind target"). This gives the learner a target to organize the steps around, which acts as a signal.
2. **Pre-train the workspace.** Before any steps, show a labeled screenshot or a quick tour of the interface areas, tools, or parts used ("This is the Query panel; this is the Preview"). Learners who are hunting for the button can't attend to the concept.
3. **Steps in segments.** Each segment is one sub-goal ("Connect the data", "Filter to Q3"). Name the sub-goal as a heading or a spoken label. Research on *subgoal labeling* shows this helps learners transfer the procedure to new problems.
4. **Narrate the why, not just the what.** "I'm filtering *before* joining so the join stays small" turns a sequence of clicks into transferable reasoning. Add a self-explanation prompt at the key decisions: "Why do you think I filtered first?"
5. **Hand over.** The learner does a similar task right away: a completion task first (part done for them), then a full one. Fade the support.
6. **Vary.** A second example with different surface details but the same structure helps the learner abstract the procedure away from this one case.

## Camera, screen, and attention

- **Use a first-person perspective.** Film over the shoulder or from the operator's eye line, and record the screen at the user's resolution. This beats a third-person camera for learning assembly and procedures (Fiorella et al., 2017), because learners don't have to mentally rotate the view.
- **Zoom and highlight the active region** at the moment it matters: crop to the relevant panel, highlight the cursor, show a click ripple. A full 4K desktop at native size is a split-attention problem.
- **Show keyboard shortcuts and values next to the cursor** or the field, not in a far corner (spatial contiguity).
- **Speak while you act** (temporal contiguity). Avoid long silent stretches of typing or waiting, and avoid explaining a step after you've already done it.
- **Hands and gestures** carry information in physical demos. Keep them in frame and point at what you name (embodiment).

## Coherence for demos

- **Prepare the state:** test data loaded, accounts logged in, notifications off, a clean desktop, bookmarks bar hidden. Detours are extraneous load. Include an error only if handling that error is part of the goal, and then make it a deliberate, labeled segment ("Here's the most common mistake, and how to recover").
- Cut waiting time (builds, loads, renders) by editing or by narrating what's happening during it. Don't jump-cut past *essential* steps, though: the learner needs to see every step they'll have to perform.
- Show only the features the goal needs. A demo of everything the product can do teaches nothing well.

## Pacing

- Slower than you think. For novices, pause after each sub-goal. In a recorded demo, a learner can pause and replay; in a live one, they can't, so slow down and check in more often.
- In recorded demos, add chapters per sub-goal so learners can jump back to the step they're stuck on.
- Live demos: ask "Where would you click next?" before you click. Making learners predict is a cheap generative activity.

## Interactive walkthroughs and product tours

- **One step per tooltip, anchored to the element it describes** (spatial contiguity). Dim the rest of the UI (signaling).
- **Have the learner perform each action** rather than clicking "Next" through descriptions. Doing it is enacting, and it confirms they found the control.
- **Keep tours short** (3–5 steps per sub-goal). Let learners leave and resume. Offer a "skip, I know this" option for experienced users (expertise reversal).
- Write conversational, second-person microcopy: "Pick the column you want to group by".
- Trigger contextual help when the learner first reaches a feature, rather than front-loading one long tour of everything.

## Code and math worked examples

- Show the problem, then the solution **built up step by step**, with each step's reasoning beside it. Put comments next to the line, or annotations next to the equation term.
- Use **consistent color** to link each variable or term to the same thing in a diagram.
- Reveal steps one at a time, and ask the learner to predict the next step before showing it.
- Fade: full example → example with blanks to complete → problem to solve alone.

## Handouts and job aids

A step-by-step reference sheet (numbered steps with screenshots, labels on each screenshot) supports doing the task later. It is a *reference*, separate from the demo itself, so it can be text-heavy.

## Checklist (demo-specific)

- [ ] Opens with the goal and the end state.
- [ ] Workspace or parts are pre-trained with labels.
- [ ] Steps are grouped under named sub-goals.
- [ ] Narration explains *why* at each decision, with at least one self-explanation or prediction prompt.
- [ ] First-person view, with zoom and highlight on the active region.
- [ ] Prepared state: no detours, notifications, or unplanned errors.
- [ ] The learner performs a similar task immediately afterward, with faded support.
