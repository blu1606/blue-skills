# Blue Skills

Reusable agent skills by Blue.

## Skills

### ai-exam-coach

Generate, grade, and adapt Vietnamese AI practice exams from a learner knowledge base.

Use it for:
- Initializing a reusable study repository with folders and a learner knowledge base.
- Creating AI practice exams and mock exams.
- Generating MCQ, multi-select, fill-in-blank, scenario, and code questions.
- Grading submissions with answer keys and rubrics.
- Updating learner knowledge profiles after generating or grading exams.

Install globally:

```bash
npx skills add blu1606/blue-skills --skill ai-exam-coach -g -y
```

Install for Codex:

```bash
npx skills add blu1606/blue-skills --skill ai-exam-coach -a codex -g -y
```

Install for Claude Code:

```bash
npx skills add blu1606/blue-skills --skill ai-exam-coach -a claude-code -g -y
```

Use after install by asking your agent:

```text
Init repo hoc tong tai ./ai-study
```

Then:

```text
Tao de on tap AI Thuc Chien 20 cau
```

or:

```text
Cham bai nay va cap nhat knowledge base
```

## Repository Layout

```text
skills/
  ai-exam-coach/
    SKILL.md
    scripts/
    references/
    evals/
```

## Security

Review skills before installing. This repository avoids embedding private source paths, credentials, or personal study data in the published skill.
