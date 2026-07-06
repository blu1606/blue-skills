# Output Formats

## Vietnamese Diacritics Rule

All learner-facing Vietnamese text must use full Vietnamese diacritics. Do not write no-diacritic Vietnamese unless the user explicitly requests it.

Use these labels:
- `Đề ôn tập`, not `De on tap`
- `Mã đề`, not `Ma de`
- `Ngày tạo`, not `Ngay tao`
- `Số câu`, not `So cau`
- `Thời gian gợi ý`, not `Thoi gian goi y`
- `Tổng điểm`, not `Tong diem`
- `Phân bổ`, not `Phan bo`
- `Hướng dẫn`, not `Huong dan`
- `Câu hỏi`, not `Cau hoi`
- `Đáp án`, not `Dap an`
- `Giải thích ngắn`, not `Giai thich ngan`
- `Báo cáo chấm điểm`, not `Bao cao cham diem`

## File-First Rule

When generating an exam, write it to Markdown files in the study repository. Chat output should only summarize:
- exam path
- answer key path
- KB path
- how the learner should submit answers

Use:

```bash
python <skill-dir>/scripts/study_repo.py init --root <study-repo-path>
python <skill-dir>/scripts/study_repo.py new-exam --root <study-repo-path> --scope mixed --count 20
```

## Exam File Template

```markdown
# Đề ôn tập AI Thực Chiến - {scope}

Mã đề: {exam-code}
Ngày tạo: {YYYY-MM-DD HH:mm}
Số câu: {count}
Thời gian gợi ý: {minutes} phút
Tổng điểm: 100

## Phân bổ

| Phần | Số câu | Điểm | Chủ đề |
| --- | ---: | ---: | --- |
| Common | ... | ... | ... |
| Business | ... | ... | ... |
| Infrastructure | ... | ... | ... |
| App Build | ... | ... | ... |

## Hướng dẫn

- Trả lời MCQ bằng A/B/C/D.
- Multi-select ghi tất cả lựa chọn, ví dụ: A,C.
- Fill-in-blank ghi đáp án ngắn.
- Scenario/code trả lời ngắn gọn, đúng trọng tâm.

## Câu hỏi

**Câu 1.** ...
A. ...
B. ...
C. ...
D. ...
```

## Answer Key Template

```markdown
# Đáp án - {exam-code}

| Câu | Đáp án | Điểm | Topic | Difficulty | Giải thích ngắn |
| ---: | --- | ---: | --- | --- | --- |
| 1 | B | 4 | rag-pipeline | Medium | ... |

## Rubric tự luận/code

**Câu X (/8):**
- ... (2d)
- ... (2d)
- ... (2d)
- ... (2d)
```

## Grading Report Template

```markdown
## Báo cáo chấm điểm - {exam-code}

Tổng điểm: {score}/100 ({percent}%)

### Điểm theo phần

| Phần | Điểm | Nhận xét |
| --- | ---: | --- |
| Common | ... | ... |
| Business | ... | ... |
| Infrastructure | ... | ... |
| App Build | ... | ... |

### Câu sai / cần sửa

| Câu | Đáp án của bạn | Đáp án đúng | Lỗi gốc | Sửa nhanh |
| ---: | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |

### Cập nhật KB

- Topics lên mức: ...
- Topics cần ôn: ...
- Đề xuất drill tiếp theo: ...
```

## Short Chat Output

After writing files, output:
1. `Đã tạo đề: <exam_path>`
2. `Đã tạo đáp án/rubric: <answer_path>`
3. `Knowledge base: <kb_path>`
4. `Làm bài trong file đề, rồi gửi đáp án theo format: 1A 2B 3A,C ...`

Do not include answer key inline unless requested.
