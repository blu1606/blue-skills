# Anti-slop quality gates

## Source-faithfulness gate

Reject or revise a draft that contains any of these without owner evidence:

- invented repository, URL, file name, API, environment variable, version,
  command output, test result, deadline, rubric, or citation;
- a team arrangement, scoring rule, or submission channel not confirmed in the
  brief;
- an example presented as real course material;
- a security instruction that asks learners to paste a secret into source code.

Ask a focused question or use `TODO — cần xác nhận` only with owner approval.

## Specificity gate

For each paragraph, identify one learner action, verification, or decision. If
none exists, delete it or replace it with a concrete instruction. Prefer:

- `Chạy pytest tests/test_api.py -v và kiểm tra 3 passed.`
- `Mở template.py, thay TODO trong hàm parse_input.`

Avoid empty claims such as “khám phá”, “mạnh mẽ”, “toàn diện”, “dễ dàng”,
“seamless”, “robust”, or “best practice” unless the following sentence names
the action and acceptance criterion that make the claim meaningful.

## Structure gate

- Do not repeat the same goal in the introduction, each section, and a closing
  recap.
- Do not add sections, learning outcomes, warnings, diagrams, or reflection
  prompts just to make the Lab look substantial.
- Use one direct verb per action. Break long, multi-action sentences.
- Keep explanations adjacent to the decision they justify.
- Do not give a sample solution before the learner has an attempt point.

## Final read-through

Read the Lab as a new learner and answer yes to all:

1. Do I know where to begin?
2. Do I know the exact artifact or behaviour I must produce?
3. Can I run or observe a real completion signal after each section?
4. Do I know what to submit, where, and whether I work alone or with a team?
5. Are all unknown facts visibly unresolved instead of invented?

## Review mode

When asked to review rather than draft, do not label prose as “AI-written” or
apply a phrase blacklist. Report only observable issues in this form:

`<vị trí> → <vấn đề thấy được> → <sửa tối thiểu bám nguồn>`

Check whether each section advances the confirmed artifact, each paragraph
contains an action, verification, or decision, and decorative headings,
recaps, warnings, reflections, or “why it matters” text actually affect
completion. Remove only the text that fails that test. Preserve useful lists,
tables, short explanations, and the learner's supplied terminology.
