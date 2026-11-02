# BẢNG SHOT 2 — Tập 3 · "Prince Charming" / Sunmola (`tap03-romance-sunmola`) · phong cách PHONG-CACH-HINH v1

> MR-S23 · 02/11/2026 · tiền kỳ (0 USD). **Thay `SHOT.md`** (giữ làm lịch sử) cho phần hình; lời đã duyệt G1 (02/11/2026 10:25) + quyết định KBCB áp ở MR-S23. Bảng **sinh máy** `python3 scripts/mrs23/shot2.py tap03` từ `scripts/mrs23/du_lieu_tap03.py` + `loi.json`; khuôn `docs/tap01-1inmm/SHOT2.md`.
> **Mốc là ƯỚC** (chưa có giọng): 155 từ/phút (đo thật MR-4), nghỉ 1.5 s đầu mỗi đoạn, thẻ chữ không đọc 4 s, thẻ tối riêng 6 s. Ở M-c/M-d thay bằng mốc whisper giọng thật (`scripts/mr6/moc_cau.py`) và chia lại thời lượng cảnh theo trọng số; cảnh tranh dài > 5 s tách thành 2 khung cắt/chuyển động của **cùng** tranh (không thêm tranh).
> Tổng ước **12:21** (lời + thẻ 11:53 · thẻ tổng kết 8 s · nguồn 20 s) · **207 cảnh** · L1 tranh 151 cảnh (465 s, TB 3.1 s) từ **144 tranh mới** (cảnh trống/vật 127 · người thật bóng/lưng/tay 4 · N1 11 · N2 2) · L2 46 cảnh (194 s) từ **17 đồ hoạ động** · L3 4 cảnh (12 s) · Veo ảnh→clip **5** khoảnh khắc (17 s) · thẻ tối 1 (6 s).
> Luật áp mọi cảnh: HIEN-CHUONG §4–§5; PHONG-CACH-HINH §1–§5; LUAT-VEO V1–V8 + BAI-HOC tập 1 mục 2; nhãn tầng + dòng nguồn lớp tĩnh góc dưới theo `loi.json`; nhãn ILLUSTRATIVE ở cảnh tranh đầu mỗi đoạn; không chữ trên hình ngoài lời đã duyệt, số liệu hồ sơ, nhãn, nguồn (M-d đối chiếu máy như `scripts/mr6/doi_chieu_chu.py`).
> **Riêng tập 3** (HIEN-CHUONG §5, MR-D23 K3): không hình hay mô tả nhạy cảm; không dựng tin nhắn đọc được, không giao diện trang hẹn hò/ứng dụng; màn hình = khối trắng mềm trơn; không quân phục, phù hiệu, cờ, huân chương; không tên giả bị cáo dùng, không tên trang hẹn hò, dịch vụ chuyển tiền; không bang/thành phố nạn nhân.
> **Nigeria / Nam Phi / London:** không cảnh định kiến (đồng hoang, thú, trang phục dân tộc); chỉ bản đồ phẳng tự vẽ (L2), nội thất trung tính, sân bay không biển hiệu.
> **P06 (S033):** chỉ thẻ tối nền mực `#1B1F24`, chữ ngà, 6 s, không tranh, không nhạc; không câu/cảnh nào khác gợi lại nhánh này (máy kiểm KC quét cả tệp này: ≤ 1 dòng).

## 0. Nhân vật và người trong hình

| Mã | Ai | Cách vẽ (cố định cả tập) | Được / không |
|---|---|---|---|
| N1 | Người phụ nữ (đại diện những người phụ nữ bị nhắm tới; KHÔNG phải nạn nhân cụ thể nào) | Phụ nữ ~50 tuổi tự nghĩ ra, tóc nâu thẳng ngang vai, khăn quàng hổ phách, áo len xám; căn hộ ấm, đèn bàn. Mặt cách điệu, thường ở góc nghiêng/sau lưng/tay; không gắn sắc tộc, không phóng đại nét | Được có mặt cách điệu, nhãn ILLUSTRATIVE. **Không** dùng cho câu về thiệt hại cá nhân cụ thể (S034 phá sản/mất nhà) — ở đó chỉ vật; không cảnh thân mật, không phòng ngủ |
| N2 | Người bạn (đại diện người tin cậy, chỉ ở P12) | Phụ nữ ~55 tuổi tự nghĩ ra, tóc bạc ngắn, áo khoác xanh teal; ngồi cạnh N1 | Được có mặt cách điệu, nhãn ILLUSTRATIVE |
| R | Sunmola (bị cáo ●) | Chỉ bóng ngược sáng, lưng, tay/tay áo trơn; trang phục trung tính; không quân phục; nhãn tên chỉ ở thẻ chữ | Không mặt, không góc 3/4 |
| R | Nhân vật giả mà Sunmola dựng ("soldier", "colonel") | **Không vẽ người**: khung hồ sơ trống (đường viền đầu-vai xám phẳng), dấu "?"; không quân phục, phù hiệu, cờ | Tránh giống những người đàn ông thật bị lấy ảnh (KBCB S016) |
| R | Những người đàn ông bị lấy ảnh; đồng phạm; điều tra viên; thẩm phán | Không vẽ; đồng phạm chỉ bóng xa/tay | Không mặt, không tên |
| R | Những người phụ nữ trong hồ sơ | Chỉ qua N1 (đại diện, tự nghĩ ra) hoặc đồ vật; không tuổi + hoàn cảnh + nơi ở ghép lại | KBCB — không nhận diện |

Tham chiếu nhất quán (PHONG-CACH-HINH §4): `ref_nv` = tranh đầu có N1 / N2 (chỉ gửi kèm cảnh có nhân vật đó); `ref_canh` = một tranh trống cùng nét (mọi cảnh khác; lời sinh ghi rõ nhân vật KHÔNG có trong cảnh).

## 1. Bảng cảnh

