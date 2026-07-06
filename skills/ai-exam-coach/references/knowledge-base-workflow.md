# Knowledge Base Workflow

## Locate KB

Use the project KB when provided or discoverable. Common names:
- `docs/user-knowledge-base.md`
- `docs/knowledge-base.md`
- `knowledge-base.md`
- `UKB.md`

If multiple exist, prefer the one tracking learner proficiency and exam history.

## Initialize Missing KB

If no KB exists, run:

```bash
python <skill-dir>/scripts/study_repo.py init --root <study-repo-path> --title "AI Practice Study"
```

This creates:
- `docs/user-knowledge-base.md`
- `exams/mock-exams/`
- `exams/mock-exams/answers/`
- `exams/common/`, `exams/business/`, `exams/infrastructure/`, `exams/app-build/`
- `reports/`

Do not create a one-off chat-only exam when the study repo is missing. Initialize the repo first, then create exam files.

## Before Generating

Read KB and extract:
- Current proficiency by module/topic.
- Recent scores and stale topics.
- Known misconceptions.
- Topics already over-tested.
- User preferences: language, style, difficulty, exam path.

Then select topics:
- 50-70% weak or stale topics.
- 20-30% broad coverage.
- 10-20% stretch topics from the target exam blueprint.

For a broad "tạo đề" request, if the KB has no clear weakness data, skip clarification and use the default mixed blueprint. Do not ask the user to choose among source folders, Day folders, or recently discovered course-note groups.

Append a generation record after creating an exam file:

```markdown
| YYYY-MM-DD | exam-code | Generated | scope/topics | pending | Intended drill: ... |
```

If the KB has no table for generated exams, add a short "Pending Practice" section.

## Exam File Creation

Before writing a generated exam, run:

```bash
python <skill-dir>/scripts/study_repo.py new-exam --root <study-repo-path> --scope mixed --count 20
```

Then write:
- student-facing questions to the returned `exam_path`
- answer key/rubric to the returned `answer_path`

Use `--scope common|business|infrastructure|app-build|mixed|mock` and `--slug <topic-slug>` when the user specifies a topic.

## During Grading

Map each question to:
- section/track
- topic tag
- difficulty
- points earned
- misconception if wrong

Use these levels:
- Blue/Ready: >= 85% and no severe conceptual miss.
- Green/Good: 70-84%.
- Yellow/Needs review: 50-69%.
- Red/Weak: < 50%.

## KB Update After Grading

Update only facts supported by the submission:
- Add exam history row with score, section scores, and short diagnosis.
- Update topic proficiency for topics tested.
- Add or remove weakness notes when evidence changed.
- Add next recommended drill.

Never:
- Delete prior attempts.
- Inflate readiness without score evidence.
- Mark a topic mastered from one easy recall question.
- Store sensitive personal info from chat in KB.

## Feedback Loop

When a user misses a question:
1. Identify the misconception.
2. Write the correction in one sentence.
3. Add a future-test hint: "test again via scenario", "test via fill-in", or "test via code".
4. Next generated exam should include 1-3 follow-up items for repeated misconceptions.

## Source Handling

Use available course notes and KB as grounding context. Do not disclose internal source paths in exam text, answer keys, reports, or final summaries.
