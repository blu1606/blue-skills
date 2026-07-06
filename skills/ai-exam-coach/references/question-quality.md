# Question Quality Rules

## Generation Principles

1. Align every question to one topic and one learning objective.
2. Prefer applied reasoning over definition recall, especially for medium/hard items.
3. Use plausible distractors based on common misconceptions from the KB.
4. Keep wording direct and positive; avoid "except", "not", "least" unless testing that distinction is essential.
5. Avoid "all of the above", "none of the above", joke options, and obviously longer correct answers.
6. Make each question independent; do not require answers from previous questions.
7. Include rationale in the answer key for why each correct answer is correct and why attractive distractors are wrong.

## Single-Answer MCQ

Required structure:
- Stem fully states the problem.
- Four options A-D.
- Exactly one best answer.
- Distractors are parallel in length, grammar, and specificity.

Good uses:
- Concept distinction: Data Drift vs Concept Drift.
- Architecture choice: RAG vs fine-tuning vs rules.
- Metric choice: Precision/Recall/F1/Goodput.
- Debug diagnosis from a short trace/log/code snippet.

## Multi-Select

Required structure:
- State "Chọn tất cả đáp án đúng".
- Usually 2 correct options out of 4 or 5.
- Avoid partial-credit ambiguity in the exam; put grading policy in answer key.
- Distractors should be individually plausible, not mutually exclusive giveaways.

Scoring default:
- Full credit: all and only correct options.
- Half credit: all selected options are correct but incomplete, or one incorrect selection with most correct options.
- Zero: mostly guessing or selecting contradictory options.

## Fill-In-Blank / Short Factual

Use for:
- Key terms: TTFT, context precision, LoRA rank.
- Simple calculations: Bayes, F1, token cost, latency.
- One-line command/concept completion.

Rules:
- Blank must have one expected answer or a small accepted set.
- Avoid blanks that depend on exact prose memorization.
- Provide accepted variants in answer key.

## Scenario Debug / Case Study

Use for:
- Agent loop/error handling.
- RAG hallucination or low faithfulness.
- AI product metric mismatch.
- Compliance/privacy incident response.
- Infra bottleneck diagnosis.

Rubric should allocate points across 3-5 concrete criteria:
- Correct diagnosis.
- Evidence from scenario.
- Practical mitigation.
- Trade-off or risk.
- Measurement/eval plan.

## Code Challenge

Rules:
- Keep solvable in 10-15 minutes unless user requests harder.
- Provide input/output and edge cases.
- Prefer Python, Pandas, NumPy, simple API glue, eval parsing, or data cleaning.
- Answer key includes reference solution and complexity/edge-case notes.

## Anti-Patterns

- Trivia without practical value.
- Questions whose answer is "it depends" without a rubric.
- Legal questions that require exact current law when not verified.
- Overly broad prompts: "Design an entire AI platform".
- Distractors that are absurd, overlapping, or grammatically incompatible.
