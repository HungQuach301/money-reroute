# BẢNG SHOT 2 — Tập 2 · Call center mạo danh IRS/USCIS / Patel (`tap02-irs-callcenter-patel`) · phong cách PHONG-CACH-HINH v1

> MR-S23 · 02/11/2026 · tiền kỳ (0 USD). **Thay `SHOT.md`** (giữ làm lịch sử) cho phần hình; lời đã duyệt G1 (02/11/2026 10:25) + quyết định KBCB áp ở MR-S23. Bảng **sinh máy** `python3 scripts/mrs23/shot2.py tap02` từ `scripts/mrs23/du_lieu_tap02.py` + `loi.json`; khuôn `docs/tap01-1inmm/SHOT2.md`.
> **Mốc là ƯỚC** (chưa có giọng): 155 từ/phút (đo thật MR-4), nghỉ 1.5 s đầu mỗi đoạn, thẻ chữ không đọc 4 s, thẻ tối riêng 6 s. Ở M-c/M-d thay bằng mốc whisper giọng thật (`scripts/mr6/moc_cau.py`) và chia lại thời lượng cảnh theo trọng số; cảnh tranh dài > 5 s tách thành 2 khung cắt/chuyển động của **cùng** tranh (không thêm tranh).
> Tổng ước **12:53** (lời + thẻ 12:25 · thẻ tổng kết 8 s · nguồn 20 s) · **183 cảnh** · L1 tranh 124 cảnh (443 s, TB 3.6 s) từ **103 tranh mới** (cảnh trống/vật 85 · người thật bóng/lưng/tay 8 · N1 7 · N2 3) · L2 47 cảnh (232 s) từ **15 đồ hoạ động** · L3 7 cảnh (31 s) · Veo ảnh→clip **5** khoảnh khắc (21 s).
> Luật áp mọi cảnh: HIEN-CHUONG §4–§5; PHONG-CACH-HINH §1–§5; LUAT-VEO V1–V8 + BAI-HOC tập 1 mục 2; nhãn tầng + dòng nguồn lớp tĩnh góc dưới theo `loi.json`; nhãn ILLUSTRATIVE ở cảnh tranh đầu mỗi đoạn; không chữ trên hình ngoài lời đã duyệt, số liệu hồ sơ, nhãn, nguồn (M-d đối chiếu máy như `scripts/mr6/doi_chieu_chu.py`).
> **Riêng tập 2** (SHOT.md MR-K23, giữ): không dựng cuộc gọi — không thoại người gọi, không chữ kịch bản, **không số điện thoại** (kể cả giả), không giao diện ứng dụng gọi/nhắn; màn hình = khối trắng mềm trơn; thẻ nhựa **trắng trơn**; không logo/con dấu/huy hiệu IRS, USCIS, DHS, HSI, DOJ, CRA, ATO — tên cơ quan chỉ chữ trơn; không tên 4 call center còn lại, không tên thương hiệu thẻ/dịch vụ chuyển tiền.
> **Ahmedabad / Ấn Độ / Singapore:** không biểu tượng tôn giáo, trang phục dân tộc, cảnh đường phố định kiến; chỉ bản đồ phẳng tự vẽ (L2) và nội thất văn phòng trung tính.
> **Tên call center ở P05 (S028):** mọi dòng có tên kèm nguyên câu ◐ (máy kiểm KB quét cả tệp này).

## 0. Nhân vật và người trong hình

| Mã | Ai | Cách vẽ (cố định cả tập) | Được / không |
|---|---|---|---|
| N1 | Người nghe máy (đại diện người nhận cuộc gọi; KHÔNG phải nạn nhân cụ thể nào trong hồ sơ) | Đàn ông ~55 tuổi tự nghĩ ra, tóc muối tiêu cắt ngắn, râu ngắn, kính gọng mảnh, áo len cardigan xanh navy ngoài sơ mi kẻ ô; nhà bếp gỗ ấm. Mặt cách điệu, không phóng đại nét, không gắn sắc tộc | Được có mặt cách điệu, nhãn ILLUSTRATIVE. **Không** dùng cho câu về nạn nhân cụ thể (S009, S010) — ở đó chỉ vật |
| N2 | Người con (đại diện người thân, chỉ ở P11) | Phụ nữ ~30 tuổi tự nghĩ ra, tóc đen buộc đuôi ngựa, áo khoác ô liu; luôn ngồi cạnh N1 | Được có mặt cách điệu, nhãn ILLUSTRATIVE |
| R | Patel (bị cáo ●) | Bóng ngược sáng, lưng, tay/tay áo sơ mi trơn sáng màu; trang phục trung tính, không phụ kiện tôn giáo/dân tộc; nhãn tên chỉ ở thẻ chữ | Không mặt, không góc 3/4 |
| R | Người gọi, quản lý call center, runner, đồng bị cáo (không tên) | Chỉ bóng xa trong phòng tối, tai nghe trên bàn, tay trên bàn phím/quầy | Không mặt; không biển hiệu, không chữ trên màn hình |
| R | Nạn nhân trong hồ sơ (người 85 tuổi, người mất $136,000) | Không vẽ người: chỉ đồ vật (ghế trống, tờ giấy trắng, lịch trơn) | KBCB — không nhận diện |

Tham chiếu nhất quán (PHONG-CACH-HINH §4): `ref_nv` = tranh đầu có N1 / N2 (chỉ gửi kèm cảnh có nhân vật đó); `ref_canh` = một tranh trống cùng nét (mọi cảnh khác; lời sinh ghi rõ nhân vật KHÔNG có trong cảnh).

## 1. Bảng cảnh