| Câu | Tầng | Mốc ước (s) | Cảnh: lớp · mã · thời lượng | Lớp chồng |
|---|---|---|---|---|
| S001 (P00) | MH | 1.5–9.6 | L1 `s001` 2.4 · veo `K1` 3.3 · L1 `s002` 2.4 |  |
| S002 (P00) | ●C | 9.6–18.9 | L1 `s003` 2.7 · L2 `G01` 3.8 · L1 `s004` 2.7 |  |
| S003 (P00) | ●C | 18.9–32.1 | L2 `G01` 4.9 · L1 `s005` 4.1 · L1 `s006` 4.1 |  |
| S004 (P00) | KBCB | 32.1–36.0 | L1 `s007` 3.9 | kbcb: The U.S. Army had nothing to do with either story. (đọc — chữ phụ đề) |
| S005 (P00) | ●C | 36.0–45.6 | L1 `s008` 3.2 · L1 `s009` 3.2 · L1 `s010` 3.2 | ten: Olayinka Sunmola · ● CONVICTED (2016 plea · 2017 sentence) |
| S006 (P00) | ◐ | 45.6–51.4 | L3 `Q01` 2.4 · L1 `s011` 1.7 · L1 `s012` 1.7 |  |
| S007 (P00) | ● | 51.4–58.8 | L2 `G02` 3.2 · L1 `s013` 2.1 · L1 `s014` 2.1 |  |
| S008 (P00) | ●C | 58.8–63.8 | L3 `Q02` 3.1 · L1 `s015` 1.9 |  |
| S009 (P00) | CHUNG | 63.8–71.2 | L1 `s016` 3.7 · L1 `s017` 3.7 | tieu_de: Real cases from the public record · MONEY REROUTE |
| S010 (P01) | ◐ | 72.7–86.2 | L1 `s018` 4.5 · L1 `s019` 4.5 · L1 `s020` 4.5 |  |
| S011 (P01) | ◐ | 86.2–97.8 | L2 `G03` 5.2 · L1 `s021` 3.2 · L1 `s022` 3.2 |  |
| S012 (P01) | ◐ | 97.8–105.6 | L2 `G03` 2.9 · L1 `s023` 2.4 · L1 `s024` 2.4 |  |
| S013 (P02) | ●C | 107.1–117.9 | L2 `G04` 3.6 · L1 `s025` 3.6 · L1 `s026` 3.6 |  |
| S014 (P02) | ●C | 117.9–129.9 | L1 `s003:2` 4.0 · L1 `s027` 4.0 · L2 `G04` 4.0 |  |
| S015 (P02) | ◐ | 129.9–136.1 | L1 `s028` 2.1 · L1 `s029` 2.1 · L1 `s030` 2.1 |  |
| S016 (P02) | KBCB | 136.1–143.1 | L1 `s031` 7.0 | kbcb: (đọc) Những người đàn ông bị lấy ảnh không có tên trong hồ sơ — không thẻ ảnh, không mặt |
| S017 (P02) (thẻ, không đọc) | KBCB | 143.1–147.1 | L1 `s032` 2.0 · L1 `s033` 2.0 | kbcb: The U.S. Army and the U.S. military had nothing to do with this scheme. |
| S018 (P03) | ◐ | 148.6–154.4 | L1 `s034` 1.9 · L1 `s035` 1.9 · L1 `s036` 1.9 |  |
| S019 (P03) | ◐ | 154.4–160.2 | L1 `s037` 1.9 · L1 `s038` 1.9 · L1 `s039` 1.9 |  |
| S020 (P04) | ●C | 161.7–170.6 | L1 `s040` 2.8 · L2 `G05` 3.3 · L1 `s041` 2.8 |  |
| S021 (P04) | ●C | 170.6–176.4 | L1 `s042` 1.9 · L2 `G05` 1.9 · L1 `s043` 1.9 |  |
| S022 (P04) | ●C | 176.4–192.7 | L2 `G05` 5.4 · L1 `s044` 5.4 · L1 `s045` 5.4 |  |
| S023 (P04) (thẻ, không đọc) | KBCB | 192.7–196.7 | L1 `s046` 4.0 | kbcb: The U.S. Army and the U.S. military had nothing to do with this scheme. |
| S024 (P04) | ◐ | 196.7–205.6 | L1 `s047` 2.7 · L1 `s048` 2.7 · veo `K2` 3.5 |  |
| S025 (P04) | ◐ | 205.6–218.0 | L2 `G06` 5.3 · L1 `s049` 3.5 · L1 `s050` 3.5 |  |
| S026 (P04) | ◐ | 218.0–221.0 | L2 `G06` 1.5 · L1 `s008:2` 1.5 |  |
| S027 (P04) | ◐ | 221.0–233.4 | L2 `G07` 5.5 · L1 `s051` 3.4 · L1 `s052` 3.4 |  |
| S028 (P05) | CHUNG | 234.9–241.1 | L1 `s053` 2.1 · L2 `G08` 2.1 · L1 `s054` 2.1 |  |
| S029 (P05) | ●C | 241.1–255.5 | L2 `G08` 6.4 · L1 `s055` 4.0 · L1 `s056` 4.0 |  |
| S030 (P05) | ●C | 255.5–262.4 | L2 `G08` 2.3 · L1 `s057` 2.3 · L1 `s058` 2.3 |  |
| S031 (P05) | ●C | 262.4–269.4 | L1 `s059` 2.3 · L1 `s060` 2.3 · L1 `s061` 2.3 |  |
| S032 (P05) | ◐ | 269.4–275.6 | L2 `G09` 2.7 · L1 `s062` 1.8 · L1 `s063` 1.8 |  |
| S033 (P06) (thẻ, không đọc) | ●C | 277.1–283.1 | TOI `thẻ tối` 6.0 | toi: nguyên văn câu S033 của loi.json trên nền mực #1B1F24, chữ ngà; 6 s; không tranh, không nhạc |
| S034 (P07) | ◐ | 284.6–296.6 | L1 `s064` 4.0 · L1 `s065` 4.0 · L1 `s066` 4.0 |  |
| S035 (P07) | ●C | 296.6–307.0 | L2 `G10` 4.6 · L1 `s067` 2.9 · L1 `s068` 2.9 |  |
| S036 (P07) | ●C | 307.0–318.3 | L2 `G10` 4.2 · L1 `s069` 3.5 · L1 `s070` 3.5 |  |
| S037 (P07) | CHUNG | 318.3–322.9 | L1 `s071` 2.3 · L1 `s072` 2.3 |  |
| S038 (P08) | TT | 324.4–338.0 | L2 `G11` 5.6 · L1 `s073` 4.0 · L1 `s074` 4.0 |  |
| S039 (P08) | TT | 338.0–343.4 | L2 `G11` 1.8 · L1 `s075` 1.8 · L1 `s076` 1.8 |  |
| S040 (P08) | ◐ | 343.4–348.8 | veo `K3` 2.1 · L1 `s075:2` 1.6 · L1 `s077` 1.6 |  |
| S041 (P08) | TT | 348.8–354.2 | L2 `G11` 1.8 · L1 `s078` 1.8 · L1 `s079` 1.8 |  |
| S042 (P08) | TT | 354.2–361.2 | L1 `s080` 2.3 · L2 `G11` 2.3 · L1 `s081` 2.3 |  |
| S043 (P09) | ● | 362.7–368.9 | veo `K4` 2.4 · L2 `G11` 1.9 · L1 `s082` 1.9 |  |
| S044 (P09) | ● | 368.9–376.2 | L1 `s083` 2.5 · L1 `s080:2` 2.5 · L1 `s084` 2.5 |  |
| S045 (P10) | TT | 377.7–380.0 | L1 `s085` 2.3 |  |
| S046 (P10) | TT | 380.0–387.8 | L1 `s086` 3.9 · L1 `s087` 3.9 |  |
| S047 (P10) | TT | 387.8–398.6 | L2 `G12` 4.1 · L1 `s088` 3.4 · L1 `s089` 3.4 |  |
| S048 (P10) | ●C | 398.6–413.3 | L2 `G12` 5.5 · L1 `s090` 4.6 · L1 `s091` 4.6 |  |
| S049 (P10) | ●C | 413.3–434.6 | L2 `G13` 21.3 |  |
| S050 (P10) | ● | 434.6–437.7 | L2 `G13` 3.1 |  |
| S051 (P10) | ● | 437.7–447.8 | L2 `G13` 3.4 · L1 `s092` 3.4 · L1 `s093` 3.4 |  |
| S052 (P10) | ◐ | 447.8–453.6 | L1 `s094` 2.9 · L1 `s095` 2.9 |  |
| S053 (P10) | ◐ | 453.6–466.4 | L1 `s096` 4.3 · L1 `s097` 4.3 · L1 `s098` 4.3 |  |
| S054 (P11) | ●C | 467.9–474.5 | L3 `T01` 3.8 · L3 `T04` 2.7 |  |
| S055 (P11) | ●C | 474.5–483.7 | L2 `G14` 4.1 · L1 `s099` 2.6 · L1 `s100` 2.6 |  |
| S056 (P11) | ●C | 483.7–495.0 | L1 `s101` 3.7 · L1 `s102` 3.7 · L1 `s103` 3.7 |  |
| S057 (P11) (thẻ, không đọc) | KBCB | 495.0–499.0 | L1 `s104` 2.0 · L1 `s105` 2.0 | kbcb: The U.S. Army and the U.S. military had nothing to do with this scheme. |
| S058 (P11) | ●C | 499.0–508.3 | L2 `G14` 3.1 · L1 `s106` 3.1 · L1 `s107` 3.1 |  |
| S059 (P11) | ●C | 508.3–520.3 | L2 `G14` 7.0 · L1 `s108` 5.0 |  |
| S060 (P11) | ●C | 520.3–531.1 | L1 `s109` 3.6 · L2 `G14` 3.6 · L1 `s110` 3.6 |  |
| S061 (P11) | ●C | 531.1–541.2 | L1 `s111` 5.0 · L1 `s112` 5.0 |  |
| S062 (P11) | ●C | 541.2–547.0 | L1 `s017:2` 1.9 · L1 `s113` 1.9 · L1 `s114` 1.9 |  |
| S063 (P11) | CHUNG | 547.0–550.1 | L1 `s115` 1.5 · L1 `s116` 1.5 |  |
| S063b (P11) | ●C | 550.1–555.9 | L1 `s117` 2.9 · L1 `s118` 2.9 |  |
| S064 (P11) | TT | 555.9–564.8 | L1 `s119` 3.0 · L1 `s120` 3.0 · L1 `s121` 3.0 |  |
| S065 (P12) | CHUNG | 566.3–572.5 | L1 `s122` 3.1 · L2 `G15` 3.1 | tieu_de: 3 LESSONS · 5 RED FLAGS · 1 RULE |
| S066 (P12) | ●C | 572.5–588.3 | L2 `G08` 5.3 · L1 `s123` 5.3 · L2 `G15` 5.3 |  |
| S067 (P12) | ●C | 588.3–603.4 | L2 `G15` 5.0 · L1 `s034:2` 5.0 · L1 `s124` 5.0 |  |
| S068 (P12) | CHUNG | 603.4–610.8 | L2 `G15` 2.5 · L1 `s125` 2.5 · L1 `s126` 2.5 |  |
| S069 (P12) | ●C | 610.8–624.3 | L2 `G15` 4.5 · L1 `s042:2` 4.5 · L1 `s127` 4.5 |  |
| S070 (P12) | CHUNG | 624.3–629.0 | L1 `s128` 1.5 · L2 `G15` 1.5 · L1 `s129` 1.5 |  |
| S071 (P12) | ●C | 629.0–639.8 | L2 `G16` 5.4 · L1 `s130` 5.4 |  |
| S072 (P12) (thẻ, không đọc) | KBCB | 639.8–643.8 | L1 `s131` 2.0 · L1 `s132` 2.0 | kbcb: The U.S. Army and the U.S. military had nothing to do with this scheme. |
| S073 (P12) | ●C | 643.8–649.2 | L2 `G16` 2.7 · L1 `s133` 2.7 |  |
| S074 (P12) | ◐ | 649.2–658.1 | L2 `G16` 3.0 · L1 `s134` 3.0 · L1 `s135` 3.0 |  |
| S075 (P12) | ◐ | 658.1–665.9 | L2 `G16` 3.9 · L1 `s136` 3.9 |  |
| S076 (P12) | ◐ | 665.9–682.9 | L2 `G16` 5.7 · L1 `s137` 5.7 · L1 `s138` 5.7 |  |
| S077 (P12) | CHUNG | 682.9–696.1 | veo `K5` 5.2 · L1 `s139` 4.0 · L1 `s140` 4.0 | bai: 1 RULE · Never send money to someone you meet online. |
| S078 (P12) | CHUNG | 696.1–706.5 | L2 `G17` 4.6 · L1 `s141` 2.9 · L1 `s142` 2.9 |  |
| S079 (P12) | CHUNG | 706.5–713.1 | L1 `s143` 3.3 · L1 `s144` 3.3 |  |
| KET | — | 713.1–721.1 | L2 `G18` thẻ tổng kết nền tối (3 + 5 + 1 dòng của SHOT.md §3, giữ nguyên chữ đã duyệt) + ic3.gov · reportfraud.ftc.gov + dòng khai AI; giữ 8 s | |
| NGUON | — | 721.1–741.1 | L2 `G19` danh sách nguồn chạy chữ (N1–N3, N6–N8) + dòng khai AI (HIEN-CHUONG §6) | |

