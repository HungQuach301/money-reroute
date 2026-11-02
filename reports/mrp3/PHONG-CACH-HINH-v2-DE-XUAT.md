# ĐỀ XUẤT PHONG-CACH-HINH v2 — chuyển động, âm thanh, nhịp (từ MR-P3)

> NHÁP của phiên MR-P3 (02/11/2026), **chưa duyệt**. Thay/bổ sung §5 "Mật độ và chuyển động" và §6 "Đơn giá" của `docs/PHONG-CACH-HINH.md` v1; thêm §7 Âm thanh, §8 Nhịp. Khi khác HIEN-CHUONG §4–§5, hiến chương thắng. Căn cứ số đo: `reports/mrp3/BAO-CAO.md`, `reports/mrp2/BAO-CAO.md`.

## §5 Chuyển động (thay v1)
1. **Không cảnh tranh nào chỉ là ảnh tĩnh trượt.** Mọi cảnh L1 có: thị sai 2.5D ≥ 2 lớp theo độ sâu (Depth Anything V2 Small, Apache-2.0, CPU) **và** đúng 1 lớp phủ phát ra từ nguồn có trong tranh — **hoặc** là clip.
2. **2.5D:** trượt ≤ 30 px ở độ sâu 1 (1080p), phóng 1,06–1,14; vật mảnh gần mép lớp ≤ 22 px; QC mép 1:1 mọi tranh (`scripts/mrp2/qc_mep.py`).
3. **Lớp phủ** (≤ 1/cảnh): hơi/khói nhẹ từ đúng vật, bụi trong vùng sáng, mưa trượt trên kính, sương trôi, cát chảy, màn hình sáng, đèn chập chờn ≤ ±6 % < 3 Hz, rung khi va chạm (khớp tiếng động). Không thêm người/chữ/vật; không phủ lên mặt nhân vật.
4. **Clip ảnh→video — mặc định Veo 3.1 Lite 720p 4 s (0,12 USD)**, phóng lên 1080p Lanczos khi dựng; 1080p (0,20 USD) chỉ khi cảnh có cạnh sắc/chi tiết nhỏ cần giữ. Phủ **≈ 1/3 thời lượng tranh** mỗi tập (≈ 60 clip). Khung đầu **không người, không chữ, không màn hình có nội dung**; lời "very slow / slightly", "nobody is there", nêu rõ vật phải đứng yên. Cảnh dài hơn clip: giữ khung đầu rồi chạy clip, **không dãn** (V2). Vật cơ khí chuyển động lớn (cửa két, bản lề) dễ biến dạng sau ~2,5 s → chỉ dùng 2,5 s đầu.
5. **Nhân vật đại diện:** mặc định **hoạt hoạ cắt ghép bằng mã** trên chính tranh (chớp mắt 0,16 s mỗi 2–3 s, nghiêng đầu ≤ 1,5°, thở ≤ 2 px; máy phẳng nhẹ, không 2.5D lên mặt). Khoảnh khắc cảm xúc lớn (≤ 3/tập): Kling v3.0 Std khung đầu = tranh nhân vật, 3 s 720p, lời ghi biên độ biểu cảm rất nhỏ, QC nhất quán `ref_nv`. **Không** Veo chữ→video cho nhân vật (ra người khác), **không** khung đầu/cuối có người cho Veo (bị lọc). Người thật: vẫn chỉ bóng/lưng/tay, không đưa vào lượt sinh có chuyển động mặt.
6. **Đo:** `scripts/mrp3/do_chuyen_dong.py` so với đối chứng phẳng cùng dòng thời gian — mục tiêu ≥ 55 % thời lượng tranh; kèm tờ 1 s và tờ 0,5 s mọi clip (V8). Thước đo không thấy chập chờn/chớp mắt → không dùng số này để loại cảnh.
7. Mức **M3** (clip ≈ 2/3 tranh) chỉ cho 1–2 đoạn cao trào/tập.

## §6 Đơn giá (đo thật MR-P3, cập nhật v1)
- Veo 3.1 Lite không tiếng 4 s: **0,12 USD (720p) · 0,20 USD (1080p)**; lượt 1 đạt 16/17 khi khung đầu không người.
- Kling v3.0 Std 720p 3 s: **0,42 USD** (giá thật, cao hơn danh mục).
- ElevenLabs Sound Effects: **≈ 11 ký tự/giây**; Eleven Music **825 ký tự/phút**.
- Ước tập ~15 phút theo §5: tranh ≈ 7,8 + clip 720p ≈ 7,4 ≈ **15 USD OpenRouter** + ElevenLabs giọng ≈ 6.100 + nhạc 3.200–12.000 + tiếng động ≈ 200 ký tự.

## §7 Âm thanh (mới)
1. **Tiếng động** ở mọi cảnh có nguồn âm trong hình/lời (điện thoại, búa toà, khoá, lật trang hồ sơ, đồng hồ đếm ngược), đặt theo **mốc từ** của giọng; nền phòng/phố rất nhỏ (−34 … −40 dB) dưới cảnh không khí.
2. **Nguồn:** CC0 — chỉ khi **trang của chính tệp** ghi CC0; ghi URL, giấy phép, sha256 từng tệp (`scripts/mrp3/cc0.py`). Giấy phép khác/không rõ → không dùng. ElevenLabs SFX cho 3–6 tiếng "nhấn" điện ảnh/tập (va chạm trầm, riser) mà CC0 thiếu.
3. **Nhạc chia theo hồi:** mỗi đoạn lời có hồi riêng (mở/móc → dẫn → dồn → lật → dư âm). Ở **cú lật** (câu đảo chiều câu chuyện): nhạc **dừng cứng đúng từ khoá** + một va chạm, lặng ≤ 1,2 s, rồi hồi mới. Eleven Music dùng "composition plan" theo đúng thời lượng hồi đo từ giọng; hoặc cắt/ghép nhạc đã duyệt (0 USD).
4. Không để lặng tuyệt đối > 0,5 s (giữ nền phòng); −14 LUFS, đỉnh thật ≤ −1,5 dBTP.

## §8 Nhịp (mới)
1. Cảnh tranh TB ~2,5 s; **điểm cắt tranh→tranh dời tới phách nhạc gần nhất trong ±0,3 s** (mỗi cảnh ≥ 1 s); ranh có L2/L3 giữ theo giọng.
2. **Chữ động cho câu trích nguyên văn** (chỉ chữ "chu" đã duyệt trong `loi.json`): từng từ hiện theo mốc giọng, nhấn đúng một từ, vạch màu theo tầng (● đỏ cam / ◐ hổ phách), dòng nguồn + nhãn tầng giữ lớp tĩnh.
3. Tiếng động "nhấn" trùng điểm cắt hoặc trùng chữ động; ≤ 1 nhấn mỗi 2 s.
