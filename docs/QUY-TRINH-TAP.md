# QUY TRÌNH SẢN XUẤT MỘT TẬP [MR] — bản 0.2

> Bản 0.2 (01/11/2026 21:34, chủ dự án duyệt theo khuyến nghị): thêm dàn truyện, khuôn nhiều phần, kho đề tài, xử lý khiếu nại; phần còn lại vẫn là nháp 0.1, chốt sau tập 1. Soạn MR-0, 01/11/2026, theo khuôn `lost-places-lab/docs/QUY-TRINH-TAP.md` bản 2.2 và `crux-lab/CHARTER.md` §5 (ba cổng), rút gọn cho kênh mới. **Chờ chủ dự án duyệt.** Khi khác `docs/HIEN-CHUONG.md`, hiến chương thắng.
> Kế hoạch theo **mốc**, không theo ngày. Mỗi mốc kết thúc bằng **DỪNG → điều phối rà độc lập trên tệp → chủ dự án quyết**.
> Đơn giá ở §6 là **số đo của lost-places-lab**, chưa đo trên kênh này — dùng làm ước, thay bằng số đo thật sau tập 1.

## 0. Sơ đồ mốc và cổng
| Mốc | Việc | Tốn tiền? | Cổng |
|---|---|---|---|
| **M-a Đề tài + hồ sơ** | Chọn vụ, gom hồ sơ sơ cấp, xếp tầng pháp lý | 0 (đọc web công khai) | — |
| **M-b Kịch bản + ước chi** | Lời có nhãn tầng, kiểm lời độc lập, bảng shot, ước chi 3 mức | 0 | **G1: đề tài + kịch bản + trần chi** |
| **M-c Tài sản tốn tiền** | Giọng, ảnh/clip AI, nhạc | theo trần G1 | (rà tài sản, không phải cổng chủ dự án) |
| **M-d Dựng + kiểm** | Bản thô, quét V8, tờ khung, kiểm pháp lý lần 2 | ~0 | — |
| **M-e Bản cuối** | Sửa ≤ 2 vòng, gói phát hành | nhỏ | **G2: bản cuối** |
| **M-f Đăng** | Chủ dự án đăng | 0 | chủ dự án |

## 1. Ai làm gì
| Bên | Việc |
|---|---|
| **Chủ dự án** | Quyết G1, G2, đăng; nạp quỹ; mọi việc không đảo ngược được (chi mới, tài khoản, nhà cung cấp mới, sửa hiến chương) và gu (giọng, hình, nhạc, tiêu đề) |
| **Điều phối** (Claude Project riêng của MR) | Viết lệnh mốc kèm trần chi; rà độc lập trên tệp; merge; ghi `NHAT-KY.md` |
| **Phiên Claude Code** | Làm theo lệnh, tự kiểm, báo cáo trung thực, DỪNG ở cuối mốc |
| **Tác tử kiểm độc lập** | Kiểm lời (K-lời) và kiểm tầng pháp lý: không đọc báo cáo của phiên làm, mở nguồn đúng trang |

## 2. M-a — Đề tài + hồ sơ
1. Vụ phải có **ít nhất một hồ sơ sơ cấp** (SEC/DOJ/FTC/toà án) mở được, tải được, ghi SHA-256.
2. Bảng trạng thái vụ: tầng (ĐÃ KẾT ÁN / BỊ CÁO BUỘC / TIN ĐỒN) cho từng người/tổ chức; ngày kiểm; kháng cáo/ân xá/huỷ án nếu có.
3. Rủi ro: người có tên chưa bị cáo buộc, vụ đang xử (rủi ro bôi nhọ cao hơn), nạn nhân dễ nhận diện, dấu hiệu nhận diện có dạy được không.
4. Trình 3 vụ xếp hạng → chủ dự án chọn (có thể gộp vào G1).

