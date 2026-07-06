# Exam Blueprint

## Core Midterm-Inspired Structure

Use this structure when the user asks for AI Thuc Chien, midterm, mock exam, or broad review.

For a broad request such as "tạo đề" or "tạo đề ôn tập", generate this mixed exam immediately. Do not ask the user to choose Day folders or source-note groups. Day/course files are grounding sources, not the exam structure.

| Section | Weight | Time | Coverage |
| --- | ---: | ---: | --- |
| Part I - Common | 50% | 60 min for full exam | AI design patterns, RAG pipeline, prompt engineering, agent architecture, observability, AI security |
| Part II - Business | 16-17% | Track segment | Product management, ROI, AI roadmap, EU AI Act, Vietnam AI/legal context |
| Part III - Infrastructure | 16-17% | Track segment | Data lakehouse, GPU FinOps, model serving, CI/CD, AI security |
| Part IV - App Build | 16-17% | Track segment | Advanced agent patterns, advanced RAG, LoRA/QLoRA, RAGAS metrics, code challenge |

For 20-question default:
- Common: 10 questions.
- Business: 3 questions.
- Infrastructure: 3 questions.
- App Build: 4 questions.

Default mixed topic coverage:
- Common questions must cover at least 4 of: AI design patterns, RAG pipeline, prompt engineering, agent architecture, observability, AI security.
- Business questions must cover at least 2 of: product management, ROI, AI roadmap, EU AI Act, Vietnam AI/legal context.
- Infrastructure questions must cover at least 2 of: data lakehouse, GPU FinOps, model serving, CI/CD, AI security.
- App Build questions must cover at least 2 of: advanced agent patterns, advanced RAG, LoRA/QLoRA, RAGAS metrics, code challenge.

For user-specified counts:
- Preserve the 50% common / 50% tracks split when count >= 12.
- For small drills (<12), prioritize requested topic and weak KB topics.
- For track-only drills, allocate all questions to that track.

Clarification rule:
- If no topic is specified, do not ask for one; use the default mixed exam.
- If a day folder is discovered during scouting, map its concepts into the blueprint silently.
- Ask only when the user explicitly says "theo ngày", "Day X", or gives contradictory scopes.

Exception: if the learner KB is empty, ask the onboarding question from `knowledge-base-workflow.md` before generating. This is not a topic clarification; it chooses between baseline diagnosis and skill-specific practice.

## Diagnostic Exam Blueprint

Use this when KB is empty and the user chooses diagnostic.

Goal:
- Measure initial proficiency, not remediate known weaknesses.
- Cover broad fundamentals with enough applied questions to expose gaps.
- Produce data for `Knowledge Matrix`, `Exam History`, and `Review Queue`.

Default 20-question diagnostic:
- Common: 10 questions.
- Business: 3 questions.
- Infrastructure: 3 questions.
- App Build: 4 questions.

Diagnostic difficulty:
- Easy: 40%.
- Medium: 45%.
- Hard: 15%.

Diagnostic type mix:
- 10 single-answer MCQ.
- 3 multi-select.
- 4 fill-in-blank / short factual.
- 2 scenario debug / product decision.
- 1 code or pseudocode challenge.

After grading diagnostic:
- Do not mark any topic "Ready" from one easy item.
- Mark strong topics as "baseline good" until confirmed by a later drill.
- Prioritize next drills from the lowest scoring sections.

## Question Type Mix

Default 20-question mix:
- 9 single-answer MCQ.
- 4 multi-select.
- 4 fill-in-blank or short factual answer.
- 2 scenario debug / product decision.
- 1 code or pseudocode challenge when App Build or Infrastructure is in scope.

Do not force code questions into Business-only drills.

## Scoring

Default 100-point scoring for 20 questions:
- Single-answer MCQ: 4 points each.
- Multi-select: 5 points each; partial credit allowed only if rubric says so.
- Fill-in-blank: 4 points each.
- Scenario/debug: 8 points each.
- Code challenge: 8 points.

For non-20 counts, state per-question points clearly and keep total at 100 unless user requests raw points.

## Difficulty

Default distribution:
- Easy/remember-understand: 30%.
- Medium/apply-analyze: 50%.
- Hard/evaluate-create/debug: 20%.

For final review, bias toward medium/hard scenario questions. For weak-topic remediation, start medium and include explanations after grading.

## Student-Facing Rules

- Do not reveal answers in the exam file unless requested.
- Include clear instructions, time estimate, and answer format.
- Number questions continuously.
- Tag questions internally in the answer key: section, topic, difficulty, cognitive level.
- Avoid "according to the material" phrasing; ask the concept directly.
