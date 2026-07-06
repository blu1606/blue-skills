#!/usr/bin/env python3
"""Initialize AI study repositories and create exam markdown files."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path


DEFAULT_TITLE = "Ôn tập AI"


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "tong-on"


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def init_git(root: Path) -> bool:
    if (root / ".git").exists():
        return False
    subprocess.run(["git", "init", "-b", "main"], cwd=root, check=True)
    return True


def kb_template(title: str, now: datetime) -> str:
    today = now.strftime("%Y-%m-%d")
    return f"""# User Knowledge Base - {title}

Tài liệu này theo dõi lộ trình ôn tập, độ bao phủ kiến thức, điểm yếu và mức độ sẵn sàng của người học.

## Tổng quan

- Trạng thái: Chưa đánh giá.
- Điểm trung bình: N/A.
- Mức độ sẵn sàng: N/A.
- Cập nhật lần cuối: {today}.

## Ma trận kiến thức

| Mảng | Chủ đề | Bao phủ | Proficiency | Ghi chú / Điểm yếu |
| --- | --- | ---: | --- | --- |
| Chung | AI design patterns | 0% | Chưa đánh giá |  |
| Chung | RAG pipeline | 0% | Chưa đánh giá |  |
| Chung | Prompt engineering | 0% | Chưa đánh giá |  |
| Chung | Agent architecture | 0% | Chưa đánh giá |  |
| Chung | Observability | 0% | Chưa đánh giá |  |
| Chung | AI security | 0% | Chưa đánh giá |  |
| Business | Product management / ROI / roadmap | 0% | Chưa đánh giá |  |
| Business | Compliance / governance | 0% | Chưa đánh giá |  |
| Infrastructure | Data lakehouse / GPU FinOps / serving | 0% | Chưa đánh giá |  |
| Infrastructure | CI/CD / AI security | 0% | Chưa đánh giá |  |
| App Build | Advanced agents / RAG / LoRA / RAGAS | 0% | Chưa đánh giá |  |
| App Build | Code challenge | 0% | Chưa đánh giá |  |

## Lịch sử bài kiểm tra

| Ngày | Mã đề | Phạm vi | Điểm | Nhận xét |
| --- | --- | --- | --- | --- |

## Đề đang chờ làm

| Ngày | Mã đề | Phạm vi / Chủ đề | Trạng thái | Mục tiêu luyện tập |
| --- | --- | --- | --- | --- |

## Hàng đợi ôn lại

- Thêm các lỗi lặp lại sau khi chấm bài.
"""


def readme_template(title: str) -> str:
    return f"""# {title}

Workspace ôn tập được tạo cho luyện đề AI.

## Cấu trúc

- `docs/user-knowledge-base.md`: hồ sơ năng lực và lịch sử bài kiểm tra.
- `exams/mock-exams/`: đề luyện tập tổng hợp.
- `exams/mock-exams/answers/`: đáp án và rubric.
- `exams/common/`, `exams/business/`, `exams/infrastructure/`, `exams/app-build/`: đề luyện theo phạm vi.
- `reports/`: báo cáo chấm điểm và ghi chú ôn tập.

## Workflow

1. Tạo đề vào `exams/`.
2. Làm bài trong file đề hoặc gửi đáp án trong chat.
3. Chấm bài bằng đáp án/rubric.
4. Cập nhật `docs/user-knowledge-base.md`.
"""


def gitignore_template() -> str:
    return """# Local/private files
.env
.env.*
*.key
*.pem

