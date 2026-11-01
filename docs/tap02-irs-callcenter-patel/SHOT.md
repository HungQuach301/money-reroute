# BẢNG SHOT — Tập 2 · Call center mạo danh IRS/USCIS / Patel (`tap02-irs-callcenter-patel`)

> MR-K23 · 01/11/2026 · NHÁP G1. Cột "Thời điểm ước" **tính máy**: `python3 scripts/mrk23/shot_tg.py docs/tap02-irs-callcenter-patel/loi.json docs/tap02-irs-callcenter-patel/SHOT.md --ghi` — lời đọc **155 từ/phút** (đo thật MR-4, QUY-TRINH §6) + 3 s nghỉ mỗi đoạn + 6 s mỗi thẻ chữ không đọc + 8 s giữ thẻ tổng kết + 45 s nguồn/nhạc kết.
> **Loại hình:** `SD` sơ đồ/đồ hoạ tự vẽ từ số liệu hồ sơ (0 USD) · `TL` ảnh trang hồ sơ thật (crop từ PDF trong `ho-so/`, 0 USD) · `CT` thẻ chữ trích nguyên văn + nguồn (0 USD) · `VEO` cảnh dựng minh hoạ Veo 3.1 Lite 1080p, clip 8 s (trả tiền) · `NEN` nền chuyển động tự làm (0 USD).
> **Bảng màu B1 "Hồ sơ"**, giọng kênh (`kozBJGqBNTqfBBClLNCL`, `eleven_v4`) — như tập 1 (`PHUONG-AN.md` §0).
> **Luật áp cho mọi hàng** (HIEN-CHUONG §1, §3 luật 8, §4; LUAT-VEO V1–V8; lệnh MR-D23 cho vụ này):
> - **Không dựng cuộc gọi**: không câu thoại của "người gọi", không giọng đóng vai, không chữ kịch bản trên màn hình, **không số điện thoại** (kể cả số giả), không giao diện ứng dụng gọi/nhắn tin.
> - Không mặt người thật; không chân dung/phác hoạ nhận ra được. Nhân vật dựng chỉ là **bàn tay hoặc bóng ngược sáng**. Không người già nhận ra được (nạn nhân KBCB).
> - **Không logo, không con dấu, không huy hiệu** IRS/USCIS/DHS/HSI/DOJ hay cơ quan thuế Canada/Úc; tên cơ quan chỉ bằng **chữ trơn** (font kênh). Không biển hiệu call center thật, không tên 4 nhóm call center còn lại, không tên thương hiệu thẻ/ứng dụng/dịch vụ chuyển tiền. Thẻ nhựa trong cảnh: **trắng trơn**.
> - Mỗi đoạn có tên cơ quan bị mạo danh: thẻ không liên quan (đọc hoặc chữ) — máy kiểm KA.
> - **Tên call center nêu ở P05 (một lần trong lời):** mỗi lần hiện tên trên hình đều đi cùng **nguyên câu ◐** (bản chữ số của S029) trên cùng khung — máy kiểm KB quét cả tệp này. Không dùng ảnh trang N1 tr. 7 (bảng tên bị cáo).
> - Nhãn: ● → `● CONVICTED`; ●T → `● CONVICTED · admitted in plea, per DOJ`; ●N → `● CONVICTED · U.S. co-defendants`; ◐ → `◐ ALLEGED`; Veo → `ILLUSTRATIVE — not the real person/event` (lần đầu mỗi đoạn). Mọi câu pháp lý có **dòng nguồn** (IBM Plex Mono ≥ 22 px), vd "Source: U.S. v. Patel et al., No. 4:16-cr-385 (S.D. Tex.), Superseding Indictment, Dkt. 6, p. 3" hoặc "Source: DOJ Press Release 20-19 (Jan. 9, 2020)".
> - **Bài học Veo MR-4 (áp mọi khe):** (1) giấu người bằng **ánh sáng** — "seen only as a dark silhouette against a bright window", "hands lit from behind" — không dựa vào chỉ dẫn phủ định/vị trí ("no face", "head outside frame", "to the right" — Veo Lite bỏ qua); (2) mô tả **cái có trong khung** ("a blank white card", "plain wooden walls") thay vì liệt kê cái cấm; (3) neo cuối mô tả **cảnh trống** cụ thể ("the table with only the phone"), không "the person leaves the frame" chung chung; (4) màn hình/giấy trong cảnh là "a soft glowing blank white rectangle" / "blank white paper"; chữ thêm ở hậu kỳ.
> - V2: khe có vật chuyển động → clip dài đúng khe, không kéo dãn. V3: neo cuối không người tiền cảnh. V7: ≤ 2 lượt/khe, lượt 2 đổi lời; **402 → DỪNG**.

