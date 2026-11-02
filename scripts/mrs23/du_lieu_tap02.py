"""MR-S23 · Dữ liệu SHOT2 tập 2 (irs-callcenter-patel). Đọc bởi scripts/mrs23/shot2.py. Quy ước mã: xem docstring shot2.py."""
TAP, THU_MUC, TIEN_TO = "tap02", "tap02-irs-callcenter-patel", "p"
TEN = "Tập 2 · Call center mạo danh IRS/USCIS / Patel"
CHI_TOI = []
HG = ("HGLOBAL was also charged; like every defendant who has not been convicted, it is presumed innocent. As of July 2018, the "
      "India-based call centers charged had yet to be arraigned; as of November 2020, the Justice Department said charges remained pending for other India-based defendants.")

NV = {
 "N1": ("Người nghe máy (đại diện người nhận cuộc gọi; KHÔNG phải nạn nhân cụ thể nào trong hồ sơ)",
        "Đàn ông ~55 tuổi tự nghĩ ra, tóc muối tiêu cắt ngắn, râu ngắn, kính gọng mảnh, áo len cardigan xanh navy ngoài sơ mi kẻ ô; nhà bếp gỗ ấm. Mặt cách điệu, không phóng đại nét, không gắn sắc tộc",
        "Được có mặt cách điệu, nhãn ILLUSTRATIVE. **Không** dùng cho câu về nạn nhân cụ thể (S009, S010) — ở đó chỉ vật"),
 "N2": ("Người con (đại diện người thân, chỉ ở P11)", "Phụ nữ ~30 tuổi tự nghĩ ra, tóc đen buộc đuôi ngựa, áo khoác ô liu; luôn ngồi cạnh N1",
        "Được có mặt cách điệu, nhãn ILLUSTRATIVE"),
}
NGUOI_THAT = [
 ("Patel (bị cáo ●)", "Bóng ngược sáng, lưng, tay/tay áo sơ mi trơn sáng màu; trang phục trung tính, không phụ kiện tôn giáo/dân tộc; nhãn tên chỉ ở thẻ chữ", "Không mặt, không góc 3/4"),
 ("Người gọi, quản lý call center, runner, đồng bị cáo (không tên)", "Chỉ bóng xa trong phòng tối, tai nghe trên bàn, tay trên bàn phím/quầy", "Không mặt; không biển hiệu, không chữ trên màn hình"),
 ("Nạn nhân trong hồ sơ (người 85 tuổi, người mất $136,000)", "Không vẽ người: chỉ đồ vật (ghế trống, tờ giấy trắng, lịch trơn)", "KBCB — không nhận diện"),
]
LUAT_RIENG = [
 "**Riêng tập 2** (SHOT.md MR-K23, giữ): không dựng cuộc gọi — không thoại người gọi, không chữ kịch bản, **không số điện thoại** (kể cả giả), không giao diện ứng dụng gọi/nhắn; màn hình = khối trắng mềm trơn; thẻ nhựa **trắng trơn**; không logo/con dấu/huy hiệu IRS, USCIS, DHS, HSI, DOJ, CRA, ATO — tên cơ quan chỉ chữ trơn; không tên 4 call center còn lại, không tên thương hiệu thẻ/dịch vụ chuyển tiền.",
 "**Ahmedabad / Ấn Độ / Singapore:** không biểu tượng tôn giáo, trang phục dân tộc, cảnh đường phố định kiến; chỉ bản đồ phẳng tự vẽ (L2) và nội thất văn phòng trung tính.",
 "**Tên call center ở P05 (S028):** mọi dòng có tên kèm nguyên câu ◐ (máy kiểm KB quét cả tệp này).",
]