# Generated caches
__pycache__/
.pytest_cache/
.DS_Store
Thumbs.db
"""


def init_repo(args: argparse.Namespace) -> None:
    root = Path(args.root).expanduser().resolve()
    now = datetime.now()
    root.mkdir(parents=True, exist_ok=True)

    dirs = [
        "docs",
        "exams/common",
        "exams/business",
        "exams/infrastructure",
        "exams/app-build",
        "exams/mock-exams/answers",
        "reports",
    ]
    created_dirs: list[str] = []
    for rel in dirs:
        path = root / rel
        if not path.exists():
            created_dirs.append(rel)
        path.mkdir(parents=True, exist_ok=True)

    created_files = []
    if write_if_missing(root / "README.md", readme_template(args.title)):
        created_files.append("README.md")
    if write_if_missing(root / ".gitignore", gitignore_template()):
        created_files.append(".gitignore")
    if write_if_missing(root / "docs" / "user-knowledge-base.md", kb_template(args.title, now)):
        created_files.append("docs/user-knowledge-base.md")

    git_created = False
    if args.git:
        git_created = init_git(root)

    result = {
        "root": str(root),
        "kb_path": str(root / "docs" / "user-knowledge-base.md"),
        "created_dirs": created_dirs,
        "created_files": created_files,
        "git_initialized": git_created,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


def table_has_data_rows(text: str, heading: str) -> bool:
    pattern = rf"##[^\n]*{re.escape(heading)}[^\n]*\s*\n(?P<body>.*?)(?:\n## |\Z)"
    match = re.search(pattern, text, flags=re.DOTALL | re.IGNORECASE)
    if not match:
        return False
    body = match.group("body")
    rows = [line.strip() for line in body.splitlines() if line.strip().startswith("|")]
    data_rows = [
        row for row in rows
        if not re.match(r"^\|\s*-+\s*\|", row)
        and not re.search(r"\|\s*(Ngày|Date|Mã đề|Exam Code|Mảng|Area)\s*\|", row, re.IGNORECASE)
    ]
    return any(row.count("|") >= 4 and not re.search(r"\|\s*\|", row) for row in data_rows)


def kb_status(args: argparse.Namespace) -> None:
    root = Path(args.root).expanduser().resolve()
    kb_path = root / "docs" / "user-knowledge-base.md"
    exists = kb_path.exists()
    text = kb_path.read_text(encoding="utf-8") if exists else ""

    has_exam_history = (
        table_has_data_rows(text, "Lịch sử bài kiểm tra")
        or table_has_data_rows(text, "Lịch sử bài Test")
        or table_has_data_rows(text, "Exam History")
    )
    has_review_items = bool(re.search(r"## (Hàng đợi ôn lại|Review Queue).*?\n\s*-\s+(?!Thêm các lỗi|Add repeated)", text, flags=re.DOTALL | re.IGNORECASE))
    has_nonzero_coverage = bool(re.search(r"\|\s*(?!0%)\d+%", text))
    has_assessed = bool(re.search(
        r"(🔵|🟢|🟡|🔴|\bReady\b|\bGood\b|\bNeeds review\b|\bWeak\b)",
        text,
        flags=re.IGNORECASE,
    ))
    is_empty = not exists or not (has_exam_history or has_review_items or has_nonzero_coverage or has_assessed)

    result = {
        "root": str(root),
        "kb_path": str(kb_path),
        "exists": exists,
        "is_empty": is_empty,
        "has_exam_history": has_exam_history,
        "has_review_items": has_review_items,
        "has_nonzero_coverage": has_nonzero_coverage,
        "has_assessed_proficiency": has_assessed,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


def scope_dir(scope: str) -> str:
    mapping = {
        "common": "exams/common",
        "business": "exams/business",
        "infrastructure": "exams/infrastructure",
        "app-build": "exams/app-build",
        "app_build": "exams/app-build",
        "mock": "exams/mock-exams",
        "mixed": "exams/mock-exams",
    }
    return mapping.get(scope, f"exams/{slugify(scope)}")


def exam_stub(title: str, code: str, scope: str, count: int, minutes: int, now: datetime) -> str:
    created = now.strftime("%Y-%m-%d %H:%M")
    return f"""# {title}

Mã đề: {code}
Ngày tạo: {created}
Phạm vi: {scope}
Số câu: {count}
Thời gian gợi ý: {minutes} phút
Tổng điểm: 100

## Phân bổ

| Phần | Số câu | Điểm | Chủ đề |
| --- | ---: | ---: | --- |
| Common | TBD | TBD | TBD |
| Business | TBD | TBD | TBD |
| Infrastructure | TBD | TBD | TBD |
| App Build | TBD | TBD | TBD |