## 3. M-b — Kịch bản + ước chi → G1
0. **Dàn truyện trước kịch bản** (0.2): logline, móc câu, bảng nhịp có nguồn + tầng, đề xuất số phần, bài học; kiểm độc lập từng nhịp; chủ dự án duyệt dàn truyện (và chọn vụ nếu có nhiều ứng viên) trước khi viết lời.
0b. **Khuôn tập (0.2, D2 PA-A):** mặc định **một vụ một tập**. Chia N phần chỉ khi **mỗi** phần có bước ngoặt có hồ sơ riêng **và** bài học riêng; cú treo cuối phần qua kiểm tầng như mọi câu. Loạt nhiều phần: G1 duyệt cả loạt (dàn truyện, bảng tầng, tổng trần chi); mỗi phần có duyệt lời riêng trước khi thu âm.
1. `docs/<tập>/NGUON.md` (mỗi nguồn: cơ quan, số vụ, ngày, URL, trang, "đã mở", SHA-256).
2. `LOI.md` + `loi.json`: mỗi câu một tầng + mã nguồn + trang; số viết bằng chữ cho TTS; câu TIN ĐỒN mở bằng "This is unverified…"; phần kết **dấu hiệu nhận diện** (3–5 dấu hiệu, mỗi cái gắn với một chi tiết của vụ).
3. **Kiểm lời độc lập** trước G1: tác tử con không đọc bản nháp cũ, mở nguồn đúng trang, chấm "khớp / mạnh hơn / sai" từng câu; riêng cột **tầng**: câu nào nói mạnh hơn trạng thái pháp lý → sửa.
4. Bảng shot: loại (sơ đồ dòng tiền, tài liệu hồ sơ, cảnh dựng minh hoạ có nhãn, chữ trích); mỗi cảnh dựng ghi nhãn ILLUSTRATIVE; không hàng nào có mặt người thật.
5. **Ước chi** từ bảng shot × đơn giá §6 — ba mức thấp/giữa/cao; đề xuất **trần cứng** từng khoản cho M-c.
6. Tiêu đề: 3 phương án ≤ 60 ký tự; không gọi bị cáo là có tội khi chưa kết án.
→ **G1 — chủ dự án duyệt:** (a) đề tài + bảng tầng pháp lý, (b) kịch bản (lời + kết dấu hiệu), (c) **trần chi** từng khoản cho M-c/M-d/M-e. Sau G1 lời và bảng shot **đóng băng**; yêu cầu mới sang tập sau, trừ lỗi nặng (sai nguồn, sai tầng, điều cấm).

## 4. M-c → M-e — Tài sản, dựng, bản cuối → G2
1. Trước mỗi lượt trả tiền: `scripts/cp/budget.py` `check()`; sau: `charge()` từ phản hồi; **402 → DỪNG**. Video AI theo `docs/LUAT-VEO.md` (V1–V8).
2. Tệp tốn tiền → LFS ≤ 10 phút; `reports/<mốc>/CHECKPOINT.md`.
3. QC tại nguồn mỗi ảnh/clip AI: mặt người (không giống người thật), nhãn ILLUSTRATIVE, chữ giả trên tài liệu, logo thật.
4. Dựng: chữ nguồn trên hình ở mọi câu pháp lý; quét `scripts/common/quet_v8.py` khi có khe Veo; tờ khung 1 s cả phim; −14 LUFS, true peak ≤ −1 dBTP.
5. **Kiểm pháp lý lần 2** trên bản dựng (tác tử độc lập): mọi chữ trên hình + lời khớp tầng; trạng thái vụ kiểm lại ngày dựng.
6. Sửa ≤ 2 vòng; vòng 3 → điều phối ghi nguyên nhân.
→ **G2 — chủ dự án duyệt bản cuối:** bản 540p/1080p, gói mô tả (nguồn đầy đủ + dòng khai AI), tiêu đề, chi thật so trần.

