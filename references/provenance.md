# Nguồn gốc tri thức
Ngày tổng hợp: 21/10/2026. Không đồng nghĩa mọi nguồn có hiệu lực đến ngày này.

| ID | Nguồn | Trạng thái / tin cậy | Phạm vi |
|---|---|---|---|
| U01 | Master prompt người dùng trong phiên tạo | Xác minh trực tiếp / cao | Yêu cầu chức năng, 5 nhóm hỏi, 10 ca thử, không bịa dữ liệu |
| H01 | Truy xuất lịch sử được phép trong phiên | Giới hạn truy xuất / trung bình | Không tìm được bản SKKN, feedback hay thành tích SKKN định danh được; không kết luận chúng không tồn tại |
| D01 | Thiết kế mới v1.0.0 | Đề xuất / cần thử thực địa | Workflow, bài học, thư viện lỗi, rubric, mẫu, feedback |
| L01–L05 | Nguồn chính thức liên kết trong legal-framework.md | Theo từng dòng | Chỉ các kết luận pháp lý đã đọc; hiệu lực phải kiểm tra lại |
| T01 | tests/results và test-report.md | Kết quả chạy nội bộ | Không phải đánh giá của hội đồng hay người dùng thật |

Không nhập nội dung hồ sơ nhân sự không liên quan từ lịch sử vào repo. Không có trường hợp thành công thực tế được xác minh ở v1.0.0. Thư viện feedback thực tế khởi tạo rỗng.

Mỗi bài học mới phải ghi: ID, phát biểu, nhãn verified/inferred/proposed, nguồn và đoạn liên quan, ngày truy cập, người kiểm chứng, độ tin cậy, giới hạn áp dụng, test hồi quy. Một nhận xét chưa đối chứng chỉ là candidate.

## Đối chiếu 22/10/2026 — v1.0.1
- R01 — Đã kiểm chứng trực tiếp: repository có v1.0.0, nhánh main ở commit 67560ede067a82d6824017c21dfa1929b1842248 trước cập nhật. Không diễn giải nội dung đã có là vừa tạo mới.
- H02 — Truy xuất được phép tiếp tục chưa cung cấp bản SKKN hoặc feedback thực địa có thể xác minh; các báo cáo trước của trợ lý không tự là bằng chứng thành công. Không đưa chi tiết lịch sử không liên quan lên repo.
- B01 — Lỗi tái hiện trong check_evidence: input None/list hoặc phase None gây AttributeError; attrition_note=true được chấp nhận. Đã sửa và có test hồi quy; đây là lỗi công cụ đã quan sát, không phải lỗi giáo viên/hội đồng.
- T02 — Đầu ra chạy mới và báo cáo tại tests/regression-20261022.md; không dùng lại kết quả cũ để tuyên bố đã chạy mới.
- B02 — Quan sát trực tiếp: bản đầu TC09 dùng trùng phương trình của đề đo trong ví dụ luyện/phản hồi; đã yêu cầu sửa, đối chiếu lại và ghi trong báo cáo. Dẫn đến bổ sung E13 và kiểm tra chéo học liệu–đề đo. Đây là bài học từ đầu ra AI nội bộ, không phải feedback giáo viên hoặc kết quả thực nghiệm.
