# Pedagogy quality gates

## Required brief

Collect these facts before drafting. Combine questions into one numbered turn.

1. **Source** — Lab brief URL, starter repository/template, or owner-approved
   source material. Ask whether links are learner-visible.
2. **Mode** — individual or team. For a team, collect size, roles, and whether
   there is one submission per team or per learner.
3. **Learner context** — audience, prerequisites, Day code, duration, and
   tools/access already available.
4. **Outcome** — concrete artifact, observable behaviour, or decision a learner
   must produce. Do not accept a vague outcome such as “understand RAG”.
5. **Assessment** — submission location, tests, review criteria, rubric,
   deadline, and late-policy facts that are actually known.

If a required answer is absent, ask it. Do not infer it from a course title.
If the owner permits an assumption, label it `TODO — cần xác nhận` in the
draft; otherwise wait.

## Confirmation gate

Before a material draft, show a five-line summary:

```text
Brief đã chốt
- Mục tiêu:
- Người học / Day:
- Link nguồn:
- Hình thức:
- Deliverable và cách kiểm tra:
```

Ask for confirmation if the answers leave competing choices. When all facts
are explicit and the owner says “viết ngay”, proceed without a redundant turn.

## Learning-flow gate

Pass every item before returning a Lab:

- The opening states what learners will produce and what they need first.
- Each `##` section has one outcome, 2–5 actions in execution order, and one
  signal a novice can use to know whether it worked.
- Steps name where to act when relevant: file, terminal, service, or UI.
- Commands are copyable and explain expected output or failure symptom.
- Prerequisites are not hidden halfway through the task.
- The final submission says exactly what to submit and how it is evaluated.
- Keep scope proportional. Merge trivial clicks; split a change of tool,
  platform, or verifiable outcome.

## Hint gate

Use a `hint-<language>` block only after the task it helps. The sample must be
grounded in the starter repository and current tests. It must not reveal a
solution before the learner has a meaningful attempt point.
