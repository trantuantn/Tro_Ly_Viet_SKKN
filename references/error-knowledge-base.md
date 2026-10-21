# Thư viện lỗi

Danh mục dự phòng **D01 đề xuất**, chưa thống kê tần suất thực tế. BLOCKER chặn trạng thái sẵn sàng nộp; MAJOR cần sửa trước chốt. Ví dụ đều hư cấu.

## E01 — Số liệu giả làm thật
- Nguyên nhân: Áp lực thành tích.
- Mức độ: BLOCKER.
- Dấu hiệu: Có tỷ lệ nhưng không có bảng nguồn.
- Khắc phục: Chuyển thành kế hoạch và bỏ kết luận thực nghiệm.
- Phòng ngừa: Bắt buộc nhãn nguồn.
- Trước: “Đã tăng 30%”.
- Sau: “Chưa có dữ liệu; sẽ đo cùng tiêu chí”.

## E02 — Sai mẫu số
- Nguyên nhân: Trộn số tham gia và số có bài.
- Mức độ: BLOCKER.
- Dấu hiệu: 32/30 hoặc tổng vượt sĩ số.
- Khắc phục: Đối chiếu nguồn, không tự sửa số gốc.
- Phòng ngừa: Lưu n ở từng thời điểm.
- Trước: “32 em đạt trong 30 em”.
- Sau: “Dữ liệu bất nhất; cần đối chiếu danh sách”.

## E03 — So sánh khác mẫu
- Nguyên nhân: Học sinh vắng hoặc chuyển lớp.
- Mức độ: MAJOR.
- Dấu hiệu: Trước 30, sau 28 không giải thích.
- Khắc phục: Phân tích mẫu ghép và hao hụt.
- Phòng ngừa: Mã ẩn danh ổn định.
- Trước: “Lớp tăng 20%”.
- Sau: “Chưa so sánh trực tiếp do khác mẫu”.

## E04 — Nhầm phần trăm
- Nguyên nhân: Không phân biệt đơn vị.
- Mức độ: MAJOR.
- Dấu hiệu: 40% lên 60% gọi tăng 20% tương đối.
- Khắc phục: Ghi tăng 20 điểm phần trăm, tương đối 50%.
- Phòng ngừa: Gắn đơn vị mọi chênh lệch.
- Trước: “Tăng 20%”.
- Sau: “Tăng 20 điểm phần trăm”.

## E05 — Thiếu tính mới
- Nguyên nhân: Chỉ đổi tên công cụ.
- Mức độ: MAJOR.
- Dấu hiệu: Giải pháp giống cách cũ.
- Khắc phục: Lập bảng cũ/mới và cơ chế.
- Phòng ngừa: Khảo sát thực hành sẵn có.
- Trước: “Dùng AI là sáng tạo”.
- Sau: “Điểm thay đổi đề xuất là chu trình phản hồi có kiểm chứng”.

## E06 — Giải pháp chung chung
- Nguyên nhân: Không mô tả thao tác.
- Mức độ: MAJOR.
- Dấu hiệu: Chỉ có “tăng cường”, “đẩy mạnh”.
- Khắc phục: Thêm bước, thời lượng, sản phẩm, chỉ báo.
- Phòng ngừa: Dùng mẫu 7 thành phần.
- Trước: “Tăng cường đọc hiểu”.
- Sau: “Cho học sinh đánh dấu luận điểm và đối chiếu bằng chứng trong 8 phút”.

## E07 — Sai viện dẫn pháp luật
- Nguyên nhân: Dùng trí nhớ hoặc văn bản cũ.
- Mức độ: BLOCKER.
- Dấu hiệu: Sai tên, điều hoặc hiệu lực.
- Khắc phục: Tra nguồn chính thức, gỡ khẳng định chưa xác minh.
- Phòng ngừa: Sổ pháp lý có ngày và chuyển tiếp.
- Trước: “TT20 quy định SKKN 30 trang”.
- Sau: “Không có căn cứ đã xác minh cho yêu cầu 30 trang”.

## E08 — Nhân quả quá mức
- Nguyên nhân: Không kiểm soát biến nhiễu.
- Mức độ: MAJOR.
- Dấu hiệu: Do giải pháp nên tất cả tăng.
- Khắc phục: Hạ mức kết luận, nêu giới hạn.
- Phòng ngừa: Thiết kế đo trước triển khai.
- Trước: “Giải pháp quyết định kết quả”.
- Sau: “Thay đổi quan sát được; chưa loại trừ tác động khác”.

## E09 — Lộ thông tin trẻ em
- Nguyên nhân: Đính kèm danh sách gốc.
- Mức độ: BLOCKER.
- Dấu hiệu: Tên, ảnh, thông tin nhận diện.
- Khắc phục: Ẩn danh, hạn chế chia sẻ.
- Phòng ngừa: Rà quyền dùng trước xuất.
- Trước: “Danh sách đầy đủ học sinh”.
- Sau: “Bảng mã HS01, HS02; khóa mã lưu riêng”.

## E10 — Nguồn không tồn tại
- Nguyên nhân: Trích dẫn AI chưa kiểm chứng.
- Mức độ: BLOCKER.
- Dấu hiệu: Không tìm được tài liệu hoặc đoạn hỗ trợ.
- Khắc phục: Bỏ hoặc thay nguồn đã đọc.
- Phòng ngừa: Sổ nguồn và kiểm tra URL.
- Trước: “Theo nghiên cứu X không tìm được”.
- Sau: “Chưa có nguồn; đây là giả thuyết”.

## E11 — Thiếu phụ lục
- Nguyên nhân: Viết báo cáo trước thiết kế đo.
- Mức độ: MAJOR.
- Dấu hiệu: Kết quả không nối được công cụ.
- Khắc phục: Bổ sung công cụ và mã minh chứng.
- Phòng ngừa: Ma trận kết luận–minh chứng.
- Trước: “Kết quả ở phụ lục không tồn tại”.
- Sau: “Chưa có phụ lục; không xác nhận kết quả”.

## E12 — Feedback thành luật
- Nguyên nhân: Một nhận xét bị khái quát.
- Mức độ: MAJOR.
- Dấu hiệu: Đổi lõi từ ý kiến đơn lẻ.
- Khắc phục: Ghi candidate và kiểm tra bối cảnh.
- Phòng ngừa: Duyệt thay đổi lõi.
- Trước: “Mọi SKKN phải 50 trang”.
- Sau: “Yêu cầu riêng cần xác minh với nơi nhận”.
