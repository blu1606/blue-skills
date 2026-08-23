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

`description`, `outcomes`, `prerequisites`, `requiredTools`, and `commonErrors`
become learner-facing reading blocks. `requiresSubmission` must be `false`
only when no artifact is submitted. `workMode` documents the agreed work mode;
the text must still state team size/roles and submission policy when relevant.

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
`hint-powershell` only for a grounded sample solution. Use tables for
comparison or troubleshooting, not a linear sequence. Use a submission section
only when it names the artifact, destination, and verification.

## Portable constructs

Use headings, paragraphs, bullets, checklists, blockquotes, images, tables,
ordinary fenced code, `hint-*` fenced code, and `:::reflect` sparingly. Do not
rely on raw HTML, JSX, custom CSS, nested directives, or hidden answer keys.
