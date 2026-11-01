# Kiểm lời độc lập MR-3b — câu đổi/mới (01/11/2026)

> Mỗi vòng một tác tử **mới**, không đọc `loi.json`, `LOI.md`, `SHOT.md`, `UOC-CHI.md`, `kiem/**`, `reports/**`, `docs/dan-truyen/**`, `docs/ung-vien/**`, git log/diff; chỉ đọc HIEN-CHUONG, NGUON.md và mở nguồn gốc (PDF trong `ho-so/`, ảnh/text trang; DOJ qua API chính thức; trang khác curl thường một lần, 403 → "chưa mở được", không đổi UA, không vượt).
> Phạm vi: thẻ KBCB (6 chỗ: S008, S045 đọc; S019, S033, S072, S076 chữ trên hình) và P21 viết lại (S093–S105). Câu khác không đổi chữ (P11, P16 giữ nguyên theo lệnh).
> Ký hiệu: **K** khớp · **MH** mạnh hơn nguồn · **S** sai · **KKĐ** không kiểm được.

| Vòng | Câu | Chấm | Tầng | Làm theo được ngay? | Bằng chứng / ghi chú | Xử lý |
|---|---|---|---|---|---|---|
| 1 | KBCB "…not accused of any wrongdoing; according to the SEC, neither company ever did business with 1inMM." | vế 2 K (qua N1 tr. 13 ¶78); vế 1 **MH nhẹ** | KBCB đúng | Không | N2, N3 **403 (chưa mở được ở vòng này)**; N1 tr. 13 ¶78 "never had any contractual or other business relationship with HBO or Netflix"; bị đơn N1 tr. 1 / bị cáo N6 tr. 1 chỉ Horwitz (+1inMM) → "not accused" chỉ đứng được **trong các vụ này** | Đổi cả 6 chỗ → "…not accused of wrongdoing **in these cases**…"; thêm nguồn N1 tr. 1, N1 tr. 13 ¶78, N6 tr. 1 |
| 1 | S093 | K | CHUNG | Không | 3 + 5 + 1 khớp các câu sau | — |
| 1 | S094 ("the six-month note… which is seventy percent a year") | K, góp ý | ◐ | Không | N1 tr. 6 ¶25: bảng có 4 kỳ phiếu 6 tháng (35 %, 35 %, 36 %, 35 %); 744.500 → 1.004.084 ≈ 34,9 %/kỳ ≈ 69,7 %/năm lãi đơn | "the" → "a … listed in"; thêm "roughly" |
| 1 | S095 | K | ◐ | Không | N12 (API DOJ, 22-027) "operating a Ponzi scheme… using victims' money to repay earlier investors" | — |
| 1 | S096, S097, S098 | K | ●T | Không | N7 tr. 12 dòng 4–6; tr. 10 dòng 1–6; tr. 9 dòng 23–24 | — |
| 1 | S099 ("the notes, the collateral and the deal papers") | **MH nhẹ** | ●T | Không | N7 tr. 9–11: giấy tờ (note, điều khoản chuyển nhượng, bản hợp đồng giả) do Horwitz đưa; "collateral" tự nó không phải giấy | → "the collateral **papers**" |
| 1 | S100 | K | ◐ | Không | N1 tr. 5 ¶18 "Neither 1inMM nor its securities offerings are registered with the Commission"; vế "friends" N12, N1 ¶28, ¶30 | — |
| 1 | S101 ("smooth payments, then sudden delays…") | K, góp ý | ●T | Không | N7 tr. 11 dòng 16–20; "sudden" không có trong nguồn | → "missed payments" (vòng 2) |
| 1 | S102, S103 | K | CHUNG | Không | N19, N20 HTTP 200 | — |
| 1 | S104 ("report suspected investment fraud… to the FTC") | **KKĐ một phần** | CHUNG | Không | N18 sec.gov **403**; N21 HTTP 200 nhưng không kiểm được FTC nhận "investment fraud" | Tách: SEC nhận tip; FTC "report a scam" |
| 1 | S105 ("Every fact in this story…") | **KKĐ** (khẳng định toàn tập) | CHUNG | Không | phép tính, bài học không phải "fact from records" | → "The case facts in this story come from…" |
| 2 | KBCB "…not accused of wrongdoing in these cases; according to the SEC, neither company ever did business with 1inMM." | **K** | KBCB đúng | Không | N1 tr. 1; N6 tr. 1; N1 tr. 13 ¶78 dòng 18–20; N1 tr. 9 ¶49; N7 tr. 10 dòng 24–26. Đứng được không cần N2/N3 | Dòng nguồn trên thẻ thêm "SEC Complaint ¶78" |
| 2 | S094 (mới) | **K** | ◐ | Không | N1 tr. 5–6 ¶25; tính lại ≈ 69,7 %/năm | — |
| 2 | S099 (mới) | **K** | ●T | Không | N7 tr. 9 dòng 27–28; tr. 10 dòng 14–18, 27–28; tr. 11 dòng 1–2, 11–12 | — |
| 2 | S101 ("smooth payments, then missed payments blamed on a partner…") | K, **lưu ý** | ●T | Không | "smooth" không có trong plea (chỉ ở N1 ¶47, ◐) | Bỏ "smooth payments"; vế "would resume" theo N7 tr. 11 dòng 20 → vòng 3 |
| 2 | S104 (mới) | vế FTC **K**; vế SEC **KKĐ** | CHUNG | Không | N21 "reporting fraud, scams…"; N18 **403** | Giữ: N18 đã mở HTTP 200 ở MR-3 (NGUON.md §1, UA khai báo của kênh); **mở lại trước ngày đăng** |
| 2 | S105 (mới) | **K** | CHUNG | Không | "case facts" giới hạn đúng; mô tả video chưa có | Mô tả video chỉ liệt kê nguồn đã mở |
| 3 | S101 ("missed payments blamed on a partner; he admitted falsely blaming the streaming platforms…, and claiming that payments would resume.") | vế thừa nhận **K**; vế "a partner" **nghiêng MH** | ●T | Không | N7 tr. 11 dòng 16–23 ("falsely reassured … caused by the actions of the online streaming platforms, and that payment on the notes would resume"); tr. 11 dòng 8–15: nền tảng **không** phải đối tác → "a partner" dễ hiểu là đối tác thật (luật 8e) | → "blamed on **someone else**"; thẻ tổng kết dòng 5 đổi theo |
| 4 | S101 ("Five: missed payments blamed on someone else; he admitted falsely blaming the streaming platforms for the missed payments, and claiming that payments would resume.") | **K** | ●T đúng | Không | N7 tr. 11 dòng 16–20, 25–27; tr. 8 dòng 12–16 (thừa nhận statement of facts). Rủi ro hiểu nền tảng là đối tác/có lỗi: **thấp** ("falsely" trước "blaming", không nêu tên) | Gợi ý không bắt buộc (thêm "which he had not even been in contact with") — **không áp**, giữ câu ngắn; KBCB đã nói ở P01, P08 và thẻ P15 |

## Tổng sau vòng 4
Câu đổi/mới (KBCB × 6, S093–S105): **sai 0 · mạnh hơn 0**; tầng đúng tất cả; "làm theo được ngay?" **Không** ở mọi câu.
**Còn KKĐ một vế (không phải sai):** S104 vế SEC dựa N18 — tác tử không mở được (403 với curl thường); N18 đã mở HTTP 200 ở MR-3 bằng UA khai báo của kênh (NGUON.md §1). N2, N3 cũng 403 ở các vòng này; thẻ KBCB nay đứng được trên N1 ¶78 (đã mở). → **Mở lại N2, N3, N18 bằng UA khai báo trước ngày đăng.**
Kiểm máy `scripts/mr3/loi_md.py` K1–K8: ĐẠT.