SC = {
 # P00
 "S001": ["E#bep_sang_dt: A smartphone lying face-up on a wooden kitchen table at dusk, its screen dark, a mug beside it, warm window light; nobody present.", "K1*1.6"],
 "S002": ["N1#n1_nghe: The listener (N1) at a warm wooden kitchen table at dusk, holding a phone to his ear, worried; the phone is dark, nothing on it.", "G01*1.5"],
 "S003": ["E#bep_up: A quiet kitchen table at dusk with a phone lying face-down beside a mug; warm window light; nobody present.*1"],
 "S004": ["G02*1.4", "R#vp_dem: A long dim office at night seen from the back of the room: rows of desks with distant workers as soft dark silhouettes against glowing blank screens; no faces."],
 "S005": ["R#patel_cua: A man seen strictly from behind, a dark silhouette in a plain light shirt standing at a tall window over a hazy night city with no landmarks; no face."],
 "S006": ["G02*1"],
 "S007": ["E#soi_chi: Symbolic still life: a dark phone on the left and a small stack of plain banknotes with no markings on the right, a thin glowing thread linking them across a dark table.", "E: Night aerial of a generic coastline with a faint dotted arc of light crossing the ocean toward another shore; no landmarks."],
 "S008": ["@vp_dem"],
 # P01
 "S009": ["E#ghe_trong: An empty armchair beside a side table with a landline-style phone and a sheet of blank white paper, late afternoon light, nobody present.", "E#lich: A plain wall calendar with blank squares, no numbers, one square softly lit."],
 "S010": ["E: A kitchen table seen over many days: a phone on the table at morning, noon and night, light changing, nobody present.", "@lich"],
 "S011": ["E: A quiet hallway with an empty coat hook and a small table holding a face-down phone; soft evening light."],
 # P02
 "S012": ["E#bac_toa: Wide shot of empty stone steps and tall classical columns at dawn, plain stone façade with no lettering, nobody present.", "G03*1.2"],
 "S013": ["G03*1.5"],
 "S014": ["G03*1.5", "E: Two clocks on a dark wall showing different times, symbolic of two countries, plain faces with no numbers."],
 "S015": ["G03*1", "E#giay_roi: Thousands of tiny paper slips drifting down through a beam of light in a dark room; symbolic, blank paper."],
 # P03
 "S016": ["E#binder: An open binder with blank white tabbed dividers on a dark desk under a lamp; pages blank."],
 "S017": ["T01*1.4", "G04*1"],
 "S018": ["T02*1.4", "G04*1"],
 "S019": ["G04*1.5", "E: An empty envelope lying open on a table, nothing inside, cold light."],
 "S020": ["G04*1", "E: A globe on a dark desk slowly lit along three distant regions by a thin lamp beam; no labels on the globe."],
 "S021": ["@binder"],
 # P04
 "S022": ["E#vp_trong: Night interior of a long open-plan office with rows of empty desks, headsets resting on them, every monitor a soft blank white glow; nobody present.", "K2*1.5"],
 "S023": ["R: Close-up of hands on a keyboard beside a headset on a desk, lit by a blank glowing screen; only hands and sleeves.", "G05*1"],
 "S024": ["G05*1.5", "E: An empty manager's glass office overlooking a dim open-plan floor at night, a desk lamp on, nobody present."],
 "S025": ["E: Rows of plain unlabeled file boxes on metal shelves in a dim storeroom, one box open with blank index cards.", "R: Hands in a plain jacket sleeve counting plain unmarked banknotes on a car seat at night, street light through the window; only hands.", "G05*1.2"],
 "S026": ["E: Two plain ledgers on two separate desks in two different rooms, each lit by one lamp; symbolic of two distant brokers.", "G05*1"],
 # P05
 "S027": ["G06*1.5", "E#skyline: A night skyline of a generic large city seen from far away, warm haze, no landmarks or signs."],
 "S028": ["R#patel_ban: A man seen strictly from behind at a desk at night, a dark silhouette in a plain light shirt reviewing blank papers; no face.", "G06*1.4"],
 "S029": ["G06*1"],
 "S030": ["E#so_do_trong: A plain organization chart drawn as empty boxes and lines on a whiteboard, no writing, cold office light."],
 "S031": ["E: A laptop on a dark desk showing a soft blank white glow, a stack of blank monthly reports beside it.", "@so_do_trong"],
 "S032": ["Q01*1.4", "@patel_ban"],
 "S033": ["Q01*1"],
 # P06
 "S034": ["G07*1.4", "E#the_trang: Plain white plastic cards fanned on a dark glass counter under one warm lamp; completely blank cards."],
 "S035": ["K3*1.2", "G07*1"],
 "S036": ["G07*1", "E#the_ho_so: A thick stack of blank index cards held by a rubber band on a dark desk, symbolic of personal records, nothing written."],
 "S037": ["T03*1.5", "E: An old wooden desk with a closed notebook and a single brass key, warm lamp light; a quiet back room."],
 "S038": ["T04*1", "G08*2"],
 "S039": ["G08*1", "E: A bank lobby at closing time, empty counters, soft light, no signage."],
 "S040": ["R: Several pairs of hands passing a plain envelope quickly from one to the next across a dark car hood at night; only hands and sleeves.", "G07*1"],
 "S041": ["G09*3"],
 "S042": ["E#dau_chan: Footprints in wet sand fading as a wave washes over them at dusk; symbolic of a trail disappearing.", "@soi_chi"],
 # P07
 "S043": ["E#hanh_lang: A long empty federal courthouse corridor with polished floor and wooden benches, morning light, no signs.", "G10*1.5"],
 "S044": ["G10*1", "R: Silhouettes of several people seated on a courtroom bench seen from the back row; heads and shoulders only as dark shapes."],
 "S045": ["G10*1.2"],
 "S046": ["E#ghe_bi_cao: An empty chair at a defense table in a quiet courtroom, papers blank; soft light.", "G11*1"],
 "S047": ["@patel_cua", "G11*1"],
 "S048": ["E#canh_may_bay: Clouds seen from above at sunset through an airplane window, the wing plain white with no markings; nobody present.", "K4*1.3"],
 # P08
 "S049": ["E: An airport terminal corridor at night, glass walls, rows of empty seats, no signs or text.", "G11*1"],
 "S050": ["G11*1", "@canh_may_bay"],
 # P09
 "S051": ["E#phong_xu: An empty wood-paneled courtroom in soft morning light, plain wooden walls and benches, dust drifting in a sunbeam.", "G11*1.2"],
 "S052": ["E#ban_tham_phan: A judge's bench seen from the empty gallery, a gavel resting on its block, nobody present."],
 "S053": ["G12*2"],
 # P10
 "S054": ["@ban_tham_phan", "G11*1.4"],
 "S055": ["G12*1.2"],
 "S056": ["E: A dark map table with three unlit desk lamps, one switched off; symbolic of open cases still pending.", "@ghe_bi_cao"],
 # P11
 "S057": ["E#bep_sang: Morning light falling across the same kitchen table, a phone lying face-down, a closed notebook and pen; calm, nobody present.", "G13*1"],
 "S058": ["@vp_trong", "G05*1"],
 "S059": ["@the_trang", "G07*1"],
 "S060": ["E: A mailbox at the end of a quiet driveway in morning light holding a single plain white envelope; no address or text.", "G13*1.8"],
 "S061": ["Q02*1.5"],
 "S062": ["G14*1", "@n1_nghe"],
 "S063": ["G14*1", "E#hen_gio: A kitchen timer on a counter ticking, close-up, warm light."],
 "S064": ["G14*1", "@the_ho_so"],
 "S065": ["G14*1", "@ghe_trong"],
 "S066": ["G14*1", "@giay_roi"],
 "S067": ["@bep_up"],
 "S068": ["K5*1.3", "N1: The listener (N1) at the kitchen table in morning light, calm, the phone face-down beside him; he writes on a blank notepad."],
 "S069": ["N2: The listener (N1) and his adult daughter (N2) talking at the kitchen table, warm afternoon light, a teapot between them.", "N2: Close-up of the daughter's (N2) hand resting on her father's (N1) hand on the table, reassuring."],
 "S070": ["G15*1.5"],
 "S071": ["G15*1"],
}
OV = {
 "S003": [("kbcb", "The IRS and U.S. Citizenship and Immigration Services had nothing to do with these calls. (đọc — chữ phụ đề)")],
 "S005": [("ten", "Hitesh Madhubhai Patel · ● CONVICTED (2020)")],
 "S008": [("tieu_de", "Real cases from the public record · MONEY REROUTE")],
 "S028": [("ten_hglobal", "ô chữ tên + nguyên câu ◐ cùng khung, bật/tắt cùng lúc: " + HG)],
 "S029": [("the_hglobal", HG)],
 "S041": [("chu", "Framework used by this channel — not the indictment's words")],
 "S057": [("tieu_de", "3 LESSONS · 5 RED FLAGS · 1 RULE")],
 "S058": [("bai", "LESSON 1 · The scary call was the front of a chain")],
 "S059": [("bai", "LESSON 2 · Cards & wires = money cashed out fast")],
 "S060": [("bai", "LESSON 3 · The IRS mostly starts with mail")],
 "S068": [("bai", "1 RULE · Hang up. Look the agency up yourself.")],
}
L2 = {
 "G01": {"hoi": "Người gọi doạ điều gì, và đòi gì?", "noi_dung": "Bốn icon nét mảnh bật lần lượt theo lời: ARREST · PRISON · FINES · DEPORTATION → mũi tên hội tụ vào ô \"PAY\"", "nhan": "ô PAY (đỏ cam, nhịp đập nhẹ)", "tang": "● · admitted in plea, per DOJ"},
 "G02": {"hoi": "Ai, ở đâu, và kết cục ra sao?", "noi_dung": "Bản đồ phẳng: chấm \"Ahmedabad, India\" → cung nét đứt sang \"United States\" (hạt chạy) → thẻ tên chữ → bộ đếm 0 → 20 YEARS", "nhan": "20 YEARS đếm lên, dừng có vạch sáng", "tang": "S004 ● · per DOJ; S006 ● CONVICTED"},
 "G03": {"hoi": "Vụ án được mở ra thế nào, quy mô bao nhiêu?", "noi_dung": "Trục: Oct. 19, 2016 indictment → Oct. 27 unsealed: bộ đếm 61 defendants → tách hai cột \"U.S.: 20 arrested\" / \"India: 32 people + 5 call centers charged\" → ô mờ viền đứt \"Alleged at the time: tens of thousands of victims · hundreds of millions of dollars\"", "nhan": "số 61 đếm lên", "tang": "TT; S015 ◐ ALLEGED"},
 "G04": {"hoi": "Bốn kiểu cuộc gọi có điểm chung gì?", "noi_dung": "Bốn thẻ hiện theo lời: IRS impersonation · Immigration impersonation · \"payday loan\" · \"government grant\" → cả bốn đổ vào ô \"PAY FIRST\" → mũi tên trả về rỗng \"nothing in return\"; S020 thêm hai thẻ chữ trơn \"Canada tax agency\" · \"Australian tax office\" · \"debt collection\"", "nhan": "ô PAY FIRST", "tang": "◐ ALLEGED (S020 per DOJ)"},
 "G05": {"hoi": "Sau cuộc gọi là ai — một người hay một dây chuyền?", "noi_dung": "Sơ đồ dây chuyền icon (không người, không tên): DATA BROKERS → CALLERS → CALL CENTER OPERATORS → PAYMENT PROCESSORS → RUNNERS (U.S.) ← DOMESTIC MANAGERS; nhánh HAWALADAR; hạt tiền chạy từ nạn nhân qua chuỗi", "nhan": "RUNNERS (U.S.) — chỗ tiền ra khỏi hệ thống", "tang": "◐ ALLEGED · Superseding Indictment pp. 4–6"},
 "G06": {"hoi": "Một call center hay cả một mạng lưới?", "noi_dung": "Bản đồ Ahmedabad phẳng, 5 chấm KHÔNG tên nối nhau (shared scripts · lists · payments, hạt chạy qua lại) → S028 một chấm sáng; ô chữ tên kèm nguyên câu ◐ cùng khung: " + HG, "nhan": "đường nối giữa 5 chấm", "tang": "S027 ◐; S028 ● PATEL — admitted in plea, per DOJ; S029 ◐ ALLEGED"},
 "G07": {"hoi": "Tiền rời nạn nhân bằng cách nào, và nhanh cỡ nào?", "noi_dung": "Dòng hạt: VICTIM → \"prepaid card / wire\" → CALL CENTER báo → RUNNERS (U.S.) toả nhiều nhánh → \"cashed out & laundered\"; đồng hồ nhỏ chạy rất nhanh chữ \"immediately\"", "nhan": "đồng hồ \"immediately\"", "tang": "● · admitted in plea, per DOJ; S036 ◐; S040 ● U.S. co-defendants"},
 "G08": {"hoi": "Hawala \"chuyển\" tiền mà không chuyển tiền thế nào?", "noi_dung": "Hai người môi giới icon ở hai nước: tiền vào môi giới 1 → môi giới 2 trả ra ở nước kia; giữa hai nước mũi tên tiền thẳng bị gạch (\"no money crosses\") → sau đó giao dịch ngược chiều bù trừ (hai mũi tên ngược). Mức khái niệm, không thao tác", "nhan": "vạch gạch đỏ cam trên đường biên — tiền không đi qua", "tang": "◐ ALLEGED · Superseding Indictment p. 6 ¶2(g)"},
 "G09": {"hoi": "Vì sao tiền rất khó lần lại?", "noi_dung": "Hai bước của kênh: 1 PLACEMENT — hạt đi vào \"system\" (cards, wires) → 2 LAYERING — hạt tách qua nhiều tay, đổi hình, dấu vết mờ dần; dòng nhỏ \"Framework used by this channel — not the indictment's words\"", "nhan": "dấu vết mờ dần ở bước 2", "tang": "CHUNG"},
 "G10": {"hoi": "Phía Mỹ của vụ kết thúc ra sao?", "noi_dung": "Lưới 24 ô trống lấp đầy dần (không tên, không mặt) → 3 bang chữ \"Texas · Arizona · Georgia\" → thang án \"probation → 20 years\" → \"Restitution: $8,970,396 (joint and several, 22 defendants)\" đếm", "nhan": "lưới 24 ô đầy", "tang": "● CONVICTED · U.S. co-defendants"},
 "G11": {"hoi": "Người đứng sau bị bắt và xét xử theo đường nào?", "noi_dung": "Trục: July 2018 (24 sentenced, ô của ông trống) → Sept. 2018 Singapore provisional arrest → Apr. 2019 extradition → Jan. 9, 2020 pleaded guilty (2 conspiracies) → Nov. 30, 2020 sentence; bản đồ India → Singapore → United States", "nhan": "mốc Sept. 2018 Singapore", "tang": "TT; ● CONVICTED"},
 "G12": {"hoi": "\"Thiệt hại thừa nhận\" khác \"bồi hoàn\" thế nào?", "noi_dung": "Thanh khoảng \"loss attributable (admitted): > $25M and < $65M\" (vùng mờ giữa hai vạch) → thanh riêng \"Restitution ordered: $8,970,396 to identified victims\" đếm; hai số ghi đúng chữ hồ sơ, không suy luận", "nhan": "khoảng $25M–$65M", "tang": "S053 ● · admitted, per DOJ; S055 ● CONVICTED"},
 "G13": {"hoi": "IRS thật liên lạc thế nào — khác cuộc gọi ra sao?", "noi_dung": "Chia đôi \"The calls\" vs \"The real IRS (per IRS)\": regular mail ✓ · no call demanding immediate payment by prepaid card/gift card/wire · chance to question or appeal ✓ · no threat of police/immigration arrest; nửa phải hiện sau", "nhan": "dòng \"does not call to demand immediate payment\"", "tang": "Source: IRS FS-2017-7"},
 "G14": {"hoi": "Năm dấu hiệu là gì?", "noi_dung": "5 thẻ RED FLAG lật lần lượt, mỗi thẻ gọi lại icon của đồ hoạ trước (G01 doạ · đồng hồ · thẻ trắng · lịch 20 ô · phí trước)", "nhan": "số thứ tự thẻ đang đọc", "tang": "theo từng câu"},
 "G15": {"hoi": "Báo ở đâu?", "noi_dung": "Thẻ nơi báo: \"Report IRS impersonation: tigta.gov\" · \"Report scams: reportfraud.ftc.gov\" + dòng \"case facts from public records — see description\"", "nhan": "tigta.gov", "tang": "CHUNG", "dong": False},
}
L3 = {
 "T01": ("`ho-so/irs-callcenter-patel/cao-trang-thay-the-4-16-cr-385-doc6-2016-10-19.pdf` tr. 3 (N1, PDF quét)", "đầu trang \"SUPERSEDING INDICTMENT / General Allegations\" + ¶1 a (tới \"immediately.\")", "impersonated U.S. Internal Revenue Service (IRS) officers", "Tiêu đề: SUPERSEDING INDICTMENT · U.S. v. PATEL et al. · No. 4:16-cr-385 (S.D. Tex.) · Dkt. 6 · p. 3; vùng đo bằng ảnh trang ở M-d (PDF không có lớp chữ)"),
 "T02": ("như T01, tr. 3", "¶1 b (USCIS scam)", "would be deported unless they paid a fine immediately", "Không lấy ¶1 c–d (không cần)"),
 "T03": ("như T01, tr. 6", "¶2 g từ \"g. Hawaladar\" tới \"…leaving a record of the transaction.\" — **cắt trên** ¶2 f, **cắt dưới** trước câu \"In a hawala system…\"", "without actually moving it", "Không lấy ¶2 f (thao tác dữ liệu, NGUON §4 cấm) và ¶3 (tên 5 nhóm call center)"),
 "T04": ("như T01, tr. 6", "¶2 g câu cuối \"The first hawaladar then owes … reverse direction.\"", "repaid by transactions conducted in the reverse direction", "Cắt dưới trước \"Call Centers\" / ¶3"),
 "Q01": ("N4 đ.8 (DOJ Press Release 20-19, Jan. 9, 2020)", "thẻ trích nền ngà", "“the top person in India and the boss for whom most of the other defendants worked” — a co-defendant, according to the Justice Department", "Chữ = `chu` S032 nguyên văn; S033 thêm dòng \"A co-defendant's description — not a court finding\""),
 "Q02": ("N2 đ.5 (DOJ Press Release 16-1257, Oct. 27, 2016)", "thẻ trích nền ngà", "“U.S. government agencies do not make these types of calls” — Homeland Security Investigations, Oct. 27, 2016", "Chữ = `chu` S061 nguyên văn; không logo HSI"),
}
CAM_L3 = "N1 tr. 1 (tên d.b.a.; danh sách bị cáo chưa xử), N1 tr. 7 (bảng tên bị cáo — tên call center chỉ dựng ô chữ kèm câu ◐), N1 tr. 4–6 ¶2(a), (e), (f), mọi trang có tên người chưa xử, ảnh chụp thông cáo N2 đ.11–12 và N3 đ.14."
VEO = {
 "K1": {"tu": "bep_sang_dt", "chuyen_dong": "The phone on the kitchen table lights up: its screen becomes a soft glowing blank white rectangle that pulses gently; dusk light shifts slowly on the table.", "neo_cuoi": "The table with only the glowing phone and the mug.", "qc": "Màn hình phải trơn (không số, không chữ, không giao diện cuộc gọi)"},
 "K2": {"tu": "vp_trong", "chuyen_dong": "Slow lateral dolly along the long dark office: rows of empty desks, headsets resting on them, every monitor a soft blank white glow; the room is still.", "neo_cuoi": "Empty desks and glowing blank monitors.", "qc": "Không biển hiệu, không chữ trên màn hình; không bóng người"},
 "K3": {"tu": "the_trang", "chuyen_dong": "A single blank white plastic card slides slowly across the dark glass counter and stops; warm lamp reflections; macro.", "neo_cuoi": "The counter holding only the blank cards.", "qc": "Thẻ phải trắng trơn (không số, không chip, không logo)"},
 "K4": {"tu": "canh_may_bay", "chuyen_dong": "View through an airplane window: the plain white wing over a sea of clouds, slow drift, warm sunset light rising.", "neo_cuoi": "Wing and clouds only.", "qc": "Không logo hãng trên cánh"},
 "K5": {"tu": "bep_sang", "chuyen_dong": "Morning light slowly brightens across the kitchen table; the face-down phone and the mug stay still; a curtain moves softly.", "neo_cuoi": "The table with the face-down phone in full morning light; nobody present.", "qc": "Không thêm người; không lật điện thoại"},
}
KET = "L2 `G16` thẻ tổng kết nền tối (3 + 5 + 1 dòng của SHOT.md §3, giữ nguyên chữ đã duyệt) + tigta.gov · reportfraud.ftc.gov + dòng khai AI; giữ 8 s"
NGUON = "L2 `G17` danh sách nguồn chạy chữ (N1–N5, N9–N11) + dòng khai AI (HIEN-CHUONG §6)"
NHAC = ["Giữ bảng nhạc `SHOT.md` §4 (MR-K23): P00 nền điện tử trầm −24 dB · P04–P06 nhịp ~90 bpm \"dây chuyền\" −22 dB · S047–S048 tăng, **cắt lặng 1 s** sau S048 (khớp K4) · P08–P10 piano thấp −26 dB · P11 sáng hơn −24 dB. Không tiếng chuông điện thoại thật, còi, còng tay. Đỉnh nhạc ≤ −18 dB dưới lời."]

