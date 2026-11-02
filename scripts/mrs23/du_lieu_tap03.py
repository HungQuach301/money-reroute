"""MR-S23 · Dữ liệu SHOT2 tập 3 (romance-sunmola). Đọc bởi scripts/mrs23/shot2.py. Quy ước mã: xem docstring shot2.py.
Lưu ý quét máy: tệp SHOT2.md tập 3 bị quét regex KC (ảnh riêng tư) — không viết các từ thuộc nhóm đó ở bất kỳ dòng nào khác
(kể cả chữ "clip" thay cho từ chỉ phim động); regex cam_them (tên điều tra viên, thẩm phán quận, bang/thành phố nạn nhân…)."""
TAP, THU_MUC, TIEN_TO = "tap03", "tap03-romance-sunmola", "s"
TEN = "Tập 3 · \"Prince Charming\" / Sunmola"
CHI_TOI = ["S033"]

NV = {
 "N1": ("Người phụ nữ (đại diện những người phụ nữ bị nhắm tới; KHÔNG phải nạn nhân cụ thể nào)",
        "Phụ nữ ~50 tuổi tự nghĩ ra, tóc nâu thẳng ngang vai, khăn quàng hổ phách, áo len xám; căn hộ ấm, đèn bàn. Mặt cách điệu, thường ở góc nghiêng/sau lưng/tay; không gắn sắc tộc, không phóng đại nét",
        "Được có mặt cách điệu, nhãn ILLUSTRATIVE. **Không** dùng cho câu về thiệt hại cá nhân cụ thể (S034 phá sản/mất nhà) — ở đó chỉ vật; không cảnh thân mật, không phòng ngủ"),
 "N2": ("Người bạn (đại diện người tin cậy, chỉ ở P12)", "Phụ nữ ~55 tuổi tự nghĩ ra, tóc bạc ngắn, áo khoác xanh teal; ngồi cạnh N1", "Được có mặt cách điệu, nhãn ILLUSTRATIVE"),
}
NGUOI_THAT = [
 ("Sunmola (bị cáo ●)", "Chỉ bóng ngược sáng, lưng, tay/tay áo trơn; trang phục trung tính; không quân phục; nhãn tên chỉ ở thẻ chữ", "Không mặt, không góc 3/4"),
 ("Nhân vật giả mà Sunmola dựng (\"soldier\", \"colonel\")", "**Không vẽ người**: khung hồ sơ trống (đường viền đầu-vai xám phẳng), dấu \"?\"; không quân phục, phù hiệu, cờ", "Tránh giống những người đàn ông thật bị lấy ảnh (KBCB S016)"),
 ("Những người đàn ông bị lấy ảnh; đồng phạm; điều tra viên; thẩm phán", "Không vẽ; đồng phạm chỉ bóng xa/tay", "Không mặt, không tên"),
 ("Những người phụ nữ trong hồ sơ", "Chỉ qua N1 (đại diện, tự nghĩ ra) hoặc đồ vật; không tuổi + hoàn cảnh + nơi ở ghép lại", "KBCB — không nhận diện"),
]
LUAT_RIENG = [
 "**Riêng tập 3** (HIEN-CHUONG §5, MR-D23 K3): không hình hay mô tả nhạy cảm; không dựng tin nhắn đọc được, không giao diện trang hẹn hò/ứng dụng; màn hình = khối trắng mềm trơn; không quân phục, phù hiệu, cờ, huân chương; không tên giả bị cáo dùng, không tên trang hẹn hò, dịch vụ chuyển tiền; không bang/thành phố nạn nhân.",
 "**Nigeria / Nam Phi / London:** không cảnh định kiến (đồng hoang, thú, trang phục dân tộc); chỉ bản đồ phẳng tự vẽ (L2), nội thất trung tính, sân bay không biển hiệu.",
 "**P06 (S033):** chỉ thẻ tối nền mực `#1B1F24`, chữ ngà, 6 s, không tranh, không nhạc; không câu/cảnh nào khác gợi lại nhánh này (máy kiểm KC quét cả tệp này: ≤ 1 dòng).",
]