| Câu | Tầng | Mốc ước (s) | Cảnh: lớp · mã · thời lượng | Lớp chồng |
|---|---|---|---|---|
| S001 (P00) | MH | 1.5–5.8 | L1 `p001` 1.6 · veo `K1` 2.6 |  |
| S002 (P00) | ●T | 5.8–19.7 | L1 `p002` 4.0 · L2 `G01` 6.0 · L1 `p003` 4.0 |  |
| S003 (P00) | KBCB | 19.7–27.4 | L1 `p004` 3.9 · L1 `p005` 3.9 | kbcb: The IRS and U.S. Citizenship and Immigration Services had nothing to do with these calls. (đọc — chữ phụ đề) |
| S004 (P00) | ●T | 27.4–38.7 | L2 `G02` 4.6 · L1 `p006` 3.3 · L1 `p007` 3.3 |  |
| S005 (P00) | NB | 38.7–41.0 | L1 `p008` 2.3 | ten: Hitesh Madhubhai Patel · ● CONVICTED (2020) |
| S006 (P00) | ● | 41.0–46.8 | L2 `G02` 2.9 · L1 `p009` 2.9 |  |
| S007 (P00) | CHUNG | 46.8–55.3 | L1 `p010` 2.8 · L1 `p011` 2.8 · L1 `p012` 2.8 |  |
| S008 (P00) | CHUNG | 55.3–62.7 | L1 `p006:2` 3.7 · L1 `p013` 3.7 | tieu_de: Real cases from the public record · MONEY REROUTE |
| S009 (P01) | ◐ | 64.2–76.2 | L1 `p014` 4.0 · L1 `p015` 4.0 · L1 `p016` 4.0 |  |
| S010 (P01) | ◐ | 76.2–86.6 | L1 `p017` 3.5 · L1 `p015:2` 3.5 · L1 `p018` 3.5 |  |
| S011 (P01) (thẻ, không đọc) | KBCB | 86.6–90.6 | L1 `p019` 4.0 | kbcb: The IRS and USCIS had nothing to do with these calls. The callers were impersonating them. |
| S012 (P02) | TT | 92.1–100.2 | L1 `p020` 2.5 · L2 `G03` 3.0 · L1 `p021` 2.5 |  |
| S013 (P02) | TT | 100.2–105.3 | L2 `G03` 3.0 · L1 `p022` 2.0 |  |
| S014 (P02) | TT | 105.3–113.8 | L2 `G03` 3.6 · L1 `p023` 2.4 · L1 `p024` 2.4 |  |
| S015 (P02) | ◐ | 113.8–128.1 | L2 `G03` 4.8 · L1 `p025` 4.8 · L1 `p026` 4.8 |  |
| S016 (P03) | ◐ | 129.6–132.3 | L1 `p027` 2.7 |  |
| S017 (P03) | ◐ | 132.3–143.5 | L3 `T01` 4.6 · L2 `G04` 3.3 · L1 `p028` 3.3 |  |
| S018 (P03) | ◐ | 143.5–154.8 | L3 `T02` 4.6 · L2 `G04` 3.3 · L1 `p029` 3.3 |  |
| S019 (P03) | ◐ | 154.8–168.7 | L2 `G04` 6.0 · L1 `p030` 4.0 · L1 `p031` 4.0 |  |
| S020 (P03) | ◐ | 168.7–179.9 | L2 `G04` 3.7 · L1 `p032` 3.7 · L1 `p033` 3.7 |  |
| S021 (P03) | KBCB | 179.9–185.7 | L1 `p027:2` 2.9 · L1 `p034` 2.9 |  |
| S022 (P04) | ◐ | 187.2–193.4 | L1 `p035` 2.5 · veo `K2` 3.7 |  |
| S023 (P04) | ◐ | 193.4–202.7 | L1 `p036` 3.1 · L2 `G05` 3.1 · L1 `p037` 3.1 |  |
| S024 (P04) | ◐ | 202.7–216.3 | L2 `G05` 5.8 · L1 `p038` 3.9 · L1 `p039` 3.9 |  |
| S025 (P04) | ◐ | 216.3–229.4 | L1 `p040` 4.1 · L1 `p041` 4.1 · L2 `G05` 4.9 |  |
| S026 (P04) | ◐ | 229.4–236.4 | L1 `p042` 2.3 · L2 `G05` 2.3 · L1 `p043` 2.3 |  |
| S027 (P05) | ◐ | 237.9–250.7 | L2 `G06` 5.5 · L1 `p044` 3.6 · L1 `p045` 3.6 |  |
| S028 (P05) | ●T | 250.7–259.2 | L1 `p046` 2.5 · L2 `G06` 3.5 · L1 `p047` 2.5 | ten_hglobal: ô chữ tên + nguyên câu ◐ cùng khung, bật/tắt cùng lúc: HGLOBAL was also charged; like every defendant who has not been convicted, it is presumed innocent. As of July 2018, the India-based call centers charged had yet to be arraigned; as of November 2020, the Justice Department said charges remained pending for other India-based defendants. |
| S029 (P05) | ◐ | 259.2–277.4 | L2 `G06` 9.1 · L1 `p048` 9.1 | the_hglobal: HGLOBAL was also charged; like every defendant who has not been convicted, it is presumed innocent. As of July 2018, the India-based call centers charged had yet to be arraigned; as of November 2020, the Justice Department said charges remained pending for other India-based defendants. |
| S030 (P05) | ◐ | 277.4–284.7 | L1 `p049` 3.7 · L1 `p050` 3.7 |  |
| S031 (P05) | ◐ | 284.7–292.9 | L1 `p051` 2.7 · L1 `p049:2` 2.7 · L1 `p052` 2.7 |  |
| S032 (P05) | ◐ | 292.9–299.1 | L3 `Q01` 3.6 · L1 `p046:2` 2.6 |  |
| S033 (P05) | CHUNG | 299.1–304.1 | L3 `Q01` 2.5 · L1 `p053` 2.5 |  |
| S034 (P06) | ●T | 305.6–317.2 | L2 `G07` 4.8 · L1 `p054` 3.4 · L1 `p055` 3.4 |  |
| S035 (P06) | ●T | 317.2–330.8 | veo `K3` 7.4 · L2 `G07` 6.2 |  |
| S036 (P06) | ◐ | 330.8–338.9 | L2 `G07` 2.7 · L1 `p056` 2.7 · L1 `p057` 2.7 |  |
| S037 (P06) | ◐ | 338.9–351.3 | L3 `T03` 5.3 · L1 `p058` 3.5 · L1 `p059` 3.5 |  |
| S038 (P06) | ◐ | 351.3–365.2 | L3 `T04` 4.6 · L2 `G08` 9.3 |  |
| S039 (P06) | ◐ | 365.2–376.8 | L2 `G08` 3.9 · L1 `p060` 3.9 · L1 `p061` 3.9 |  |
| S040 (P06) | ●N | 376.8–386.5 | L1 `p062` 3.2 · L2 `G07` 3.2 · L1 `p063` 3.2 |  |
| S041 (P06) | CHUNG | 386.5–409.3 | L2 `G09` 13.7 · L1 `p064` 4.6 · L1 `p065` 4.6 | chu: Framework used by this channel — not the indictment's words |
| S042 (P06) | CHUNG | 409.3–417.5 | L1 `p066` 4.1 · L1 `p010:2` 4.1 |  |
| S043 (P07) | ●N | 419.0–435.6 | L1 `p067` 4.8 · L2 `G10` 7.1 · L1 `p068` 4.8 |  |
| S044 (P07) | ●N | 435.6–447.6 | L2 `G10` 6.0 · L1 `p069` 6.0 |  |
| S045 (P07) | ●N | 447.6–455.4 | L2 `G10` 4.2 · L1 `p070` 3.5 |  |
| S046 (P07) | ◐ | 455.4–468.9 | L1 `p071` 4.5 · L2 `G11` 4.5 · L1 `p072` 4.5 |  |
| S047 (P07) | ●T | 468.9–484.8 | L1 `p008:2` 5.3 · L2 `G11` 5.3 · L1 `p073` 5.3 |  |
| S048 (P07) | TT | 484.8–493.7 | L1 `p074` 2.7 · veo `K4` 3.5 · L1 `p075` 2.7 |  |
| S049 (P08) | TT | 495.2–500.6 | L1 `p076` 1.8 · L2 `G11` 1.8 · L1 `p077` 1.8 |  |
| S050 (P08) | TT | 500.6–507.2 | L2 `G11` 2.2 · L1 `p074:2` 2.2 · L1 `p078` 2.2 |  |
| S051 (P09) | ● | 508.7–521.8 | L1 `p079` 4.1 · L2 `G11` 4.9 · L1 `p080` 4.1 |  |
| S052 (P09) | ● | 521.8–524.9 | L1 `p081` 1.5 · L1 `p079:2` 1.5 |  |
| S053 (P09) | ●T | 524.9–538.9 | L2 `G12` 9.3 · L1 `p082` 4.6 |  |
| S054 (P10) | ● | 540.4–548.5 | L1 `p081:2` 2.4 · L2 `G11` 3.3 · L1 `p083` 2.4 |  |
| S055 (P10) | ● | 548.5–555.5 | L2 `G12` 3.8 · L1 `p084` 3.2 |  |
| S056 (P10) | ◐ | 555.5–564.8 | L1 `p085` 3.1 · L1 `p071:2` 3.1 · L1 `p044:2` 3.1 |  |
| S057 (P11) | CHUNG | 566.3–572.5 | L1 `p086` 2.1 · L2 `G13` 2.1 · L1 `p087` 2.1 | tieu_de: 3 LESSONS · 5 RED FLAGS · 1 RULE |
| S058 (P11) | ◐ | 572.5–586.8 | L1 `p035:2` 4.8 · L2 `G05` 4.8 · L1 `p088` 4.8 | bai: LESSON 1 · The scary call was the front of a chain |
| S059 (P11) | ●T | 586.8–609.6 | L1 `p054:2` 7.6 · L2 `G07` 7.6 · L1 `p066:2` 7.6 | bai: LESSON 2 · Cards & wires = money cashed out fast |
| S060 (P11) | CHUNG | 609.6–639.4 | L1 `p089` 7.8 · L2 `G13` 14.1 · L1 `p090` 7.8 | bai: LESSON 3 · The IRS mostly starts with mail |
| S061 (P11) | CHUNG | 639.4–648.3 | L3 `Q02` 5.3 · L1 `p020:2` 3.6 |  |
| S062 (P11) | ●T | 648.3–659.5 | L2 `G14` 3.7 · L1 `p002:2` 3.7 · L1 `p091` 3.7 |  |
| S063 (P11) | ◐ | 659.5–672.3 | L2 `G14` 4.3 · L1 `p092` 4.3 · L1 `p093` 4.3 |  |
| S064 (P11) | ●T | 672.3–683.5 | L2 `G14` 3.7 · L1 `p056:2` 3.7 · L1 `p094` 3.7 |  |
| S065 (P11) | ◐ | 683.5–690.5 | L2 `G14` 2.3 · L1 `p014:2` 2.3 · L1 `p095` 2.3 |  |
| S066 (P11) | ◐ | 690.5–699.0 | L2 `G14` 2.8 · L1 `p025:2` 2.8 · L1 `p096` 2.8 |  |
| S067 (P11) (thẻ, không đọc) | KBCB | 699.0–703.0 | L1 `p004:2` 4.0 | kbcb: The IRS and USCIS had nothing to do with these calls. The callers were impersonating them. |
| S068 (P11) | CHUNG | 703.0–713.1 | veo `K5` 4.0 · L1 `p097` 3.0 · L1 `p098` 3.0 | bai: 1 RULE · Hang up. Look the agency up yourself. |
| S069 (P11) | ◐ | 713.1–724.7 | L1 `p099` 3.9 · L1 `p100` 3.9 · L1 `p101` 3.9 |  |
| S070 (P11) | CHUNG | 724.7–738.3 | L2 `G15` 8.1 · L1 `p102` 5.4 |  |
| S071 (P11) | CHUNG | 738.3–744.8 | L2 `G15` 3.3 · L1 `p103` 3.3 |  |
| KET | — | 744.8–752.8 | L2 `G16` thẻ tổng kết nền tối (3 + 5 + 1 dòng của SHOT.md §3, giữ nguyên chữ đã duyệt) + tigta.gov · reportfraud.ftc.gov + dòng khai AI; giữ 8 s | |
| NGUON | — | 752.8–772.8 | L2 `G17` danh sách nguồn chạy chữ (N1–N5, N9–N11) + dòng khai AI (HIEN-CHUONG §6) | |

