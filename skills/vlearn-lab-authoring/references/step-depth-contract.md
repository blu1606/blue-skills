# Độ sâu tối thiểu cho một step Lab

Dùng contract này khi người học cần hiểu một quy trình kỹ thuật, không chỉ chép
lệnh. Mục tiêu là mỗi section đủ dài để giải thích bản chất và quyết định, nhưng
không kéo dài bằng kiến thức ngoài nguồn, recap, hay câu chữ chung chung.

## Ngân sách từ theo loại section

Đếm **prose dành cho người học**; không tính YAML, heading, URL, code fence,
bảng, checklist hoặc khối `:::reflect`.

| Loại section `##` | Số từ mục tiêu | Khi dùng |
| --- | ---: | --- |
| Chuẩn bị hoặc định hướng | 180–300 | Chọn môi trường, mở repo, xác định đích đến |
| Thao tác kỹ thuật hoặc quyết định chính | 500–1.000 | Data, cấu hình, train, debug, đánh giá, so sánh |
| Nộp bài hoặc tổng kết có artifact | 220–360 | Verify, đóng gói, report và điều kiện hoàn thành |

Nếu nguồn không đủ dữ kiện để đạt độ sâu này mà không suy diễn, hỏi một câu
tập trung hoặc giữ section ngắn và nêu rõ giới hạn. Không bịa giải thích để đủ
số từ.

## Cấu trúc bắt buộc cho section kỹ thuật hoặc quyết định chính

Mỗi section phải đi theo đường suy nghĩ của người học, theo thứ tự phù hợp:

1. **Bản chất và câu hỏi đang giải quyết** — 120–200 từ. Nêu trạng thái hiện
   tại, khái niệm hoặc rủi ro thực tế, và vì sao bước này cần cho artifact cuối.
2. **Giải nghĩa từ khóa** — 100–160 từ khi một thuật ngữ quyết định thao tác.
   Nói thuật ngữ đó có nghĩa gì *trong Lab này*, nó ảnh hưởng quyết định nào,
   và nhầm lẫn nào cần tránh. Dùng glossary inline khi construct được hỗ trợ.
3. **Giải thích lựa chọn thiết kế** — 100–180 từ khi section có hàm, file,
   cấu hình hoặc phương án trung tâm. Nêu trách nhiệm, input/output hoặc tác
   động của nó; lợi ích, chi phí/rủi ro và phương án thay thế. Chỉ giải thích
   vì sao A được chọn thay B khi nguồn hoặc brief xác nhận rationale đó. Nếu
   nguồn chỉ yêu cầu dùng A, nói rõ đó là contract cần giữ và không suy diễn
   lý do tác giả không cung cấp.
4. **Thao tác có lý do** — 2–5 hành động theo thứ tự. Mỗi hành động gồm nơi
   làm, việc làm, lý do làm lúc này, điều bị đánh đổi hoặc cần giữ nguyên, và
   điều cần quan sát; một lệnh trần không phải là một step hoàn chỉnh.
5. **Checkpoint và chuyển pha** — 80–160 từ. Nêu artifact/trạng thái cần thấy,
   cách đọc nó, rồi giải thích vì sao checkpoint đó mở đường cho bước kế tiếp.

Phần 2 chỉ bắt buộc khi có thuật ngữ mới hoặc dễ nhầm. Phần 3 chỉ bắt buộc khi
có quyết định thiết kế thực sự để giải thích. Không biến mỗi section thành một
bài giảng lý thuyết tách rời thao tác.

## Cổng chất lượng

Trước khi trả, kiểm tra từng section:

- Tôi có giải thích bản chất trước khi yêu cầu người học làm chưa?
- Thuật ngữ trung tâm có được tách nghĩa theo ngữ cảnh thay vì chỉ nêu định
  nghĩa từ điển chưa?
- Với hàm, file, cấu hình hoặc phương án chính, người học có hiểu trách nhiệm,
  input/output hoặc tác động, lợi ích, hạn chế và trade-off đã được nguồn xác
  nhận chưa?
- Sau từng lệnh hoặc cụm thao tác, người học có biết cần thấy gì và nó có ý
  nghĩa gì không?
- Độ dài có đến từ bằng chứng, lý do và checkpoint thực, thay vì lặp mục tiêu
  hoặc thêm câu dẫn rỗng không?

Nếu một câu trả lời là không, viết lại section đó trước khi tăng số section.
