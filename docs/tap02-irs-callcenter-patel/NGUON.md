# NGUỒN — Tập 2 · Call center mạo danh IRS/USCIS / Hitesh Madhubhai Patel (`tap02-irs-callcenter-patel`)

> MR-K23 · 01/11/2026 (UTC; 02/11/2026 sáng giờ Hà Nội) · NHÁP G1. Mã N1–N11 giữ nguyên như `docs/kho-de-tai/irs-callcenter-patel.md` §8 và `docs/dan-truyen/irs-callcenter-patel.md` §7 (cùng mã → kiểm chéo được với dàn truyện đã duyệt).
> **Quy ước trang/đoạn:** N1 = "Page x of 81" ở đầu trang (trùng số trang PDF; PDF quét, đọc bằng ảnh trang `pdftoppm`). N2–N5 = thông cáo DOJ lấy qua API chính thức `https://www.justice.gov/api/v1/press_releases.json?parameters[title]=…`; **đ.n = thẻ `<p>` thứ n không rỗng trong trường `body`** của bản OPA (`/archives/opa/pr/…`). Bản JSON đã lưu trong repo (cột Tệp) để kiểm lại không cần mạng.
> Mọi nguồn dưới đây mở **đường chính thức**, không vượt rào; trang trả 403/404 ghi "chưa mở được" và **không dùng**. Không gửi thông tin cá nhân của chủ dự án trong request (curl mặc định, không UA khai báo).

## 1. Bảng nguồn

