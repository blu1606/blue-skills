#!/usr/bin/env python3
"""Initialize AI study repositories and create exam markdown files."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path


DEFAULT_TITLE = "AI Practice Study"


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

This file tracks learner proficiency, exam coverage, and follow-up drills.

## Overview

- Status: Not assessed yet.
- Average score: N/A.
- Readiness: N/A.
- Last updated: {today}.

## Knowledge Matrix

| Area | Topic | Coverage | Proficiency | Notes / Weaknesses |
| --- | --- | ---: | --- | --- |
| Common | AI design patterns | 0% | Not assessed |  |
| Common | RAG pipeline | 0% | Not assessed |  |
| Common | Prompt engineering | 0% | Not assessed |  |
| Common | Agent architecture | 0% | Not assessed |  |
| Common | Observability | 0% | Not assessed |  |
| Common | AI security | 0% | Not assessed |  |
| Business | Product management / ROI / roadmap | 0% | Not assessed |  |
| Business | Compliance / governance | 0% | Not assessed |  |
| Infrastructure | Data lakehouse / GPU FinOps / serving | 0% | Not assessed |  |
| Infrastructure | CI/CD / AI security | 0% | Not assessed |  |
| App Build | Advanced agents / RAG / LoRA / RAGAS | 0% | Not assessed |  |
| App Build | Code challenge | 0% | Not assessed |  |

## Exam History

| Date | Exam Code | Scope | Score | Notes |
| --- | --- | --- | --- | --- |

## Pending Practice

| Date | Exam Code | Scope / Topics | Status | Intended Drill |
| --- | --- | --- | --- | --- |

## Review Queue

- Add repeated misses here after grading.
"""


def readme_template(title: str) -> str:
    return f"""# {title}

Study workspace generated for AI exam practice.

## Structure

- `docs/user-knowledge-base.md`: learner profile and exam history.
- `exams/mock-exams/`: mixed practice exams.
- `exams/mock-exams/answers/`: answer keys and rubrics.
- `exams/common/`, `exams/business/`, `exams/infrastructure/`, `exams/app-build/`: scoped drills.
- `reports/`: grading reports and review notes.

## Workflow

1. Generate an exam into `exams/`.
2. Complete answers in the exam file or send answers in chat.
3. Grade with the answer key/rubric.
4. Update `docs/user-knowledge-base.md`.
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

Ma de: {code}
Ngay tao: {created}
Pham vi: {scope}
So cau: {count}
Thoi gian goi y: {minutes} phut
Tong diem: 100

## Phan bo

| Phan | So cau | Diem | Chu de |
| --- | ---: | ---: | --- |
| Common | TBD | TBD | TBD |
| Business | TBD | TBD | TBD |
| Infrastructure | TBD | TBD | TBD |
| App Build | TBD | TBD | TBD |

## Huong dan

- Tra loi MCQ bang A/B/C/D.
- Multi-select ghi tat ca lua chon, vi du: A,C.
- Fill-in-blank ghi dap an ngan.
- Scenario/code tra loi ngan gon, dung trong tam.

## Cau hoi

<!-- Agent writes student-facing questions here. Do not include answer key in this file. -->
"""


def answer_stub(title: str, code: str, scope: str, now: datetime) -> str:
    created = now.strftime("%Y-%m-%d %H:%M")
    return f"""# Dap an va rubric - {title}

Ma de: {code}
Ngay tao: {created}
Pham vi: {scope}

| Cau | Dap an | Diem | Topic | Difficulty | Giai thich ngan |
| ---: | --- | ---: | --- | --- | --- |

## Rubric tu luan/code

<!-- Agent writes answer key, rationales, and rubrics here. -->
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
    title = args.title or f"De on tap AI - {args.scope}"

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

    exam_parser = subparsers.add_parser("new-exam", help="create exam and answer markdown files")
    exam_parser.add_argument("--root", required=True, help="study repository path")
    exam_parser.add_argument("--title", default="De on tap AI", help="exam title")
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
