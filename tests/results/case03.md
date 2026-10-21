# AI hỗ trợ giáo viên thiết kế câu hỏi phân hóa môn Toán lớp 5 thông qua quy trình duyệt và phản hồi

**DỰ THẢO — CHƯA TRIỂN KHAI, CHƯA CÓ KẾT QUẢ THỰC NGHIỆM — CHƯA SẴN SÀNG NỘP.** Khung đề xuất, chưa đối chiếu mẫu cơ quan nhận. Phạm vi: một lớp 5; thời gian dự kiến 6 tuần. Tác giả, đơn vị, năm học, sĩ số, lịch, sách đang dùng: [CẦN XÁC MINH]. Công cụ AI/phiên bản/ngày dùng: chưa chọn và chưa sử dụng trong triển khai. Các câu hỏi dưới đây là học liệu đề xuất trong bản thảo, không phải hồ sơ đầu ra AI đã thử tại lớp.

## 1. Đặt vấn đề

Việc thiết kế câu hỏi phân hóa đòi hỏi giáo viên giữ cùng mục tiêu học tập nhưng điều chỉnh mức hỗ trợ, số bước suy luận và yêu cầu giải thích. AI có thể được thử nghiệm như công cụ tạo bản nháp, song đáp án đúng và sự phù hợp lứa tuổi không được bảo đảm chỉ bằng yêu cầu trong prompt. Sáng kiến vì vậy tập trung vào chu trình giáo viên lập ma trận, yêu cầu bản nháp, kiểm tra độc lập, sử dụng và điều chỉnh theo bài làm.

Mục tiêu dự kiến là tạo được bộ câu hỏi được giáo viên kiểm chứng, hỗ trợ học sinh tiếp cận cùng mục tiêu theo nhu cầu và khảo sát chi phí thời gian soạn. Không đặt số prompt hoặc số câu sinh ra làm chỉ báo hiệu quả. Chưa khảo sát nên không khẳng định lớp có chênh lệch năng lực ở mức nào hoặc giáo viên đang quá tải bao nhiêu.

## 2. Cơ sở lý luận và căn cứ

Phân hóa trong đề xuất là điều chỉnh mức hỗ trợ và độ sâu nhiệm vụ, không cố định học sinh vào nhóm năng lực. Một học sinh có thể cần hỗ trợ ở nội dung này và làm nhiệm vụ mở rộng ở nội dung khác. AI chỉ hỗ trợ khâu chuẩn bị của giáo viên; học sinh tự đọc, tính, giải thích và kiểm tra, không phải có tài khoản AI.

Giả thuyết thiết kế là ma trận rõ cùng bước kiểm chứng có thể làm bản nháp thuận tiện hơn cho giáo viên, còn phản hồi từ bài làm giúp điều chỉnh mức hỗ trợ. Đây chưa phải kết luận hiệu quả. Không viện dẫn pháp luật hoặc nghiên cứu ngoài chưa đọc. Nội dung Toán cụ thể phải đối chiếu yêu cầu cần đạt và kế hoạch lớp trước thử nghiệm; các nhiệm vụ số thập phân bên dưới chỉ dùng khi học sinh đã học kiến thức liên quan.

## 3. Thực trạng và khảo sát dự kiến

Chưa có dữ liệu học sinh, bộ câu hỏi hiện hành, thời gian soạn hoặc tỉ lệ lỗi AI. Tuần 1 giáo viên dự kiến thu bài khảo sát A, kiểm kê học liệu có sẵn và ghi thời gian thiết kế thủ công một bộ câu hỏi theo cùng ma trận. Không gọi bộ thủ công kém hơn bộ có AI khi chưa đánh giá.

Giáo viên lập mã HS, ghi bài hợp lệ và lý do thiếu; khóa mã lưu tại cơ sở. Dữ liệu đưa vào prompt chỉ là mục tiêu, nội dung học liệu được phép dùng và khó khăn mô tả chung; không tải tên, ảnh, điểm cá nhân, hồ sơ sức khỏe, danh sách hoặc tài liệu nội bộ chưa có quyền dùng.

## 4. Giải pháp và quy trình cụ thể

### 4.1. Ma trận câu hỏi và điểm thay đổi đề xuất

Mỗi bộ gồm nhiệm vụ nền tảng chung và lựa chọn hỗ trợ/mở rộng. Mục tiêu chung của ví dụ là vận dụng phép tính số thập phân trong tình huống độ dài; không dùng câu khó hơn chỉ bằng cách tăng số lớn hoặc thêm từ ngữ rối.