SC = {
 # P00
 "S001": ["E#phong_khach: A dark living room at night, a lamp glowing softly, thin curtains at an open window, a sofa throw and a cold cup of tea; nobody present.", "K1*1.4", "E#laptop_dem: A laptop glowing in a dark living room, its screen a soft blank white rectangle, a sofa throw and a cold cup of tea nearby; nobody present."],
 "S002": ["E#khung_trong: A single empty profile frame glowing on a dark screen: a flat grey head-and-shoulders outline with a small question mark, no photo.", "G01*1.4", "E: A world map drawn on old paper on a desk at night with a single pin of light far away; no labels."],
 "S003": ["G01*1.2", "E: A desk at night with a plain laptop and a stack of blank cardboard boxes beside it, lamp light; nobody present.", "E: A plain olive canvas duffel bag with no markings resting by an empty doorway; symbolic of a claimed assignment."],
 "S004": ["E: A plain profile frame cracked down the middle on a dark screen, flat grey outline, no photo."],
 "S005": ["R#sun_cua: A man seen strictly from behind, a dark silhouette in a plain shirt at a window over a hazy night city with no landmarks; no face.", "E: A laptop and several phones lying face-down on a desk in a dark rented room, curtains drawn; nobody present."],
 "S006": ["Q01*1.4", "E: A paper crown made of folded blank paper on a table, soft spotlight; symbolic fairy-tale prince."],
 "S007": ["G02*1.5", "E: A long empty prison corridor in soft muted light, rows of closed plain doors; nobody present."],
 "S008": ["Q02*1.6", "E: A tall window in an empty courtroom with dust drifting in the light, nobody present."],
 "S009": ["E: An open notebook with a red pencil and three blank lines circled, warm desk lamp; symbolic of red flags.", "N1#n1_laptop: The woman (N1) seen from behind on the sofa, lit by the laptop glow, leaning in to read; the screen is a soft blank white rectangle."],
 # P01
 "S010": ["E: A rural post office counter at dusk with a stack of plain parcels and an old scale, nobody present, no signs.", "E: A plain sealed envelope resting on a post office counter beside an old scale, evening light; nobody present."],
 "S011": ["G03*1.6", "E: A wall of empty picture frames in a dark hallway, one lit; symbolic of fictitious profiles."],
 "S012": ["G03*1.2", "E: An aerial view at night of a vast suburban grid with countless lit windows; symbolic, no landmarks.", "R: Distant silhouettes of a few men around a table in a dim room, backlit, seen from behind; no faces."],
 # P02
 "S013": ["G04*1", "E: A wall calendar with plain blank squares turning back through many pages; no numbers."],
 "S014": ["@khung_trong", "E: A row of identical empty profile frames lined up on a dark screen, flat grey outlines, no photos.", "G04*1"],
 "S015": ["E: A shattered padlock icon drawn as a simple metal padlock broken open on a dark desk beside a laptop; symbolic of hacked accounts.", "E: A shoebox of loose blank photo prints, all white, scattered on a table under a lamp."],
 "S016": ["E: A row of empty coat hooks in a quiet hallway, soft light; nobody present."],
 "S017": ["E: A quiet empty government building corridor at dawn, plain walls, no flags or signs."],
 # P03
 "S018": ["N1#n1_qua: The woman (N1) smiling softly at a bouquet of flowers on her table, morning light, a small stuffed bear beside it.", "E: A plain greeting card standing open on a windowsill, blank inside, flowers and a box of chocolates beside it."],
 "S019": ["E: A city map spread on a desk with a magnifying glass over unlabeled streets, lamp at night.", "R: Hands in plain sleeves typing on a laptop in a dark room, the screen a soft blank glow; only hands."],
 # P04
 "S020": ["N1: The woman (N1) reading at her laptop late at night, worried expression, the screen a soft blank glow.", "G05*1.2"],
 "S021": ["E#hop: Plain cardboard boxes taped shut and stacked by a front door, blank labels, morning light; nobody present.", "G05*1", "E: A bank counter at closing time with an empty pen chained to the desk, soft light, no signs."],
 "S022": ["G05*1", "E: A desk with blank government-style folders and a closed laptop, cold light; symbolic of a fake mission."],
 "S023": ["E: A plain olive duffel bag with no markings left on an empty bench at dusk; symbolic."],
 "S024": ["E: Laptops, tablets and phones in plain unbranded boxes on a table, packing tape beside them.", "E#hien_nha: Dawn light across an empty wooden front porch, a potted plant and a plain bench; nobody present.", "K2*1.3"],
 "S025": ["G06*1.5", "E: A shipping label stuck on a box with every line blank, a pen resting on top."],
 "S026": ["G06*1", "@sun_cua"],
 "S027": ["G07*1.6", "E: A dark living room after midnight, the laptop closed on the sofa, a cup left on the table; nobody present.", "N1: The woman (N1) seen from behind at a window at dawn, alone, holding a dark phone."],
 # P05
 "S028": ["E: A lone keyboard on a desk in a dark room lit by one lamp; nobody present.", "G08*1"],
 "S029": ["G08*1.6", "R: Several pairs of hands passing plain unbranded boxes along a table in a dim room; only hands and sleeves."],
 "S030": ["G08*1", "E: An old balance scale with a much heavier pile of plain coins on one side, warm lamp."],
 "S031": ["E: A row of plain payment cards with no numbers or logos laid on a dark table under cold light.", "E: A shop counter at night with a closed register, nobody present, no signs."],
 "S032": ["G09*1.5", "E: Stacks of plain unbranded computer boxes in a dim warehouse aisle; nobody present."],
 # P06
 "S033": ["TOI"],
 # P07
 "S034": ["E: An empty house with a plain moving box on the floor and bare walls, afternoon light; nobody present.", "E: A closed laptop on an empty office desk with a cardboard box of personal items beside it.", "E: A row of empty chairs in a waiting room, cold light, no signs."],
 "S035": ["G10*1.6", "E: Seven small lamps on a dark table, all lit; symbolic, no labels."],
 "S036": ["G10*1.2", "E: A cracked teacup on a saucer under soft light; symbolic of psychological harm."],
 "S037": ["E: A coin on one side of a scale and a single wilted flower on the other, balanced; symbolic, warm light."],
 # P08
 "S038": ["G11*1.4", "E: A wide empty stone courthouse staircase at dawn, plain façade with no lettering."],
 "S039": ["G11*1", "E#cong_bay: An empty airport departure gate at night seen through glass, an aircraft waiting outside, no logos or signs."],
 "S040": ["K3*1.3", "@cong_bay"],
 "S041": ["G11*1", "E: An airplane wing over clouds at dawn, plain white, no markings."],
 "S042": ["E#phong_xu: An empty wood-paneled courtroom in soft morning light, plain wooden walls and benches, dust drifting in a sunbeam.", "G11*1"],
 # P09
 "S043": ["K4*1.3", "G11*1"],
 "S044": ["E: A judge's bench seen from the empty gallery, a gavel resting on its block, nobody present.", "@phong_xu"],
 # P10
 "S045": ["E: Two closed courtroom doors side by side, one lit, one dark; symbolic of two hearings."],
 "S046": ["E: An empty witness stand with a glass of water and a microphone, soft light; nobody present.", "E: A box of tissues on a courtroom railing, nobody present."],
 "S047": ["G12*1.2", "E: A thick stack of blank spreadsheet printouts with rows of unreadable lines on a table, desk lamp."],
 "S048": ["G12*1.2", "E: An iceberg drawn in a dark sea with most of its mass below the waterline; symbolic of an underestimate."],
 "S049": ["G13*2"],
 "S050": ["G13*1"],
 "S051": ["G13*1", "E: Plain envelopes arranged in neat rows on a table under warm light; symbolic of payments to victims."],
 "S052": ["E: An airplane parked on a quiet tarmac at dusk, stairs down, no markings; nobody present."],
 "S053": ["E: A small house with a plain sale sign shape with no text, at dusk; no landmarks.", "E: A courtroom clerk's counter with a plain sealed envelope, nobody present."],
 # P11
 "S054": ["T01*1.4", "T04*1"],
 "S055": ["G14*1.6", "E: Four plain folders laid out in a row on a long table, lamp light."],
 "S056": ["E: A theatrical mask of plain white cardboard lying on a dark table under a spotlight; symbolic of a false role.", "E: An empty chair in front of a mirror reflecting only a dark room; symbolic of a false image."],
 "S057": ["E: A quiet empty corridor in a government building at dawn, no flags or signs."],
 "S058": ["G14*1", "E: A pencil eraser and a calculator beside a stack of blank financial pages, desk lamp."],
 "S059": ["G14*1.4"],
 "S060": ["E: A dating-style profile card drawn as a blank white card with a small heart outline, lying on a dark table.", "G14*1"],
 "S061": ["N1: The woman (N1) sitting alone on a park bench in autumn, seen from the side, quiet; no other people.", "E: A kitchen table set for one, warm evening light."],
 "S062": ["@n1_laptop", "E: A lighted window in an apartment building at night, one among many dark ones."],
 "S063": ["N1: The woman (N1) holding a warm cup by a window at dawn, calm, gentle light."],
 "S063b": ["E: An old wooden bench on an empty pier at dusk, still water; symbolic of the past."],
 "S064": ["E: A high fence and a distant prison building at dusk, plain, no signs.", "E: A calendar on a plain wall with many blank pages ahead, no numbers."],
 # P12
 "S065": ["E#binh_minh: A sunrise window over a quiet room, a closed laptop on the table, warm light; nobody present.", "G15*1"],
 "S066": ["G08*1", "E: Many hands silhouetted around one glowing blank screen in a dark room; symbolic of several people behind one profile.", "G15*1"],
 "S067": ["G15*1", "@n1_qua"],
 "S068": ["G15*1", "E: A front door with a chain lock in morning light, nobody present."],
 "S069": ["G15*1", "@hop"],
 "S070": ["N2: The woman (N1) talking with her friend (N2) at a café table, the friend listening, warm light.", "G15*1"],
 "S071": ["G16*1", "E: A blank profile frame with a small red flag icon drawn beside it on a dark screen."],
 "S072": ["E: A small table with a closed notebook under morning light; nobody present."],
 "S073": ["G16*1", "E: A stack of plain unbranded electronics boxes with a red tag tied on top."],
 "S074": ["G16*1", "E: Three blank name tags on a table, all pointing to one shadow; symbolic."],
 "S075": ["G16*1", "E: A row of dominoes falling, the last one stopped by a hand-drawn line; symbolic."],
 "S076": ["G16*1", "E: A magnifying glass over an empty photo frame on a desk, lamp light."],
 "S077": ["K5*1.3", "N2: The woman (N1) and her friend (N2) walking together in a park in morning light, seen from behind."],
 "S078": ["G17*1.6", "E: A laptop on a kitchen table showing a soft blank white glow, a cup of tea beside it, morning light."],
 "S079": ["E: A tidy desk with a stack of plain bound records and a desk lamp, warm light, nobody present."],
}
OV = {
 "S004": [("kbcb", "The U.S. Army had nothing to do with either story. (đọc — chữ phụ đề)")],
 "S005": [("ten", "Olayinka Sunmola · ● CONVICTED (2016 plea · 2017 sentence)")],
 "S009": [("tieu_de", "Real cases from the public record · MONEY REROUTE")],
 "S016": [("kbcb", "(đọc) Những người đàn ông bị lấy ảnh không có tên trong hồ sơ — không thẻ ảnh, không mặt")],
 "S033": [("toi", "nguyên văn câu S033 của loi.json trên nền mực #1B1F24, chữ ngà; 6 s; không tranh, không nhạc")],
 "S065": [("tieu_de", "3 LESSONS · 5 RED FLAGS · 1 RULE")],
 "S077": [("bai", "1 RULE · Never send money to someone you meet online.")],
}
L2 = {
 "G01": {"hoi": "Hắn tự nhận là ai?", "noi_dung": "Khung hồ sơ trống lật hai mặt theo lời: \"American soldier · stranded in Nigeria · on a mission\" → \"colonel, U.S. Army · deployed to South Africa · needs computer equipment\" → dấu \"MISREPRESENTED — per the court\"", "nhan": "dấu MISREPRESENTED", "tang": "● CONVICTED · per 7th Cir. opinion"},
 "G02": {"hoi": "Án nặng cỡ nào?", "noi_dung": "Bộ đếm 0 → 324 MONTHS → quy đổi = 27 YEARS (năm ô năm hiện dần)", "nhan": "27 YEARS", "tang": "● CONVICTED"},
 "G03": {"hoi": "Một người đàn ông hay một hệ thống hồ sơ giả?", "noi_dung": "2012: một khiếu nại (một chấm) → mở ra lưới hàng chục khung hồ sơ trống (\"dozens of fictitious profiles\", per prosecutors) → bản đồ Mỹ phẳng nhiều chấm **rải ngẫu nhiên, không theo bang/thành phố** \"hundreds of women\" ◐", "nhan": "khung đầu tiên giữa lưới", "tang": "◐ ALLEGED · per prosecutors"},
 "G04": {"hoi": "Bắt đầu khi nào, từ đâu, bằng gì?", "noi_dung": "Trục: March 2008 · South Africa → khung hồ sơ \"fictitious names\" · \"successful businessmen\" · \"pictures of men in U.S. military uniforms\" (chữ, không hình quân phục)", "nhan": "mốc March 2008", "tang": "● CONVICTED · per 7th Cir. opinion"},
 "G05": {"hoi": "Từ tin cậy tới yêu cầu: tiền và hàng đi theo đường nào?", "noi_dung": "Thanh \"trust\" đầy dần (thơ, thiệp, hoa — icon) → ô \"REQUESTS: money · electronics\" → \"false claims of financial distress\" → \"for work on behalf of the U.S. government\" gạch đứt", "nhan": "ô REQUESTS", "tang": "● per 7th Cir. opinion; S024 ◐"},
 "G06": {"hoi": "Gửi cho ai thật sự?", "noi_dung": "Ba nhãn \"driver\" · \"co-worker\" · \"hotel manager\" + tên \"Ilumsa Sunmola\" → cả ba mũi tên gộp vào MỘT bóng \"Sunmola himself\" (per prosecutors)", "nhan": "cú gộp ba thành một", "tang": "◐ ALLEGED · per prosecutors"},
 "G07": {"hoi": "Vì sao tiền cứ phải gửi thêm?", "noi_dung": "Vòng lặp: EMERGENCY → MONEY → new EMERGENCY (mỗi vòng thanh tiền dày hơn) → \"money runs out / refused\" → đường đứt: relationship ENDED", "nhan": "đường đứt cuối vòng", "tang": "◐ ALLEGED · per prosecutors"},
 "G08": {"hoi": "Ai đứng ở giữa đường dây?", "noi_dung": "Sơ đồ toả tia: ô trung tâm \"organizer or leader (upheld)\" → recruited accomplices · received stolen goods & wire transfers · directed what to tell victims; mũi tên phần lợi nhuận dày hơn \"larger share (evidence suggesting)\"", "nhan": "ô trung tâm", "tang": "● per 7th Cir. opinion"},
 "G09": {"hoi": "Ngoài những người phụ nữ, ai còn thiệt hại?", "noi_dung": "Nhánh phụ \"credit card fraud affecting various businesses\" (court) → bộ đếm \"one computer manufacturer: $800,000+\" (per prosecutors)", "nhan": "$800,000+", "tang": "S031 ● court; S032 ◐ ALLEGED"},
 "G10": {"hoi": "Toà cân nhắc thiệt hại nào ngoài tiền?", "noi_dung": "Ngưỡng \"5 or more victims\" (vạch) → 7 chấm sáng (PSR listed seven, upheld) → hai thẻ \"upward departure: psychological injury\" · \"gratuitous infliction of injury\"", "nhan": "chấm thứ 7 vượt vạch 5", "tang": "● per 7th Cir. opinion"},
 "G11": {"hoi": "Từ cáo trạng tới nhận tội mất bao lâu?", "noi_dung": "Trục: Nov. 20, 2013 indictment (8 counts) → Aug. 9, 2014 arrest, London → Feb. 2015 to U.S. custody → Feb. 29, 2016 trial begins → 3 DAYS → guilty plea, all 8 counts, no plea agreement", "nhan": "3 DAYS", "tang": "TT; ● CONVICTED"},
 "G12": {"hoi": "Con số thiệt hại nói được bao nhiêu?", "noi_dung": "Hai lớp: 13 victims in PSR + 39 additional → thanh \"around $1.7 million\" với phần mờ phía trên ghi \"underestimate\" (per investigator, as recorded by the court)", "nhan": "phần mờ \"underestimate\"", "tang": "TT; ● per 7th Cir. opinion"},
 "G13": {"hoi": "Bản án được tính từ những gì?", "noi_dung": "Khối xếp chồng 6 enhancement theo lời (organizer/leader · acting on behalf of a government agency · substantial financial hardship · vulnerable victims · intended loss $2,054,972.66 · outside the U.S.) → 324 MONTHS → restitution $1,707,260.98 → amended $1,669,050.98", "nhan": "324 MONTHS", "tang": "● CONVICTED"},
 "G14": {"hoi": "Kháng cáo thay đổi được gì?", "noi_dung": "Bốn thẻ \"challenged\": enhancements · loss · restitution · deterrence → mỗi thẻ đóng dấu \"rejected\" theo lời → \"AFFIRMED — Apr. 16, 2018\"", "nhan": "AFFIRMED", "tang": "● per 7th Cir. opinion"},
 "G15": {"hoi": "Ba bài học rút ra?", "noi_dung": "Tiêu đề 3 LESSONS · 5 RED FLAGS · 1 RULE → ba thẻ bài học gọi lại hình G08 (tổ chức), lưới chấm (chọn theo hoàn cảnh), thanh \"underestimate\" (G12)", "nhan": "thẻ bài học đang đọc", "tang": "theo từng câu"},
 "G16": {"hoi": "Năm dấu hiệu là gì?", "noi_dung": "5 thẻ RED FLAG lật lần lượt, mỗi thẻ gọi lại icon (khung hồ sơ · hộp điện tử · ba nhãn gộp một · vòng khẩn cấp · khung ảnh + kính lúp)", "nhan": "số thứ tự thẻ đang đọc", "tang": "theo từng câu"},
 "G17": {"hoi": "Báo ở đâu?", "noi_dung": "Thẻ nơi báo: \"ic3.gov\" · \"reportfraud.ftc.gov\"", "nhan": "ic3.gov", "tang": "CHUNG", "dong": False},
}
L3 = {
 "T01": ("`ho-so/romance-sunmola/ca7-opinion-17-1299-2018.pdf` tr. 1 (N2)", "khối đầu trang từ \"United States Court of Appeals / For the Seventh Circuit\" tới \"Defendant-Appellant.\" — **cắt dưới trước** dòng \"Appeal from…\" (dòng đó có tên thẩm phán quận, tên này nằm trong danh sách cấm của tập)", "UNITED STATES OF AMERICA v. OLAYINKA I. SUNMOLA · No. 17-1299", "NGUON §4: trang được dùng"),
 "T04": ("như T01, tr. 18", "\"III. CONCLUSION / For the foregoing reasons, we AFFIRM.\"", "we AFFIRM", "NGUON §4: trang được dùng"),
 "Q01": ("N1 (USAO S.D. Ill., Feb. 2, 2017)", "thẻ trích nền ngà", "“Prince Charming” — U.S. Attorney's Office, Southern District of Illinois", "Chữ = `chu` S006 nguyên văn"),
 "Q02": ("N2 tr. 17", "thẻ trích nền ngà", "“the most devastating crime one could ever imagine without someone laying hands or even eyes on another human being” — the sentencing judge, as quoted by the U.S. Court of Appeals for the Seventh Circuit", "Chữ = `chu` S008 nguyên văn; nếu điều phối duyệt tr. 17 có thể thay bằng crop trang"),
}
CAM_L3 = "N2 tr. 2 (đoạn nhánh P06; bang nạn nhân), tr. 8, tr. 4 và 14 (tên điều tra viên), tr. 11–12, tr. 14 (tên dịch vụ chuyển tiền, trang hẹn hò); N2 tr. 1 dòng \"Appeal from…\" (tên thẩm phán quận); N2 tr. 10 (có câu trích lời bị cáo và chủ đề khủng bố — không crop); mọi ảnh chụp thông cáo N1. **Đề xuất (chưa dùng):** N2 tr. 17 câu \"The judge mentioned general deterrence in a mere four sentences out of the eight-page transcript…\" làm crop cho S059 — cần điều phối thêm vào NGUON §4 (trang không có tên/chi tiết cấm); hiện S059 dùng L2 G14."
VEO = {
 "K1": {"tu": "phong_khach", "chuyen_dong": "The thin curtains move in a night breeze; the lamp light flickers softly on the sofa throw; slow push-in.", "neo_cuoi": "The quiet lamp-lit room; nobody present.", "qc": "Khung đầu không màn hình (BAI-HOC mục 2)"},
 "K2": {"tu": "hien_nha", "chuyen_dong": "Morning light slowly sweeps across the empty porch boards; leaves of the plant stir; dust drifts.", "neo_cuoi": "The bright empty porch.", "qc": "Khung đầu không nhãn/chữ (BAI-HOC mục 2); hộp hàng chỉ ở tranh tĩnh"},
 "K3": {"tu": "cong_bay", "chuyen_dong": "Through the glass of the empty gate the waiting aircraft's lights blink slowly; reflections slide across the glass; nobody present.", "neo_cuoi": "The empty gate and the aircraft at night.", "qc": "Không logo hãng, không bảng chuyến bay"},
 "K4": {"tu": "phong_xu", "chuyen_dong": "Slow push-in toward the empty bench; dust drifts in the sunbeam; light brightens a little.", "neo_cuoi": "The empty courtroom bench in morning light.", "qc": "Không con dấu, không cờ"},
 "K5": {"tu": "binh_minh", "chuyen_dong": "Sunrise light slowly fills the quiet room; curtains move softly; the closed laptop stays on the table.", "neo_cuoi": "The bright room with the closed laptop; nobody present.", "qc": "Không thêm người"},
}
KET = "L2 `G18` thẻ tổng kết nền tối (3 + 5 + 1 dòng của SHOT.md §3, giữ nguyên chữ đã duyệt) + ic3.gov · reportfraud.ftc.gov + dòng khai AI; giữ 8 s"
NGUON = "L2 `G19` danh sách nguồn chạy chữ (N1–N3, N6–N8) + dòng khai AI (HIEN-CHUONG §6)"
NHAC = ["Giữ bảng nhạc `SHOT.md` §4 (MR-K23): P00–P03 piano ấm chậm −24 dB · P04–P05 lạnh dần, dây thấp −22 dB · **P06 im lặng** (thẻ tối 6 s) · P07 một nốt piano thấp −26 dB · P08 nhịp tăng, **cắt lặng 1 s** sau S042 · P09–P11 nền tĩnh −26 dB · P12 sáng hơn −24 dB. Không còi, còng tay, tiếng nức nở."]