## 2. Đồ hoạ động L2 (17 đồ hoạ; mã, 0 USD — khuôn `scripts/mr6/l2.py`; PHONG-CACH-HINH §2: hiện dần theo mốc từ, hạt tiền, số đếm, một điểm nhấn đỏ cam)

| Mã | Câu hỏi đồ hoạ trả lời | Hiện dần (theo lời) | Điểm nhấn duy nhất | Câu | Nhãn tầng |
|---|---|---|---|---|---|
| G01 | Hắn tự nhận là ai? | Khung hồ sơ trống lật hai mặt theo lời: "American soldier · stranded in Nigeria · on a mission" → "colonel, U.S. Army · deployed to South Africa · needs computer equipment" → dấu "MISREPRESENTED — per the court" | dấu MISREPRESENTED | S002, S003 | ● CONVICTED · per 7th Cir. opinion |
| G02 | Án nặng cỡ nào? | Bộ đếm 0 → 324 MONTHS → quy đổi = 27 YEARS (năm ô năm hiện dần) | 27 YEARS | S007 | ● CONVICTED |
| G03 | Một người đàn ông hay một hệ thống hồ sơ giả? | 2012: một khiếu nại (một chấm) → mở ra lưới hàng chục khung hồ sơ trống ("dozens of fictitious profiles", per prosecutors) → bản đồ Mỹ phẳng nhiều chấm **rải ngẫu nhiên, không theo bang/thành phố** "hundreds of women" ◐ | khung đầu tiên giữa lưới | S011, S012 | ◐ ALLEGED · per prosecutors |
| G04 | Bắt đầu khi nào, từ đâu, bằng gì? | Trục: March 2008 · South Africa → khung hồ sơ "fictitious names" · "successful businessmen" · "pictures of men in U.S. military uniforms" (chữ, không hình quân phục) | mốc March 2008 | S013, S014 | ● CONVICTED · per 7th Cir. opinion |
| G05 | Từ tin cậy tới yêu cầu: tiền và hàng đi theo đường nào? | Thanh "trust" đầy dần (thơ, thiệp, hoa — icon) → ô "REQUESTS: money · electronics" → "false claims of financial distress" → "for work on behalf of the U.S. government" gạch đứt | ô REQUESTS | S020, S021, S022 | ● per 7th Cir. opinion; S024 ◐ |
| G06 | Gửi cho ai thật sự? | Ba nhãn "driver" · "co-worker" · "hotel manager" + tên "Ilumsa Sunmola" → cả ba mũi tên gộp vào MỘT bóng "Sunmola himself" (per prosecutors) | cú gộp ba thành một | S025, S026 | ◐ ALLEGED · per prosecutors |
| G07 | Vì sao tiền cứ phải gửi thêm? | Vòng lặp: EMERGENCY → MONEY → new EMERGENCY (mỗi vòng thanh tiền dày hơn) → "money runs out / refused" → đường đứt: relationship ENDED | đường đứt cuối vòng | S027 | ◐ ALLEGED · per prosecutors |
| G08 | Ai đứng ở giữa đường dây? | Sơ đồ toả tia: ô trung tâm "organizer or leader (upheld)" → recruited accomplices · received stolen goods & wire transfers · directed what to tell victims; mũi tên phần lợi nhuận dày hơn "larger share (evidence suggesting)" | ô trung tâm | S028, S029, S030, S066 | ● per 7th Cir. opinion |
| G09 | Ngoài những người phụ nữ, ai còn thiệt hại? | Nhánh phụ "credit card fraud affecting various businesses" (court) → bộ đếm "one computer manufacturer: $800,000+" (per prosecutors) | $800,000+ | S032 | S031 ● court; S032 ◐ ALLEGED |
| G10 | Toà cân nhắc thiệt hại nào ngoài tiền? | Ngưỡng "5 or more victims" (vạch) → 7 chấm sáng (PSR listed seven, upheld) → hai thẻ "upward departure: psychological injury" · "gratuitous infliction of injury" | chấm thứ 7 vượt vạch 5 | S035, S036 | ● per 7th Cir. opinion |
| G11 | Từ cáo trạng tới nhận tội mất bao lâu? | Trục: Nov. 20, 2013 indictment (8 counts) → Aug. 9, 2014 arrest, London → Feb. 2015 to U.S. custody → Feb. 29, 2016 trial begins → 3 DAYS → guilty plea, all 8 counts, no plea agreement | 3 DAYS | S038, S039, S041, S042, S043 | TT; ● CONVICTED |
| G12 | Con số thiệt hại nói được bao nhiêu? | Hai lớp: 13 victims in PSR + 39 additional → thanh "around $1.7 million" với phần mờ phía trên ghi "underestimate" (per investigator, as recorded by the court) | phần mờ "underestimate" | S047, S048 | TT; ● per 7th Cir. opinion |
| G13 | Bản án được tính từ những gì? | Khối xếp chồng 6 enhancement theo lời (organizer/leader · acting on behalf of a government agency · substantial financial hardship · vulnerable victims · intended loss $2,054,972.66 · outside the U.S.) → 324 MONTHS → restitution $1,707,260.98 → amended $1,669,050.98 | 324 MONTHS | S049, S050, S051 | ● CONVICTED |
| G14 | Kháng cáo thay đổi được gì? | Bốn thẻ "challenged": enhancements · loss · restitution · deterrence → mỗi thẻ đóng dấu "rejected" theo lời → "AFFIRMED — Apr. 16, 2018" | AFFIRMED | S055, S058, S059, S060 | ● per 7th Cir. opinion |
| G15 | Ba bài học rút ra? | Tiêu đề 3 LESSONS · 5 RED FLAGS · 1 RULE → ba thẻ bài học gọi lại hình G08 (tổ chức), lưới chấm (chọn theo hoàn cảnh), thanh "underestimate" (G12) | thẻ bài học đang đọc | S065, S066, S067, S068, S069, S070 | theo từng câu |
| G16 | Năm dấu hiệu là gì? | 5 thẻ RED FLAG lật lần lượt, mỗi thẻ gọi lại icon (khung hồ sơ · hộp điện tử · ba nhãn gộp một · vòng khẩn cấp · khung ảnh + kính lúp) | số thứ tự thẻ đang đọc | S071, S073, S074, S075, S076 | theo từng câu |
| G17 | Báo ở đâu? | Thẻ nơi báo: "ic3.gov" · "reportfraud.ftc.gov" | ic3.gov | S078 | CHUNG |