| Mức nhiệm vụ | Yêu cầu | Hỗ trợ | Sản phẩm |
|---|---|---|---|
| Có hỗ trợ | Thực hiện hai phép tính theo kế hoạch gợi ý | Câu hỏi trung gian, chỗ ghi đơn vị | Lời giải và kiểm tra |
| Độc lập | Tự lập kế hoạch hai bước | Không cho sẵn phép tính | Lời giải, lý do thứ tự |
| Mở rộng | So sánh hai cách, tạo dữ kiện có ràng buộc | Câu hỏi giải thích | Lập luận và kiểm chứng |

Khác biệt dự kiến là lưu được mối liên hệ mục tiêu–bản nháp–lỗi–bản sửa–bài làm, thay vì chỉ nhận một danh sách câu hỏi. Đây là điểm thay đổi quy trình cần đối chiếu thực hành tại trường; việc sử dụng AI tự nó không chứng minh tính mới.

### 4.2. Quy trình bảy bước của giáo viên

1. **Chốt mục tiêu và giới hạn (dự kiến 5 phút/bộ):** đối chiếu nội dung học, ghi kiến thức được dùng, nhiệm vụ chung, mức hỗ trợ và tiêu chí đáp án. Không gửi AI yêu cầu “soạn câu phân hóa” thiếu bối cảnh.
2. **Yêu cầu bản nháp (3–5 phút):** dùng prompt ở phụ lục, chỉ đưa học liệu được phép chia sẻ. Ghi công cụ, phiên bản hiển thị, ngày dùng; nếu công cụ không cung cấp phiên bản thì ghi không hiển thị, không đoán.
3. **Giải và kiểm tra độc lập (10–15 phút):** giáo viên tự giải mọi câu không nhìn đáp án AI trước; kiểm tra phép tính, đơn vị, tính đủ của dữ kiện, số bước và độ rõ. Đối chiếu nguồn gốc học liệu nếu có dẫn nguồn. Không coi AI tự nhận “đã kiểm tra” là kiểm chứng.
4. **Duyệt sư phạm (5 phút):** đối chiếu ma trận và độ phù hợp lớp 5; loại câu cần kiến thức chưa học, câu có nhiều cách hiểu ngoài chủ đích hoặc chứa giả định đời sống không phù hợp. Với câu chưa thống nhất đáp án, nhờ đồng nghiệp rà nếu có thể; chưa giải quyết thì không sử dụng.
5. **Tổ chức học (10–15 phút trong hoạt động phù hợp):** mọi em làm nhiệm vụ nền tảng trước; giáo viên dùng bài làm để mời chọn hỗ trợ hoặc mở rộng. Học sinh có thể đổi nhiệm vụ sau trao đổi; không công khai bảng xếp hạng nhóm.
6. **Thu phản hồi (3–5 phút):** học sinh nêu phép tính khó hoặc câu chưa rõ; giáo viên kiểm tra lỗi do kiến thức, cách diễn đạt hay đáp án. Nếu phát hiện câu sai khi đang dạy, dừng câu đó, thông báo sửa và không dùng để đánh giá bất lợi cho học sinh.
7. **Lưu phiên bản và điều chỉnh (5 phút):** giữ prompt, bản nháp, đáp án tự giải, lỗi phát hiện, bản được duyệt, phản hồi ẩn danh và bản sau sửa. Chỉ đưa bản đã duyệt vào ngân hàng dùng lại.

Các thời lượng là dự toán cần đo, chưa phải bằng chứng tiết kiệm. Giáo viên chịu trách nhiệm duyệt cuối; không để AI tự chấm và quyết định nhóm học sinh. Nếu khâu duyệt mất quá nhiều thời gian, giảm số câu, tái sử dụng câu đã kiểm chứng hoặc quay lại cách thiết kế thủ công.

### 4.3. Học liệu minh họa và đáp án

**Câu chung độc lập:** “Một sợi dây dài 8,5 m. Người ta cắt đi 2,75 m rồi cắt tiếp 1,5 m. Hỏi còn lại bao nhiêu mét dây?” Hai cách đúng: 8,5 − 2,75 = 5,75; 5,75 − 1,5 = 4,25 m; hoặc 2,75 + 1,5 = 4,25; 8,5 − 4,25 = 4,25 m. Kiểm tra tổng phần cắt và phần còn lại bằng 8,5 m.

**Biến thể hỗ trợ:** cùng dữ kiện, thêm hai câu “Sau lần cắt thứ nhất còn bao nhiêu?” và “Sau lần thứ hai còn bao nhiêu?”. Giáo viên có thể cung cấp bảng ba dòng “ban đầu/cắt/còn”, không viết hộ phép tính nếu đang đo khả năng lựa chọn phép tính. Khi kiểm tra cuối kỳ, bỏ hỗ trợ và ghi điều kiện thống nhất.

