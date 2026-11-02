#!/usr/bin/env python3
"""MR-6 · Danh sách tranh L1 mới (b001…) + lời sinh → reports/mr6/loi_anh.json (0 USD, dựng lại được).
Phong cách = tờ A của MR-P1 (reports/mrp1/A/PHONG-CACH.md, tiền tố + hậu tố nguyên văn) + sửa PHONG-CACH-HINH v1 §4:
HAI tham chiếu — ref_nv (lab/mrp1/A/a01_l1.png, chỉ cảnh có nhà đầu tư) và ref_canh (lab/mrp1/A/a15_l1.png, cảnh trống).
Cảnh không có nhà đầu tư ghi rõ "The investor woman is NOT in this scene"."""
import json, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
A = json.load(open(os.path.join(ROOT, "reports", "mrp1", "A", "loi_anh.json")))
NV, MAN, EMPTY = "nv", "man", "empty"
# (id, loại: nv = có nhà đầu tư; man = có người vest tối (bóng/lưng/tay); empty = không người / người không nhận ra), mô tả cảnh
DS = [
 # P00–P01
 ("b001", MAN, "An actor's dressing room at night: a mirror framed by warm bulbs reflecting only an empty chair, a dark suit jacket hanging on a hook. Nobody in the mirror."),
 ("b002", MAN, "Close-up of a hand in a dark suit sleeve with a cufflink setting a brass hourglass down on a polished desk next to a closed leather portfolio. Only the hand and sleeve."),
 ("b003", EMPTY, "A modern office corridor at night with glass walls, blurred city lights beyond, completely empty, cool teal light."),
 ("b004", EMPTY, "Exterior of a modest low-rise office building at dusk in Los Angeles, a lone palm tree, warm windows; absolutely no signage or lettering on the building. No people."),
 ("b005", EMPTY, "A cluttered desk with film reel canisters, a vintage film splicer and a green-shaded desk lamp; dust in the lamp beam. No people."),
 ("b006", EMPTY, "A single gold coin standing on its edge under a spotlight on a dark table, surrounded by hundreds of ordinary grey pebbles. Symbolic still life, no markings on the coin."),
 ("b007", NV, "Close-up over a restaurant table: the investor's hands in mustard cardigan sleeves rest near a closed fountain pen; across the table a hand in a dark suit sleeve gestures persuasively. Candlelight. Faces out of frame."),
 ("b008", EMPTY, "A quiet law library with tall shelves of thick bound law books with plain unmarked spines, a reading table with a green lamp. No people."),
 ("b009", EMPTY, "A brass hourglass on a dark desk beside a short stack of plain coins; sand falling, warm side light. No markings."),
 ("b010", NV, "Night kitchen: the investor sits alone at the table with a pen and a blank notepad, thinking hard, lit by one small lamp."),
 ("b011", EMPTY, "A vast dark empty warehouse floor with silent machines under dust sheets, a single shaft of light. Nothing is being produced. No people."),
 ("b012", NV, "The investor in a small home office leaning toward a laptop whose screen is a soft blurred glow, hopeful expression, afternoon light through blinds."),
 ("b013", NV, "Bright morning kitchen: the investor smiles while looking down at her phone (screen not visible), relieved, sunlight on the table."),
 ("b014", EMPTY, "Two empty office chairs facing each other across a glass table at night, city lights blurred behind. No people."),
 # P07 nhóm, nhà đầu tư con
 ("b015", MAN, "An elegant dinner party in a dim home: several invented guests seen only as soft dark silhouettes against warm lamplight, glasses raised; the man in the dark suit at the head of the table seen strictly from behind. No faces visible."),
 ("b016", EMPTY, "Backyard gathering at dusk: hands clinking wine glasses over a table with string lights, all faces out of frame. Warm and friendly mood."),
 ("b017", EMPTY, "A chain of hands passing a sealed blank envelope from one person to the next across a long table, only hands and sleeves visible, varied sleeves."),
 ("b018", NV, "The investor sits at a table looking across at an empty chair; a pen lies between them. Uncertain mood, dim light."),
 ("b019", EMPTY, "A crowded community hall seen from the back, rows of invented people as dark silhouettes facing a soft light, no faces, no signs."),
 ("b020", EMPTY, "Hundreds of tiny paper boats on dark water drifting away from a single larger boat, seen from above at dusk. Symbolic, no markings."),
 # P08–P09
 ("b021", EMPTY, "A heavy steel safe-deposit box lying open and completely empty under a single lamp on a dark table."),
 ("b022", EMPTY, "A film reel canister wrapped in a chain with a padlock, on a dark shelf, dramatic side light. No labels."),
 ("b023", EMPTY, "A private screening room after hours: the projector is off, a thin haze in the air, empty seats in darkness, the screen dark."),
 ("b024", MAN, "Close-up: hands in dark suit sleeves slide a closed thick leather folder across a desk toward the viewer. Only hands. Nothing written on the folder."),
 ("b025", EMPTY, "A printer in a dark office at night pushing out a stream of blank white pages that pile onto the floor. Pages completely blank."),
 ("b026", NV, "The investor holds a magnifying glass over a blank sheet of paper on her kitchen table, lamp light, skeptical expression."),
 ("b027", MAN, "The man in the dark suit, strictly from behind, stands at a large desk covered with stacks of closed blank folders, lit by a single lamp in a dark room."),
 # P10–P11 tiền đi đâu
 ("b028", EMPTY, "A massive bank vault door half open onto darkness, cold light spilling out. No people, no markings."),
 ("b029", EMPTY, "A sleek dark sports car in a dim garage, light catching its curves; no badges, no license plate."),
 ("b030", EMPTY, "A luxurious empty living room with floor-to-ceiling windows at night overlooking city lights, designer furniture, a fire in a fireplace. No people."),
 ("b031", MAN, "A conference room: several invented investors around a table as dark silhouettes seen from behind, the man in the dark suit at the head of the table as a backlit silhouette. No faces."),
 ("b032", MAN, "Close-up: a hand in a dark suit sleeve places a small stack of coins onto a larger pile that other hands (varied sleeves) are building on a table. Only hands."),
 ("b033", NV, "The investor raises one hand, palm outward, in a calm 'wait' gesture at a table; the other hand rests on a closed notebook."),
 # P12–P14
 ("b034", NV, "Dawn kitchen: the investor smiles faintly at her phone (screen not visible), coffee steaming. Calm, reassured."),
 ("b035", MAN, "The man in the dark suit stands at a tall window, strictly from behind, as autumn leaves blow past outside; time passing."),
 ("b036", EMPTY, "A stack of sealed blank envelopes on a desk growing very tall, lit by a lamp, the top envelopes leaning precariously."),
 ("b037", NV, "Night hallway: the investor stands with a phone pressed to her ear, worried, lit by a cold window."),
 ("b038", EMPTY, "A pile of plain blank envelopes on a doormat inside a dark front door, more slipping through the mail slot."),
 ("b039", EMPTY, "An empty kitchen chair with a mustard knit cardigan draped over its back, a wet window behind (no rain falling), cold night light. No people."),
 # P15 trấn an
 ("b040", EMPTY, "A still lake at night under a pale moon with thin mist lying on the water; perfectly calm. No people."),
 ("b041", MAN, "The man in the dark suit as a backlit silhouette seated at a desk at night, head bowed over a phone whose glow is hidden from view. Strictly from behind."),
 ("b042", MAN, "Close-up of a phone in a dark room held in a hand in a dark suit sleeve; the screen faces away from the viewer; only a cold glow on the cuff."),
 ("b043", EMPTY, "A dark carnival-style masquerade mask lying on a desk next to a smartphone face-down, lamp light. Symbolic."),
 ("b044", EMPTY, "A judge's gavel resting on its wooden block in a dim empty courtroom, light from a high window."),
 ("b045", EMPTY, "A rain-wet window at night with still droplets on the glass (no rain falling) and blurred city lights beyond."),
 # P16 đếm ngược
 ("b046", MAN, "Close-up: hands in dark suit sleeves typing on a laptop at night; the screen is a blurred glow facing away. Only hands."),
 ("b047", EMPTY, "A law office waiting area at night with empty leather chairs and a closed wooden door, warm lamp. No signs, no lettering."),
 ("b048", NV, "Close-up: the investor's hand in a mustard cardigan sleeve pauses in mid-air above a smartphone lying on the table; she does not touch it."),
 ("b049", EMPTY, "A wall clock with a completely blank face and no numerals in a dark office, its hands near the top; dramatic shadow."),
 ("b050", EMPTY, "A deserted city street at night, wet asphalt reflecting street lamps, no signs, no cars, no people."),
 # P17
 ("b051", EMPTY, "An empty federal courtroom at dawn: judge's bench, clerk desk, rows of empty benches, light beams through tall windows. No seals, no flags, no lettering."),
 ("b052", EMPTY, "A heavy round bank vault door swinging shut with large steel bolts, cold blue light. No people."),
 ("b053", EMPTY, "Pre-dawn in a dark private office: a desk lamp still on over scattered closed folders, an empty leather chair turned away from the desk, a tall window with a faint blue sky. No people."),
 # P18–P19
 ("b054", EMPTY, "A single pen resting on a closed folder on a wooden courtroom table, a lamp nearby, shallow depth of field."),
 ("b055", EMPTY, "The empty public gallery of a courtroom, wooden benches, long beams of morning light with dust."),
 ("b056", EMPTY, "A heavy steel door at the end of a stark empty corridor, cold fluorescent light. No people, no signs."),
 ("b057", EMPTY, "A conference room at night with tall stacks of plain binders on a long table, no labels on the binders. No people."),
 ("b058", EMPTY, "An empty red carpet with velvet ropes and distant camera flashes as soft bokeh, no people, no logos, no backdrop text."),
 ("b059", EMPTY, "An empty theater stage with one spotlight on a lone wooden chair, heavy curtains half open. No people."),
 # P21
 ("b060", EMPTY, "A tower of champagne glasses on a table in a dark room, the top glass being filled, glowing amber liquid spilling into lower glasses. No people visible."),
 ("b061", NV, "Morning: the investor sits at her kitchen table writing in a notebook (writing not legible, seen from an angle), calm and determined, sunlight."),
 ("b062", NV, "The investor closes a laptop and sets down her glasses, thoughtful, in a sunny home office."),
]
# Cảnh phụ để đạt mật độ ~2,5 s/cảnh (mỗi đoạn thêm khung chuyển, cận vật, toàn cảnh) — vẫn cùng luật.
DS += [
 # P00–P03
 ("b063", NV, "Dawn kitchen wide shot from the doorway: the investor at the table with her phone, the room still blue with early light."),
 ("b064", EMPTY, "A smartphone lying face up on a wooden table at dawn, its screen a soft blurred green glow, steam from a coffee mug beside it. Screen content completely blurred."),
 ("b065", EMPTY, "Night: a smartphone face up on a kitchen table glowing with a cold blurred light, a wet dark window behind it (no rain falling)."),
 ("b066", EMPTY, "Rows of grey archive boxes on tall metal shelves in a dim records room, a shaft of light, no labels on the boxes."),
 ("b067", MAN, "A film set at night: a camera crane and lights silhouetted, the man in the dark suit seen far away strictly from behind in the glow."),
 ("b068", EMPTY, "A large movie projector beam cutting through haze in a dark room, close-up on the lens light."),
 ("b069", EMPTY, "A scale model city of Los Angeles-like hills at dusk with tiny lights, painted in dark teal and amber, no landmarks, no signs."),
 ("b070", EMPTY, "Close-up of film strips hanging from a rack in an editing room, backlit amber, frames completely blurred."),
 ("b071", MAN, "The man in the dark suit, strictly from behind, opens the door of a small office into darkness, light from the hall."),
 ("b072", NV, "The investor listening intently across a restaurant table, candlelight, the other diner out of frame."),
 ("b073", EMPTY, "A map-like abstract painting of glowing routes across a dark ocean, seen from high above, like a distribution network, no labels."),
 ("b074", EMPTY, "A row of glowing television screens in a dark showroom, each showing only abstract blurred color, no logos."),
 ("b075", EMPTY, "Close-up of a stack of coins growing taller beside a film reel on a desk, warm light. No markings."),
 # P04–P06
 ("b076", MAN, "Close-up of a fountain pen nib above a blank sheet of paper held still by a hand in a dark suit sleeve. Nothing written."),
 ("b077", EMPTY, "A pair of old-fashioned brass balance scales on a dark desk, one pan heavier with coins, the other empty."),
 ("b078", EMPTY, "A calendar-like wall of blank square tiles in a dark room with a beam of light crossing them, no numbers, no letters."),
 ("b079", EMPTY, "A small plant seedling sprouting from a pile of coins, dramatically lit, symbolic growth."),
 ("b080", NV, "The investor at her kitchen table doing mental math, eyebrows raised, a pencil in hand, notepad blank."),
 ("b081", EMPTY, "A row of dominoes about to fall on a dark table, side light."),
 ("b082", NV, "The investor in conversation on a sofa with an invented friend seen from behind (only back of head and shoulder), warm living room, evening."),
 ("b083", EMPTY, "A grand cinema marquee at night with all its letter rows completely empty and blank, bulbs glowing. No text."),
 # P07–P09
 ("b084", MAN, "A golf course clubhouse terrace at sunset, invented men and women as silhouettes chatting, the man in the dark suit among them strictly from behind. No faces."),
 ("b085", EMPTY, "A family living room in the evening, an invented couple seen from behind on a sofa looking at a tablet (screen blurred), cozy lamp light."),
 ("b086", EMPTY, "A ladder of hands, each handing coins down to the next, painted as a symbolic vertical composition, only hands and sleeves."),
 ("b087", EMPTY, "Close-up of a broken chain link on a dark table, symbolic of a missing connection."),
 ("b088", EMPTY, "A row of empty bank teller windows at night, brass grilles, no signs."),
 ("b089", EMPTY, "Close-up of a padlock hanging open on an empty hook on a wall, lamp light."),
 ("b090", EMPTY, "A filing cabinet drawer pulled open and completely empty in a dark office."),
 ("b091", MAN, "Close-up of a rubber stamp being pressed by a hand in a dark suit sleeve onto a blank page; no ink marks visible, nothing written."),
 ("b092", EMPTY, "A stack of blank papers with a fountain pen on top lit by a single lamp, everything blank."),
 ("b093", EMPTY, "A theater backstage: a painted flat of a building facade seen from behind, held up by wooden braces — a facade with nothing behind it."),
 # P10–P11
 ("b094", EMPTY, "Coins spilling out of a tipped jar across a polished table, motion frozen, warm light."),
 ("b095", EMPTY, "A private jet interior with empty cream leather seats and small oval windows glowing with sunset, no logos."),
 ("b096", EMPTY, "A walk-in closet with rows of expensive suits and shoes under soft spotlights, no logos."),
 ("b097", EMPTY, "A swimming pool at night with underwater lights glowing on a modern terrace, no house facade details, no people."),
 ("b098", EMPTY, "A set of house keys on a marble kitchen island, morning light, nobody around."),
 ("b099", EMPTY, "Two transparent glass jars connected by a tube, coins flowing from one jar into the other, symbolic, dark background."),
 # P12–P14
 ("b100", EMPTY, "A spiral staircase seen from above descending into darkness, symbolic, no people."),
 ("b101", EMPTY, "A hamster-wheel-like large brass wheel turning in a dark room, symbolic of a cycle, no animals."),
 ("b102", EMPTY, "Autumn leaves falling past a dark office window at dusk, seen from inside."),
 ("b103", EMPTY, "A desk calendar-like flip block whose pages are all blank, flipping in a gust, dark room."),
 ("b104", EMPTY, "A dried-up fountain in a courtyard at night, the basin empty, a few leaves inside."),
 ("b105", NV, "The investor sits on the edge of her bed at night holding her phone, worried, the room dark."),
 ("b106", EMPTY, "An answering machine-like small device with a red blinking light on a hallway table at night, no display text."),
 ("b107", NV, "The investor looking out of a rain-streaked window at night (still droplets, no rain falling), arms crossed, anxious."),
 # P15–P16
 ("b108", EMPTY, "A smartphone face-down vibrating on a nightstand at night, a faint glow at its edge."),
 ("b109", MAN, "The man in the dark suit, strictly from behind, standing in a dark room lit only by a wall of glowing blurred monitors."),
 ("b110", EMPTY, "A ventriloquist-style empty chair beside a microphone on a stand in a dark empty room, symbolic of speaking for someone else."),
 ("b111", EMPTY, "A row of identical empty office cubicles at night lit by cold light, no logos, no signs."),
 ("b112", NV, "The investor reading her phone at the kitchen table at night (screen not visible), hopeful but tired."),
 ("b113", EMPTY, "A large analog wall clock in a dark hallway with a completely blank face, only hands, no numerals, a sense of time running."),
 ("b114", EMPTY, "An empty conference table with a single closed laptop at one end and a cold cup of coffee, early morning grey light."),
 ("b115", NV, "The investor at her table pushes the phone away from her with one hand, deciding to wait, lamp light."),
 # P17–P18
 ("b116", EMPTY, "A city skyline at dawn under a heavy cloud bank, first light on the towers, no signs, no landmarks."),
 ("b117", EMPTY, "A row of tall government-style building windows at dawn with the lights coming on one by one, no flags, no seals."),
 ("b118", EMPTY, "Close-up of a steel padlock snapping shut on a chain around a filing cabinet, cold light."),
 ("b119", EMPTY, "An empty quiet residential street at dawn with dark parked cars and street lamps turning off, no people, no license plates."),
 ("b120", EMPTY, "A courthouse hallway with tall wooden doors closed, morning light on a polished floor, empty, no lettering."),
 ("b121", EMPTY, "Close-up of the bars of a courtroom railing with soft light, symbolic, empty."),
 ("b122", EMPTY, "A calendar-free composition: two seasons' light passing over an empty courtroom bench, painterly."),
 ("b123", EMPTY, "Close-up of a judge's empty high-backed leather chair behind the bench, dramatic light."),
 ("b124", EMPTY, "A pair of scales of justice as a brass sculpture on a dark pedestal, no lettering."),
 ("b125", EMPTY, "Stacks of coins slowly being moved from one side of a table to the other by many invented hands, only hands visible."),
 # P19–P21
 ("b126", EMPTY, "An empty government agency hallway at night with closed office doors, no plaques, no lettering."),
 ("b127", EMPTY, "Close-up of a pen signing on a line at the bottom of a page seen from such an angle that nothing is legible, hand in plain white shirt sleeve."),
 ("b128", EMPTY, "A movie premiere red rope stanchion fallen on the floor of an empty hall, spotlight."),
 ("b129", EMPTY, "A cardboard cutout silhouette of a man in a suit standing in an empty spotlight on a stage, flat and hollow from behind. No face."),
 ("b130", EMPTY, "A dark empty movie theater after the show, litter on the floor, the screen dark."),
 ("b131", NV, "The investor at dawn standing at her kitchen window holding a mug, looking out, resolved."),
 ("b132", EMPTY, "Close-up of a magnifying glass resting on a closed notebook on a table, morning sunlight."),
 ("b133", EMPTY, "A short fuse burning toward a closed box on a dark table, symbolic of a short clock, no explosion."),
 ("b134", EMPTY, "A glowing star-shaped spotlight on an empty pedestal in a dark gallery — a famous partner who is not there."),
 ("b135", EMPTY, "A ventriloquist's empty puppet chair and a single microphone under a spotlight, symbolic of one voice for all the proof."),
 ("b136", EMPTY, "A whisper chain: a row of invented people seen from behind leaning to whisper into each other's ears, faces hidden, warm light."),
 ("b137", EMPTY, "A finger pointing away toward a distant blurred office building, only the hand and sleeve visible, symbolic of blame."),
 ("b138", NV, "The investor standing at a library help desk area looking at a computer monitor whose screen is blurred, focused, checking information."),
 ("b139", EMPTY, "A sunrise over calm water, warm hopeful light, no people."),
 ("b140", NV, "The investor walking out of her front door into morning light, seen from slightly behind, purposeful."),
 # bổ sung cảnh chuyển tiếp
 ("b141", EMPTY, "A smartphone face-down on a dark wooden table under a single lamp, a thin glow escaping at its edge, deep shadows."),
 ("b142", MAN, "The man in the dark suit, strictly from behind, walking down a long corridor of film reel shelves toward a lit doorway."),
 ("b143", EMPTY, "Overhead view of a desk at night with scattered blank envelopes, a lamp, a closed laptop and a cold coffee cup."),
 ("b144", EMPTY, "A row of mailboxes in an apartment lobby at night, all closed, no names, no numbers."),
 ("b145", EMPTY, "Close-up of an old film camera's lens reflecting a red-orange light, dark background."),
 ("b146", EMPTY, "A long empty boardroom table seen from one end, chairs pushed back, papers gone, dawn light."),
 ("b147", EMPTY, "Heavy theater curtains closing on a dark stage, a last sliver of light."),
 ("b148", EMPTY, "A lighthouse beam sweeping over a dark sea at night, symbolic of independent verification."),
 ("b149", NV, "The investor holding a cup of coffee at her kitchen table at dawn, smiling slightly, the phone face-down beside her."),
 ("b150", EMPTY, "A quiet suburban kitchen at dawn, empty, a coffee mug on the table, birds outside the window. No people."),
]