## 3. Hồ sơ thật L3 (nền ngà B1; crop trang giữ nguyên dạng, khoanh câu; thẻ trích nguyên văn có dòng nguồn)

| Mã | Tệp · trang / nguồn | Vùng | Khoanh / chữ | Câu | Ghi chú |
|---|---|---|---|---|---|
| T01 | `ho-so/romance-sunmola/ca7-opinion-17-1299-2018.pdf` tr. 1 (N2) | khối đầu trang từ "United States Court of Appeals / For the Seventh Circuit" tới "Defendant-Appellant." — **cắt dưới trước** dòng "Appeal from…" (dòng đó có tên thẩm phán quận, tên này nằm trong danh sách cấm của tập) | UNITED STATES OF AMERICA v. OLAYINKA I. SUNMOLA · No. 17-1299 | S054 | NGUON §4: trang được dùng |
| T04 | như T01, tr. 18 | "III. CONCLUSION / For the foregoing reasons, we AFFIRM." | we AFFIRM | S054 | NGUON §4: trang được dùng |
| Q01 | N1 (USAO S.D. Ill., Feb. 2, 2017) | thẻ trích nền ngà | “Prince Charming” — U.S. Attorney's Office, Southern District of Illinois | S006 | Chữ = `chu` S006 nguyên văn |
| Q02 | N2 tr. 17 | thẻ trích nền ngà | “the most devastating crime one could ever imagine without someone laying hands or even eyes on another human being” — the sentencing judge, as quoted by the U.S. Court of Appeals for the Seventh Circuit | S008 | Chữ = `chu` S008 nguyên văn; nếu điều phối duyệt tr. 17 có thể thay bằng crop trang |