| Mã | Cơ quan | Tài liệu | Số vụ / docket | Ngày | URL | Trang/đoạn dùng trong lời | Đã mở (ngày UTC, HTTP, đường) | Tệp + SHA-256 |
|---|---|---|---|---|---|---|---|---|
| N1 | Toà S.D. Tex. (DOJ đăng) | Superseding Indictment, Document 6 (bản chứng thực "Unsealed 10/27/16") | 4:16-cr-00385 | nộp 19/10/2016 | https://www.justice.gov/usao-sdtx/file/905837/dl?inline | tr. 1, 3, 4, 5, 6, 7 | 01/11/2026, tệp repo (LFS), SHA khớp kho §8; đọc ảnh trang 3–7 ở MR-K23 | `ho-so/irs-callcenter-patel/cao-trang-thay-the-4-16-cr-385-doc6-2016-10-19.pdf` — `04fb7cb3c4cfda5b444a66c9415878635346dfb1f6c3333e5acf41867a7b2bdf` |
| N2 | DOJ (OPA) | Thông cáo 16-1257 "Dozens of Individuals Indicted in Multimillion-Dollar Indian Call Center Scam Targeting U.S. Victims" | như trên | 27/10/2016 | https://www.justice.gov/archives/opa/pr/dozens-individuals-indicted-multimillion-dollar-indian-call-center-scam-targeting-us-victims | đ.1, 5, 8, 9, 10, 11, 12 | 01/11/2026, HTTP 200, API DOJ | `ho-so/irs-callcenter-patel/doj-api-16-1257-2016-10-27.json` — `a3cbba8e34ea0b6e423abbe8c3656de306e69544d3e78b36e2dd6cf1bbc5e002` |
| N3 | DOJ (OPA) | Thông cáo 18-961 "24 Defendants Sentenced in Multimillion Dollar India-Based Call Center Scam Targeting U.S. Victims" | như trên | 20/07/2018 | https://www.justice.gov/archives/opa/pr/24-defendants-sentenced-multimillion-dollar-india-based-call-center-scam-targeting-us-victims | đ.1, 3, 8, 9, 10, 11, 14, 15; danh sách `<li>` sau đ.12–13 (22 Houston, 1 Atlanta, 1 Phoenix) | 01/11/2026, HTTP 200, API DOJ | `ho-so/irs-callcenter-patel/doj-api-18-961-2018-07-20.json` — `bfb84638fd74e264fb5bea3154471121dde765c24e33788af1f329f4c0d4f20c` |
| N4 | DOJ (OPA) | Thông cáo 20-19 "Indian National Pleads Guilty to Owning, Funding, and Operating India-Based Call Centers…" | như trên | 09/01/2020 | https://www.justice.gov/archives/opa/pr/indian-national-pleads-guilty-owning-funding-and-operating-india-based-call-centers-scammed | đ.2, 5, 6, 7, 8, 9, 10, 11 | 01/11/2026, HTTP 200, API DOJ | `ho-so/irs-callcenter-patel/doj-api-20-19-2020-01-09.json` — `90fae8027de00aaebc56d6fc8076c92b713940c08f8a0137dae99cc5bc22c649` |
| N5 | DOJ (OPA) | Thông cáo 20-1294 "Owner and Operator of India-Based Call Centers Sentenced to Prison…" | như trên | 30/11/2020 | https://www.justice.gov/archives/opa/pr/owner-and-operator-india-based-call-centers-sentenced-prison-scamming-us-victims-out-millions | đ.1, 2, 9, 12 | 01/11/2026, HTTP 200, API DOJ | `ho-so/irs-callcenter-patel/doj-api-20-1294-2020-11-30.json` — `96cd2548a9923709e212a7f5b2a6c436fcafabb189811fcaa9594711a780a2f6` |
| N6 | BOP | Inmate Locator (JSON chính thức `bop.gov/PublicInfo/execute/inmateloc?todo=query&output=json&nameFirst=hitesh&nameLast=patel`) | — | tra 01/11/2026 | https://www.bop.gov/inmateloc/ | **không dùng trong lời** (chỉ kiểm trạng thái, §2) | 01/11/2026, HTTP 200 | phản hồi 1.672 byte, SHA-256 `b63772c0…a8475` (không lưu) |
| N7 | DOJ Office of the Pardon Attorney | Clemency Grants Trump 2025–present; Commutations Biden 2021–2025; Pardons Biden 2021–2025 | — | tra 01/11/2026 | https://www.justice.gov/pardon/clemency-grants-president-donald-j-trump-2025-present ; …/commutations-granted-president-joseph-biden-2021-2025 ; …/pardons-granted-president-joseph-biden-2021-2025 | **không dùng trong lời** (§2) | 01/11/2026, HTTP 200 ×3; tìm "Hitesh"/"Hinglaj": 0 | không lưu (SHA `263d2e35…670a`, `22990a79…bbe1a1`, `d0be25c3…22fe9d6`) |
| N8 | 5th Cir. | Kháng cáo của Patel (nếu có) | — | — | — | **không dùng** | **chưa mở được** (kho §8; không tìm thêm ở MR-K23) | — |
| N9 | IRS | Fact sheet FS-2017-7 "How to know it's really the IRS calling or knocking on your door" | — | 19/04/2017 | https://www.irs.gov/newsroom/how-to-know-its-really-the-irs-calling-or-knocking-on-your-door | đoạn "The IRS initiates most contacts through regular mail…"; mục "Note that the IRS does not:" (3 gạch đầu dòng); "Know Who to Contact" (TIGTA) | 01/11/2026, HTTP 200, curl mặc định | không lưu (SHA phản hồi `b5288c33…cb`) |
| N10 | FTC | ReportFraud.ftc.gov (trang chủ, "File A Complaint") | — | — | https://reportfraud.ftc.gov/ | lời S070 | 01/11/2026, HTTP 200 | không lưu (SHA `874400…387c`) |
| N11 | TIGTA | "Report Crime and Misconduct" — mục "IRS Scams and Fraud": "Someone is impersonating an IRS or Treasury employee." | — | — | https://www.tigta.gov/reportcrime-misconduct | lời S070 | 01/11/2026, HTTP 200 | không lưu (SHA `dbbd32…3a17`) |
| — | FTC | consumer.ftc.gov "government imposter scams" | — | — | https://consumer.ftc.gov/articles/government-imposter-scams | **không dùng** | **chưa mở được** (MR-D23: HTTP 403; không thử lại bằng UA khác) | — |

Ghi chú đoạn: bản OPA của N4 có 16 đoạn, N5 có 17 đoạn; số đoạn trong lời khớp đúng cách đánh của dàn truyện đã duyệt (N4 đ.5 "According to admissions…", đ.6 "In his plea, Patel admitted…", đ.8 "A co-defendant described…", đ.9 "Patel was prosecuted…", đ.10 "U.S. District Judge David Hittner… accepted", đ.11 "A total of 24 domestic defendants…"; N5 đ.12 "The indictment in this case… Charges remain pending…").

