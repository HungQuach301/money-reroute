# BÁO CÁO MR-K23 — Kịch bản tập 2 (`irs-callcenter-patel`) và tập 3 (`romance-sunmola`) → G1

> Phiên Claude Code, 01/11/2026 (UTC; sáng 02/11 giờ Hà Nội). Nhánh `claude/mr-k23-tap-2-3-3zvw9l` từ `main` @ `11b69dc`. Trần theo lệnh: **0 mọi khoản**.
> **Chi thật: 0 USD.** Không gọi API trả tiền, không sinh giọng hay hình, không gặp 402. Chỉ đọc hồ sơ công khai: 2 PDF trong repo (SHA-256 khớp kho), API thông cáo chính thức của DOJ, các trang công khai IRS, TIGTA, FTC, IC3, BOP và Pardon Attorney.
> Không vượt rào truy cập. Hai URL trang ân xá Trump 2017–2021 trả 404 → ghi "chưa mở được". Không gửi thông tin cá nhân của chủ dự án trong request (curl mặc định). Không merge, không xoá nhánh, không force-push.
> Preflight chạy riêng trước mỗi commit, chạy `--range origin/main..HEAD` trước mỗi lần đẩy; chỉ commit/đẩy khi mã thoát = 0.

## 1. Sản phẩm

| Tệp | Tập 2 — Patel | Tập 3 — Sunmola |
|---|---|---|
| `docs/tap0X-<vụ>/NGUON.md` | N1–N11: số vụ, ngày, URL, trang/đoạn, đã mở, SHA-256; trạng thái vụ (luật 4); đối chiếu chữ trích; trang được/cấm crop | N1–N8, cùng các cột |
| `loi.json` + `LOI.md` (dựng máy) | **71 câu** (69 đọc, 2 thẻ chữ), **1.860 từ**, 11.571 ký tự gửi TTS | **80 câu** (76 đọc, 4 thẻ chữ), **1.747 từ**, 10.810 ký tự gửi TTS |
| `SHOT.md` | 27 hàng · **≈ 13:41** (155 từ/phút) · Veo 7 / **10** / 15 khe | 24 hàng · **≈ 13:12** · Veo 7 / **10** / 15 khe |
| `UOC-CHI.md` (dựng máy) | OpenRouter 3,36 / **6,80** / 13,60 USD; ElevenLabs ≈ 8.517 / **10.800** / 16.455 ký tự tính | OpenRouter 3,36 / **6,80** / 13,60 USD; ElevenLabs ≈ 8.148 / **10.365** / 15.785 |
| `PHUONG-AN.md` | 3 tiêu đề ≤ 60 ký tự; giọng và B1 theo tập 1; gợi ý thumbnail | như trên |
| `kiem/vong*.md` | Vòng 1 (71 câu), vòng 2 | Vòng 1 (79 câu), vòng 2, 3, 4 |

**Công cụ mới** (`scripts/mrk23/`, 0 USD):
- `loi_md.py`: tổng quát hoá `scripts/mr3/loi_md.py`. Đọc luật riêng từng tập từ khoá `kiem_rieng` trong `loi.json`.
  - **KB:** HGLOBAL — mọi đoạn có tên phải có câu ◐ **đọc**; mọi chữ trên hình có tên phải chứa câu ◐; mọi dòng `SHOT.md` có tên phải kèm câu ◐.
  - **KC:** đúng một câu về ảnh riêng tư trong cả tập, câu đó là thẻ chữ, và `SHOT.md` nhắc tới nó ≤ 1 dòng.
  - **KA:** cơ quan bị mạo danh / quân đội bị mạo xưng phải kèm câu "không liên quan" trong cùng đoạn.
  - **KD:** regex cấm riêng từng tập: tên thành phố nạn nhân, tên 4 call center còn lại, tên thương hiệu thẻ/ứng dụng/dịch vụ chuyển tiền, chữ "bribe", tên giả, chi tiết tự sát, tên điều tra viên, số điện thoại…
  - **K5 mở rộng:** câu ●T phải có chủ thể DOJ hoặc "admitted"; câu ●C phải có chủ thể toà.
- `shot_tg.py`: chép từ `scripts/mr3/shot_tg.py`, đổi nhịp đọc sang 155 từ/phút (số đo thật).
- `uoc_chi.py`: dựng `UOC-CHI.md` từ đơn giá thật của QUY-TRINH §6.