## 4b. Kho đề tài (0.2)
- Giữ `docs/kho-de-tai/` ≥ 10 vụ đạt HIEN-CHUONG §3 luật 8 (nhân vật trung tâm ●), có ≥ 1 hồ sơ sơ cấp mở được, chia đều các trụ: Ponzi/đầu tư · lừa tình & sextortion (nạn nhân người lớn) · rửa tiền · gian lận doanh nghiệp/kế toán · mạo danh & lừa đảo công nghệ · người trong cuộc (ngân hàng/công ty). Hai tập liền nhau không cùng trụ khi kho cho phép.
- Bổ sung kho khi còn < 6 vụ chưa làm.
- **Luật đệm (01/11/2026 23:33):** tập đăng liên tục, không chờ số liệu tập trước. Lúc nào cũng có **≥ 2 tập đã qua G1** chờ sản xuất; khi một tập vào M-c, một tập mới vào dàn truyện. Thứ tự tập 2–5 chốt cứng; từ tập 6 là dự kiến, số liệu xem chỉ dùng để đổi chỗ từ tập 6.

## 4c. Xử lý khiếu nại / đính chính (0.2)
Mọi khiếu nại (người trong vụ, luật sư, YouTube) → điều phối ghi NHAT-KY, kiểm câu bị khiếu nại với nguồn đúng trang → trình chủ dự án theo bậc tăng dần: (1) sửa mô tả, (2) ghim bình luận đính chính, (3) dựng lại đoạn bị khiếu nại, (4) gỡ video. Không trả lời người khiếu nại khi chủ dự án chưa quyết. Lỗi nguồn/tầng thật → sửa ngay ở bậc thấp nhất đủ khắc phục, ghi bài học vào luật.

## 5. Luật đứng
- Không đoán; số đo thật thắng số tự khai; chấm từ tệp đã render.
- Mỗi lệnh có gọi API trả tiền ghi ước chi + trần cứng; phiên không có trần = 0.
- Số dư đọc **trước và sau** mỗi phiên tốn tiền (OpenRouter `/api/v1/credits`, ElevenLabs `/v1/user/subscription`), ghi vào báo cáo + `COST-LEDGER.csv`.
- Không merge, không xoá nhánh, không force-push. Báo cáo tiếng Việt. DỪNG cuối mốc.

## 6. Đơn giá tham chiếu (số của lost-places-lab) + **số đo thật trên MR** (MR-4, 01/11/2026)
| Khoản | Đơn giá tham chiếu | Nguồn | **Đo thật MR-4** |
|---|---|---|---|
| Veo 3.1 Lite 1080p qua OpenRouter | 0,30 USD/clip 6 s; 0,40 USD/clip 8 s; ~1,1–1,2 lượt/khe | lost-places-lab NHAT-KY R-139–R-147 | **0,40 USD/clip 8 s, không âm** (`usage.cost` 3/3 lượt; bảng `/api/v1/videos/models`: 0,05 USD/s không âm, 0,08 USD/s có âm); **1,5 lượt/khe** trên 2 khe rủi ro cao nhất (V12 1 lượt, V06 2 lượt) — mẫu nhỏ, khe dễ hơn có thể ~1,0 |
| Veo 3.1 Fast 1080p | 0,60 USD/clip | R-139 | chưa đo |
| Ảnh NB2.1 Batch 2K (Gemini) | 0,028 USD/ảnh | lost-places-lab QUY-TRINH §7 | không có khoá |
| TTS ElevenLabs `eleven_v4` | ~0,44 ký tự tính tiền / ký tự gửi | QUY-TRINH §7 | **0,4401** ký tự tính / ký tự gửi (6.109 / 13.881, 25 lượt; header `Character-Cost` = chênh `/v1/user/subscription`); lời tập 1 một lượt 12.230 gửi → 5.383 tính; nhịp đọc thật **155 từ/phút** (2.005 từ → 12:55) |
| Eleven Music | ~825 ký tự / phút nhạc | QUY-TRINH §7 | chưa đo |