## 2. Trạng thái vụ (HIEN-CHUONG §3 luật 4) — kiểm ngày chốt lời 01/11/2026 (UTC)

| Mục | Kết quả | Dùng trong lời? |
|---|---|---|
| Patel — BOP | 1 bản ghi "HITESH MADHUBHA PATEL", 50 tuổi, FCI Fort Dix, `projRelDate` 10/06/2034 (định dạng Mỹ). Khớp tên đệm + tuổi (N5: 44 tuổi năm 2020) nhưng BOP không ghi số vụ → **chưa xác minh tuyệt đối** | **Không** — lời không nêu ngày ra tù hay nơi giam |
| Patel — ân xá/giảm án | N7: 0 kết quả (Trump 2025–nay cập nhật 20/10/2026; Biden). Trang Trump 2017–2021: URL `…/pardons-granted-president-donald-trump` và `…/commutations-granted-president-donald-trump` trả **404** → **chưa mở được** | Không nói gì về ân xá |
| Patel — kháng cáo | N8 chưa mở được | Không nói gì về kháng cáo |
| HGLOBAL và các bị cáo ở Ấn Độ | Nguồn mới nhất mở được: N5 đ.12 (11/2020) "Charges remain pending for other India-based defendants. They are presumed innocent…". Trang nạn nhân DOJ `us-v-hglobal` trả 404 (kho §5). **Không suy trạng thái sau 7/2018 (HGLOBAL) / 11/2020 (nhóm)** | Có — luôn gắn mốc "As of July 2018 / As of November 2020" (câu ◐ nhịp 4b, quyết định chủ dự án MR-5) |
| 24 bị cáo ở Mỹ | N3, N4 đ.11: đã kết án, tuyên án | Theo nhóm, không tên |

**Kiểm lại ở ngày đăng** (luật 4): BOP, N7 (và trang Trump 2017–2021 nếu tìm được URL chính thức), trạng thái HGLOBAL/bị cáo ở Ấn Độ qua API DOJ (tìm "HGLOBAL", "Hitesh Patel", "call center Ahmedabad").

## 3. Chữ trích trên hình (đối chiếu nguyên văn)

| Câu | Chữ trên hình | Nguồn | Khớp |
|---|---|---|---|
| S032 | "the top person in India and the boss for whom most of the other defendants worked" — a co-defendant, according to the Justice Department | N4 đ.8 (cũng N5 đ.10) | nguyên văn |
| S061 | "U.S. government agencies do not make these types of calls" — Homeland Security Investigations, Oct. 27, 2016 | N2 đ.5 (lời Executive Associate Director HSI) | nguyên văn (trích giữa câu) |
| S029 | Câu ◐ HGLOBAL (bản chữ số) | N1 tr. 1; N3 đ.15; N5 đ.12 | câu của dàn truyện nhịp 4b, đổi số sang chữ số cho hình |
| S045, S055 | "Restitution: $8,970,396" | N3 đ.11; N5 đ.2 (ghi "$8, 970,396" — lỗi gõ khoảng trắng của thông cáo) | số khớp |

## 4. Trang hồ sơ dùng làm hình (TL) và trang cấm
- **Dùng được:** N1 tr. 3 (đầu "General Allegations", ¶1(a)–(b)) — crop phần tiêu đề và ¶1(a); N1 tr. 6 phần định nghĩa hawala (¶2(g), dòng "money can be made available internationally without actually moving it").
- **Cấm crop:** N1 tr. 1 (tên d.b.a. trùng thương hiệu lớn; danh sách bị cáo chưa xử), N1 tr. 7 (bảng tên bị cáo HGLOBAL — chỉ được dựng lại **ô chữ** "HGLOBAL" kèm câu ◐, không ảnh trang), N1 tr. 4–6 ¶2(a), (e), (f) (thao tác thẻ/dữ liệu), mọi trang có tên người chưa xử, ảnh chụp thông cáo N2 đ.11–12 (thành phố nạn nhân), N3 đ.14 (thao tác chi tiết, tên thẻ quà tặng).
