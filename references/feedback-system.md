# Hệ thống học từ phản hồi
Thiết kế D01; sổ phản hồi thực tế chưa có bản ghi.

Nhận từ giáo viên, tổ chuyên môn, ban giám hiệu, hội đồng hoặc người dùng Skill. Lưu vai trò, không cần tên thật. Phân loại: nội dung chuyên môn / dữ liệu / pháp lý / tính mới / trình bày / vận hành / riêng tư.

Mỗi bản ghi có ID, ngày, vai trò, ngữ cảnh, phiên bản, trích đoạn được phép, vấn đề, bằng chứng, mức độ, nguyên nhân dự kiến, hành động, người phụ trách, test hồi quy, trạng thái, kết quả kiểm chứng, phiên bản sửa. Dùng templates/feedback-record.json.

Luồng: received → triaged → investigating → proposed → validated → released → closed. Có nhánh rejected/deferred kèm lý do; thất bại kiểm thử quay lại investigating. Lưu lịch sử chuyển trạng thái, không xóa phản hồi trái chiều.

Sửa cục bộ bản thảo nếu có căn cứ. Đổi quy tắc lõi cần người quản trị duyệt, nguồn đối chiếu hoặc tái hiện độc lập, kiểm thử hồi quy và đánh giá ảnh hưởng. Không có số lượng phản hồi tối thiểu thay thế kiểm chứng chất lượng. Phản hồi yêu cầu bịa số liệu bị từ chối, vẫn đề xuất cách đo thật.

Đóng vòng: trả lời điều đã sửa, điều chưa sửa và lý do, bằng chứng kiểm tra lại. Không tự gửi tin tới hội đồng hoặc người góp ý. Chỉ xuất bản bản ghi đã ẩn danh và được phép; sổ thật mặc định lưu riêng khỏi repo công khai.