## 2. Đồ hoạ động L2 (15 đồ hoạ; mã, 0 USD — khuôn `scripts/mr6/l2.py`; PHONG-CACH-HINH §2: hiện dần theo mốc từ, hạt tiền, số đếm, một điểm nhấn đỏ cam)

| Mã | Câu hỏi đồ hoạ trả lời | Hiện dần (theo lời) | Điểm nhấn duy nhất | Câu | Nhãn tầng |
|---|---|---|---|---|---|
| G01 | Người gọi doạ điều gì, và đòi gì? | Bốn icon nét mảnh bật lần lượt theo lời: ARREST · PRISON · FINES · DEPORTATION → mũi tên hội tụ vào ô "PAY" | ô PAY (đỏ cam, nhịp đập nhẹ) | S002 | ● · admitted in plea, per DOJ |
| G02 | Ai, ở đâu, và kết cục ra sao? | Bản đồ phẳng: chấm "Ahmedabad, India" → cung nét đứt sang "United States" (hạt chạy) → thẻ tên chữ → bộ đếm 0 → 20 YEARS | 20 YEARS đếm lên, dừng có vạch sáng | S004, S006 | S004 ● · per DOJ; S006 ● CONVICTED |
| G03 | Vụ án được mở ra thế nào, quy mô bao nhiêu? | Trục: Oct. 19, 2016 indictment → Oct. 27 unsealed: bộ đếm 61 defendants → tách hai cột "U.S.: 20 arrested" / "India: 32 people + 5 call centers charged" → ô mờ viền đứt "Alleged at the time: tens of thousands of victims · hundreds of millions of dollars" | số 61 đếm lên | S012, S013, S014, S015 | TT; S015 ◐ ALLEGED |
| G04 | Bốn kiểu cuộc gọi có điểm chung gì? | Bốn thẻ hiện theo lời: IRS impersonation · Immigration impersonation · "payday loan" · "government grant" → cả bốn đổ vào ô "PAY FIRST" → mũi tên trả về rỗng "nothing in return"; S020 thêm hai thẻ chữ trơn "Canada tax agency" · "Australian tax office" · "debt collection" | ô PAY FIRST | S017, S018, S019, S020 | ◐ ALLEGED (S020 per DOJ) |
| G05 | Sau cuộc gọi là ai — một người hay một dây chuyền? | Sơ đồ dây chuyền icon (không người, không tên): DATA BROKERS → CALLERS → CALL CENTER OPERATORS → PAYMENT PROCESSORS → RUNNERS (U.S.) ← DOMESTIC MANAGERS; nhánh HAWALADAR; hạt tiền chạy từ nạn nhân qua chuỗi | RUNNERS (U.S.) — chỗ tiền ra khỏi hệ thống | S023, S024, S025, S026, S058 | ◐ ALLEGED · Superseding Indictment pp. 4–6 |
| G06 | Một call center hay cả một mạng lưới? | Bản đồ Ahmedabad phẳng, 5 chấm KHÔNG tên nối nhau (shared scripts · lists · payments, hạt chạy qua lại) → S028 một chấm sáng; ô chữ tên kèm nguyên câu ◐ cùng khung: HGLOBAL was also charged; like every defendant who has not been convicted, it is presumed innocent. As of July 2018, the India-based call centers charged had yet to be arraigned; as of November 2020, the Justice Department said charges remained pending for other India-based defendants. | đường nối giữa 5 chấm | S027, S028, S029 | S027 ◐; S028 ● PATEL — admitted in plea, per DOJ; S029 ◐ ALLEGED |
| G07 | Tiền rời nạn nhân bằng cách nào, và nhanh cỡ nào? | Dòng hạt: VICTIM → "prepaid card / wire" → CALL CENTER báo → RUNNERS (U.S.) toả nhiều nhánh → "cashed out & laundered"; đồng hồ nhỏ chạy rất nhanh chữ "immediately" | đồng hồ "immediately" | S034, S035, S036, S040, S059 | ● · admitted in plea, per DOJ; S036 ◐; S040 ● U.S. co-defendants |
| G08 | Hawala "chuyển" tiền mà không chuyển tiền thế nào? | Hai người môi giới icon ở hai nước: tiền vào môi giới 1 → môi giới 2 trả ra ở nước kia; giữa hai nước mũi tên tiền thẳng bị gạch ("no money crosses") → sau đó giao dịch ngược chiều bù trừ (hai mũi tên ngược). Mức khái niệm, không thao tác | vạch gạch đỏ cam trên đường biên — tiền không đi qua | S038, S039 | ◐ ALLEGED · Superseding Indictment p. 6 ¶2(g) |
| G09 | Vì sao tiền rất khó lần lại? | Hai bước của kênh: 1 PLACEMENT — hạt đi vào "system" (cards, wires) → 2 LAYERING — hạt tách qua nhiều tay, đổi hình, dấu vết mờ dần; dòng nhỏ "Framework used by this channel — not the indictment's words" | dấu vết mờ dần ở bước 2 | S041 | CHUNG |
| G10 | Phía Mỹ của vụ kết thúc ra sao? | Lưới 24 ô trống lấp đầy dần (không tên, không mặt) → 3 bang chữ "Texas · Arizona · Georgia" → thang án "probation → 20 years" → "Restitution: $8,970,396 (joint and several, 22 defendants)" đếm | lưới 24 ô đầy | S043, S044, S045 | ● CONVICTED · U.S. co-defendants |
| G11 | Người đứng sau bị bắt và xét xử theo đường nào? | Trục: July 2018 (24 sentenced, ô của ông trống) → Sept. 2018 Singapore provisional arrest → Apr. 2019 extradition → Jan. 9, 2020 pleaded guilty (2 conspiracies) → Nov. 30, 2020 sentence; bản đồ India → Singapore → United States | mốc Sept. 2018 Singapore | S046, S047, S049, S050, S051, S054 | TT; ● CONVICTED |
| G12 | "Thiệt hại thừa nhận" khác "bồi hoàn" thế nào? | Thanh khoảng "loss attributable (admitted): > $25M and < $65M" (vùng mờ giữa hai vạch) → thanh riêng "Restitution ordered: $8,970,396 to identified victims" đếm; hai số ghi đúng chữ hồ sơ, không suy luận | khoảng $25M–$65M | S053, S055 | S053 ● · admitted, per DOJ; S055 ● CONVICTED |
| G13 | IRS thật liên lạc thế nào — khác cuộc gọi ra sao? | Chia đôi "The calls" vs "The real IRS (per IRS)": regular mail ✓ · no call demanding immediate payment by prepaid card/gift card/wire · chance to question or appeal ✓ · no threat of police/immigration arrest; nửa phải hiện sau | dòng "does not call to demand immediate payment" | S057, S060 | Source: IRS FS-2017-7 |
| G14 | Năm dấu hiệu là gì? | 5 thẻ RED FLAG lật lần lượt, mỗi thẻ gọi lại icon của đồ hoạ trước (G01 doạ · đồng hồ · thẻ trắng · lịch 20 ô · phí trước) | số thứ tự thẻ đang đọc | S062, S063, S064, S065, S066 | theo từng câu |
| G15 | Báo ở đâu? | Thẻ nơi báo: "Report IRS impersonation: tigta.gov" · "Report scams: reportfraud.ftc.gov" + dòng "case facts from public records — see description" | tigta.gov | S070, S071 | CHUNG |

