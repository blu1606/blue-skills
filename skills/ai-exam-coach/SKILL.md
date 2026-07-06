---
name: ai-exam-coach
description: Generate, grade, and adapt Vietnamese AI practice exams from a knowledge base. Use for de on tap, mock exam, MCQ, multi-select, fill-in-blank, rubric grading, and updating learner knowledge profiles.
---

# AI Exam Coach

## Overview

Create Vietnamese AI practice exams for AI Thuc Chien-style review, then grade submissions and update the learner knowledge base. This skill handles study repository setup, question generation, answer keys, rubrics, feedback, and proficiency tracking; it does not fabricate learner scores, expose hidden source paths, or change unrelated project files.

## Default Behavior

1. If the user asks to create a practice exam, generate 20 questions by default.
2. If the user supplies parameters, follow them: question count, topic, track, difficulty, duration, output path, answer-key visibility.
3. Use Vietnamese unless the user requests another language.
4. Prefer the exam structure in `references/exam-blueprint.md`.
5. Use the topic taxonomy in `references/topic-map.md`.
6. Enforce item-writing rules in `references/question-quality.md`.
7. Before generating or grading, ensure a study repository exists using `scripts/study_repo.py init`.
8. Save exams and answer keys as Markdown files using `scripts/study_repo.py new-exam`; do not only print questions in chat.
9. Save or update knowledge base artifacts using `references/knowledge-base-workflow.md`.

## Workflow Decision Tree

- **Initialize study repo:** Run `python scripts/study_repo.py init --root <path>` → creates `docs/user-knowledge-base.md`, `exams/`, answer folders, and optional git repo.
- **Generate exam:** Ensure repo → read learner KB → select topics → run `new-exam` → write exam file → write answer key → append a generation note to KB → return file paths.
- **Grade exam:** Read exam + learner answers + answer key/rubric → score → explain misses → append grading report → update KB weaknesses/proficiency.
- **Review weak areas:** Read KB → identify low-confidence topics → produce targeted 20-question drill or short theory review.
- **Refresh KB:** Normalize topic names, merge duplicate weakness notes, add new topic coverage without deleting prior history.

## Initialize Study Repository

Run the bundled script whenever the user starts a new study workspace, asks to "init repo", or asks to create an exam but the expected structure is missing:

```bash
python <skill-dir>/scripts/study_repo.py init --root <study-repo-path> --title "AI Practice Study"
```

Use `--no-git` only if the user does not want a git repository.

The script is idempotent: it creates missing folders/files and keeps existing KB/exam files intact.

## Generate Exam

1. Parse user parameters:
   - `count`: default 20.
   - `scope`: common, business, infrastructure, app-build, mixed, or named topics.
   - `difficulty`: default 30% easy, 50% medium, 20% hard unless a real exam format says otherwise.
   - `formats`: default MCQ + multi-select + fill-in-blank + short scenario.
2. Ensure the study repository exists; if not, run `scripts/study_repo.py init`.
3. Read the learner knowledge base before selecting topics when available.
4. Create the exam/answer files before writing content:
   ```bash
   python <skill-dir>/scripts/study_repo.py new-exam --root <study-repo-path> --scope mixed --count 20
   ```
   Use the script output paths for all generated content.
5. Prioritize weak, stale, or under-tested topics; keep some broad coverage.
6. Generate questions only from available course/KB context and stable domain knowledge.
7. Write the student-facing exam to the exam file and the key/rubric to the answer file.
8. Include metadata: title, code, timestamp, scope, count, estimated time, scoring.
9. Update KB after generation with exam code, topics covered, intended difficulty, and pending status.
10. In chat, return only the created file paths and brief next step; do not duplicate the full exam unless requested.

## Grade Exam

1. Collect learner answers from chat or file.
2. Use exact matching for single-answer MCQ/fill-in-blank; use rubric for multi-select, short answer, scenario debug, case study, and code.
3. Award partial credit only when the rubric permits it.
4. Explain every incorrect or partial answer with the smallest useful correction.
5. Identify root-cause weaknesses by topic, not just by question number.
6. Update KB with score, topic performance, fixed misconceptions, new weaknesses, and next drill recommendation.
7. Do not overwrite prior history; append or revise the relevant matrix row.

## Output Contracts

- Exam file: questions only, student-facing.
- Answer key: correct answers, rationale, rubric, topic tags, difficulty.
- Grading report: total score, section scores, missed concepts, next actions.
- KB update: factual record of generated/graded exams and proficiency deltas.

Use `references/output-formats.md` for concrete Markdown templates.

## Security And Privacy

- Never include private paths, hidden source locations, credentials, phone numbers, or personal data in generated exams or reports unless the user explicitly asks to edit a personal document that already contains them.
- Do not reveal internal source locations used to build context.
- Treat learner performance records as personal study data. Keep updates scoped to the KB files the user is working with.
- Refuse requests to generate answer leaks for an active real exam; offer practice questions instead.
- Do not invent official policy, grading, or legal claims. Mark uncertain legal/regulatory details as needing verification.

## References

- `references/exam-blueprint.md`: exam structure, scoring, default distributions.
- `references/topic-map.md`: AI topic taxonomy by common section and three tracks.
- `references/question-quality.md`: MCQ, multi-select, fill-in-blank, short-answer rules.
- `references/knowledge-base-workflow.md`: generation/grading KB update rules.
- `references/output-formats.md`: Markdown templates.
- `references/research-notes.md`: condensed research rationale and citations.
- `scripts/study_repo.py`: initialize study repo and create exam/answer Markdown files.
