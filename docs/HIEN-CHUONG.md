# MONEY REROUTE — HIẾN CHƯƠNG v1 (NHÁP MR-0)

> Trạng thái: **NHÁP, chờ chủ dự án duyệt** (soạn MR-0, 01/11/2026). Nguồn thẩm quyền số một về nội dung; mọi tệp khác phải khớp. Hiến chương < 2 trang.
> Căn cứ khuôn: `lost-places-lab` (BIBLE §7 luật 3 tầng, §7.1 nhạy cảm, §10 khai AI) và `crux-lab` (CHARTER §4 nhân vật ILLUSTRATIVE, RIGHTS §F footage ngoài) — chỉ mượn cấu trúc, không mượn kết luận.

## 1. Định vị
- **Kênh:** drama bài học tài chính / lừa đảo, tiếng Anh, không lộ mặt. Mỗi tập kể **một vụ có hồ sơ công khai** như một câu chuyện có nhịp phim, và kết bằng **các dấu hiệu nhận diện** người xem dùng được.
- **Lời hứa (EN, nháp):** *"Real cases from the public record — how the money was rerouted, and the red flags you can spot next time."*
- **Chỉ dạy nhận diện, không dạy làm.** Tập giải thích *vì sao* nạn nhân tin và *dấu hiệu nào* lẽ ra phải thấy. **Không** hướng dẫn từng bước cách lừa, cách rửa tiền, cách né cơ quan chức năng; chi tiết cơ chế chỉ ở mức đủ hiểu dấu hiệu.
- **Không khuyên đầu tư**, không khuyên pháp lý, không dự báo thị trường. Câu kết hướng tới nguồn chính thức (SEC, FTC, CFPB…), không tới sản phẩm.

## 2. Nguồn được dùng
- **Hồ sơ sơ cấp công khai:** SEC (litigation releases, complaints, administrative proceedings), DOJ (thông cáo, cáo trạng, bản án), FTC (complaints, orders), toà án (PACER/CourtListener: cáo trạng, phán quyết, biên bản tuyên án). Báo chí lớn chỉ để **bổ sung bối cảnh**, không làm trụ cho câu về tội.
- Mỗi tập có `docs/<tập>/NGUON.md`: số vụ/docket, cơ quan, ngày, URL, trang, cột "đã mở", SHA-256 PDF. Không mở được → không dùng câu cần nguồn đó.
- **Ghi nguồn hai chỗ:** trên hình (dòng nhỏ khi nêu sự việc pháp lý, vd "Source: SEC v. X, No. 1:23-cv-…, S.D.N.Y. 2024") **và** trong mô tả video (danh sách đầy đủ có liên kết).

## 3. Ba tầng pháp lý (mọi câu về người/tổ chức thật thuộc đúng MỘT tầng)
| Tầng | Nghĩa | Điều kiện nguồn | Cách nói (EN) | Nhãn hình |
|---|---|---|---|---|
| **ĐÃ KẾT ÁN** | Có bản án/nhận tội có hiệu lực, hoặc phán quyết dân sự cuối cùng | Bản án, judgment, plea agreement, thông cáo DOJ/SEC về kết quả | Nói thẳng, kèm năm + toà: "In 2024, a federal jury convicted…" | ● CONVICTED / ● JUDGMENT |
| **BỊ CÁO BUỘC** | Đã có cáo trạng/đơn kiện của cơ quan, chưa kết luận (hoặc dàn xếp **không thừa nhận**) | Cáo trạng, complaint, settlement order | Luôn gắn chủ thể và chữ "alleged": "The SEC alleges…", "Prosecutors charged… He has pleaded not guilty." Dàn xếp không thừa nhận: "settled without admitting or denying" | ◐ ALLEGED |
| **TIN ĐỒN** | Lời đồn, cáo buộc trên mạng, suy đoán; không có hồ sơ cơ quan/toà | — | Mở bằng "This is unverified…" / "Online claims say…, but no court or agency has found…" | ○ UNVERIFIED |
Luật thi hành:
1. Kịch bản đánh nhãn tầng **từng câu** (`loi.json`); câu không nhãn không được thu âm.
2. **Không nâng tầng:** không biến BỊ CÁO BUỘC thành ĐÃ KẾT ÁN bằng giọng chắc chắn; bị cáo được tuyên vô tội/huỷ án → nói rõ, không ám chỉ.
3. **Tin đồn về người cụ thể có tên: mặc định KHÔNG dùng.** Chỉ dùng khi bản thân tin đồn là một phần hồ sơ (vd được nhắc trong đơn kiện) và không nêu tên cá nhân không bị cáo buộc.
4. Kiểm trạng thái vụ **ngày chốt lời** và **ngày đăng** (kháng cáo, ân xá, huỷ án); ghi ngày kiểm vào gói phát hành.
5. Người không bị cáo buộc (nạn nhân, nhân chứng, người nhà): không nêu tên trừ khi đã công khai tự nguyện và cần cho truyện.

## 4. Hình ảnh người thật và nhân vật minh hoạ
- **Không mặt người thật**: không ảnh chụp, không footage, không chân dung AI, không phác hoạ nhận ra được, không giọng nhái của bị cáo, nạn nhân, nhân chứng, quan chức.
- **Nhân vật minh hoạ**: cảnh dựng lại dùng nhân vật **không mặt hoặc cách điệu**, không giống người thật; **luôn có nhãn trên hình** "ILLUSTRATIVE — not the real person" (hoặc "DRAMATIZATION") khi xuất hiện lần đầu mỗi đoạn.
- Lời trích nguyên văn từ hồ sơ hiện bằng **chữ trên hình** (trích dẫn + nguồn), không bằng giọng đóng vai.
- Được dùng: tài liệu hồ sơ (trang đơn kiện, cáo trạng — tài liệu chính phủ Mỹ, kiểm từng tệp), sơ đồ dòng tiền tự vẽ từ số liệu hồ sơ, logo **không** (trừ khi cần nhận diện và chỉ dạng chữ).

## 5. Danh sách cấm (vi phạm = không phát hành)
- Bịa trích dẫn, số tiền, ngày, số vụ, cơ quan, nạn nhân, hoặc "tài liệu rò rỉ" không có nguồn công khai.
- Trình bày cáo buộc như đã kết án; nói ai đó có tội khi chưa có bản án.
- Hướng dẫn thực hiện lừa đảo/rửa tiền/né kiểm soát ở mức làm theo được.
- Mặt/giọng người thật; hình AI giả làm ảnh tư liệu, ảnh hiện trường, tài liệu toà án thật.
- Chế giễu nạn nhân; giật gân trên nạn nhân còn sống hoặc thân nhân trực tiếp.
- Khuyên đầu tư, quảng bá sản phẩm tài chính, liên kết tiếp thị tới nền tảng bị nêu trong vụ.

## 6. Khai AI
- YouTube Studio → "AI use" = **Yes** cho mọi tập có cảnh dựng tả thực hoặc giọng AI. Đọc lại trang Help khai AI (support.google.com/youtube/answer/14328491) trước mỗi lần đăng, ghi ngày đọc.
- Dòng khai cố định trong mô tả (EN, nháp): *"Dramatized scenes use AI-generated visuals and illustrative characters, not the real people involved. Narration voice is AI-generated. Facts are drawn from the public court and agency records listed below."*

## 7. Thẩm quyền và thay đổi
Hiến chương → quyết định của chủ dự án trong `docs/NHAT-KY.md` → `docs/QUY-TRINH-TAP.md` → `docs/LUAT-VEO.md`. Chỉ chủ dự án sửa hiến chương; mọi sửa ghi mục MR-xx.
