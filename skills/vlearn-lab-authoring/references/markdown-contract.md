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

Use fenced blocks for commands. A `hint-python`, `hint-bash`, or
`hint-powershell` sample is optional: use it only for a grounded, useful small
reference after the learner has a meaningful attempt point; omit it when no
sample improves the next action or check. Use tables for comparison or
troubleshooting, not a linear sequence. Use a submission section only when it
names the artifact, destination, and verification.

## GitHub link and submission-folder contract

When the owner provides a GitHub Lab link, show that exact link early in the
opening or preparation section, before the learner is asked to install, clone,
or run anything from it. The link must be copyable and must not be replaced by
a guessed mirror, branch, or setup URL.

For a Lab with a submission, write the matching root-folder requirement in the
learner-facing submission section:

```text
# Cá nhân
KX-DAYXX-HoVaTen-MSSV/

# Nhóm
KX-DAYXX-TenNhom/
├── TEAMMATES.md
└── ...artifact đã xác nhận...
```

`TEAMMATES.md` belongs at the root of a team submission and lists every member's
full name and MSSV. Preserve `DAYXX` as the required naming pattern unless the
owner supplies a more specific confirmed Day value. Do not invent member names,
MSSVs, a GitHub link, or a submission destination.

## Portable constructs

Use headings, paragraphs, bullets, checklists, blockquotes, images, tables,
ordinary fenced code, optional `hint-*` fenced code, and these content blocks
sparingly:

```md
:::goal{title="Câu hỏi hoặc đầu ra của phần này"}
...
:::

:::decision{title="Lựa chọn cần hiểu"}
...
:::

:::caution{title="Rủi ro cần tránh"}
...
:::

:::checkpoint{title="Dấu hiệu có thể sang bước tiếp theo"}
...
:::
```

Use a block only when its title and body identify a real concept, decision,
risk, or verification signal. `:::reflect` remains for one answerable learner
reflection. Do not rely on raw HTML, JSX, custom CSS, nested directives,
hidden answer keys, or `<details>`/`<summary>` dropdowns: raw HTML is not
rendered by the Markdown reader.