**Biến thể mở rộng:** “Giữ chiều dài ban đầu là 8,5 m và lần cắt đầu là 2,75 m. Hãy chọn chiều dài lần cắt thứ hai để phần còn lại lớn hơn 3 m; nêu một lựa chọn và kiểm tra.” Gợi ý đáp án cho giáo viên: sau lần một còn 5,75 m; chẳng hạn cắt 2 m thì còn 3,75 m, đáp ứng yêu cầu. Học sinh có thể thử và kiểm tra, không yêu cầu ký hiệu bất phương trình chưa học. Chấp nhận nhiều lựa chọn dương nhỏ hơn 2,75 m.

Bài mở rộng không đưa vào điểm trước–sau chung nếu khác yêu cầu. Không dùng việc học sinh hoàn thành nhiều câu hơn để kết luận tiến bộ khi thời gian và hỗ trợ khác nhau.

### 4.4. Phương án hoàn toàn không thiết bị

Giáo viên dùng ma trận giấy, sách đã đối chiếu và bộ câu hỏi tự soạn: chọn một bài hai bước, tạo một phiên bản có gợi ý, một bản độc lập và một câu giải thích/mở rộng; tự giải, đối chiếu đơn vị rồi nhờ đồng nghiệp rà khi có điều kiện. Học sinh làm trong vở, trao đổi miệng hoặc dùng phiếu viết tay. Không có máy in thì chép lên bảng. Nếu giáo viên không truy cập được AI trong toàn bộ 6 tuần, vẫn triển khai chu trình phân hóa thủ công nhưng báo rõ không kiểm nghiệm được đóng góp của AI; không gọi đó là kết quả thử nghiệm AI.

## 5. Tổ chức trong 6 tuần

| Tuần | Hoạt động | Hồ sơ dự kiến |
|---|---|---|
| 1 | Khảo sát A; rà mục tiêu; đo cách soạn thủ công | MC01, ma trận, nhật ký thời gian |
| 2 | Tạo thử một bộ; duyệt toàn bộ; dùng mức hỗ trợ | MC02 gồm nháp và bản duyệt |
| 3 | Phân tích lỗi học sinh và lỗi câu hỏi | MC03, bài làm mã hóa |
| 4 | Điều chỉnh phân hóa, đo tiếp thời gian và số câu bị loại | Nhật ký phiên bản |
| 5 | Giảm hỗ trợ, kiểm tra khả năng tự giải | Sản phẩm độc lập |
| 6 | Khảo sát B; tổng hợp chất lượng, thời gian, giới hạn | MC04, MC05 |

Người phụ trách là giáo viên môn; đồng nghiệp rà một số bộ theo điều kiện thực tế. Lịch, số bộ và người phối hợp chưa được xác nhận. Dự kiến một đến hai hoạt động ngắn/tuần, lồng vào kế hoạch có sẵn.

## 6. Kế hoạch đánh giá hiệu quả và chi phí

**Học sinh:** so sánh bài A/B cá nhân cùng rubric /6, dùng mẫu ghép đủ hai bài. Ngưỡng đạt dự kiến từ 4/6 và không tiêu chí nào bằng 0, chốt trước thu dữ liệu. Báo số tăng/không đổi/giảm, số vắng và mức hỗ trợ; không thay dữ liệu thiếu bằng 0.

**Học liệu:** mỗi bộ ghi số câu nháp, số lỗi toán học, số lỗi diễn đạt, số câu ngoài mục tiêu, số sửa và số bị loại. Một câu có thể có nhiều lỗi nên tổng số lỗi không đồng nghĩa số câu lỗi. Tỉ lệ câu cần sửa = số câu có ít nhất một lỗi/số câu được rà × 100, khi mẫu số lớn hơn 0. Chưa có giá trị đo được.

**Thời gian:** ghi toàn bộ phút lập ma trận, tạo nháp, kiểm tra, sửa và định dạng, kể cả các lần thất bại. So sánh các bộ thủ công và có AI tương đương số câu, mục tiêu, độ khó bằng bảng mô tả; không chỉ tính thời gian nhập prompt. Việc giáo viên quen nội dung và khác biệt chủ đề làm so sánh chưa hoàn toàn công bằng. Có thể báo AI làm tăng thời gian nếu đó là kết quả thật.

