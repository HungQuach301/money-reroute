# NGUỒN — Tập 3 · "Prince Charming": đường dây lừa tình / Olayinka Ilumsa Sunmola (`tap03-romance-sunmola`)

> MR-K23 · 01/11/2026 (UTC; 02/11/2026 sáng giờ Hà Nội) · NHÁP G1. Mã N1–N8 giữ nguyên như `docs/kho-de-tai/romance-sunmola.md` §8 và `docs/dan-truyen/romance-sunmola.md` §7.
> **Quy ước trang/đoạn:** N2 (opinion 7th Cir., 18 trang) = số trang in ở đầu trang, trùng số trang PDF (`pdftotext -layout`). N1 (thông cáo DOJ USAO S.D. Ill., API chính thức) **không đánh số đoạn** — HTML tách đoạn không ổn định (một đoạn bị cắt đôi giữa câu "manipulating them into wiring / him money…") → dẫn bằng **vài chữ đầu đoạn/câu** trong ngoặc kép.
> Mọi nguồn mở **đường chính thức**, không vượt rào; 403/404 ghi "chưa mở được", **không dùng**. Không gửi thông tin cá nhân của chủ dự án trong request (curl mặc định).

## 1. Bảng nguồn

| Mã | Cơ quan | Tài liệu | Số vụ / docket | Ngày | URL | Trang/đoạn dùng trong lời | Đã mở (ngày UTC, HTTP, đường) | Tệp + SHA-256 |
|---|---|---|---|---|---|---|---|---|
| N1 | DOJ USAO S.D. Ill. | Thông cáo "'Prince Charming' Behind Bars: Nigerian Romance Scammer Nets 27-Year Prison Sentence" (tiêu đề của DOJ — kênh **không** dùng chữ "Scammer" ở giọng kể, luật 8d) | (3:13-cr-30272 theo N2) | 02/02/2017 | https://www.justice.gov/usao-sdil/pr/prince-charming-behind-bars-nigerian-romance-scammer-nets-27-year-prison-sentence | các câu dẫn bằng chữ đầu trong `loi.json` | 01/11/2026, HTTP 200, API `justice.gov/api/v1/press_releases.json?parameters[title]=Prince Charming` (1 kết quả) | `ho-so/romance-sunmola/doj-api-sdil-2017-02-02.json` — `09ef97f8c2e764b8dbfef3a0abf3d55821c629dbfa600ce005d04d12c56f9680` |
| N2 | Toà Phúc thẩm Khu 7 | Opinion (Bauer), United States v. Olayinka I. Sunmola | No. 17-1299; USDC No. 3:13-cr-30272-DRH-1 | 16/04/2018 | https://media.ca7.uscourts.gov/cgi-bin/OpinionsWeb/processWebInputExternal.pl?Submit=Display&Path=Y2018/D04-16/C:17-1299:J:Bauer:aut:T:fnOp:N:2140267:S:0 | tr. 1, 2, 3, 4, 5, 6–7, 8, 8–9, 10, 11–12, 14, 17, 18 | tệp repo (LFS), SHA khớp kho §8; `pdftotext`, đọc đủ 18 trang ở MR-K23 | `ho-so/romance-sunmola/ca7-opinion-17-1299-2018.pdf` — `cc362fa04d95dd71c5af59f50a3f2e6ab4b0393a9c65f54754e7ab710959953b` |
| N3 | Federal Bureau of Prisons | Inmate Locator (JSON chính thức `bop.gov/PublicInfo/execute/inmateloc?todo=query&output=json&nameFirst=olayinka&nameLast=sunmola`) | — | tra 01/11/2026 | https://www.bop.gov/inmateloc/ | S064: 1 bản ghi duy nhất "OLAYINKA ILUMSA SUNMOLA", #11507-025, FCI Oakdale I, `projRelDate` 09/20/2037, `actRelDate` trống | 01/11/2026, HTTP 200 | phản hồi 396 byte, SHA-256 `8066b7b61b0a42afa90e1d207349a168739abe2268adaff9f533c25aa3d8171c` (không lưu) |
| N4 | DOJ Office of the Pardon Attorney | Clemency Grants by President Donald J. Trump (2025–Present) | — | cập nhật 20/10/2026 | https://www.justice.gov/pardon/clemency-grants-president-donald-j-trump-2025-present | **không dùng trong lời** (§2) | 01/11/2026, HTTP 200; tìm "Sunmola": 0 | không lưu (SHA `263d2e35…670a`) |
| N5 | DOJ Office of the Pardon Attorney | Commutations / Pardons Granted by President Joseph Biden (2021–2025) | — | — | https://www.justice.gov/pardon/commutations-granted-president-joseph-biden-2021-2025 ; https://www.justice.gov/pardon/pardons-granted-president-joseph-biden-2021-2025 | **không dùng trong lời** (§2) | 01/11/2026, HTTP 200 ×2; tìm "Sunmola" trong HTML: 0 (PDF quét đính kèm trang giảm án: kho §8 — không tìm chữ được) | không lưu |
| N6 | FBI / IC3 | Public Service Announcement I-080519-PSA "Cyber Actors Use Online Dating Sites To Conduct Confidence/Romance Fraud And Recruit Money Mules" | — | 05/08/2019 | https://www.ic3.gov/PSA/2019/PSA190805 | "the elderly, women, and those who have lost a spouse are often targeted"; "Most cyber criminals do not use their own photographs… A reverse image search can determine if a profile picture is being used elsewhere on the internet"; "Never send money to someone you meet online"; "Claims to be… a U.S. service member serving overseas"; "Asks for money, goods…"; "Reports a sudden personal crisis…" | 01/11/2026, HTTP 200, curl mặc định | không lưu (SHA phản hồi `b40f7ca1…c7ce8`) |
| N7 | FBI / IC3 | Internet Crime Complaint Center (trang chủ, "File a Complaint") | — | — | https://www.ic3.gov/ | S078 | 01/11/2026, HTTP 200 | không lưu (SHA `d2b971…d6fa`) |
| N8 | FTC | ReportFraud.ftc.gov (trang chủ) | — | — | https://reportfraud.ftc.gov/ | S078 | 01/11/2026, HTTP 200 | không lưu (SHA `874400…387c`) |
| — | Toà S.D. Ill. | Cáo trạng, judgment, docket 3:13-cr-30272 | 3:13-cr-30272-DRH-1 | — | — | **không dùng** — mọi câu về tội danh dựa N2 tr. 3 | **chưa mở được** (kho §8: CourtListener 403/401; PACER cấm — K5 hoãn PACER) | — |
| — | FTC / FBI | consumer.ftc.gov "What to know about romance scams"; fbi.gov "Romance Scams" | — | — | (dàn truyện §7) | **không dùng** | **chưa mở được** (MR-D23: HTTP 403; không thử lại bằng UA khác) | — |