Bản JSON các thông cáo DOJ lấy qua API được lưu ở `ho-so/<vụ>/doj-api-*.json` (SHA-256 ghi trong NGUON) để kiểm lại không cần mạng.

## 2. Áp các yêu cầu riêng của lệnh

### Patel — giữ tên HGLOBAL (quyết định chủ dự án MR-5)
- **Lời:** tên được đọc đúng một lần (S028, ●T: "According to the Justice Department, Patel admitted… including one called HGLOBAL"). Câu ◐ nhịp 4b đi **ngay sau** (S029), đọc nguyên văn, số viết bằng chữ.
- **Hình:** tên chỉ hiện ở SHOT hàng 11. Ô chữ và nguyên câu ◐ (bản chữ số) hiện cùng khung, bật và tắt cùng lúc. Nhãn ● ghi rõ "PATEL" để người xem không tưởng nhãn ● là của call center (đề xuất của kiểm vòng 2). Không dùng ảnh trang N1 tr. 7.
- **Không suy trạng thái sau 7/2018.** Kiểm máy KB đạt. Hai vòng kiểm độc lập đều xác nhận câu ◐ khớp N1 tr. 1, N3 đ.15, N5 đ.12.
- **Lưu ý cho điều phối:** câu ◐ đã khoá giữ thì hiện tại "it is presumed innocent". Kiểm vòng 1 gợi ý có thể đổi thành "was" nếu chủ dự án cho sửa; phiên **không đổi** vì đây là câu chủ dự án đã duyệt. Cần kiểm lại trạng thái HGLOBAL vào ngày đăng (luật 4).

### Sunmola — một câu khái niệm về ảnh riêng tư (K3)
- Câu S033 "With at least one woman, it went further: he threatened to expose private images." là thẻ chữ tối (doc=false), giữ 6 s, không nhạc, không hình (SHOT hàng 11).
- Không câu nào khác, kể cả bài học, dấu hiệu và thẻ tổng kết, gợi lại nhánh này. Kiểm máy KC đạt; hai vòng kiểm độc lập xác nhận. Tên tội "interstate extortion" (S038) được giữ vì là tội danh bắt buộc, không gắn với ảnh.
- Không tên giả, không tên trang hẹn hò/dịch vụ chuyển tiền, không tổ hợp tuổi + hoàn cảnh + bang, không lời nạn nhân, không chi tiết tự sát hay váy cưới, không tên điều tra viên/chuyên gia/công tố.

### Chung
- en-US; số viết bằng chữ (K3 đạt).
- Phần tổng kết rõ ở cuối mỗi tập: 3 bài học + 5 dấu hiệu + 1 nguyên tắc + nơi báo cáo (TIGTA/FTC; IC3/FTC), kèm thẻ tổng kết B1 trên hình.
- Mỗi câu ghi tầng, nguồn và trang/đoạn.

### SHOT — áp bài học Veo MR-4
- Giấu người bằng ánh sáng: "dark silhouette against a bright window", "hands lit from behind".
- Lời Veo mô tả **cái có trong khung**, không dựa vào chỉ dẫn phủ định hay vị trí.
- Neo cuối là cảnh trống mô tả cụ thể. Màn hình là "soft blank white rectangle", thẻ nhựa trắng trơn.
- Các khe có người (Patel V03, V10; Sunmola V03, V06, V10) được đánh dấu rủi ro cao, sinh trước ở M-c.

## 3. Kiểm lời độc lập (mỗi vòng một tác tử mới, không đọc dàn truyện/báo cáo, tự mở nguồn đúng trang)

| Vòng | Tập 2 — Patel | Tập 3 — Sunmola |
|---|---|---|
| 1 (toàn bộ) | 58 khớp · **6 mạnh hơn** · 0 sai · 7 không cần nguồn · 0 "làm theo được" | 71 khớp · **2 mạnh hơn + 2 sai tầng** · 0 sai · 6 không cần nguồn · 0 "làm theo được" |
| Sửa sau vòng 1 | S007 "American hands" → "people in the United States"; S037 thêm "According to the indictment" (hawala); S043 "up to twenty years" → "from probation to twenty years in prison" (N3 có 2 án quản chế); S046 "are" → "were presumed innocent" (nhóm 32 người gồm cả Patel); S059 bỏ ghép "gift cards" vào ●T, viết lại theo N4 đ.5; S063 tách vế "question or appeal" sang lời IRS; S049 bỏ trùng ý | S076 bỏ ghép "ảnh quân phục" (toà) với "ảnh người khác" → lời DOJ, ◐; S048 "could not reach all of them"; S063 sửa tầng; tuỳ chọn: S003/S004 tách "không đúng sự thật"; S008 ● → ●C; S012 bỏ "evidence presented in court showed"; S007 thêm nguồn N2 tr. 4 |
| 2 (câu sửa + lướt toàn bộ) | **7/7 khớp; lướt 71 câu: 0 vi phạm** | 7/8 khớp; **S063 mạnh hơn nhẹ** → tách thành CHUNG + ●C (S063b) theo đề xuất; SHOT "hàng 15" → "hàng 11"; S059 "eight-page transcript of his oral statement" |
| 3 (câu sửa) | — | xem §6 |

