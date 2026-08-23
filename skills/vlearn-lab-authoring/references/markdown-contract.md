# VLearn Markdown contract

## Minimum valid import

The VLearn Markdown importer accepts front matter, but does not require it.
Every document must have at least one `##` heading; each `##` becomes one
reader section. Without front matter, use one leading `#` heading so the module
has a title.

## Recommended front matter

Use only facts that the owner supplied. Omit unknown fields rather than filling
them with generic text.

```yaml
---
id: "day03-track01-example" # optional stable source slug
day: "D03" # required when the confirmed brief names a Day
title: "Lab 03 — ..."
description: "Một câu nêu artifact hoặc kỹ năng kiểm chứng được."
outcomes:
  - "..."
prerequisites:
  - "..."
requiredTools:
  - "..."
commonErrors:
  - "Triệu chứng cụ thể → cách xử lý cụ thể"
requiresSubmission: true
workMode: "individual" # hoặc team
---
```

`id` and `day` identify the Markdown source in Studio; they do not become
learner-facing reading blocks. When the confirmed brief names a Day, `day` is
required and must use the canonical `DNN` form (for example, `D21`).
`description`, `outcomes`, `prerequisites`, `requiredTools`, and `commonErrors`
become learner-facing reading blocks. `requiresSubmission` must be `false`
only when no artifact is submitted. The importer creates a submission form by
default, so suppress it only with the unquoted YAML boolean
`requiresSubmission: false`. `workMode` documents the agreed work mode; the
text must still state team size/roles and submission policy when relevant.

## Metadata validation gate

Before returning a source with front matter, verify all of the following:

- Opening and closing `---` delimiters are on their own lines, and the content
  is a YAML mapping.
- Use only the supported keys shown above. `day`, when present, is an exact
  `DNN` value that matches the confirmed brief. `id`, when present, is a
  confirmed stable source slug. Omit unknown facts; do not add `duration`,
  `difficulty`, `author`, tags, or custom keys until importer support is
  confirmed.
- `outcomes`, `prerequisites`, `requiredTools`, and `commonErrors` are YAML
  lists when present. `requiresSubmission` is a boolean and `workMode` is
  exactly `individual` or `team`.
- Do not leave empty, duplicate, placeholder, or inferred metadata values.
- The body agrees with the metadata: its title and sections serve the stated
  outcomes; `requiresSubmission: true` has an exact submission instruction;
  a team Lab states confirmed roles, size, and submission policy.

## Section pattern

```md
# Lab 03 — Tên cụ thể

## Chuẩn bị repo và chạy baseline

Mục tiêu: thấy được <output hoặc trạng thái> trước khi sửa.

1. Trong <nơi thao tác>, mở <file hoặc URL>.
2. Chạy <lệnh thật>.

Kết quả mong đợi: <output, file, UI state, hoặc test cụ thể>.

## Hoàn thành <artifact cụ thể>

...
```

Use fenced blocks for commands. Use `hint-python`, `hint-bash`, or
`hint-powershell` only for a grounded sample solution after the learner has a
meaningful attempt point. Use tables for comparison or troubleshooting, not a
linear sequence. Use a submission section only when it names the artifact,
destination, and verification.

## Portable constructs

Use headings, paragraphs, bullets, checklists, blockquotes, images, tables,
ordinary fenced code, `hint-*` fenced code, and `:::reflect` sparingly. Do not
rely on raw HTML, JSX, custom CSS, nested directives, or hidden answer keys.