## 3. Hồ sơ thật L3 (nền ngà B1; crop trang giữ nguyên dạng, khoanh câu; thẻ trích nguyên văn có dòng nguồn)

| Mã | Tệp · trang / nguồn | Vùng | Khoanh / chữ | Câu | Ghi chú |
|---|---|---|---|---|---|
| T01 | `ho-so/irs-callcenter-patel/cao-trang-thay-the-4-16-cr-385-doc6-2016-10-19.pdf` tr. 3 (N1, PDF quét) | đầu trang "SUPERSEDING INDICTMENT / General Allegations" + ¶1 a (tới "immediately.") | impersonated U.S. Internal Revenue Service (IRS) officers | S017 | Tiêu đề: SUPERSEDING INDICTMENT · U.S. v. PATEL et al. · No. 4:16-cr-385 (S.D. Tex.) · Dkt. 6 · p. 3; vùng đo bằng ảnh trang ở M-d (PDF không có lớp chữ) |
| T02 | như T01, tr. 3 | ¶1 b (USCIS scam) | would be deported unless they paid a fine immediately | S018 | Không lấy ¶1 c–d (không cần) |
| T03 | như T01, tr. 6 | ¶2 g từ "g. Hawaladar" tới "…leaving a record of the transaction." — **cắt trên** ¶2 f, **cắt dưới** trước câu "In a hawala system…" | without actually moving it | S037 | Không lấy ¶2 f (thao tác dữ liệu, NGUON §4 cấm) và ¶3 (tên 5 nhóm call center) |
| T04 | như T01, tr. 6 | ¶2 g câu cuối "The first hawaladar then owes … reverse direction." | repaid by transactions conducted in the reverse direction | S038 | Cắt dưới trước "Call Centers" / ¶3 |
| Q01 | N4 đ.8 (DOJ Press Release 20-19, Jan. 9, 2020) | thẻ trích nền ngà | “the top person in India and the boss for whom most of the other defendants worked” — a co-defendant, according to the Justice Department | S032, S033 | Chữ = `chu` S032 nguyên văn; S033 thêm dòng "A co-defendant's description — not a court finding" |
| Q02 | N2 đ.5 (DOJ Press Release 16-1257, Oct. 27, 2016) | thẻ trích nền ngà | “U.S. government agencies do not make these types of calls” — Homeland Security Investigations, Oct. 27, 2016 | S061 | Chữ = `chu` S061 nguyên văn; không logo HSI |

