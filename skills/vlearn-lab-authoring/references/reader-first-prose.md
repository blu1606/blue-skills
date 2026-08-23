# Giọng văn dễ đọc, bám việc làm cho VLearn Lab

Dùng hướng dẫn này khi một Lab đúng kỹ thuật nhưng đang cụt, rời câu, hoặc
giống danh sách lệnh. Mục tiêu là giúp người học hiểu việc mình đang làm để
hoàn thành đúng Lab; không thêm câu chuyện, lý do kỹ thuật, hay yêu cầu không
có trong nguồn và brief đã xác nhận.

Đọc cùng `step-depth-contract.md` khi viết hoặc review một Lab mới. Hướng dẫn
này quyết định nhịp câu; contract quyết định độ sâu tối thiểu của từng section.

## Viết theo đường đi của người học

- Mở một phần bằng điểm vào cụ thể mà nguồn đã nêu: thao tác họ sắp làm, lỗi
  họ cần kiểm tra, hoặc kết quả họ cần tạo. Nếu nguồn không có một tình huống
  gần gũi, đi thẳng vào thao tác thay vì bịa ví dụ đời thường.
- Mỗi đoạn chỉ dẫn một câu hỏi hoặc một ý: việc này là gì, vì sao làm lúc này,
  hoặc cần quan sát điều gì. Đừng dồn khái niệm, lệnh, cảnh báo và kết luận vào
  cùng một đoạn.
- Viết thành những đoạn ngắn nhưng trọn ý. Xen kẽ đoạn giải thích với danh sách
  hành động khi thứ tự quan trọng; đừng biến mọi dòng thành một mệnh lệnh hoặc
  nhãn rời rạc.
- Giải thích thuật ngữ ở lần đầu người học phải dựa vào nó để quyết định. Nêu
  nghĩa ngắn trong ngữ cảnh Lab, rồi quay lại thao tác; không mở một bài giảng
  lý thuyết nếu nguồn không yêu cầu.
- Nối các bước bằng quan hệ thật: kết quả vừa quan sát được cho biết gì và vì
  sao nó cho phép làm bước kế tiếp. Tránh thêm câu chuyển ý chỉ để nghe mượt.

## Nhịp cho một bước Lab

Ưu tiên vòng lặp sau, miễn là nguồn hoặc brief có đủ dữ kiện:

1. **Giải thích:** đặt người học vào giai đoạn hiện tại và nêu vai trò của
   thao tác đối với kết quả Lab.
2. **Hành động:** gọi đúng tệp, vị trí giao diện, lệnh hoặc lựa chọn mà nguồn
   cung cấp; mỗi câu chỉ có một động từ chính.
3. **Quan sát:** nói họ cần nhìn thấy, kiểm tra, hoặc quyết định gì tiếp theo.
   Chỉ nêu output, trạng thái, hay lý do khi chúng được xác nhận.

Không phải bước nào cũng cần đủ ba câu. Một thao tác hiển nhiên có thể ngắn;
một bước có rủi ro hoặc khái niệm mới cần phần giải thích và dấu hiệu hoàn
thành rõ hơn.

## Mẫu sửa câu máy móc

Đây là mẫu minh hoạ cấu trúc, không phải dữ kiện để chép vào Lab.

**Trước**

> Chạy lệnh. Sửa tệp. Kiểm tra kết quả.

**Sau**

> Ở bước này, bạn dùng `<lệnh được nguồn cung cấp>` để kiểm tra trạng thái
> hiện tại trước khi thay đổi. Mở `<tệp hoặc vị trí được nguồn nêu>`, thực hiện
> đúng sửa đổi đã yêu cầu, rồi chạy lại lệnh. Khi thấy `<dấu hiệu hoàn thành đã
> xác nhận>`, bạn biết thay đổi đã đạt điều kiện để chuyển sang bước tiếp theo.

Khi áp dụng, thay toàn bộ phần trong ngoặc nhọn bằng tên và dấu hiệu có thật
từ nguồn. Nếu nguồn chỉ có lệnh mà không nói ý nghĩa hoặc kết quả mong đợi,
hãy giải thích phần quan sát được hoặc hỏi chủ sở hữu; đừng tự điền khoảng
trống.

## Cổng đọc lại

Trước khi trả Lab, kiểm tra nhanh:

1. Người học có biết bắt đầu ở đâu và mục tiêu gần nhất của phần này không?
2. Mỗi đoạn có đang phục vụ một hành động, quan sát, hoặc quyết định cụ thể
   không?
3. Thuật ngữ mới đã được làm rõ đúng lúc, bằng ngôn ngữ phù hợp với người học
   chưa?
4. Sau mỗi nhóm hành động, người học có biết cần thấy gì và nó có nghĩa gì
   không?
5. Các đoạn có nối bằng kết quả thực tế của bước trước, thay vì khẩu hiệu hay
   tóm tắt lặp lại, không?
6. Mọi tên riêng, lệnh, đường dẫn, đầu ra, quy tắc nộp bài và lý do kỹ thuật có
   bám nguồn hoặc brief đã xác nhận không?

Nếu một câu trả lời là không, sửa ít nhất có thể. Với dữ kiện chưa có, hỏi một
câu tập trung hoặc dùng `TODO — cần xác nhận` khi chủ sở hữu đã cho phép.
