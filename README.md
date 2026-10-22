# SKKN-Master-Pro v1.0.1
**Siêu Trợ Lý Viết Sáng Kiến Kinh Nghiệm** cho giáo viên Việt Nam: viết, phản biện, kiểm định số liệu, minh chứng và cải tiến bản thảo. Phạm vi: tiểu học, THCS, THPT; mở rộng theo môn và địa phương bằng hồ sơ thích nghi.

## Bắt đầu
Trên nền tảng hỗ trợ Agent Skills, đặt toàn bộ nội dung repo trong thư mục `skkn-master-pro` thuộc thư mục skills của nền tảng. Điểm vào là [SKILL.md](SKILL.md), YAML có `name` và `description`; metadata giao diện ở `agents/openai.yaml`. Repo không phải website hoặc chương trình tự sinh hồ sơ; cần tác nhân AI đọc và thực hiện hướng dẫn.

Ví dụ kích hoạt:
> Dùng $skkn-master-pro viết SKKN Toán lớp 3 về sơ đồ đoạn thẳng. Mục đích cải tiến dạy học; dự kiến 8 tuần, một lớp; chưa có dữ liệu khảo sát; văn phong sư phạm. Hãy viết đầy đủ phần có thể làm và đánh dấu phần cần xác minh.

> Dùng $skkn-master-pro phản biện bản SKKN đính kèm, kiểm tra số liệu trước–sau và chấm rubric nội bộ 100 điểm.

Skill chỉ hỏi một lượt những thông tin còn thiếu thuộc 5 nhóm. Có thể làm tiếp với giả định công khai. Thiếu minh chứng thì bản giao là dự thảo, không tuyên bố sẵn sàng nộp.

## Tri thức và giới hạn
12 bước workflow; 8 bài học đề xuất; 12 loại lỗi dự phòng và 1 lỗi đầu ra thử đã quan sát; vòng feedback có quản trị; 6 mẫu phương pháp; 8 tiêu chí tổng 100 điểm. Không có bản SKKN hoặc feedback/thành công thực địa được xác minh trong nguồn truy xuất của phiên tạo. Không dùng dữ liệu giả định làm kết quả thật. Nguồn gốc được ghi tại [provenance](references/provenance.md).

Pháp lý được tra cứu nhưng một số nguồn toàn văn bị lỗi truy cập: xem [legal-framework](references/legal-framework.md). Luôn rà hiệu lực, chuyển tiếp, địa phương và thời điểm hồ sơ; không đóng cứng văn bản cũ. Rubric không phải tiêu chí chính thức.

## Kiểm tra
```bash
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/check_evidence.py du-lieu.json
```
Python 3, chỉ thư viện chuẩn cho các script trong repo. JSON đầu vào ví dụ **minh họa**:
```json
{"before":{"n":30,"passed":12,"percent":40},"after":{"n":30,"passed":18,"percent":60},"source_status":"illustrative"}
```
Khi thay đổi mẫu số, thêm `attrition_note` là chuỗi có nội dung; boolean/số/chuỗi trắng không được chấp nhận. JSON phải là object với `before` và `after` là object; khóa trùng hoặc hằng NaN/Infinity bị từ chối. Exit code check_evidence: 0 không phát hiện lỗi số học, 1 có lỗi, 2 đầu vào không đọc được. Số học hợp lệ không chứng thực nguồn hoặc tác động.

Kết quả gốc v1.0.0 xem [test-report](tests/test-report.md); lượt chạy mới 22/10/2026 xem [báo cáo hồi quy](tests/regression-20261022.md) và [nhật ký tự động](tests/automated-20261022.txt). Không có kiểm thử hội đồng, triển khai lớp học hoặc xuất Word/PDF trong phiên bản này.

## Bảo trì
Góp ý theo [feedback-system](references/feedback-system.md), dùng phiếu JSON nhưng lưu bản thực tế ở nơi riêng được phép. Trước công khai phải ẩn danh. Không tự thay quy tắc cốt lõi từ phản hồi đơn lẻ. Sửa → ghi nguồn/lý do → chạy test → người quản trị duyệt → cập nhật CHANGELOG và phiên bản → commit. Không đồng bộ dữ liệu học sinh lên GitHub.

Phiên bản tiếp theo: nguồn pháp lý gốc đầy đủ, hồ sơ địa phương đã xác minh, ví dụ đa môn có dữ liệu được phép, đánh giá giáo viên độc lập, xuất Word đúng mẫu và bộ thử hồi quy tự động cho hành vi LLM. Giấy phép hiện giữ quyền; chủ repo có thể chọn giấy phép nguồn mở sau.

## Danh mục tệp