| Chỉ báo | Trước/thủ công | Sau/có AI | Trạng thái |
|---|---|---|---|
| Điểm trung bình học sinh /6, mẫu ghép | Chưa có | Chưa có | Chưa tính |
| Số đạt/n và tỉ lệ | Chưa có | Chưa có | Chưa tính |
| Phút hoàn thiện mỗi bộ cùng quy mô | Chưa đo | Chưa đo | Chưa so sánh |
| Câu lỗi/câu được rà | Chưa thu | Chưa thu | Chưa tính |
| Chi phí công cụ, in ấn | Chưa xác minh | Chưa xác minh | Không giả định miễn phí |

Một lớp trước–sau không tách tác động AI khỏi phân hóa, sự luyện tập và việc giáo viên chuẩn bị kỹ hơn. Kết quả học sinh nếu có chỉ phản ánh thay đổi trong giai đoạn áp dụng tổ hợp giải pháp. Chưa có căn cứ xác định phần đóng góp riêng của AI hoặc khả năng khái quát.

## 7. Khả năng áp dụng và nhân rộng

Điều kiện cốt lõi là giáo viên có khả năng tự kiểm tra toán học, thời gian duyệt và quy tắc bảo vệ dữ liệu. Thiết bị cho giáo viên là điều kiện thử thành phần AI; thiết bị học sinh không bắt buộc. Cần kiểm tra khả năng truy cập, chi phí và điều kiện dùng thực tế trước chọn công cụ. Chỉ mở rộng sau khi có hồ sơ lỗi, chất lượng bài làm và chi phí; lớp khác cần đối chiếu nội dung đã học. Không lấy số câu trong ngân hàng làm bằng chứng nhân rộng thành công.

## 8. Kết luận và kiến nghị

Đề xuất xác định rõ vai trò hỗ trợ của AI và trách nhiệm duyệt của giáo viên, có học liệu, quy trình và phương án giấy. Hiện chưa có bằng chứng tiết kiệm thời gian hoặc cải thiện kết quả học sinh. Đề nghị tổ chuyên môn rà ma trận và đáp án, nhà trường xác định điều kiện sử dụng công cụ phù hợp; sau 6 tuần bổ sung dữ liệu thật, kể cả kết quả không thuận lợi, trước khi hoàn thiện hồ sơ.

## 9. Tài liệu tham khảo

Đã đọc tài liệu quy trình nội bộ SKKN-Master-Pro v1.0.0: `references/workflow.md`, `evidence-policy.md`, `lessons-learned.md`, `success-patterns.md`, `error-knowledge-base.md`, `quality-rubric.md`; `templates/ai-innovation-skkn.md`, `survey-template.md`, `impact-report.md`; ngày đọc 21/10/2026. Tác giả cá nhân/năm xuất bản chưa xác minh, không có URL công khai được cung cấp. Đây không phải nguồn chứng minh hiệu quả AI. Các ví dụ, prompt và rubric là đề xuất tự biên soạn. Tài liệu chương trình, sách và hướng dẫn công cụ chỉ được bổ sung vào nguồn đã dùng sau khi được đọc, xác minh; chưa viện dẫn quy định pháp luật trong bản này.

## 10. Phụ lục

### A. Prompt mẫu đề xuất, chưa phải nhật ký sử dụng thật

“Bạn hỗ trợ giáo viên tạo bản nháp Toán lớp 5. Nội dung được phép dùng: [giáo viên nhập phần đã đối chiếu chương trình]. Mục tiêu: vận dụng cộng, trừ số thập phân trong bài toán độ dài hai bước. Tạo 3 nhiệm vụ: có câu hỏi trung gian; giải độc lập; mở rộng bằng giải thích hoặc chọn dữ kiện. Dùng cùng mục tiêu, không gắn nhãn học sinh. Mỗi câu có đề, đáp án tự giải từng bước, đơn vị, tiêu chí đánh giá và lỗi có thể gặp. Không dùng kiến thức chưa liệt kê. Không tạo nguồn tham khảo hoặc thông tin học sinh. Nếu thiếu nội dung để xác định độ phù hợp, nêu rõ thiếu. Giáo viên sẽ kiểm tra toàn bộ trước dùng.”

### B. Checklist duyệt và nhật ký phiên bản

Mỗi câu phải được đánh dấu: đúng mục tiêu; kiến thức đã học; dữ kiện đủ; lời văn rõ; phép tính và đáp án tự giải đúng; đơn vị đúng; mức hỗ trợ phù hợp; không thông tin định danh; không nguồn giả; bản phát học sinh khớp đáp án. Bất kỳ mục chưa rõ nào đều chuyển câu về sửa, chưa phát.