# ---- cảnh chen (mật độ giữa): thêm tranh cho câu dài, giữ ≤ 3 cảnh/câu ----
CHEN = {
 "S005": ["E: A night skyline of a generic large city across a dark bay, warm haze, no landmarks."],
 "S006": ["E: A fairy-tale storybook lying closed on a table, plain cover with no title, soft light."],
 "S007": ["E: A gavel resting on its block under soft courtroom light, nobody present."],
 "S010": ["E: An envelope and a plain complaint form with blurred unreadable lines on a desk, pen beside it."],
 "S011": ["E: A notebook listing many blank lines, each with a small grey outline icon, under a lamp; symbolic."],
 "S013": ["E: A dark desk with a laptop and a dozen phones lined up, screens off, a lamp; nobody present."],
 "S015": ["E: A hand-drawn chain of grey profile outlines on paper, linked by thin lines; symbolic."],
 "S017": ["E: A plain wooden desk name stand with no name, alone on an empty desk."],
 "S018": ["E: A handwritten-style letter with every line blurred and unreadable, tied with a ribbon, beside a teacup."],
 "S019": ["E: A tourist postcard rack with all cards blank white, at dusk; no city names."],
 "S020": ["E: A sealed padded envelope and a roll of tape on a kitchen counter, evening light."],
 "S022": ["E: A plain wooden desk with an unmarked brass compass and a folded paper map; symbolic of a mission."],
 "S025": ["E: A hotel reception desk at night, a bell on the counter, nobody present, no signs."],
 "S028": ["N1: The woman (N1) alone at her keyboard late at night, seen from behind, the screen a soft blank glow."],
 "S029": ["E: A chessboard with one king surrounded by many pawns, lamp light; symbolic of a leader."],
 "S030": ["E: A cake cut into very unequal slices on a plate; symbolic of a larger share."],
 "S031": ["E: A closed small shop with its shutter half down at night, no signs."],
 "S032": ["E: A loading dock at night with a pallet of plain boxes, nobody present, no signs."],
 "S034": [],
 "S035": ["N1: The woman (N1) sitting at her kitchen table with a pile of blank bills, head in her hands, seen from the side."],
 "S036": ["E: A dim hallway with a single chair facing a window, rain on the glass."],
 "S037": ["E: A small potted plant beginning to recover in morning light; quiet."],
 "S038": ["E: A thick closed binder with eight plain tabs on a courtroom table, nobody present."],
 "S039": ["E: A rainy night street with black cabs blurred in the distance, no signs, no landmarks."],
 "S040": ["E: A boarding pass shape with every field blank lying on an airport bench."],
 "S041": ["E: A long empty jet bridge corridor, cold light, nobody present."],
 "S042": ["E: A jury box with fourteen empty chairs in soft light."],
 "S043": ["E: A pen resting on a single blank signature line on a white page, soft morning light."],
 "S044": ["E: A microphone on a lectern facing the bench in an empty courtroom."],
 "S047": ["E: A postal service-style canvas mail bag with no markings on a table beside the spreadsheet; nobody present."],
 "S048": ["E: A telephone on a desk with a long list of blank names, many crossed with faint lines."],
 "S051": ["E: A stack of plain checks with no names or numbers, held by a clip, on a desk."],
 "S052": ["E: A one-way road sign shape with no text on an empty airport road at dusk."],
 "S053": ["E: A set of four plain house keys on a ring lying on a table, warm light."],
 "S055": ["E: A stack of four plain briefs bound with clips on an appellate court table."],
 "S056": ["E: A row of plain empty chairs in an appellate courtroom, high windows, dust in light."],
 "S057": ["E: A plain closed briefcase standing next to an empty bench, nobody present."],
 "S058": ["E: Scattered coins being counted into neat piles by an unseen lamp-lit desk; no people."],
 "S059": ["E: An eight-page stack of blank paper with four short lines highlighted faintly; symbolic."],
 "S060": ["N1: The woman (N1) in her living room looking at old blank photo frames on a shelf, seen from behind."],
 "S062": ["E: A single glowing heart outline drawn on a foggy window; symbolic."],
 "S063": ["E: Two cups of tea on a small table by a window, morning light; warm and safe."],
 "S063b": ["E: A closed old diary with a ribbon on a shelf, soft light."],
 "S064": ["E: A long road leading to a distant plain building under a pale sky; quiet, no signs."],
 "S067": ["E: A map table with many small lamps scattered unevenly, some brighter; symbolic of circumstances."],
 "S068": ["E: A public service poster shape on a wall with all text blurred and unreadable, soft light."],
 "S069": ["E: An iceberg tip above dark water with the hidden mass glowing faintly below."],
 "S070": ["E: A telephone and a notepad on a counter in morning light, the notepad blank."],
 "S072": ["E: A sealed empty envelope on a table, nobody present."],
 "S074": ["E: A courier's empty trolley in a hallway, nobody present, no signs."],
 "S076": ["N1: The woman (N1) holding a printed blank photo beside her laptop, comparing, curious."],
 "S077": ["E: A closed padlock on a small box of money-shaped blank paper on a table; symbolic of keeping it."],
 "S078": ["N1: The woman (N1) typing on a laptop at her kitchen table in morning light, calm and determined; the screen is a soft blank glow."],
 "S079": ["E: A quiet bookshelf of plain bound records with no titles, warm light."],
}
for _k, _v in CHEN.items():
    SC[_k] = (SC[_k] + _v)[:3]