def main():
    out = {"_ghi_chu": __doc__.strip().splitlines()[0], "model": "google/gemini-nano-banana-2.1", "tien_to": A["tien_to"], "hau_to": A["hau_to"],
           "ref_nv": "lab/mrp1/A/a01_l1.png", "ref_canh": "lab/mrp1/A/a15_l1.png",
           "ref_loi_nv": A["ref_loi"],
           "ref_loi_canh": ("The attached image is the STYLE REFERENCE for this series. Match its art style, rendering, palette and lighting exactly. "
                            "Do not copy its composition or its content. The investor woman is NOT in this scene."),
           "tranh": {}}
    for tid, loai, p in DS:
        if loai == EMPTY: p += " The investor woman is NOT in this scene; no recognizable faces."
        if loai == MAN: p += " The investor woman is NOT in this scene. The man's face is never visible: no profile, no cheek, no ear."
        out["tranh"][tid] = {"loai": loai, "ref": "ref_nv" if loai == NV else "ref_canh", "luot1": p}
    assert len(out["tranh"]) == len(DS)
    json.dump(out, open(os.path.join(ROOT, "reports", "mr6", "loi_anh.json"), "w"), ensure_ascii=False, indent=1)
    print(len(DS), "tranh")

if __name__ == "__main__":
    main()
