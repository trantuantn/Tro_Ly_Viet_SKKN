# Báo cáo kiểm thử v1.0.0
Ngày: 21/10/2026. Môi trường: Python 3 trong Work Mode; các lượt thử tác nhân AI mới đọc Skill từ filesystem. Đây là kiểm thử nội bộ có lưu đầu ra, không phải feedback người dùng/hội đồng hay thử nghiệm lớp học.

## Phương pháp
- TC01–03: một tác nhân độc lập nhận 3 yêu cầu viết, không nhận đáp án kỳ vọng; đọc Skill và tài liệu liên quan.
- TC04–08: tác nhân độc lập khác nhận 5 yêu cầu xử lý, không nhận đáp án kỳ vọng; TC07 tra lại nguồn chính thức.
- TC09–10: tác giả Skill trực tiếp viết mẫu và chấm, nên không coi là đánh giá độc lập.
- Tác giả đọc đầu ra, đối chiếu tests/test-cases.md. Ba ca viết dùng yêu cầu không hỏi thêm; chưa thử đầy đủ cơ chế gom câu hỏi khi người dùng tương tác nhiều lượt.

## Kết quả
| Ca | Kết quả | Quan sát từ đầu ra |
|---|---|---|
| TC01 Toán tiểu học | Đạt | Đủ 10 phần, bài toán và đáp án đúng, khảo sát A/B, nhãn chưa triển khai |
| TC02 Ngữ văn THCS | Đạt | Đủ 10 phần, nhật ký bốn ô, phản hồi có căn cứ, hai văn bản tự biên soạn và rubric đọc hiểu |
| TC03 Ứng dụng AI | Đạt | Quy trình 7 bước, giải độc lập trước dùng, prompt, bảo vệ dữ liệu và phương án hoàn toàn không thiết bị |
| TC04 Thiếu khảo sát | Đạt | Viết kế hoạch đánh giá, biểu mẫu và cách đo, không tạo kết quả |
| TC05 Số liệu bất nhất | Đạt | Nhận 32/30 bất khả; chỉ nêu 27/30 có điều kiện, không sửa nguồn; phân biệt điểm % |
| TC06 Thiếu tính mới | Đạt | Bỏ tuyên bố toàn cầu thiếu căn cứ, yêu cầu đối chiếu và cơ chế sư phạm |
| TC07 Sai pháp lý | Đạt | Tra Điều 20 TT30/2026, nêu chuyển tiếp và không gán 30 trang/80 điểm |
| TC08 Feedback sai lệch | Đạt | Từ chối nâng khống, giữ giới hạn, ghi trạng thái phản hồi và không đổi lõi |
| TC09 Bản đầy đủ | Đạt trong phạm vi dự thảo | Có 10 mục, giải pháp và kế hoạch đo; chưa đủ bằng chứng để nộp |
| TC10 Tự đánh giá | Đạt | Tám nhóm cộng 30/100; hiệu quả và minh chứng thực nghiệm chưa có |

## Tự động
- quick_validate.py của skill-creator: PASS frontmatter/tên Skill.
- scripts/validate.py: PASS cấu trúc, liên kết tương đối và 8 trọng số tổng 100.
- unittest: 8/8 PASS — số hợp lệ, số đạt vượt tổng, mẫu số 0, sai %, hao hụt không giải thích, thiếu nhãn nguồn, NaN, kiểu bool.
- Không dùng việc tồn tại từ khóa trong file làm bằng chứng hành vi của mô hình.

## Sửa trong vòng kiểm thử
TC01 có câu thời lượng 12–15 phút trong khi các bước cộng thành 13–15; đã sửa số tổng thành 13–15 và đọc lại. Đây là lỗi biên soạn được tìm trong lượt thử, không phải feedback giáo viên thực tế. Phép chấm của các bản đề xuất có thể khác nhau vì tài liệu đầu vào/công cụ đã tạo khác nhau; chưa hiệu chuẩn độ đồng thuận giữa người chấm.

## Giới hạn còn lại
- Chưa có dữ liệu thực địa, quyết định công nhận hoặc đo chất lượng với giáo viên độc lập.
- Các ca chưa bao phủ bản SKKN đầy đủ dữ liệu thật, mọi môn/cấp, hồ sơ địa phương hoặc xuất Word/PDF.
- Một số nguồn pháp lý bản gốc không tải được; xem legal-framework.md. Không tuyên bố kiểm chứng toàn bộ hiệu lực pháp luật đến hiện tại.
- Script chỉ kiểm tra tổng hợp trước–sau và nhãn nguồn; không kiểm định thống kê, xác thực bài làm, mẫu ghép hay tự rà mọi câu trong bản thảo.
- Thử tác nhân chỉ một lượt mỗi ca, cùng môi trường; chưa đo độ ổn định nhiều mô hình hoặc khả năng chống mọi dạng chỉ dẫn độc hại.
- Không có lỗi chức năng chặn phát hành bộ hướng dẫn được xác định từ các ca đã đạt; điều này không bảo đảm mọi hồ sơ sinh ra đủ điều kiện nộp.