## 1. Bảng shot

| # | Đoạn / câu | Thời điểm ước | Loại | Nội dung hình | Nhãn / chữ trên hình | Khe Veo (8 s) + lời Veo (khẳng định, bài học MR-4) |
|---|---|---|---|---|---|---|
| 1 | P00 S001 | 0:03–0:07 | VEO | Bàn bếp gỗ lúc chạng vạng; điện thoại nằm ngửa, màn hình **sáng trắng trơn**; ánh cửa sổ ấm phía sau | Hậu kỳ: chữ chung "Unknown" trên màn hình; "ILLUSTRATIVE — not a real call" | **V01**. "A smartphone lying face-up on a wooden kitchen table at dusk; its screen glows as a soft, blank white rectangle and pulses gently; warm window light behind; the table holds only the phone and a mug." V3: neo cuối = bàn chỉ có điện thoại |
| 2 | P00 S002–S003 | 0:07–0:29 | SD + CT | Thẻ chữ ngôi thứ ba: "Threats: arrest · prison · fines · deportation"; thẻ không liên quan "The IRS and U.S. Citizenship and Immigration Services had nothing to do with these calls." (chữ trơn, không logo) | `● CONVICTED · admitted in plea, per DOJ`; nguồn DOJ 20-19 ¶5 | — |
| 3 | P00 S004–S006 | 0:29–0:48 | SD | Bản đồ phẳng tự vẽ: chấm "Ahmedabad, India" → cung nét đứt sang Mỹ; thẻ tên chữ "Hitesh Madhubhai Patel" (**không ảnh**); bộ đếm "20 YEARS" | S004 `● · admitted in plea, per DOJ`; S006 `● CONVICTED`; nguồn DOJ 20-19 ¶5–6; DOJ 20-1294 ¶1–2 | — |
| 4 | P00 S007–S008 | 0:48–1:04 | VEO + SD | Những tấm thẻ nhựa **trắng trơn** xoè trên quầy tối dưới một đèn bàn; chồng sơ đồ chấm mờ "phone → ? → cash" | "ILLUSTRATIVE" | **V02**. "Several plain white plastic cards, completely blank, fanned out on a dark glass counter under a single warm desk lamp; slow push-in; shallow focus." Không tay |
| 5 | P01 S009–S011 | 1:07–1:36 | VEO + SD | Đôi tay người lớn tuổi **ngược sáng** đặt trên mặt bàn cạnh một tờ giấy **trắng trơn**; chồng chữ "$12,300 · age 85 — per the indictment"; lịch 20 ô tự vẽ cho S010 ("multiple calls · 20 days · $136,000"); S011 thẻ không liên quan **chữ, không đọc** (6 s) | "ILLUSTRATIVE — not the real person"; `◐ ALLEGED`; nguồn DOJ 16-1257 ¶11–12 | **V03**. "Close-up of an older person's hands resting on a kitchen table beside a sheet of blank white paper, lit from behind by a bright window so the hands are soft silhouettes; the frame shows only the table surface, the hands and the paper." V3: neo cuối = tay rút khỏi bàn, chỉ còn tờ giấy. **Không** thành phố, không ngày |
| 6 | P02 S012–S015 | 1:39–2:15 | VEO + SD | Bậc thềm toà nhà cột đá cổ điển lúc bình minh, không biển tên, không người; dòng thời gian "Oct. 19, 2016 indictment · Oct. 27 unsealed · 61 defendants · 20 arrests (U.S.) · 32 people + 5 call centers charged (India)"; S015 chữ "Alleged at the time: tens of thousands of victims · hundreds of millions of dollars" | TT không nhãn; S015 `◐ ALLEGED`; nguồn DOJ 16-1257 ¶1, ¶8 | **V04**. "Wide shot of empty stone steps and tall classical columns at dawn, soft pink light, plain stone façade with no lettering." V3/V4: không người |
| 7 | P03 S016–S019 | 2:18–2:57 | TL + SD | Crop N1 tr. 3 (tiêu đề "General Allegations" + ¶1(a)); 4 thẻ chữ: "IRS impersonation" · "Immigration impersonation" · "'Payday loan' with an upfront fee" · "'Government grant' with a processing fee" | `◐ ALLEGED`; nguồn Superseding Indictment, Dkt. 6, pp. 3–4 | Không lời mẫu, không số điện thoại |
| 8 | P03 S020–S021 | 2:57–3:15 | SD + CT | Thẻ chữ "Scripts also included: Canada tax agency · Australian tax office · debt collection"; thẻ không liên quan S021 | `◐ ALLEGED` (per DOJ); nguồn DOJ 20-19 ¶6 | Không logo/cờ cơ quan |
| 9 | P04 S022–S026 | 3:18–4:07 | VEO + SD | Phòng làm việc ban đêm, các dãy bàn **trống**, tai nghe đặt trên bàn, màn hình **sáng trắng trơn**; chồng **sơ đồ tổ chức tự vẽ** (ô chữ, không người): Data brokers → Callers → Call center operators → Payment processors → Domestic managers → Runners · Hawaladar | "ILLUSTRATIVE"; `◐ ALLEGED`; nguồn Superseding Indictment pp. 4–6 | **V05**. "Night interior of a long open-plan office with rows of empty desks; headsets resting on the desks; every monitor shows a soft blank white glow; slow lateral dolly; the room is still." Không biển hiệu, không chữ |
| 10 | P05 S027 | 4:10–4:23 | SD | Bản đồ Ahmedabad tự vẽ, **5 chấm không tên**, đường nối giữa các chấm ("shared scripts · lists · payments") | `◐ ALLEGED`; nguồn Superseding Indictment pp. 6–7 | Không tên 4 nhóm còn lại |
| 11 | P05 S028–S029 | 4:23–4:50 | SD + CT | Một chấm sáng lên; ô chữ "HGLOBAL — operated and funded, admitted in plea (per DOJ)" và **ngay dưới, cùng khung, nguyên câu ◐**: "HGLOBAL was also charged; like every defendant who has not been convicted, it is presumed innocent. As of July 2018, the India-based call centers charged had yet to be arraigned; as of November 2020, the Justice Department said charges remained pending for other India-based defendants." Câu ◐ giữ trên hình suốt S029 | S028 `● CONVICTED · admitted in plea, per DOJ`; S029 `◐ ALLEGED`; nguồn DOJ 20-19 ¶6; DOJ 18-961 ¶15; DOJ 20-1294 ¶12; Indictment p. 1 | Ô chữ và câu ◐ hiện **cùng lúc**, tắt cùng lúc (KB) |
| 12 | P05 S030–S033 | 4:50–5:16 | SD + CT | Ô chữ "Listed role: call center operator" (dựng chữ, **không** ảnh trang bảng); "Monthly income & expense reports → personal email"; chữ trích S032 + dòng S033 "A co-defendant's description — not a court finding" | `◐ ALLEGED`; nguồn Indictment p. 7; DOJ 20-19 ¶7–8 | Không tên đồng bị cáo |
| 13 | P06 S034–S036 | 5:19–5:53 | VEO + SD | Một tấm thẻ nhựa **trắng trơn** trượt qua mặt quầy kính tối; chồng **sơ đồ dòng tiền**: victim → "prepaid card / wire" → runners (U.S.) → nhiều nhánh | "ILLUSTRATIVE"; S034–S035 `● · admitted in plea, per DOJ`; S036 `◐ ALLEGED` | **V06**. "A single blank white plastic card slides slowly across a dark glass counter and stops; reflections of warm lamps; macro shot; the counter holds only the card at the end." Không tay |
| 14 | P06 S037–S039 | 5:53–6:30 | VEO + SD | Hai cuốn sổ **trắng trơn** trên hai bàn ở hai nơi (ghép đôi khung ở hậu kỳ); sơ đồ hawala vẽ là **bù trừ** giữa hai người môi giới (hai mũi tên ngược chiều, **không** mũi tên tiền chạy thẳng sang Ấn Độ); TL crop N1 tr. 6 dòng "without actually moving it" | "ILLUSTRATIVE"; `◐ ALLEGED`; nguồn Indictment p. 6 ¶2(g); DOJ 16-1257 ¶10 | **V07**. "An open ledger notebook with blank white pages and a closed pen on a wooden desk, lit by a single lamp at night; a page turns slowly by itself." V2: giấy chuyển động → đủ 8 s |
| 15 | P06 S040–S042 | 6:30–7:11 | SD | Thẻ khái niệm của kênh: "1 PLACEMENT — money enters (cards, wires)" → "2 LAYERING — moved, changed, many hands"; dòng nhỏ "Framework used by this channel — not the indictment's words" | S040 `● CONVICTED · U.S. co-defendants`; nguồn DOJ 18-961 ¶14 | Không "integration"; không thao tác |
| 16 | P07 S043–S045 | 7:14–7:51 | SD | **Lưới 24 ô trống** (không tên, không mặt); bản đồ Mỹ 3 bang chữ "Texas · Arizona · Georgia"; "probation to 20 years in prison"; "Restitution: $8,970,396 (joint and several, 22 defendants)" | `● CONVICTED · U.S. co-defendants`; nguồn DOJ 18-961 ¶1, ¶11; DOJ 20-19 ¶11 | — |
| 17 | P07 S046 | 7:51–8:04 | CT | Thẻ chữ "India side: 32 people + 5 call centers charged — not yet arraigned (July 2018) — presumed innocent" | `◐ ALLEGED`; nguồn DOJ 18-961 ¶15 | Không tên |
| 18 | P07 S047–S048 | 8:04–8:29 | VEO | **Cú treo giữa tập:** cánh máy bay **trắng trơn** ngoài cửa sổ lúc hoàng hôn; chữ "September 2018 — Singapore" ở cuối | "ILLUSTRATIVE"; S047 `● · admitted in plea, per DOJ` (vế "would later admit") | **V08**. "View through an airplane window of a plain white wing at sunset above a sea of clouds; slow drift; warm orange light." Không logo hãng. Nhạc: nhịp tăng, cắt lặng 1 s sau S048 |
| 19 | P08 S049–S050 | 8:32–8:44 | SD | Bản đồ tự vẽ India → Singapore → United States (mũi tên tới "United States", không ghi thành phố); mốc "Sept. 2018 provisional arrest · Apr. 2019 extradition" | TT; nguồn DOJ 20-19 ¶9 | Không cảnh bắt giữ, không phù hiệu cảnh sát |
| 20 | P09 S051–S053 | 8:47–9:17 | VEO + SD | Phòng xử gỗ **trống**, tường gỗ trơn, ánh sáng sớm; chồng "Jan. 9, 2020 — pleaded guilty: (1) wire fraud conspiracy (2) general conspiracy"; "Loss attributable (admitted): > $25M and < $65M" | `● CONVICTED`; S053 `● · admitted in plea, per DOJ`; nguồn DOJ 20-19 ¶2, ¶8, ¶10 | **V09**. "An empty wood-paneled courtroom in soft morning light, plain wooden walls and benches, dust motes drifting in a sunbeam; slow push-in toward the empty bench." Không con dấu/cờ. **Không** ghi "money laundering conviction" |
| 21 | P10 S054–S056 | 9:20–9:44 | SD + CT | "Nov. 30, 2020 — 20 years + 3 years supervised release" · "Restitution: $8,970,396"; thẻ S056 "Other India-based defendants: charges pending (Nov. 2020) — presumed innocent" | S054–S055 `● CONVICTED`; S056 `◐ ALLEGED`; nguồn DOJ 20-1294 ¶1–2, ¶12 | — |
| 22 | P11 S057 | 9:47–9:54 | NEN | Tiêu đề "WHAT TO TAKE AWAY" · 3 LESSONS · 5 RED FLAGS · 1 RULE | | — |
| 23 | P11 S058–S061 | 9:54–11:09 | SD + CT | 3 thẻ **bài học**: L1 chiếu lại sơ đồ tổ chức (hàng 9); L2 chiếu lại sơ đồ dòng tiền + thẻ "placement → layering" (hàng 13, 15); L3 thẻ "How the IRS actually contacts you" — 4 dòng chữ của N9; chữ trích HSI S061 | S058 `◐ ALLEGED`; S059 `● · admitted in plea, per DOJ`; S060 "Source: IRS FS-2017-7"; S061 "Source: DOJ Press Release 16-1257" | Không logo IRS |
| 24 | P11 S062–S067 | 11:09–12:06 | SD | 5 thẻ **dấu hiệu**, mỗi thẻ chiếu lại hình đoạn tương ứng (hàng 2, 7, 13, 5, 7); S067 thẻ không liên quan **chữ, không đọc** (6 s) | S062, S064 `● · admitted in plea, per DOJ`; S063, S065, S066 `◐ ALLEGED` | — |
| 25 | P11 S068 | 12:06–12:16 | VEO | Bàn tay **ngược sáng** lật úp điện thoại xuống bàn bếp, ánh sáng sớm; neo cuối chỉ còn điện thoại úp | "ILLUSTRATIVE"; chữ "1 RULE: Hang up. Look the agency up yourself." | **V10**. "Morning kitchen table, backlit by a bright window: a hand, seen as a dark silhouette, turns a smartphone face-down on the table and withdraws; the shot ends on the table with only the face-down phone and a mug." |
| 26 | P11 S069–S071 | 12:16–12:56 | NEN | **Thẻ tổng kết B1** (§3) toàn khung; dải dưới "tigta.gov · reportfraud.ftc.gov"; dòng khai AI (HIEN-CHUONG §6). Giữ thẻ thêm 8 s sau S071 | S069 `◐` "according to the Justice Department" (DOJ 18-961 ¶3) | — |
| 27 | Kết | 12:56–13:41 | NEN | Danh sách nguồn chạy chữ + nhạc kết | Nguồn N1–N5, N9–N11 | — |