Trang/vùng cấm (NGUON.md §4): N2 tr. 2 (đoạn nhánh P06; bang nạn nhân), tr. 8, tr. 4 và 14 (tên điều tra viên), tr. 11–12, tr. 14 (tên dịch vụ chuyển tiền, trang hẹn hò); N2 tr. 1 dòng "Appeal from…" (tên thẩm phán quận); N2 tr. 10 (có câu trích lời bị cáo và chủ đề khủng bố — không crop); mọi ảnh chụp thông cáo N1. **Đề xuất (chưa dùng):** N2 tr. 17 câu "The judge mentioned general deterrence in a mere four sentences out of the eight-page transcript…" làm crop cho S059 — cần điều phối thêm vào NGUON §4 (trang không có tên/chi tiết cấm); hiện S059 dùng L2 G14.

## 4. Khoảnh khắc ảnh→clip (Veo 3.1 Lite, 5 ≤ 5; khung đầu = tranh L1 KHÔNG người — BAI-HOC tập 1 mục 2)

| Mã | Khung đầu (tranh) | Chuyển động (lời Veo khẳng định, mô tả cái có trong khung) | Neo cuối | Câu | Rủi ro / QC |
|---|---|---|---|---|---|
| K1 | `s001` — A dark living room at night, a lamp glowing softly, thin curtains at an open window, a sof… | The thin curtains move in a night breeze; the lamp light flickers softly on the sofa throw; slow push-in. | The quiet lamp-lit room; nobody present. | S001 | Khung đầu không màn hình (BAI-HOC mục 2) |
| K2 | `s048` — Dawn light across an empty wooden front porch, a potted plant and a plain bench; nobody pr… | Morning light slowly sweeps across the empty porch boards; leaves of the plant stir; dust drifts. | The bright empty porch. | S024 | Khung đầu không nhãn/chữ (BAI-HOC mục 2); hộp hàng chỉ ở tranh tĩnh |
| K3 | `s075` — An empty airport departure gate at night seen through glass, an aircraft waiting outside, … | Through the glass of the empty gate the waiting aircraft's lights blink slowly; reflections slide across the glass; nobody present. | The empty gate and the aircraft at night. | S040 | Không logo hãng, không bảng chuyến bay |
| K4 | `s080` — An empty wood-paneled courtroom in soft morning light, plain wooden walls and benches, dus… | Slow push-in toward the empty bench; dust drifts in the sunbeam; light brightens a little. | The empty courtroom bench in morning light. | S043 | Không con dấu, không cờ |
| K5 | `s122` — A sunrise window over a quiet room, a closed laptop on the table, warm light; nobody prese… | Sunrise light slowly fills the quiet room; curtains move softly; the closed laptop stays on the table. | The bright room with the closed laptop; nobody present. | S077 | Không thêm người |