Trang/vùng cấm (NGUON.md §4): N1 tr. 1 (tên d.b.a.; danh sách bị cáo chưa xử), N1 tr. 7 (bảng tên bị cáo — tên call center chỉ dựng ô chữ kèm câu ◐), N1 tr. 4–6 ¶2(a), (e), (f), mọi trang có tên người chưa xử, ảnh chụp thông cáo N2 đ.11–12 và N3 đ.14.

## 4. Khoảnh khắc ảnh→clip (Veo 3.1 Lite, 5 ≤ 5; khung đầu = tranh L1 KHÔNG người — BAI-HOC tập 1 mục 2)

| Mã | Khung đầu (tranh) | Chuyển động (lời Veo khẳng định, mô tả cái có trong khung) | Neo cuối | Câu | Rủi ro / QC |
|---|---|---|---|---|---|
| K1 | `p001` — A smartphone lying face-up on a wooden kitchen table at dusk, its screen dark, a mug besid… | The phone on the kitchen table lights up: its screen becomes a soft glowing blank white rectangle that pulses gently; dusk light shifts slowly on the table. | The table with only the glowing phone and the mug. | S001 | Màn hình phải trơn (không số, không chữ, không giao diện cuộc gọi) |
| K2 | `p035` — Night interior of a long open-plan office with rows of empty desks, headsets resting on th… | Slow lateral dolly along the long dark office: rows of empty desks, headsets resting on them, every monitor a soft blank white glow; the room is still. | Empty desks and glowing blank monitors. | S022 | Không biển hiệu, không chữ trên màn hình; không bóng người |
| K3 | `p054` — Plain white plastic cards fanned on a dark glass counter under one warm lamp; completely b… | A single blank white plastic card slides slowly across the dark glass counter and stops; warm lamp reflections; macro. | The counter holding only the blank cards. | S035 | Thẻ phải trắng trơn (không số, không chip, không logo) |
| K4 | `p074` — Clouds seen from above at sunset through an airplane window, the wing plain white with no … | View through an airplane window: the plain white wing over a sea of clouds, slow drift, warm sunset light rising. | Wing and clouds only. | S048 | Không logo hãng trên cánh |
| K5 | `p086` — Morning light falling across the same kitchen table, a phone lying face-down, a closed not… | Morning light slowly brightens across the kitchen table; the face-down phone and the mug stay still; a curtain moves softly. | The table with the face-down phone in full morning light; nobody present. | S068 | Không thêm người; không lật điện thoại |

