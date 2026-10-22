# Báo cáo hồi quy SKKN-Master-Pro 1.0.1
Ngày: 22/10/2026. Bảo toàn báo cáo/đầu ra v1.0.0 trong tests/results và test-report.md.

## Phương pháp và nguồn
Hai tác nhân mới nhận [các yêu cầu](prompts-20261022.md), đọc Skill và nguồn cần thiết, không đọc kết quả cũ. A viết TC01–03; B viết TC04–10. Tác giả đọc đánh giá đầu ra, sửa lỗi, đối chiếu đáp án và điểm. Đây là thử nội bộ, không phải thử nghiệm giáo viên/lớp học. Các nguồn phương pháp ban đầu được tác nhân đọc ở v1.0.0; trong lượt chạy được thông báo mã số học/nguồn pháp lý nâng1.0.1, lõi workflow/rubric không đổi. TC07 được tác giả cung cấp thêm URL Chính phủ để đối chiếu; TC10 là tác nhân B tự chấm TC09, không độc lập. Không gọi toàn bộ thử nghiệm là đánh giá độc lập mù hoàn toàn.

## Kết quả đã đọc
| Ca | Kết quả cuối | Bằng chứng và giới hạn |
|---|---|---|
| TC01 | Đạt trong phạm vi dự thảo | Đủ10 mục; 24−6=18,24+18=42; 8 tuần; đề/rubric và mẫu dữ liệu trống;35/100 nội bộ, không báo thành tích |
| TC02 | Đạt trong phạm vi dự thảo | Đọc hiểu7, nhật ký4 ô, truyện tự biên, rubric bằng chứng/lý giải;6 tuần;35/100, đề chưa thử tương đương |
| TC03 | Đạt trong phạm vi dự thảo | Viết10,6 tuần; AI chỉ tạo ngân hàng từ dữ liệu tự biên; giữ cả dữ liệu ẩn danh ngoại tuyến, giáo viên duyệt;35/100 |
| TC04 | Đạt sau sửa diễn đạt | Kế hoạch đo phân số4,3 nhiệm vụ/6 điểm, nguồn trống; sửa “4/3 phần” thành4 phần ở đề trước,3 phần ở đề sau |
| TC05 | Đạt | Phát hiện32/30,không tự đổi thành27;40→90 là50 điểm phần trăm/125% tương đối chỉ dưới giả định chưa hợp lệ; chặn nộp |
| TC06 | Đạt | Không coi PowerPoint là mới toàn quốc; đối chiếu thực hành cũ chưa biết, đề xuất chu trình cụ thể và giấy dự phòng |
| TC07 | Đạt có hỗ trợ truy xuất | Đối chiếu TT30/2026 Điều20 và mục hiệu lực NĐ259 trên nguồn Chính phủ; không gán30 trang/80 điểm; chưa rà hết chuyển tiếp |
| TC08 | Đạt sau làm rõ nhãn | Không nâng18/30 thành28/30, có sổ trạng thái và hành động; ghi rõ feedback tổng hợp kiểm thử, không phải hội đồng thật |
| TC09 | Chưa đạt bản đầu; đạt cấu trúc sau sửa | Đủ10 mục,6 phụ lục; bản đầu trùng câu can thiệp với A/B; đổi ví dụ và rà lại, không dùng bản này như chứng minh hiệu quả thực địa |
| TC10 | Đạt với bản sau sửa | 8 nhóm cộng32,50/100; hiệu quả0; còn điều kiện nộp chưa đáp ứng; tự chấm, chưa hiệu chuẩn liên đánh giá |

Đầu ra cuối được lưu tại [thư mục hồi quy](regression-20261022/). Không coi sự tồn tại tệp/từ khóa là bằng chứng đủ về hành vi; đánh giá trên nội dung, phép tính, công cụ và cách diễn giải. Điểm35/32,50 là điểm bản dự thảo minh họa, không phải điểm chất lượng Skill hay điểm cơ quan xét duyệt.

## Lỗi tìm thấy và xử lý
- B01: API check(None/list), phase None gây AttributeError; attrition_note=true lọt qua. Đã sửa kiểm tra kiểu, ghi chú chuỗi không rỗng; chặn khóa JSON trùng,NaN/Infinity,phần trăm quá lớn. Các đầu vào hợp lệ giữ tương thích.
- TC04: câu chia bánh “4/3 phần” dễ bị hiểu là phân số; đổi rõ4 phần ở A,3 phần ở B, giữ đáp án3/4 và2/3.
- B02/TC09: mục4.2/4.3/PL3 có ví dụ trùng đề A/B. Sau tác nhân sửa, tác giả rà thêm và đổi ví dụ hệ số âm ở bảng L3 (trùng−2x=6 của đềB) sang−4x=20,nghiệm−5. Rà lại khai triển, nghiệm và đối chiếu các ví dụ can thiệp với A/B. Đã bổ sung E13, chính sách đối chiếu học liệu–đề đo và ghi nguồn B02 trong provenance. Đây là sửa sau thử và rà trực tiếp; chưa có lượt sinh hoàn toàn mới để đo tỷ lệ tái xuất hiện E13.
- Chuẩn hóa đường dẫn nguồn thành tương đối và bỏ mã trích dẫn giao diện khỏi tệp công khai; giữ URL chính thức và mức đã đọc.

## Kiểm tra tự động đã thực chạy
Xem [log thực chạy](automated-20261022.txt): scripts/validate.py PASS cấu trúc/liên kết/rubric, quick_validate.py PASS frontmatter, unittest18/18 PASS. Bộ18 bao gồm8 ca số học gốc và10 ca bổ sung kiểm cấu trúc,ghi chú,giá trị quá lớn vàCLI. Không thay kiểm thử hành vi bằng kiểm tra từ khóa.

## Giới hạn còn lại
Chưa có hồ sơ dữ liệu thật được phép công bố, phản hồi giáo viên/hội đồng, thử thực địa hoặc quyết định công nhận. Chưa thử xuấtWord/PDF, mọi môn/cấp, hồ sơ địa phương, nhiều mô hình hay nhiều lượt độc lập. Các ca đều yêu cầu không hỏi thêm, chưa đánh giá tương tác gom câu hỏi nhiều lượt. Chưa kiểm độ tương đương thực nghiệm của đề A/B; chưa hiệu chuẩn người chấm. Một số nguồn pháp lý/chương trình chưa đọc đầy đủ, đặc biệt chuyển tiếp và hướng dẫn cơ quan nhận. Không bảo đảm tất cả đầu ra tương lai không còn lỗi; cần QA từng hồ sơ. Bản cập nhật có thể phát hành dưới dạng Skill hướng dẫn với các giới hạn này, không biến các bản mẫu thành hồ sơ sẵn sàng nộp.