QC mỗi clip (M-c): không người/mặt, không chữ/số/logo mọc ra (V5/V8, bài học tập 1: chữ giả mọc trên vật có chữ), chuyển động không méo; ≤ 2 lượt/khe, lượt 2 đổi lời (V7); hỏng 2 lượt → dùng tranh tĩnh có đẩy/kéo (0 USD, KHÔNG phải vá sau 402 — 402 thì DỪNG).

## 5. Danh sách tranh L1 (144 tranh mới; lời sinh = tiền tố/hậu tố tờ A `reports/mrp1/A/PHONG-CACH.md` + mô tả dưới)

| Mã | Loại | Mô tả cảnh (EN, gốc lời sinh) | Dùng ở |
|---|---|---|---|
| s001 | E | A dark living room at night, a lamp glowing softly, thin curtains at an open window, a sofa throw and a cold cup of tea; nobody present. | S001 |
| s002 | E | A laptop glowing in a dark living room, its screen a soft blank white rectangle, a sofa throw and a cold cup of tea nearby; nobody present. | S001 |
| s003 | E | A single empty profile frame glowing on a dark screen: a flat grey head-and-shoulders outline with a small question mark, no photo. | S002, S014 |
| s004 | E | A world map drawn on old paper on a desk at night with a single pin of light far away; no labels. | S002 |
| s005 | E | A desk at night with a plain laptop and a stack of blank cardboard boxes beside it, lamp light; nobody present. | S003 |
| s006 | E | A plain olive canvas duffel bag with no markings resting by an empty doorway; symbolic of a claimed assignment. | S003 |
| s007 | E | A plain profile frame cracked down the middle on a dark screen, flat grey outline, no photo. | S004 |
| s008 | R | A man seen strictly from behind, a dark silhouette in a plain shirt at a window over a hazy night city with no landmarks; no face. | S005, S026 |
| s009 | E | A laptop and several phones lying face-down on a desk in a dark rented room, curtains drawn; nobody present. | S005 |
| s010 | E | A night skyline of a generic large city across a dark bay, warm haze, no landmarks. | S005 |
| s011 | E | A paper crown made of folded blank paper on a table, soft spotlight; symbolic fairy-tale prince. | S006 |
| s012 | E | A fairy-tale storybook lying closed on a table, plain cover with no title, soft light. | S006 |
| s013 | E | A long empty prison corridor in soft muted light, rows of closed plain doors; nobody present. | S007 |
| s014 | E | A gavel resting on its block under soft courtroom light, nobody present. | S007 |
| s015 | E | A tall window in an empty courtroom with dust drifting in the light, nobody present. | S008 |
| s016 | E | An open notebook with a red pencil and three blank lines circled, warm desk lamp; symbolic of red flags. | S009 |
| s017 | N1 | The woman (N1) seen from behind on the sofa, lit by the laptop glow, leaning in to read; the screen is a soft blank white rectangle. | S009, S062 |
| s018 | E | A rural post office counter at dusk with a stack of plain parcels and an old scale, nobody present, no signs. | S010 |
| s019 | E | A plain sealed envelope resting on a post office counter beside an old scale, evening light; nobody present. | S010 |
| s020 | E | An envelope and a plain complaint form with blurred unreadable lines on a desk, pen beside it. | S010 |
| s021 | E | A wall of empty picture frames in a dark hallway, one lit; symbolic of fictitious profiles. | S011 |
| s022 | E | A notebook listing many blank lines, each with a small grey outline icon, under a lamp; symbolic. | S011 |
| s023 | E | An aerial view at night of a vast suburban grid with countless lit windows; symbolic, no landmarks. | S012 |
| s024 | R | Distant silhouettes of a few men around a table in a dim room, backlit, seen from behind; no faces. | S012 |
| s025 | E | A wall calendar with plain blank squares turning back through many pages; no numbers. | S013 |
| s026 | E | A dark desk with a laptop and a dozen phones lined up, screens off, a lamp; nobody present. | S013 |
| s027 | E | A row of identical empty profile frames lined up on a dark screen, flat grey outlines, no photos. | S014 |
| s028 | E | A shattered padlock icon drawn as a simple metal padlock broken open on a dark desk beside a laptop; symbolic of hacked accounts. | S015 |
| s029 | E | A shoebox of loose blank photo prints, all white, scattered on a table under a lamp. | S015 |
| s030 | E | A hand-drawn chain of grey profile outlines on paper, linked by thin lines; symbolic. | S015 |
| s031 | E | A row of empty coat hooks in a quiet hallway, soft light; nobody present. | S016 |
| s032 | E | A quiet empty government building corridor at dawn, plain walls, no flags or signs. | S017 |
| s033 | E | A plain wooden desk name stand with no name, alone on an empty desk. | S017 |
| s034 | N1 | The woman (N1) smiling softly at a bouquet of flowers on her table, morning light, a small stuffed bear beside it. | S018, S067 |
| s035 | E | A plain greeting card standing open on a windowsill, blank inside, flowers and a box of chocolates beside it. | S018 |
| s036 | E | A handwritten-style letter with every line blurred and unreadable, tied with a ribbon, beside a teacup. | S018 |
| s037 | E | A city map spread on a desk with a magnifying glass over unlabeled streets, lamp at night. | S019 |
| s038 | R | Hands in plain sleeves typing on a laptop in a dark room, the screen a soft blank glow; only hands. | S019 |
| s039 | E | A tourist postcard rack with all cards blank white, at dusk; no city names. | S019 |
| s040 | N1 | The woman (N1) reading at her laptop late at night, worried expression, the screen a soft blank glow. | S020 |
| s041 | E | A sealed padded envelope and a roll of tape on a kitchen counter, evening light. | S020 |
| s042 | E | Plain cardboard boxes taped shut and stacked by a front door, blank labels, morning light; nobody present. | S021, S069 |
| s043 | E | A bank counter at closing time with an empty pen chained to the desk, soft light, no signs. | S021 |
| s044 | E | A desk with blank government-style folders and a closed laptop, cold light; symbolic of a fake mission. | S022 |
| s045 | E | A plain wooden desk with an unmarked brass compass and a folded paper map; symbolic of a mission. | S022 |
| s046 | E | A plain olive duffel bag with no markings left on an empty bench at dusk; symbolic. | S023 |
| s047 | E | Laptops, tablets and phones in plain unbranded boxes on a table, packing tape beside them. | S024 |
| s048 | E | Dawn light across an empty wooden front porch, a potted plant and a plain bench; nobody present. | S024 |
| s049 | E | A shipping label stuck on a box with every line blank, a pen resting on top. | S025 |
| s050 | E | A hotel reception desk at night, a bell on the counter, nobody present, no signs. | S025 |
| s051 | E | A dark living room after midnight, the laptop closed on the sofa, a cup left on the table; nobody present. | S027 |
| s052 | N1 | The woman (N1) seen from behind at a window at dawn, alone, holding a dark phone. | S027 |
| s053 | E | A lone keyboard on a desk in a dark room lit by one lamp; nobody present. | S028 |
| s054 | N1 | The woman (N1) alone at her keyboard late at night, seen from behind, the screen a soft blank glow. | S028 |
| s055 | R | Several pairs of hands passing plain unbranded boxes along a table in a dim room; only hands and sleeves. | S029 |
| s056 | E | A chessboard with one king surrounded by many pawns, lamp light; symbolic of a leader. | S029 |
| s057 | E | An old balance scale with a much heavier pile of plain coins on one side, warm lamp. | S030 |
| s058 | E | A cake cut into very unequal slices on a plate; symbolic of a larger share. | S030 |
| s059 | E | A row of plain payment cards with no numbers or logos laid on a dark table under cold light. | S031 |
| s060 | E | A shop counter at night with a closed register, nobody present, no signs. | S031 |
| s061 | E | A closed small shop with its shutter half down at night, no signs. | S031 |
| s062 | E | Stacks of plain unbranded computer boxes in a dim warehouse aisle; nobody present. | S032 |
| s063 | E | A loading dock at night with a pallet of plain boxes, nobody present, no signs. | S032 |
| s064 | E | An empty house with a plain moving box on the floor and bare walls, afternoon light; nobody present. | S034 |
| s065 | E | A closed laptop on an empty office desk with a cardboard box of personal items beside it. | S034 |
| s066 | E | A row of empty chairs in a waiting room, cold light, no signs. | S034 |
| s067 | E | Seven small lamps on a dark table, all lit; symbolic, no labels. | S035 |
| s068 | N1 | The woman (N1) sitting at her kitchen table with a pile of blank bills, head in her hands, seen from the side. | S035 |
| s069 | E | A cracked teacup on a saucer under soft light; symbolic of psychological harm. | S036 |
| s070 | E | A dim hallway with a single chair facing a window, rain on the glass. | S036 |
| s071 | E | A coin on one side of a scale and a single wilted flower on the other, balanced; symbolic, warm light. | S037 |
| s072 | E | A small potted plant beginning to recover in morning light; quiet. | S037 |
| s073 | E | A wide empty stone courthouse staircase at dawn, plain façade with no lettering. | S038 |
| s074 | E | A thick closed binder with eight plain tabs on a courtroom table, nobody present. | S038 |
| s075 | E | An empty airport departure gate at night seen through glass, an aircraft waiting outside, no logos or signs. | S039, S040 |
| s076 | E | A rainy night street with black cabs blurred in the distance, no signs, no landmarks. | S039 |
| s077 | E | A boarding pass shape with every field blank lying on an airport bench. | S040 |
| s078 | E | An airplane wing over clouds at dawn, plain white, no markings. | S041 |
| s079 | E | A long empty jet bridge corridor, cold light, nobody present. | S041 |
| s080 | E | An empty wood-paneled courtroom in soft morning light, plain wooden walls and benches, dust drifting in a sunbeam. | S042, S044 |
| s081 | E | A jury box with fourteen empty chairs in soft light. | S042 |
| s082 | E | A pen resting on a single blank signature line on a white page, soft morning light. | S043 |
| s083 | E | A judge's bench seen from the empty gallery, a gavel resting on its block, nobody present. | S044 |
| s084 | E | A microphone on a lectern facing the bench in an empty courtroom. | S044 |
| s085 | E | Two closed courtroom doors side by side, one lit, one dark; symbolic of two hearings. | S045 |
| s086 | E | An empty witness stand with a glass of water and a microphone, soft light; nobody present. | S046 |
| s087 | E | A box of tissues on a courtroom railing, nobody present. | S046 |
| s088 | E | A thick stack of blank spreadsheet printouts with rows of unreadable lines on a table, desk lamp. | S047 |
| s089 | E | A postal service-style canvas mail bag with no markings on a table beside the spreadsheet; nobody present. | S047 |
| s090 | E | An iceberg drawn in a dark sea with most of its mass below the waterline; symbolic of an underestimate. | S048 |
| s091 | E | A telephone on a desk with a long list of blank names, many crossed with faint lines. | S048 |
| s092 | E | Plain envelopes arranged in neat rows on a table under warm light; symbolic of payments to victims. | S051 |
| s093 | E | A stack of plain checks with no names or numbers, held by a clip, on a desk. | S051 |
| s094 | E | An airplane parked on a quiet tarmac at dusk, stairs down, no markings; nobody present. | S052 |
| s095 | E | A one-way road sign shape with no text on an empty airport road at dusk. | S052 |
| s096 | E | A small house with a plain sale sign shape with no text, at dusk; no landmarks. | S053 |
| s097 | E | A courtroom clerk's counter with a plain sealed envelope, nobody present. | S053 |
| s098 | E | A set of four plain house keys on a ring lying on a table, warm light. | S053 |
| s099 | E | Four plain folders laid out in a row on a long table, lamp light. | S055 |
| s100 | E | A stack of four plain briefs bound with clips on an appellate court table. | S055 |
| s101 | E | A theatrical mask of plain white cardboard lying on a dark table under a spotlight; symbolic of a false role. | S056 |
| s102 | E | An empty chair in front of a mirror reflecting only a dark room; symbolic of a false image. | S056 |
| s103 | E | A row of plain empty chairs in an appellate courtroom, high windows, dust in light. | S056 |
| s104 | E | A quiet empty corridor in a government building at dawn, no flags or signs. | S057 |
| s105 | E | A plain closed briefcase standing next to an empty bench, nobody present. | S057 |
| s106 | E | A pencil eraser and a calculator beside a stack of blank financial pages, desk lamp. | S058 |
| s107 | E | Scattered coins being counted into neat piles by an unseen lamp-lit desk; no people. | S058 |
| s108 | E | An eight-page stack of blank paper with four short lines highlighted faintly; symbolic. | S059 |
| s109 | E | A dating-style profile card drawn as a blank white card with a small heart outline, lying on a dark table. | S060 |
| s110 | N1 | The woman (N1) in her living room looking at old blank photo frames on a shelf, seen from behind. | S060 |
| s111 | N1 | The woman (N1) sitting alone on a park bench in autumn, seen from the side, quiet; no other people. | S061 |
| s112 | E | A kitchen table set for one, warm evening light. | S061 |
| s113 | E | A lighted window in an apartment building at night, one among many dark ones. | S062 |
| s114 | E | A single glowing heart outline drawn on a foggy window; symbolic. | S062 |
| s115 | N1 | The woman (N1) holding a warm cup by a window at dawn, calm, gentle light. | S063 |
| s116 | E | Two cups of tea on a small table by a window, morning light; warm and safe. | S063 |
| s117 | E | An old wooden bench on an empty pier at dusk, still water; symbolic of the past. | S063b |
| s118 | E | A closed old diary with a ribbon on a shelf, soft light. | S063b |
| s119 | E | A high fence and a distant prison building at dusk, plain, no signs. | S064 |
| s120 | E | A calendar on a plain wall with many blank pages ahead, no numbers. | S064 |
| s121 | E | A long road leading to a distant plain building under a pale sky; quiet, no signs. | S064 |
| s122 | E | A sunrise window over a quiet room, a closed laptop on the table, warm light; nobody present. | S065 |
| s123 | E | Many hands silhouetted around one glowing blank screen in a dark room; symbolic of several people behind one profile. | S066 |
| s124 | E | A map table with many small lamps scattered unevenly, some brighter; symbolic of circumstances. | S067 |
| s125 | E | A front door with a chain lock in morning light, nobody present. | S068 |
| s126 | E | A public service poster shape on a wall with all text blurred and unreadable, soft light. | S068 |
| s127 | E | An iceberg tip above dark water with the hidden mass glowing faintly below. | S069 |
| s128 | N2 | The woman (N1) talking with her friend (N2) at a café table, the friend listening, warm light. | S070 |
| s129 | E | A telephone and a notepad on a counter in morning light, the notepad blank. | S070 |
| s130 | E | A blank profile frame with a small red flag icon drawn beside it on a dark screen. | S071 |
| s131 | E | A small table with a closed notebook under morning light; nobody present. | S072 |
| s132 | E | A sealed empty envelope on a table, nobody present. | S072 |
| s133 | E | A stack of plain unbranded electronics boxes with a red tag tied on top. | S073 |
| s134 | E | Three blank name tags on a table, all pointing to one shadow; symbolic. | S074 |
| s135 | E | A courier's empty trolley in a hallway, nobody present, no signs. | S074 |
| s136 | E | A row of dominoes falling, the last one stopped by a hand-drawn line; symbolic. | S075 |
| s137 | E | A magnifying glass over an empty photo frame on a desk, lamp light. | S076 |
| s138 | N1 | The woman (N1) holding a printed blank photo beside her laptop, comparing, curious. | S076 |
| s139 | N2 | The woman (N1) and her friend (N2) walking together in a park in morning light, seen from behind. | S077 |
| s140 | E | A closed padlock on a small box of money-shaped blank paper on a table; symbolic of keeping it. | S077 |
| s141 | E | A laptop on a kitchen table showing a soft blank white glow, a cup of tea beside it, morning light. | S078 |
| s142 | N1 | The woman (N1) typing on a laptop at her kitchen table in morning light, calm and determined; the screen is a soft blank glow. | S078 |
| s143 | E | A tidy desk with a stack of plain bound records and a desk lamp, warm light, nobody present. | S079 |
| s144 | E | A quiet bookshelf of plain bound records with no titles, warm light. | S079 |

## 6. Nhạc

Giữ bảng nhạc `SHOT.md` §4 (MR-K23): P00–P03 piano ấm chậm −24 dB · P04–P05 lạnh dần, dây thấp −22 dB · **P06 im lặng** (thẻ tối 6 s) · P07 một nốt piano thấp −26 dB · P08 nhịp tăng, **cắt lặng 1 s** sau S042 · P09–P11 nền tĩnh −26 dB · P12 sáng hơn −24 dB. Không còi, còng tay, tiếng nức nở.

## 7. Kiểm máy (scripts/mrs23/shot2.py)

- Mỗi câu 1–3 cảnh · mã cảnh tồn tại · ≥ 6 đồ hoạ L2 động có câu hỏi + một điểm nhấn · ≤ 5 Veo, khung đầu tranh loại E · tranh dùng ≤ 2 lần · cảnh tranh ≥ 1,5 s · tranh người thật có từ khoá bóng/lưng/tay, không mặt · từ cấm hình (biếm hoạ, quân phục/phù hiệu/logo/con dấu/cờ) · regex cấm của tập (`kiem_rieng.cam_them`) · KB/KC quét cả tệp này.
- Kết quả: **ĐẠT (0 lỗi)**