## 2. Tổng khe Veo

| Mức | Số khe 8 s | Khe |
|---|---|---|
| **Giữa (đề xuất)** | **10** | V01–V10 như bảng |
| Thấp | 7 | bỏ V02, V07, V08 (thay `SD`/`NEN`) |
| Cao | 15 | thêm 5 khe phụ: V05b (dãy bàn trống góc thấp, cho P04 dài), V06b (thẻ trắng xếp chồng cận), V08b (đường băng đêm, đèn dẫn đường), V09b (hành lang toà nhà trống), V11 (bình minh trên mái nhà thành phố không địa danh, cho đoạn kết) |

Mỗi khe: kiểm trước khi gửi (0 USD) theo V1–V6 và bài học MR-4; QC tại nguồn: không mặt (bóng ngược sáng không lộ mắt/mũi/miệng), không chữ/logo/con dấu, không số điện thoại/giao diện, thẻ nhựa trắng trơn; quét `scripts/common/quet_v8.py` + tờ 0,5 s ở M-d.
Khe có người (V03 tay, V10 tay) là khe rủi ro cao nhất → ở M-c sinh trước, áp đúng cách MR-4 đã đạt (V06_l2: ngược sáng thành bóng).

## 3. Thẻ tổng kết trên hình (B1 "Hồ sơ", hàng 26)

