# Output Formats

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
# De on tap AI Thuc Chien - {scope}

Ma de: {exam-code}
Ngay tao: {YYYY-MM-DD HH:mm}
So cau: {count}
Thoi gian goi y: {minutes} phut
Tong diem: 100

## Phan bo

| Phan | So cau | Diem | Chu de |
| --- | ---: | ---: | --- |
| Common | ... | ... | ... |
| Business | ... | ... | ... |
| Infrastructure | ... | ... | ... |
| App Build | ... | ... | ... |

## Huong dan

- Tra loi MCQ bang A/B/C/D.
- Multi-select ghi tat ca lua chon, vi du: A,C.
- Fill-in-blank ghi dap an ngan.
- Scenario/code tra loi ngan gon, dung trong tam.

## Cau hoi

**Cau 1.** ...
A. ...
B. ...
C. ...
D. ...
```

## Answer Key Template

```markdown
# Dap an - {exam-code}

| Cau | Dap an | Diem | Topic | Difficulty | Giai thich ngan |
| ---: | --- | ---: | --- | --- | --- |
| 1 | B | 4 | rag-pipeline | Medium | ... |

## Rubric tu luan/code

**Cau X (/8):**
- ... (2d)
- ... (2d)
- ... (2d)
- ... (2d)
```

## Grading Report Template

```markdown
## Bao cao cham diem - {exam-code}

Tong diem: {score}/100 ({percent}%)

### Diem theo phan

| Phan | Diem | Nhan xet |
| --- | ---: | --- |
| Common | ... | ... |
| Business | ... | ... |
| Infrastructure | ... | ... |
| App Build | ... | ... |

### Cau sai / can sua

| Cau | Dap an cua ban | Dap an dung | Loi goc | Sua nhanh |
| ---: | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |

### Cap nhat KB

- Topics len muc: ...
- Topics can on: ...
- De xuat drill tiep theo: ...
```

## Short Chat Output

After writing files, output:
1. `Da tao de: <exam_path>`
2. `Da tao dap an/rubric: <answer_path>`
3. `Knowledge base: <kb_path>`
4. `Lam bai trong file de, roi gui dap an theo format: 1A 2B 3A,C ...`

Do not include answer key inline unless requested.