QC mỗi clip (M-c): không người/mặt, không chữ/số/logo mọc ra (V5/V8, bài học tập 1: chữ giả mọc trên vật có chữ), chuyển động không méo; ≤ 2 lượt/khe, lượt 2 đổi lời (V7); hỏng 2 lượt → dùng tranh tĩnh có đẩy/kéo (0 USD, KHÔNG phải vá sau 402 — 402 thì DỪNG).

## 5. Danh sách tranh L1 (103 tranh mới; lời sinh = tiền tố/hậu tố tờ A `reports/mrp1/A/PHONG-CACH.md` + mô tả dưới)

| Mã | Loại | Mô tả cảnh (EN, gốc lời sinh) | Dùng ở |
|---|---|---|---|
| p001 | E | A smartphone lying face-up on a wooden kitchen table at dusk, its screen dark, a mug beside it, warm window light; nobody present. | S001 |
| p002 | N1 | The listener (N1) at a warm wooden kitchen table at dusk, holding a phone to his ear, worried; the phone is dark, nothing on it. | S002, S062 |
| p003 | N1 | Close-up of the listener's (N1) hand gripping the edge of the kitchen table, knuckles tense, the dark phone beside it. | S002 |
| p004 | E | A quiet kitchen table at dusk with a phone lying face-down beside a mug; warm window light; nobody present. | S003, S067 |
| p005 | E | A front door seen from inside a quiet home at dusk, closed and locked, a small lamp lit on a side table; nobody present. | S003 |
| p006 | R | A long dim office at night seen from the back of the room: rows of desks with distant workers as soft dark silhouettes against glowing blank screens; no faces. | S004, S008 |
| p007 | E | A tall office tower at night in a hazy generic city, many lit windows, no signs or lettering. | S004 |
| p008 | R | A man seen strictly from behind, a dark silhouette in a plain light shirt standing at a tall window over a hazy night city with no landmarks; no face. | S005, S047 |
| p009 | E | A long empty prison corridor drawn in soft muted light, rows of closed plain doors; nobody present. | S006 |
| p010 | E | Symbolic still life: a dark phone on the left and a small stack of plain banknotes with no markings on the right, a thin glowing thread linking them across a dark table. | S007, S042 |
| p011 | E | Night aerial of a generic coastline with a faint dotted arc of light crossing the ocean toward another shore; no landmarks. | S007 |
| p012 | E | A single banknote shape made of light dissolving into particles over a dark table; symbolic, no markings. | S007 |
| p013 | E | An open notebook with a red pencil and three blank lines circled, warm desk lamp; symbolic of red flags. | S008 |
| p014 | E | An empty armchair beside a side table with a landline-style phone and a sheet of blank white paper, late afternoon light, nobody present. | S009, S065 |
| p015 | E | A plain wall calendar with blank squares, no numbers, one square softly lit. | S009, S010 |
| p016 | E | A pair of reading glasses resting on a folded blank sheet of paper on a small table, lamp light. | S009 |
| p017 | E | A kitchen table seen over many days: a phone on the table at morning, noon and night, light changing, nobody present. | S010 |
| p018 | E | A kitchen window at night with rain streaks, a phone glowing faintly on the sill; nobody present. | S010 |
| p019 | E | A quiet hallway with an empty coat hook and a small table holding a face-down phone; soft evening light. | S011 |
| p020 | E | Wide shot of empty stone steps and tall classical columns at dawn, plain stone façade with no lettering, nobody present. | S012, S061 |
| p021 | E | A dark wooden jury room with twelve empty chairs around a long table, soft morning light. | S012 |
| p022 | E | A heavy closed binder bound with a plain ribbon on a table, light falling on it; no text. | S013 |
| p023 | E | Two clocks on a dark wall showing different times, symbolic of two countries, plain faces with no numbers. | S014 |
| p024 | E | A row of plain metal handrails and empty waiting benches in a government building lobby at dawn, no signs. | S014 |
| p025 | E | Thousands of tiny paper slips drifting down through a beam of light in a dark room; symbolic, blank paper. | S015, S066 |
| p026 | E | An aerial view at night of a vast suburban grid with countless lit windows; symbolic of many households, no landmarks. | S015 |
| p027 | E | An open binder with blank white tabbed dividers on a dark desk under a lamp; pages blank. | S016, S021 |
| p028 | E | An old desk phone with its receiver off the hook resting on a stack of blank paper, cold light. | S017 |
| p029 | E | A plain folder of blank forms on a kitchen table beside reading glasses, afternoon light; no text. | S018 |
| p030 | E | An empty envelope lying open on a table, nothing inside, cold light. | S019 |
| p031 | E | A small cash box lying open and empty on a dark table under a lamp. | S019 |
| p032 | E | A globe on a dark desk slowly lit along three distant regions by a thin lamp beam; no labels on the globe. | S020 |
| p033 | E | Three plain paper files fanned on a dark desk, each a different muted color, no labels. | S020 |
| p034 | E | A closed office door with frosted glass and no lettering, light behind it, a quiet corridor. | S021 |
| p035 | E | Night interior of a long open-plan office with rows of empty desks, headsets resting on them, every monitor a soft blank white glow; nobody present. | S022, S058 |
| p036 | R | Close-up of hands on a keyboard beside a headset on a desk, lit by a blank glowing screen; only hands and sleeves. | S023 |
| p037 | E | A stack of plain printed lists with every line blurred and unreadable, beside a headset on a desk. | S023 |
| p038 | E | An empty manager's glass office overlooking a dim open-plan floor at night, a desk lamp on, nobody present. | S024 |
| p039 | R | Silhouettes of a few distant people standing in a dim office doorway, backlit, seen from behind; no faces. | S024 |
| p040 | E | Rows of plain unlabeled file boxes on metal shelves in a dim storeroom, one box open with blank index cards. | S025 |
| p041 | R | Hands in a plain jacket sleeve counting plain unmarked banknotes on a car seat at night, street light through the window; only hands. | S025 |
| p042 | E | Two plain ledgers on two separate desks in two different rooms, each lit by one lamp; symbolic of two distant brokers. | S026 |
| p043 | E | An old brass weighing scale balanced on a desk, both pans empty, warm lamp. | S026 |
| p044 | E | A night skyline of a generic large city seen from far away, warm haze, no landmarks or signs. | S027, S056 |
| p045 | E | Five small lamps on a dark table connected by thin glowing threads; symbolic network, no labels. | S027 |
| p046 | R | A man seen strictly from behind at a desk at night, a dark silhouette in a plain light shirt reviewing blank papers; no face. | S028, S032 |
| p047 | E | A leather office chair turned away from the camera at a large desk at night, the room empty. | S028 |
| p048 | E | A dark empty corridor with five closed plain doors in a row, soft light under each; no signs. | S029 |
| p049 | E | A plain organization chart drawn as empty boxes and lines on a whiteboard, no writing, cold office light. | S030, S031 |
| p050 | E | A plain index card pinned to a corkboard, the writing on it blurred and unreadable, desk lamp. | S030 |
| p051 | E | A laptop on a dark desk showing a soft blank white glow, a stack of blank monthly reports beside it. | S031 |
| p052 | E | An email inbox suggested only as a soft glowing blank rectangle on a monitor in a dark room, a coffee cup beside it. | S031 |
| p053 | E | A scale of justice made of simple brass on a shelf, slightly out of focus, warm light. | S033 |
| p054 | E | Plain white plastic cards fanned on a dark glass counter under one warm lamp; completely blank cards. | S034, S059 |
| p055 | E | A shop counter at night with a display rack of plain blank cards, lights dimmed, nobody present. | S034 |
| p056 | E | A thick stack of blank index cards held by a rubber band on a dark desk, symbolic of personal records, nothing written. | S036, S064 |
| p057 | E | A row of blank identity-style cards laid face-down on a dark table, cold light; no faces, no text. | S036 |
| p058 | E | An old wooden desk with a closed notebook and a single brass key, warm lamp light; a quiet back room. | S037 |
| p059 | E | Two distant city skylines at dusk on either side of a dark sea, no landmarks; symbolic of two countries. | S037 |
| p060 | E | A bank lobby at closing time, empty counters, soft light, no signage. | S039 |
| p061 | E | A plain bank deposit envelope sealed on a counter, nothing written on it, cool light. | S039 |
| p062 | R | Several pairs of hands passing a plain envelope quickly from one to the next across a dark car hood at night; only hands and sleeves. | S040 |
| p063 | E | A car parked under a single streetlight at night on an empty street, engine running, exhaust in the cold air; nobody visible. | S040 |
| p064 | E | A glass of clear water with a drop of ink spreading and fading until it disappears; symbolic of layering. | S041 |
| p065 | E | A maze of narrow paper corridors seen from above, a single coin lost inside; symbolic. | S041 |
| p066 | E | Footprints in wet sand fading as a wave washes over them at dusk; symbolic of a trail disappearing. | S042, S059 |
| p067 | E | A long empty federal courthouse corridor with polished floor and wooden benches, morning light, no signs. | S043 |
| p068 | E | A wooden gavel and block on a bench under soft courtroom light, nobody present. | S043 |
| p069 | R | Silhouettes of several people seated on a courtroom bench seen from the back row; heads and shoulders only as dark shapes. | S044 |
| p070 | E | Neat stacks of plain envelopes being sorted into slots on a wall, no addresses; symbolic of restitution to victims. | S045 |
| p071 | E | An empty chair at a defense table in a quiet courtroom, papers blank; soft light. | S046, S056 |
| p072 | E | A map table with a lamp lighting only one region, the rest in shadow; no labels, symbolic of the India side. | S046 |
| p073 | E | A calendar page turning in the wind on an empty desk by an open window, no numbers visible. | S047 |
| p074 | E | Clouds seen from above at sunset through an airplane window, the wing plain white with no markings; nobody present. | S048, S050 |
| p075 | E | A boarding gate at night seen through glass, an aircraft waiting, no logos or signs. | S048 |
| p076 | E | An airport terminal corridor at night, glass walls, rows of empty seats, no signs or text. | S049 |
| p077 | E | A pair of plain metal gates opening in an airport corridor at night, empty. | S049 |
| p078 | E | A government jet stair on a quiet tarmac at dawn, no markings; nobody present. | S050 |
| p079 | E | An empty wood-paneled courtroom in soft morning light, plain wooden walls and benches, dust drifting in a sunbeam. | S051, S052 |
| p080 | E | A pen resting on a single blank signature line on a white page, soft morning light. | S051 |
| p081 | E | A judge's bench seen from the empty gallery, a gavel resting on its block, nobody present. | S052, S054 |
| p082 | E | A long measuring tape stretched across a dark table between two weights; symbolic of a range. | S053 |
| p083 | E | A heavy wooden door to a courtroom closing slowly, light slicing through; nobody present. | S054 |
| p084 | E | Plain envelopes arranged in neat rows on a table under warm light, symbolic of payments to victims. | S055 |
| p085 | E | A dark map table with three unlit desk lamps, one switched off; symbolic of open cases still pending. | S056 |
| p086 | E | Morning light falling across the same kitchen table, a phone lying face-down, a closed notebook and pen; calm, nobody present. | S057 |
| p087 | N1 | The listener (N1) sitting at the morning kitchen table, reading a plain blank booklet, calm. | S057 |
| p088 | E | A long chain of paper links stretching from a phone into darkness on a table; symbolic of a chain behind a call. | S058 |
| p089 | E | A mailbox at the end of a quiet driveway in morning light holding a single plain white envelope; no address or text. | S060 |
| p090 | N1 | The listener (N1) holding a plain white envelope at the mailbox in morning light, curious, relaxed. | S060 |
| p091 | E | A heavy closed door with a small barred window at the end of a dim corridor, nobody present; symbolic threat of arrest. | S062 |
| p092 | E | A kitchen timer on a counter ticking, close-up, warm light. | S063 |
| p093 | E | An hourglass with sand pouring fast on a kitchen counter, warm light; symbolic pressure. | S063 |
| p094 | E | A gift-shop rack of plain blank cards in soft light, slightly out of focus, nobody present. | S064 |
| p095 | N1 | The listener (N1) looking at the dark phone on the counter, deciding not to answer, evening light. | S065 |
| p096 | E | An envelope marked only with a simple open-hand outline, empty, on a table; symbolic of an upfront fee. | S066 |
| p097 | N1 | The listener (N1) at the kitchen table in morning light, calm, the phone face-down beside him; he writes on a blank notepad. | S068 |
| p098 | N1 | The listener (N1) looking up an official number in a plain blank printed directory, morning light. | S068 |
| p099 | N2 | The listener (N1) and his adult daughter (N2) talking at the kitchen table, warm afternoon light, a teapot between them. | S069 |
| p100 | N2 | Close-up of the daughter's (N2) hand resting on her father's (N1) hand on the table, reassuring. | S069 |
| p101 | N2 | The daughter (N2) and the listener (N1) laughing together while washing dishes, warm kitchen light. | S069 |
| p102 | E | A plain laptop on the kitchen table showing a soft blank white glow, a cup of tea beside it, morning light. | S070 |
| p103 | E | A tidy desk with a stack of plain bound records and a desk lamp, warm light, nobody present. | S071 |

## 6. Nhạc

Giữ bảng nhạc `SHOT.md` §4 (MR-K23): P00 nền điện tử trầm −24 dB · P04–P06 nhịp ~90 bpm "dây chuyền" −22 dB · S047–S048 tăng, **cắt lặng 1 s** sau S048 (khớp K4) · P08–P10 piano thấp −26 dB · P11 sáng hơn −24 dB. Không tiếng chuông điện thoại thật, còi, còng tay. Đỉnh nhạc ≤ −18 dB dưới lời.

## 7. Kiểm máy (scripts/mrs23/shot2.py)

- Mỗi câu 1–3 cảnh · mã cảnh tồn tại · ≥ 6 đồ hoạ L2 động có câu hỏi + một điểm nhấn · ≤ 5 Veo, khung đầu tranh loại E · tranh dùng ≤ 2 lần · cảnh tranh ≥ 1,5 s · tranh người thật có từ khoá bóng/lưng/tay, không mặt · từ cấm hình (biếm hoạ, quân phục/phù hiệu/logo/con dấu/cờ) · regex cấm của tập (`kiem_rieng.cam_them`) · KB/KC quét cả tệp này.
- Kết quả: **ĐẠT (0 lỗi)**
