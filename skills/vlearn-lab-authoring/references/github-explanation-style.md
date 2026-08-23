# Explain a GitHub Lab for a real learner

Use this guide after retrieving the exact GitHub Markdown source. The goal is
not to reformat a README. It is to help a learner understand the actual Lab
well enough to complete it without losing the source's technical meaning.

## Map the source before writing

Identify only facts visible in the retrieved file:

- the Lab's real goal and final artifact or observable result;
- the sequence of files, commands, services, or decisions the learner must
  move through;
- prerequisite concepts or setup the source states;
- expected checkpoints, failures, and submission details the source actually
  gives.

If the source names a command but not its purpose, explain only the visible
effect or ask the owner for context. Do not invent an architecture, business
story, test output, or rationale to make the prose more engaging.

## Write as a connected walkthrough

Start each major phase with a short paragraph that tells the learner where they
are in the Lab, why this next action matters to the confirmed outcome, and what
they should notice. Then give the ordered actions. Follow code or a command
with the relevant expected observation and a brief interpretation when the
source supports it. Bridge naturally to the next phase when the previous
checkpoint enables it.

Use natural Vietnamese prose with full diacritics and complete sentences. Mix
brief explanatory paragraphs with numbered actions when the order matters. A
short sentence is welcome when it carries one clear idea; do not make every
line a slogan, imperative fragment, or label. Prefer the learner's everyday
view: “Trước hết, hãy … để …”, “Khi thấy …, bạn biết rằng …”, “Từ kết quả này,
bạn có thể …”. Do not force these exact phrases or add a transition where the
connection is already clear.

## Keep the explanation useful

- Explain a term at its first decision point when a novice needs it to act;
  do not add a textbook detour.
- Name the real file, command, or UI location before asking the learner to use
  it. Describe code by its stated role, inputs, outputs, or nearby behaviour,
  not by guessed internals.
- Keep the “why” next to the action it justifies. Do not collect generic theory
  in an opening wall of text or append a ceremonial recap.
- Preserve the source's official names, URLs, commands, and rubric wording.
  Quote code exactly; explain around it in plain language.
- For a genuine gap, ask a focused question or use an owner-approved TODO.
  Smooth writing must not hide uncertainty.

## Readability gate

Before returning, read each section as a learner and check:

1. Can I tell what this phase contributes to the final Lab outcome?
2. Does the explanation lead naturally into the action instead of repeating a
   heading or issuing an unexplained command?
3. After the action, do I know what to look for and why it matters?
4. Are paragraphs short enough to scan but complete enough to sound human?
5. Did every technical claim come from the GitHub source or confirmed brief?