| Tệp | Chức năng |
|---|---|
| [.gitignore](.gitignore) | Loại cache Python khỏi Git |
| [CHANGELOG.md](CHANGELOG.md) | Phiên bản và thay đổi |
| [LICENSE](LICENSE) | Trạng thái quyền sử dụng |
| [README.md](README.md) | Sử dụng và danh mục |
| [SKILL.md](SKILL.md) | Điểm vào và quy tắc vận hành |
| [agents/openai.yaml](agents/openai.yaml) | Metadata giao diện Agent Skills |
| [examples/sample-skkn.md](examples/sample-skkn.md) | Bản minh họa đầy đủ cấu trúc |
| [references/error-knowledge-base.md](references/error-knowledge-base.md) | 13 loại lỗi và ví dụ sửa |
| [references/evidence-policy.md](references/evidence-policy.md) | Nguồn, số liệu, ẩn danh và diễn giải tác động |
| [references/feedback-system.md](references/feedback-system.md) | Tiếp nhận, xác minh và đóng vòng phản hồi |
| [references/legal-framework.md](references/legal-framework.md) | Nguồn pháp lý, hiệu lực và giới hạn truy cập |
| [references/lessons-learned.md](references/lessons-learned.md) | 8 bài học đề xuất |
| [references/provenance.md](references/provenance.md) | Nguồn gốc và độ tin cậy tri thức |
| [references/quality-rubric.md](references/quality-rubric.md) | 8 tiêu chí,100 điểm và lỗi chặn |
| [references/success-patterns.md](references/success-patterns.md) | 6 mẫu phương pháp, chưa gán thành tích |
| [references/workflow.md](references/workflow.md) | 12 bước đầu vào–đầu ra–kiểm tra–xử lý lỗi |
| [scripts/check_evidence.py](scripts/check_evidence.py) | Kiểm tra dữ liệu JSON |
| [scripts/validate.py](scripts/validate.py) | Kiểm tra cấu trúc, link và rubric |
| [templates/ai-innovation-skkn.md](templates/ai-innovation-skkn.md) | Khung có kiểm soát AI |
| [templates/feedback-record.json](templates/feedback-record.json) | Phiếu phản hồi rỗng |
| [templates/impact-report.md](templates/impact-report.md) | Báo cáo trước–sau và giới hạn |
| [templates/local-profile.md](templates/local-profile.md) | Thích nghi môn/cấp/địa phương |
| [templates/promotion-skkn.md](templates/promotion-skkn.md) | Khung kèm đối chiếu hồ sơ thăng hạng |
| [templates/standard-skkn.md](templates/standard-skkn.md) | Khung SKKN chung |
| [templates/survey-template.md](templates/survey-template.md) | Công cụ khảo sát và hướng dẫn chấm |
| [tests/acceptance-criteria.md](tests/acceptance-criteria.md) | Tiêu chuẩn nghiệm thu |
| [tests/results/case01.md](tests/results/case01.md) | Đầu ra thực chạy của tình huống kiểm thử |
| [tests/results/case02.md](tests/results/case02.md) | Đầu ra thực chạy của tình huống kiểm thử |
| [tests/results/case03.md](tests/results/case03.md) | Đầu ra thực chạy của tình huống kiểm thử |
| [tests/results/case04.md](tests/results/case04.md) | Đầu ra thực chạy của tình huống kiểm thử |
| [tests/results/case05.md](tests/results/case05.md) | Đầu ra thực chạy của tình huống kiểm thử |
| [tests/results/case06.md](tests/results/case06.md) | Đầu ra thực chạy của tình huống kiểm thử |
| [tests/results/case07.md](tests/results/case07.md) | Đầu ra thực chạy của tình huống kiểm thử |
| [tests/results/case08.md](tests/results/case08.md) | Đầu ra thực chạy của tình huống kiểm thử |
| [tests/results/case09.md](tests/results/case09.md) | Đầu ra thực chạy của tình huống kiểm thử |
| [tests/results/case10.md](tests/results/case10.md) | Đầu ra thực chạy của tình huống kiểm thử |
| [tests/test-cases.md](tests/test-cases.md) | 10 đầu vào và tiêu chí |
| [tests/test-report.md](tests/test-report.md) | Kết quả chạy thực tế |
| [tests/test_evidence.py](tests/test_evidence.py) | 18 kiểm thử số học và CLI |

## Tệp bổ sung ở v1.0.1

| Tệp | Chức năng |
|---|---|
| [tests/prompts-20261022.md](tests/prompts-20261022.md) | Đầu vào thực giao và thiết kế lượt thử |
| [tests/regression-20261022.md](tests/regression-20261022.md) | Đánh giá đầu ra, sửa lỗi và giới hạn lượt thử mới |
| [tests/automated-20261022.txt](tests/automated-20261022.txt) | Log lệnh kiểm tra thực chạy |
| [tests/regression-20261022/case01.md](tests/regression-20261022/case01.md) | Đầu ra mới TC01, tình huống kiểm thử tổng hợp |
| [tests/regression-20261022/case02.md](tests/regression-20261022/case02.md) | Đầu ra mới TC02, tình huống kiểm thử tổng hợp |
| [tests/regression-20261022/case03.md](tests/regression-20261022/case03.md) | Đầu ra mới TC03, tình huống kiểm thử tổng hợp |
| [tests/regression-20261022/case04.md](tests/regression-20261022/case04.md) | Đầu ra mới TC04, tình huống kiểm thử tổng hợp |
| [tests/regression-20261022/case05.md](tests/regression-20261022/case05.md) | Đầu ra mới TC05, tình huống kiểm thử tổng hợp |
| [tests/regression-20261022/case06.md](tests/regression-20261022/case06.md) | Đầu ra mới TC06, tình huống kiểm thử tổng hợp |
| [tests/regression-20261022/case07.md](tests/regression-20261022/case07.md) | Đầu ra mới TC07, tình huống kiểm thử tổng hợp |
| [tests/regression-20261022/case08.md](tests/regression-20261022/case08.md) | Đầu ra mới TC08, tình huống kiểm thử tổng hợp |
| [tests/regression-20261022/case09.md](tests/regression-20261022/case09.md) | Đầu ra mới TC09, tình huống kiểm thử tổng hợp |
| [tests/regression-20261022/case10.md](tests/regression-20261022/case10.md) | Đầu ra mới TC10, tình huống kiểm thử tổng hợp |