Nhật ký gồm mã bộ/câu, ngày, công cụ/phiên bản hiển thị, prompt, bản nháp, phép giải của giáo viên, lỗi, bản sửa, người duyệt, phút từng khâu, mã bài làm phản hồi, quyết định giữ/sửa/loại. Các ô để trống đến khi có hoạt động thật; không dựng một cuộc hội thoại AI giả làm minh chứng.

### C. Đề đo và rubric

Đề A (15 phút): “Một cuộn dây dài 9,6 m. Cắt lần thứ nhất 2,35 m, lần thứ hai 1,8 m. Hỏi còn lại bao nhiêu mét?” Học sinh nêu lượng cần tìm trước, viết lời giải, kiểm tra. Đáp án: sau lần một 7,25 m; còn 5,45 m; chấp nhận tính tổng đã cắt 4,15 m rồi trừ.

Đề B (15 phút): “Một cuộn dây dài 9,4 m. Cắt lần thứ nhất 2,25 m, lần thứ hai 1,7 m. Hỏi còn lại bao nhiêu mét?” Đáp án: sau lần một 7,15 m; còn 5,45 m; hoặc tổng đã cắt 3,95 m. Hai đề cùng cấu trúc nhưng cần rà độ khó trước dùng; không dùng nguyên đề để luyện. Hai kết quả tình cờ bằng nhau không chứng minh hai đề có độ khó tương đương.

| Tiêu chí | 0 | 1 | 2 |
|---|---|---|---|
| Kế hoạch | Chưa hợp lý | Có bước đúng, thiếu liên kết | Hai bước hợp lý, giải thích đại lượng |
| Tính và đơn vị | Chưa có kết quả đúng có ý nghĩa | Có phần đúng, còn lỗi | Phép tính, kết quả, đơn vị đúng |
| Giải thích/kiểm tra | Không có hoặc không phù hợp | Kiểm tra đúng một phần | Cách kiểm tra đúng, giải thích rõ |

Đề chỉ đo một phạm vi vận dụng phép tính, chưa đại diện toàn bộ năng lực Toán lớp 5. Hỗ trợ tiếp cận cần thiết được ghi nhận và giữ tương đương hai lần; không cho gợi ý lời giải nếu đang đo khả năng độc lập.

### D. Sổ minh chứng và bảo quản

MC01: bài A, thực hành và thời gian thủ công; MC02: ma trận, prompt, nháp, đáp án, bản duyệt; MC03: bài làm và nhật ký sử dụng; MC04: bài B; MC05: bảng tổng hợp. Tất cả **chưa có**. Mỗi mã cần ngày, tệp, người giữ, mẫu, công cụ, tiêu chí chấm, dữ liệu thiếu, quyền sử dụng và trạng thái xác minh. Lưu khóa mã riêng; chỉ đưa bản ẩn danh hoặc tổng hợp vào báo cáo, không tải dữ liệu nhận diện trẻ em lên AI/repository công khai.

### E. Tự đánh giá nội bộ

| Nhóm | Mức 0–4 | Điểm | Căn cứ/giới hạn |
|---|---:|---:|---|
| Cấp thiết /10 | 1 | 2,50 | Mục 1 có bài toán thiết kế, chưa đo nhu cầu |
| Tính mới /15 | 1 | 3,75 | Chu trình duyệt, chưa đối chiếu cách cũ |
| Khoa học /15 | 2 | 7,50 | Có phép đo, giới hạn, chưa thử công cụ |
| Khả thi /10 | 2 | 5,00 | Bảy bước và phương án giấy, chưa xác nhận nguồn lực |
| Hiệu quả /15 | 0 | 0 | Chưa triển khai |
| Minh chứng /20 | 1 | 5,00 | Có đầu vào và công cụ thiết kế, không phải bằng chứng hiệu quả |
| Nhân rộng /10 | 1 | 2,50 | Điều kiện dự kiến, chưa thử lớp khác |
| Trình bày /5 | 3 | 3,75 | Đủ phần, chưa đối chiếu nơi nhận |
| **Tổng** | | **30,00/100** | Rubric nội bộ D01, không phải đánh giá công nhận |

Đã xử lý khi soạn: không gọi dùng AI là tự động mới; không khẳng định tiết kiệm; có kiểm tra đáp án độc lập, dữ liệu an toàn và phương án hoàn toàn không thiết bị; không dựng đầu ra thử nghiệm. Cần xác minh công cụ, phiên bản, chi phí, lịch, nội dung, mẫu nhận; cần thu toàn bộ MC và rà công cụ đánh giá. **Trạng thái cuối: kế hoạch đầy đủ cấu trúc, chưa sẵn sàng nộp.**