Nền giấy ngà `#F4F1EA`; chữ mực `#1B1F24`; tiêu đề nhóm IBM Plex Serif SemiBold; dòng Inter. Mỗi dòng ≤ 48 ký tự; không tên người, không tên call center, không logo:

| Nhóm | Dòng (EN, đúng chữ trên hình) | Câu lời | Màu số |
|---|---|---|---|
| **3 LESSONS** | 1. The scary call was the front of a chain | S058 | xanh két `#2B7A78` |
| | 2. Cards & wires = money cashed out fast | S059 | xanh két |
| | 3. The IRS mostly starts with mail | S060 | xanh két |
| **5 RED FLAGS** | 1. Threats: arrest, prison, deportation | S062 | đỏ cam `#D9480F` |
| | 2. "Pay now" — no time to check | S063 | đỏ cam |
| | 3. A specific payment method | S064 | đỏ cam |
| | 4. Repeated calls over days | S065 | đỏ cam |
| | 5. A loan or grant with a fee first | S066 | đỏ cam |
| **1 RULE** | Hang up. Look the agency up yourself. | S068 | mực, nền ô xám `#8A8F98` 15 % |

Chân thẻ (IBM Plex Mono ≥ 22 px): "Report IRS impersonation: tigta.gov — Report scams: reportfraud.ftc.gov". Thẻ là bài học chung, không nhãn tầng.

## 4. Nhạc (Eleven Music, nằm trong ước "Giữa" 4 phút của `UOC-CHI.md`)

| Đoạn | Hàng | Nhạc | Mức |
|---|---|---|---|
| P00 | 1–4 | nền điện tử trầm, một xung nhịp chậm như chuông điện thoại xa (không tiếng chuông thật) | −24 dB |
| P04–P06 | 9–15 | lớp nhịp đều ~90 bpm, cảm giác "dây chuyền" | −22 dB |
| P07 S047–S048 | 18 | nhịp tăng, cao độ lên; **cắt lặng 1 s** sau S048 | −18 dB → 0 |
| P08–P10 | 19–21 | piano thấp, nền tĩnh | −26 dB |
| P11 | 22–26 | nền sáng hơn, giữ dưới lời | −24 dB |

Lời luôn nghe rõ (đỉnh nhạc ≤ −18 dB dưới lời); không hiệu ứng còi, chuông điện thoại thật, súng, còng tay.