## Hướng dẫn

- Trả lời MCQ bằng A/B/C/D.
- Multi-select ghi tất cả lựa chọn, ví dụ: A,C.
- Fill-in-blank ghi đáp án ngắn.
- Scenario/code trả lời ngắn gọn, đúng trọng tâm.

## Câu hỏi

<!-- Agent ghi câu hỏi dành cho người học tại đây. Không đưa đáp án vào file này. -->
"""


def answer_stub(title: str, code: str, scope: str, now: datetime) -> str:
    created = now.strftime("%Y-%m-%d %H:%M")
    return f"""# Đáp án và rubric - {title}

Mã đề: {code}
Ngày tạo: {created}
Phạm vi: {scope}

| Câu | Đáp án | Điểm | Topic | Difficulty | Giải thích ngắn |
| ---: | --- | ---: | --- | --- | --- |

## Rubric tự luận/code

<!-- Agent ghi đáp án, giải thích và rubric tại đây. -->
"""


def new_exam(args: argparse.Namespace) -> None:
    root = Path(args.root).expanduser().resolve()
    if not (root / "docs" / "user-knowledge-base.md").exists():
        init_args = argparse.Namespace(root=str(root), title=args.title, git=False)
        init_repo(init_args)

    now = datetime.now()
    stamp = now.strftime("%Y%m%d-%H%M")
    scope = slugify(args.scope)
    slug = slugify(args.slug or args.scope)
    code = args.code or f"{scope}-{stamp}"
    minutes = args.minutes or max(20, round(args.count * 3))
    title = args.title or f"Đề ôn tập AI - {args.scope}"

    exam_dir = root / scope_dir(scope)
    answer_dir = exam_dir / "answers"
    if scope in {"mock", "mixed"}:
        answer_dir = root / "exams" / "mock-exams" / "answers"

    exam_dir.mkdir(parents=True, exist_ok=True)
    answer_dir.mkdir(parents=True, exist_ok=True)

    exam_name = f"{code}-{slug}.md"
    answer_name = f"{code}-{slug}-answers.md"
    exam_path = exam_dir / exam_name
    answer_path = answer_dir / answer_name

    write_if_missing(exam_path, exam_stub(title, code, args.scope, args.count, minutes, now))
    write_if_missing(answer_path, answer_stub(title, code, args.scope, now))

    result = {
        "root": str(root),
        "kb_path": str(root / "docs" / "user-knowledge-base.md"),
        "exam_code": code,
        "exam_path": str(exam_path),
        "answer_path": str(answer_path),
        "scope": args.scope,
        "count": args.count,
        "minutes": minutes,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AI exam study repository helper")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="initialize a study repository")
    init_parser.add_argument("--root", required=True, help="study repository path")
    init_parser.add_argument("--title", default=DEFAULT_TITLE, help="study repository title")
    init_parser.add_argument("--no-git", dest="git", action="store_false", help="do not initialize git")
    init_parser.set_defaults(git=True, func=init_repo)

    status_parser = subparsers.add_parser("kb-status", help="inspect whether the learner KB has evidence")
    status_parser.add_argument("--root", required=True, help="study repository path")
    status_parser.set_defaults(func=kb_status)

    exam_parser = subparsers.add_parser("new-exam", help="create exam and answer markdown files")
    exam_parser.add_argument("--root", required=True, help="study repository path")
    exam_parser.add_argument("--title", default="Đề ôn tập AI", help="exam title")
    exam_parser.add_argument("--scope", default="mixed", help="common, business, infrastructure, app-build, mixed, mock")
    exam_parser.add_argument("--count", type=int, default=20, help="question count")
    exam_parser.add_argument("--minutes", type=int, default=None, help="suggested duration")
    exam_parser.add_argument("--slug", default=None, help="file slug")
    exam_parser.add_argument("--code", default=None, help="exam code")
    exam_parser.set_defaults(func=new_exam)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
