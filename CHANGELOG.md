# Nhật ký phiên bản
## 1.0.1 — 2026-10-22
- Sửa kiểm tra JSON sai cấu trúc; chặn ghi chú hao hụt sai kiểu, khóa trùng và số không hữu hạn.
- Bổ sung E13 từ lỗi trùng học liệu–đề đo phát hiện trong TC09, cùng yêu cầu đối chiếu trước phát hành.
- Tăng kiểm thử số học/CLI từ 8 lên 18; chạy lại 10 tình huống với đầu ra mới.
- Đối chiếu lại TT30/2026 và làm rõ việc NĐ259/2026 thay thế NĐ115/2020 từ nguồn Chính phủ.
- Giữ nguyên rubric và định dạng đầu vào hợp lệ; bảo toàn tài liệu/đầu ra v1.0.0.

## 1.0.0 — 2026-10-21
- Khởi tạo quy trình 12 bước, 8 bài học đề xuất, 12 loại lỗi, 6 mẫu phương pháp.
- Rubric nội bộ 100 điểm; chính sách minh chứng và feedback có quản trị.
- Mẫu SKKN, khảo sát, tác động; kiểm tra số học và cấu trúc; forward-test có lưu đầu ra.
- Nguồn pháp lý có trạng thái xác minh, lưu giới hạn truy cập.

Quy ước: PATCH sửa lỗi/nguồn không đổi hành vi; MINOR thêm mẫu hoặc năng lực tương thích; MAJOR đổi workflow/rubric hoặc định dạng dữ liệu. Mọi thay đổi phải ghi lý do, nguồn, test và ảnh hưởng. Không tự động phát hành từ feedback chưa kiểm chứng.