## 4. Đề xuất trần cho M-c (theo đơn giá THẬT QUY-TRINH §6)

| | Tập 2 | Tập 3 |
|---|---|---|
| M-c `openrouter_usd` | **7,50** (giữa 10 khe × 0,40 × 1,5 = 6,00 + ≈ 25 %) | **7,50** |
| M-c `elevenlabs_chars` (ký tự tính) | **12.500** (giữa ≈ 9.920) · chặn gửi ≤ 24.000 | **12.000** (giữa ≈ 9.485) · chặn gửi ≤ 22.000 |
| M-d | 0 | 0 |
| M-e | 1,60 USD + 2.000 ký tự | 1,60 USD + 2.000 ký tự |
| **Cả tập** | **9,10 USD + 14.500 ký tự** | **9,10 USD + 14.000 ký tự** |

Số dư OpenRouter khả dụng cho MR trước mỗi M-c: ≥ 8,20 USD (V7), chưa tính phần các phiên lost-places-lab chạy cùng lúc. Số dư gần nhất do chủ dự án báo là 25,65 USD; MR-5 có trần 8,30 USD. Nhạc 825 ký tự/phút vẫn là số tham chiếu, chưa đo trên MR.

## 5. Cần chủ dự án / điều phối quyết ở G1
1. **Tiêu đề.**
   - Tập 2: đề xuất T1 "Fake IRS Calls From India: How the Money Got Out" (48 ký tự). T2 không có tên cơ quan.
   - Tập 3: đề xuất T1 "A Fake Soldier, 27 Years in Prison: A Romance Scheme" (52 ký tự).
   - Câu hỏi luật 8e: tiêu đề có tên cơ quan bị mạo danh, kèm chữ "Fake" — chấp nhận được không? (Tập 1 tránh tên thương hiệu trong tiêu đề.)
2. **Câu ◐ HGLOBAL:** giữ "it is presumed innocent" như đã duyệt, hay đổi "was"?
3. **Thẻ "không liên quan" chỉ hiện chữ** (Patel P01, P11; Sunmola P02, P11, P12, theo cách tập 1 làm với HBO/Netflix): đạt luật 8e theo cả hai vòng kiểm. Có muốn cho đọc thành lời thêm một lần ở mỗi tập không?
4. **Độ dài:** Sunmola ≈ 13:12, ngắn hơn ước 15 phút của dàn truyện. Lý do: bỏ mọi chi tiết nhận diện nạn nhân, chỉ thêm phần kháng cáo có hồ sơ (N2 tr. 5–17).
5. **Trần M-c** ở §4.

## 6. Kết quả cuối, trạng thái vụ, việc còn mở
- **Trạng thái vụ** (kiểm 01/11/2026 UTC):
  - Patel: BOP có bản ghi khớp tên đệm + tuổi nhưng chưa xác minh tuyệt đối → **không đưa vào lời**. Không có ân xá trên các trang mở được. Kháng cáo chưa mở được.
  - Sunmola: BOP còn thụ án, dự kiến ra 2037 (S064 gắn mốc). Không có ân xá.
  - **Kiểm lại ngày đăng.**
- **Còn mở:**
  - Plea agreement/judgment của Patel và hồ sơ S.D. Ill. của Sunmola chưa mở được (PACER cấm) → lời giữ chủ thể "according to the Justice Department" / "according to the appeals court".
  - Trích dẫn "887 F.3d 830" chưa đối chiếu, nên không ghi trên hình.
  - Nghe tai các tên ở M-c (bảng phát âm trong LOI.md).
- **Kiểm vòng 3 tập 3:** kết quả ghi ở `docs/tap03-romance-sunmola/kiem/vong3.md` và tóm ở dòng cuối báo cáo này.

**DỪNG — chờ điều phối rà và G1.**