## 2. Trạng thái vụ (HIEN-CHUONG §3 luật 4) — kiểm ngày chốt lời 01/11/2026 (UTC)

| Mục | Kết quả | Dùng trong lời? |
|---|---|---|
| BOP | 1 bản ghi duy nhất khớp đủ họ, tên, tên đệm (N3): đang thụ án, FCI Oakdale I, dự kiến ra 20/09/2037 | **Có** (S064, tầng TT, gắn mốc "As of November 2026"). Kiểm lại ngày đăng |
| Ân xá / giảm án | N4, N5: 0 kết quả (HTML); PDF quét Biden chưa tìm chữ được → kiểm **một phần**; BOP vẫn ghi ngày ra 2037 → không có dấu hiệu được giảm án tới mãn hạn | Không nói gì về ân xá |
| Phúc thẩm | N2: AFFIRM 16/04/2018. Trích dẫn reporter "887 F.3d 830" **chưa đối chiếu** → trên hình dùng "No. 17-1299 (7th Cir. Apr. 16, 2018)" | Có (S054) |

## 3. Chữ trích trên hình (đối chiếu nguyên văn)

| Câu | Chữ trên hình | Nguồn | Khớp |
|---|---|---|---|
| S006 | "Prince Charming" — U.S. Attorney's Office, Southern District of Illinois | N1 ("…believe that he was her "Prince Charming,"…") | nguyên văn |
| S008 | "the most devastating crime one could ever imagine without someone laying hands or even eyes on another human being" — the sentencing judge, as quoted by the U.S. Court of Appeals for the Seventh Circuit | N2 tr. 17 | nguyên văn **bản của toà phúc thẩm** (N1 trích khác chữ: "…without laying hands…" — không dùng bản N1) |
| S033 | "With at least one woman, it went further: he threatened to expose private images." | N2 tr. 2 ("threatened to post photos of a third woman") | **câu khái niệm của kênh** (không phải trích), đúng một lần, thẻ chữ, không đọc (K3 MR-D23) |
| S049, S051 | "Intended loss: $2,054,972.66"; "Restitution: $1,707,260.98 → amended to $1,669,050.98" | N2 tr. 4; tr. 5 | số khớp |

## 4. Trang hồ sơ dùng làm hình (TL) và trang cấm
- **Dùng được:** N2 tr. 1 (đầu opinion: tên vụ, số vụ, ngày quyết) và tr. 18 ("For the foregoing reasons, we AFFIRM.").
- **Cấm crop:** N2 tr. 2 (đoạn bóc lột/ảnh riêng tư; bang của nạn nhân), tr. 8 (tổ hợp tuổi + hoàn cảnh nhận diện nạn nhân), tr. 4 và 14 (tên điều tra viên), tr. 11–12 (thao tác thẻ/cửa hàng nhận hàng), tr. 14 (tên dịch vụ chuyển tiền, tên trang hẹn hò). Không ảnh chụp thông cáo N1 (tên giả bị cáo dùng, tên trang hẹn hò, lời nạn nhân, chi tiết tự sát/váy cưới, đoạn ảnh khiêu dâm).