# ---- cảnh chen (mật độ giữa, PHONG-CACH-HINH §5): thêm tranh cho câu dài, giữ ≤ 3 cảnh/câu ----
CHEN = {
 "S002": ["N1: Close-up of the listener's (N1) hand gripping the edge of the kitchen table, knuckles tense, the dark phone beside it."],
 "S003": ["E: A front door seen from inside a quiet home at dusk, closed and locked, a small lamp lit on a side table; nobody present."],
 "S004": ["E: A tall office tower at night in a hazy generic city, many lit windows, no signs or lettering."],
 "S006": ["E: A long empty prison corridor drawn in soft muted light, rows of closed plain doors; nobody present."],
 "S007": ["E: A single banknote shape made of light dissolving into particles over a dark table; symbolic, no markings."],
 "S008": ["E: An open notebook with a red pencil and three blank lines circled, warm desk lamp; symbolic of red flags."],
 "S009": ["E: A pair of reading glasses resting on a folded blank sheet of paper on a small table, lamp light."],
 "S010": ["E: A kitchen window at night with rain streaks, a phone glowing faintly on the sill; nobody present."],
 "S012": ["E: A dark wooden jury room with twelve empty chairs around a long table, soft morning light."],
 "S013": ["E: A heavy closed binder bound with a plain ribbon on a table, light falling on it; no text."],
 "S014": ["E: A row of plain metal handrails and empty waiting benches in a government building lobby at dawn, no signs."],
 "S015": ["E: An aerial view at night of a vast suburban grid with countless lit windows; symbolic of many households, no landmarks."],
 "S017": ["E: An old desk phone with its receiver off the hook resting on a stack of blank paper, cold light."],
 "S018": ["E: A plain folder of blank forms on a kitchen table beside reading glasses, afternoon light; no text."],
 "S019": ["E: A small cash box lying open and empty on a dark table under a lamp.", ],
 "S020": ["E: Three plain paper files fanned on a dark desk, each a different muted color, no labels."],
 "S021": ["E: A closed office door with frosted glass and no lettering, light behind it, a quiet corridor."],
 "S023": ["E: A stack of plain printed lists with every line blurred and unreadable, beside a headset on a desk."],
 "S024": ["R: Silhouettes of a few distant people standing in a dim office doorway, backlit, seen from behind; no faces."],
 "S026": ["E: An old brass weighing scale balanced on a desk, both pans empty, warm lamp."],
 "S027": ["E: Five small lamps on a dark table connected by thin glowing threads; symbolic network, no labels."],
 "S028": ["E: A leather office chair turned away from the camera at a large desk at night, the room empty."],
 "S029": ["E: A dark empty corridor with five closed plain doors in a row, soft light under each; no signs."],
 "S030": ["E: A plain index card pinned to a corkboard, the writing on it blurred and unreadable, desk lamp."],
 "S031": ["E: An email inbox suggested only as a soft glowing blank rectangle on a monitor in a dark room, a coffee cup beside it."],
 "S033": ["E: A scale of justice made of simple brass on a shelf, slightly out of focus, warm light."],
 "S034": ["E: A shop counter at night with a display rack of plain blank cards, lights dimmed, nobody present."],
 "S036": ["E: A row of blank identity-style cards laid face-down on a dark table, cold light; no faces, no text."],
 "S037": ["E: Two distant city skylines at dusk on either side of a dark sea, no landmarks; symbolic of two countries."],
 "S039": ["E: A plain bank deposit envelope sealed on a counter, nothing written on it, cool light."],
 "S040": ["E: A car parked under a single streetlight at night on an empty street, engine running, exhaust in the cold air; nobody visible."],
 "S041": ["E: A glass of clear water with a drop of ink spreading and fading until it disappears; symbolic of layering.", "E: A maze of narrow paper corridors seen from above, a single coin lost inside; symbolic."],
 "S043": ["E: A wooden gavel and block on a bench under soft courtroom light, nobody present."],
 "S045": ["E: Neat stacks of plain envelopes being sorted into slots on a wall, no addresses; symbolic of restitution to victims."],
 "S046": ["E: A map table with a lamp lighting only one region, the rest in shadow; no labels, symbolic of the India side."],
 "S047": ["E: A calendar page turning in the wind on an empty desk by an open window, no numbers visible."],
 "S048": ["E: A boarding gate at night seen through glass, an aircraft waiting, no logos or signs."],
 "S049": ["E: A pair of plain metal gates opening in an airport corridor at night, empty."],
 "S050": ["E: A government jet stair on a quiet tarmac at dawn, no markings; nobody present."],
 "S051": ["E: A pen resting on a single blank signature line on a white page, soft morning light."],
 "S052": ["@phong_xu"],
 "S053": ["E: A long measuring tape stretched across a dark table between two weights; symbolic of a range."],
 "S054": ["E: A heavy wooden door to a courtroom closing slowly, light slicing through; nobody present."],
 "S055": ["E: Plain envelopes arranged in neat rows on a table under warm light, symbolic of payments to victims."],
 "S056": ["@skyline"],
 "S057": ["N1: The listener (N1) sitting at the morning kitchen table, reading a plain blank booklet, calm."],
 "S058": ["E: A long chain of paper links stretching from a phone into darkness on a table; symbolic of a chain behind a call."],
 "S059": ["@dau_chan"],
 "S060": ["N1: The listener (N1) holding a plain white envelope at the mailbox in morning light, curious, relaxed."],
 "S061": ["@bac_toa"],
 "S062": ["E: A heavy closed door with a small barred window at the end of a dim corridor, nobody present; symbolic threat of arrest."],
 "S063": ["E: An hourglass with sand pouring fast on a kitchen counter, warm light; symbolic pressure."],
 "S064": ["E: A gift-shop rack of plain blank cards in soft light, slightly out of focus, nobody present."],
 "S065": ["N1: The listener (N1) looking at the dark phone on the counter, deciding not to answer, evening light."],
 "S066": ["E: An envelope marked only with a simple open-hand outline, empty, on a table; symbolic of an upfront fee."],
 "S068": ["N1: The listener (N1) looking up an official number in a plain blank printed directory, morning light."],
 "S069": ["N2: The daughter (N2) and the listener (N1) laughing together while washing dishes, warm kitchen light."],
 "S070": ["E: A plain laptop on the kitchen table showing a soft blank white glow, a cup of tea beside it, morning light."],
 "S071": ["E: A tidy desk with a stack of plain bound records and a desk lamp, warm light, nobody present."],
}
for _k, _v in CHEN.items():
    SC[_k] = (SC[_k] + _v)[:3]
