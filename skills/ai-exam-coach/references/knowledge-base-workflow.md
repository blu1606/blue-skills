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

First check whether the KB has learner evidence:

```bash
python <skill-dir>/scripts/study_repo.py kb-status --root <study-repo-path>
```

Treat KB as empty when:
- `Exam History` has no attempt rows.
- `Knowledge Matrix` still has only `0%` coverage or `Chưa đánh giá`/`Not assessed`.
- `Review Queue` has no real weakness items.
- No graded diagnostic or practice report exists.

If KB is empty, do not claim personalization. Ask exactly one onboarding question:

```text
Knowledge base hiện chưa có dữ liệu năng lực. Bạn muốn:
1. Làm bài diagnostic tổng hợp 20 câu (Recommended) để đo baseline ban đầu
2. Luyện từng kỹ năng, ví dụ RAG, Agent, Prompt Engineering, RAGAS, AI Product, Model Serving
```

If the user chooses diagnostic, create a diagnostic mixed exam. If the user chooses skill drill, ask for the skill only if it was not already specified.

Then select topics:
- 50-70% weak or stale topics.
- 20-30% broad coverage.
- 10-20% stretch topics from the target exam blueprint.

For a broad "tạo đề" request with a non-empty KB, skip clarification and use the default mixed blueprint plus KB weaknesses. Do not ask the user to choose among source folders, Day folders, or recently discovered course-note groups.

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

If grading a diagnostic exam, use the result to initialize the learner profile:
- Fill initial proficiency levels by section/topic.
- Add the first `Exam History` row.
- Create `Review Queue` from missed or partial-credit topics.
- Recommend the next 1-2 drills based on lowest sections.

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
