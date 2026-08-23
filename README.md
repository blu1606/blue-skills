# Blue Skills

Reusable agent skills by Blue.

## Skills

### ai-exam-coach

Generate, grade, and adapt Vietnamese AI practice exams from a learner knowledge base. Generated Vietnamese content is written with full diacritics by default.

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
Init repo học tổng tại ./ai-study
```

Then:

```text
Tạo đề ôn tập AI Thực Chiến 20 câu
```

### vlearn-lab-authoring

Create or review VLearn Markdown Labs from a confirmed teaching brief. The
skill asks for the Lab/repository link, individual versus team mode,
deliverable/rubric, and execution constraints before it drafts. It validates
VLearn Markdown structure, learner flow, source faithfulness, and anti-slop
quality gates.

Install globally:

```bash
npx skills add blu1606/blue-skills --skill vlearn-lab-authoring -g -y
```

Then ask your agent:

```text
Soạn Lab Day 03 từ brief này. Hãy hỏi các thông tin còn thiếu trước khi viết.
```

or:

```text
Chấm bài này và cập nhật knowledge base
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
