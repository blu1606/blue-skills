# Output Formats

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

When not writing files, output:
1. Exam metadata.
2. Questions.
3. "Gui dap an cua ban theo format: 1A 2B 3A,C ..."

Do not include answer key inline unless requested.
