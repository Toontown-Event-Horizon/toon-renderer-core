from panda3d.core import VBase4
from direct.directnotify.DirectNotifyGlobal import *

notify = directNotify.newCategory("ClothingGlobals")

Shirts = [
    "phase_3/maps/desat_shirt_1.png",
    "phase_3/maps/desat_shirt_2.png",
    "phase_3/maps/desat_shirt_3.png",
    "phase_3/maps/desat_shirt_4.png",
    "phase_3/maps/desat_shirt_5.png",
    "phase_3/maps/desat_shirt_6.png",
    "phase_3/maps/desat_shirt_7.png",
    "phase_3/maps/desat_shirt_8.png",
    "phase_3/maps/desat_shirt_9.png",
    "phase_3/maps/desat_shirt_10.png",
    "phase_3/maps/desat_shirt_11.png",
    "phase_3/maps/desat_shirt_12.png",
    "phase_3/maps/desat_shirt_13.png",
    "phase_3/maps/desat_shirt_14.png",
    "phase_3/maps/desat_shirt_15.png",
    "phase_3/maps/desat_shirt_16.png",
    "phase_3/maps/desat_shirt_17.png",
    "phase_3/maps/desat_shirt_18.png",
    "phase_3/maps/desat_shirt_19.png",
    "phase_3/maps/desat_shirt_20.png",
    "phase_3/maps/desat_shirt_21.png",
    "phase_3/maps/desat_shirt_22.png",
    "phase_3/maps/desat_shirt_23.png",
]
BoyShirts = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (8, 8),
    (9, 9),
    (10, 0),
    (11, 0),
    (14, 10),
    (16, 0),
    (17, 0),
    (18, 12),
    (19, 13),
]
GirlShirts = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (5, 5),
    (6, 6),
    (7, 7),
    (9, 9),
    (12, 0),
    (13, 11),
    (15, 11),
    (16, 0),
    (20, 0),
    (21, 0),
    (22, 0),
]


Sleeves = [
    "phase_3/maps/desat_sleeve_1.png",
    "phase_3/maps/desat_sleeve_2.png",
    "phase_3/maps/desat_sleeve_3.png",
    "phase_3/maps/desat_sleeve_4.png",
    "phase_3/maps/desat_sleeve_5.png",
    "phase_3/maps/desat_sleeve_6.png",
    "phase_3/maps/desat_sleeve_7.png",
    "phase_3/maps/desat_sleeve_8.png",
    "phase_3/maps/desat_sleeve_9.png",
    "phase_3/maps/desat_sleeve_10.png",
    "phase_3/maps/desat_sleeve_15.png",
    "phase_3/maps/desat_sleeve_16.png",
    "phase_3/maps/desat_sleeve_19.png",
    "phase_3/maps/desat_sleeve_20.png",
]
BoyShorts = [
    "phase_3/maps/desat_shorts_1.png",
    "phase_3/maps/desat_shorts_2.png",
    "phase_3/maps/desat_shorts_4.png",
    "phase_3/maps/desat_shorts_6.png",
    "phase_3/maps/desat_shorts_7.png",
    "phase_3/maps/desat_shorts_8.png",
    "phase_3/maps/desat_shorts_9.png",
    "phase_3/maps/desat_shorts_10.png",
]
SHORTS = 0
SKIRT = 1
GirlBottoms = [
    ("phase_3/maps/desat_skirt_1.png", SKIRT),
    ("phase_3/maps/desat_skirt_2.png", SKIRT),
    ("phase_3/maps/desat_skirt_3.png", SKIRT),
    ("phase_3/maps/desat_skirt_4.png", SKIRT),
    ("phase_3/maps/desat_skirt_5.png", SKIRT),
    ("phase_3/maps/desat_shorts_1.png", SHORTS),
    ("phase_3/maps/desat_shorts_5.png", SHORTS),
    ("phase_3/maps/desat_skirt_6.png", SKIRT),
    ("phase_3/maps/desat_skirt_7.png", SKIRT),
    ("phase_3/maps/desat_shorts_10.png", SHORTS),
]
ClothesColors = [
    VBase4(0.933594, 0.265625, 0.28125, 1.0),
    VBase4(0.863281, 0.40625, 0.417969, 1.0),
    VBase4(0.710938, 0.234375, 0.4375, 1.0),
    VBase4(0.992188, 0.480469, 0.167969, 1.0),
    VBase4(0.996094, 0.898438, 0.320312, 1.0),
    VBase4(0.550781, 0.824219, 0.324219, 1.0),
    VBase4(0.242188, 0.742188, 0.515625, 1.0),
    VBase4(0.433594, 0.90625, 0.835938, 1.0),
    VBase4(0.347656, 0.820312, 0.953125, 1.0),
    VBase4(0.191406, 0.5625, 0.773438, 1.0),
    VBase4(0.285156, 0.328125, 0.726562, 1.0),
    VBase4(0.460938, 0.378906, 0.824219, 1.0),
    VBase4(0.546875, 0.28125, 0.75, 1.0),
    VBase4(0.570312, 0.449219, 0.164062, 1.0),
    VBase4(0.640625, 0.355469, 0.269531, 1.0),
    VBase4(0.996094, 0.695312, 0.511719, 1.0),
    VBase4(0.832031, 0.5, 0.296875, 1.0),
    VBase4(0.992188, 0.480469, 0.167969, 1.0),
    VBase4(0.550781, 0.824219, 0.324219, 1.0),
    VBase4(0.433594, 0.90625, 0.835938, 1.0),
    VBase4(0.347656, 0.820312, 0.953125, 1.0),
    VBase4(0.96875, 0.691406, 0.699219, 1.0),
    VBase4(0.996094, 0.957031, 0.597656, 1.0),
    VBase4(0.855469, 0.933594, 0.492188, 1.0),
    VBase4(0.558594, 0.589844, 0.875, 1.0),
    VBase4(0.726562, 0.472656, 0.859375, 1.0),
    VBase4(0.898438, 0.617188, 0.90625, 1.0),
    VBase4(1.0, 1.0, 1.0, 1.0),
    VBase4(0.0, 0.2, 0.956862, 1.0),
    VBase4(0.972549, 0.094117, 0.094117, 1.0),
    VBase4(0.447058, 0.0, 0.90196, 1.0),
]
ShirtStyles = {
    "bss1": [
        0,
        0,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (27, 27),
        ],
    ],
    "bss2": [
        1,
        1,
        [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)],
    ],
    "bss3": [
        2,
        2,
        [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)],
    ],
    "bss4": [
        3,
        3,
        [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)],
    ],
    "bss5": [4, 4, [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (9, 9), (10, 10), (11, 11), (12, 12)]],
    "bss6": [
        5,
        5,
        [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)],
    ],
    "bss7": [
        8,
        8,
        [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (8, 8), (9, 9), (11, 11), (12, 12), (27, 27)],
    ],
    "bss8": [
        9,
        9,
        [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)],
    ],
    "bss9": [
        10,
        0,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (27, 27),
        ],
    ],
    "bss10": [
        11,
        0,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (27, 27),
        ],
    ],
    "bss11": [
        14,
        10,
        [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)],
    ],
    "bss12": [16, 0, [(27, 27), (27, 4), (27, 5), (27, 6), (27, 7), (27, 8), (27, 9)]],
    "bss13": [
        17,
        0,
        [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)],
    ],
    "bss14": [
        18,
        12,
        [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (8, 8), (9, 9), (11, 11), (12, 12), (27, 27)],
    ],
    "bss15": [
        19,
        13,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (27, 27),
        ],
    ],
    "gss1": [
        0,
        0,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26),
            (27, 27),
        ],
    ],
    "gss2": [
        1,
        1,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26),
        ],
    ],
    "gss3": [
        2,
        2,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26),
        ],
    ],
    "gss4": [
        3,
        3,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26),
        ],
    ],
    "gss5": [
        5,
        5,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26),
        ],
    ],
    "gss6": [
        6,
        6,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26),
        ],
    ],
    "gss7": [
        7,
        7,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26),
        ],
    ],
    "gss8": [
        9,
        9,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26),
        ],
    ],
    "gss9": [12, 0, [(27, 27)]],
    "gss10": [
        13,
        11,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26),
        ],
    ],
    "gss11": [
        15,
        11,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26),
        ],
    ],
    "gss12": [16, 0, [(27, 27), (27, 4), (27, 5), (27, 6), (27, 7), (27, 8), (27, 9)]],
    "gss13": [
        20,
        0,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26),
        ],
    ],
    "gss14": [
        21,
        0,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26),
        ],
    ],
    "gss15": [
        22,
        0,
        [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (21, 21),
            (22, 22),
            (23, 23),
            (24, 24),
            (25, 25),
            (26, 26),
        ],
    ],
    "c_ss1": [25, 16, [(27, 27)]],
    "c_ss2": [27, 18, [(27, 27)]],
    "c_ss3": [38, 27, [(27, 27)]],
    "c_bss1": [26, 17, [(27, 27)]],
    "c_bss2": [28, 19, [(27, 27)]],
    "c_bss3": [37, 26, [(27, 27)]],
    "c_bss4": [39, 28, [(27, 27)]],
    "c_gss1": [23, 14, [(27, 27)]],
    "c_gss2": [24, 15, [(27, 27)]],
    "c_gss3": [35, 24, [(27, 27)]],
    "c_gss4": [36, 25, [(27, 27)]],
    "c_gss5": [40, 29, [(27, 27)]],
    "c_ss4": [45, 34, [(27, 27)]],
    "c_ss5": [46, 35, [(27, 27)]],
    "c_ss6": [52, 41, [(27, 27)]],
    "c_ss7": [53, 42, [(27, 27)]],
    "c_ss8": [54, 43, [(27, 27)]],
    "c_ss9": [55, 44, [(27, 27)]],
    "c_ss10": [56, 45, [(27, 27)]],
    "c_ss11": [57, 46, [(27, 27)]],
    "hw_ss1": [29, 20, [(27, 27)]],
    "hw_ss2": [30, 21, [(27, 27)]],
    "hw_ss3": [114, 101, [(27, 27)]],
    "hw_ss4": [115, 102, [(27, 27)]],
    "hw_ss5": [122, 109, [(27, 27)]],
    "hw_ss6": [123, 110, [(27, 27)]],
    "hw_ss7": [124, 111, [(27, 27)]],
    "hw_ss8": [125, 112, [(27, 27)]],
    "hw_ss9": [126, 113, [(27, 27)]],
    "wh_ss1": [31, 22, [(27, 27)]],
    "wh_ss2": [32, 22, [(27, 27)]],
    "wh_ss3": [33, 23, [(27, 27)]],
    "wh_ss4": [34, 23, [(27, 27)]],
    "vd_ss1": [41, 30, [(27, 27)]],
    "vd_ss2": [42, 31, [(27, 27)]],
    "vd_ss3": [43, 32, [(27, 27)]],
    "vd_ss4": [44, 33, [(27, 27)]],
    "vd_ss5": [69, 58, [(27, 27)]],
    "vd_ss6": [70, 59, [(27, 27)]],
    "vd_ss7": [96, 85, [(27, 27)]],
    "sd_ss1": [47, 36, [(27, 27)]],
    "sd_ss2": [48, 37, [(27, 27)]],
    "sd_ss3": [116, 103, [(27, 27)]],
    "tc_ss1": [49, 38, [(27, 27)]],
    "tc_ss2": [50, 39, [(27, 27)]],
    "tc_ss3": [51, 40, [(27, 27)]],
    "tc_ss4": [62, 51, [(27, 27)]],
    "tc_ss5": [63, 52, [(27, 27)]],
    "tc_ss6": [64, 53, [(27, 27)]],
    "tc_ss7": [65, 54, [(27, 27)]],
    "j4_ss1": [58, 47, [(27, 27)]],
    "j4_ss2": [59, 48, [(27, 27)]],
    "c_ss12": [60, 49, [(27, 27)]],
    "c_ss13": [61, 50, [(27, 27)]],
    "pj_ss1": [66, 55, [(27, 27)]],
    "pj_ss2": [67, 56, [(27, 27)]],
    "pj_ss3": [68, 57, [(27, 27)]],
    "sa_ss1": [71, 60, [(27, 27)]],
    "sa_ss2": [72, 61, [(27, 27)]],
    "sa_ss3": [73, 62, [(27, 27)]],
    "sa_ss4": [74, 63, [(27, 27)]],
    "sa_ss5": [75, 64, [(27, 27)]],
    "sa_ss6": [76, 65, [(27, 27)]],
    "sa_ss7": [77, 66, [(27, 27)]],
    "sa_ss8": [78, 67, [(27, 27)]],
    "sa_ss9": [79, 68, [(27, 27)]],
    "sa_ss10": [80, 69, [(27, 27)]],
    "sa_ss11": [81, 70, [(27, 27)]],
    "sa_ss12": [82, 71, [(27, 27)]],
    "sa_ss13": [83, 72, [(27, 27)]],
    "sa_ss14": [84, 73, [(27, 27)]],
    "sa_ss15": [85, 74, [(27, 27)]],
    "sa_ss16": [86, 75, [(27, 27)]],
    "sa_ss17": [87, 76, [(27, 27)]],
    "sa_ss18": [88, 77, [(27, 27)]],
    "sa_ss19": [89, 78, [(27, 27)]],
    "sa_ss20": [90, 79, [(27, 27)]],
    "sa_ss21": [91, 80, [(27, 27)]],
    "sa_ss22": [92, 81, [(27, 27)]],
    "sa_ss23": [93, 82, [(27, 27)]],
    "sa_ss24": [94, 83, [(27, 27)]],
    "sa_ss25": [95, 84, [(27, 27)]],
    "sa_ss26": [106, 93, [(27, 27)]],
    "sa_ss27": [110, 97, [(27, 27)]],
    "sa_ss28": [111, 98, [(27, 27)]],
    "sa_ss29": [120, 107, [(27, 27)]],
    "sa_ss30": [121, 108, [(27, 27)]],
    "sa_ss31": [118, 105, [(27, 27)]],
    "sa_ss32": [127, 114, [(27, 27)]],
    "sa_ss33": [128, 115, [(27, 27)]],
    "sa_ss34": [129, 116, [(27, 27)]],
    "sa_ss35": [130, 117, [(27, 27)]],
    "sa_ss36": [131, 118, [(27, 27)]],
    "sa_ss37": [132, 119, [(27, 27)]],
    "sa_ss38": [133, 120, [(27, 27)]],
    "sa_ss39": [134, 121, [(27, 27)]],
    "sa_ss40": [135, 122, [(27, 27)]],
    "sa_ss41": [136, 123, [(27, 27)]],
    "sa_ss42": [137, 124, [(27, 27)]],
    "sa_ss43": [138, 125, [(27, 27)]],
    "sa_ss44": [139, 126, [(27, 27)]],
    "sa_ss45": [140, 127, [(27, 27)]],
    "sa_ss46": [141, 128, [(27, 27)]],
    "sa_ss47": [142, 129, [(27, 27)]],
    "sa_ss48": [143, 130, [(27, 27)]],
    "sa_ss49": [144, 116, [(27, 27)]],
    "sa_ss50": [145, 131, [(27, 27)]],
    "sa_ss51": [146, 133, [(27, 27)]],
    "sa_ss52": [147, 134, [(27, 27)]],
    "sa_ss53": [148, 135, [(27, 27)]],
    "sa_ss54": [149, 136, [(27, 27)]],
    "sa_ss55": [150, 137, [(27, 27)]],
    "sc_1": [97, 86, [(27, 27)]],
    "sc_2": [98, 86, [(27, 27)]],
    "sc_3": [99, 86, [(27, 27)]],
    "sil_1": [100, 87, [(27, 27)]],
    "sil_2": [101, 88, [(27, 27)]],
    "sil_3": [102, 89, [(27, 27)]],
    "sil_4": [103, 90, [(27, 27)]],
    "sil_5": [104, 91, [(27, 27)]],
    "sil_6": [105, 92, [(27, 27)]],
    "sil_7": [107, 94, [(27, 27)]],
    "sil_8": [108, 95, [(27, 27)]],
    "emb_us1": [103, 90, [(27, 27)]],
    "emb_us2": [100, 87, [(27, 27)]],
    "emb_us3": [101, 88, [(27, 27)]],
    "sb_1": [109, 96, [(27, 27)]],
    "jb_1": [112, 99, [(27, 27)]],
    "jb_2": [113, 100, [(27, 27)]],
    "ugcms": [117, 104, [(27, 27)]],
    "lb_1": [119, 106, [(27, 27)]],
}
BottomStyles = {
    "bbs1": [0, [0, 1, 2, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],
    "bbs2": [1, [0, 1, 2, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],
    "bbs3": [2, [0, 1, 2, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],
    "bbs4": [3, [0, 1, 2, 4, 6, 8, 9, 11, 12, 13, 15, 16, 17, 18, 19, 20, 27]],
    "bbs5": [4, [0, 1, 2, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],
    "bbs6": [5, [0, 1, 2, 4, 6, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 27]],
    "bbs7": [6, [0, 1, 2, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 27]],
    "bbs8": [7, [0, 1, 2, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27]],
    "vd_bs1": [8, [27]],
    "vd_bs2": [23, [27]],
    "vd_bs3": [24, [27]],
    "c_bs1": [9, [27]],
    "c_bs2": [10, [27]],
    "c_bs5": [15, [27]],
    "sd_bs1": [11, [27]],
    "sd_bs2": [44, [27]],
    "pj_bs1": [16, [27]],
    "pj_bs2": [17, [27]],
    "pj_bs3": [18, [27]],
    "wh_bs1": [19, [27]],
    "wh_bs2": [20, [27]],
    "wh_bs3": [21, [27]],
    "wh_bs4": [22, [27]],
    "hw_bs1": [47, [27]],
    "hw_bs2": [48, [27]],
    "hw_bs5": [49, [27]],
    "hw_bs6": [50, [27]],
    "hw_bs7": [51, [27]],
    "gsk1": [0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 21, 22, 23, 24, 25, 26, 27]],
    "gsk2": [1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 21, 22, 23, 24, 25, 26]],
    "gsk3": [2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 21, 22, 23, 24, 25, 26]],
    "gsk4": [3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 21, 22, 23, 24, 25, 26]],
    "gsk5": [4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 21, 22, 23, 24, 25, 26]],
    "gsk6": [7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 21, 22, 23, 24, 25, 26, 27]],
    "gsk7": [8, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 21, 22, 23, 24, 25, 26, 27]],
    "gsh1": [5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 21, 22, 23, 24, 25, 26, 27]],
    "gsh2": [6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 21, 22, 23, 24, 25, 26, 27]],
    "gsh3": [9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 21, 22, 23, 24, 25, 26, 27]],
    "c_gsk1": [10, [27]],
    "c_gsk2": [11, [27]],
    "c_gsk3": [12, [27]],
    "vd_gs1": [13, [27]],
    "vd_gs2": [27, [27]],
    "vd_gs3": [28, [27]],
    "c_gsk4": [14, [27]],
    "sd_gs1": [15, [27]],
    "sd_gs2": [48, [27]],
    "c_gsk5": [16, [27]],
    "c_gsk6": [17, [27]],
    "c_bs3": [12, [27]],
    "c_bs4": [13, [27]],
    "j4_bs1": [14, [27]],
    "j4_gs1": [18, [27]],
    "c_gsk7": [19, [27]],
    "pj_gs1": [20, [27]],
    "pj_gs2": [21, [27]],
    "pj_gs3": [22, [27]],
    "wh_gsk1": [23, [27]],
    "wh_gsk2": [24, [27]],
    "wh_gsk3": [25, [27]],
    "wh_gsk4": [26, [27]],
    "sa_bs1": [25, [27]],
    "sa_bs2": [26, [27]],
    "sa_bs3": [27, [27]],
    "sa_bs4": [28, [27]],
    "sa_bs5": [29, [27]],
    "sa_bs6": [30, [27]],
    "sa_bs7": [31, [27]],
    "sa_bs8": [32, [27]],
    "sa_bs9": [33, [27]],
    "sa_bs10": [34, [27]],
    "sa_bs11": [35, [27]],
    "sa_bs12": [36, [27]],
    "sa_bs13": [41, [27]],
    "sa_bs14": [46, [27]],
    "sa_bs15": [45, [27]],
    "sa_bs16": [52, [27]],
    "sa_bs17": [53, [27]],
    "sa_bs18": [54, [27]],
    "sa_bs19": [55, [27]],
    "sa_bs20": [56, [27]],
    "sa_bs21": [57, [27]],
    "sa_gs1": [29, [27]],
    "sa_gs2": [30, [27]],
    "sa_gs3": [31, [27]],
    "sa_gs4": [32, [27]],
    "sa_gs5": [33, [27]],
    "sa_gs6": [34, [27]],
    "sa_gs7": [35, [27]],
    "sa_gs8": [36, [27]],
    "sa_gs9": [37, [27]],
    "sa_gs10": [38, [27]],
    "sa_gs11": [39, [27]],
    "sa_gs12": [40, [27]],
    "sa_gs13": [45, [27]],
    "sa_gs14": [50, [27]],
    "sa_gs15": [49, [27]],
    "sa_gs16": [57, [27]],
    "sa_gs17": [58, [27]],
    "sa_gs18": [59, [27]],
    "sa_gs19": [60, [27]],
    "sa_gs20": [61, [27]],
    "sa_gs21": [62, [27]],
    "sc_bs1": [37, [27]],
    "sc_bs2": [38, [27]],
    "sc_bs3": [39, [27]],
    "sc_gs1": [41, [27]],
    "sc_gs2": [42, [27]],
    "sc_gs3": [43, [27]],
    "sil_bs1": [40, [27]],
    "sil_gs1": [44, [27]],
    "hw_bs3": [42, [27]],
    "hw_gs3": [46, [27]],
    "hw_bs4": [43, [27]],
    "hw_gs4": [47, [27]],
    "hw_gs1": [51, [27]],
    "hw_gs2": [52, [27]],
    "hw_gs5": [54, [27]],
    "hw_gs6": [55, [27]],
    "hw_gs7": [56, [27]],
    "hw_gsk1": [53, [27]],
}
MAKE_A_TOON = 1
TAMMY_TAILOR = 2004
LONGJOHN_LEROY = 1007
TAILOR_HARMONY = 4008
BONNIE_BLOSSOM = 5007
WARREN_BUNDLES = 3008
WORNOUT_WAYLON = 9010
TailorCollections = {
    MAKE_A_TOON: [["bss1", "bss2"], ["gss1", "gss2"], ["bbs1", "bbs2"], ["gsk1", "gsh1"]],
    TAMMY_TAILOR: [["bss1", "bss2"], ["gss1", "gss2"], ["bbs1", "bbs2"], ["gsk1", "gsh1"]],
    LONGJOHN_LEROY: [["bss3", "bss4", "bss14"], ["gss3", "gss4", "gss14"], ["bbs3", "bbs4"], ["gsk2", "gsh2"]],
    TAILOR_HARMONY: [["bss5", "bss6", "bss10"], ["gss5", "gss6", "gss9"], ["bbs5"], ["gsk3", "gsh3"]],
    BONNIE_BLOSSOM: [["bss7", "bss8", "bss12"], ["gss8", "gss10", "gss12"], ["bbs6"], ["gsk4", "gsk5"]],
    WARREN_BUNDLES: [["bss9", "bss13"], ["gss7", "gss11"], ["bbs7"], ["gsk6"]],
    WORNOUT_WAYLON: [["bss11", "bss15"], ["gss13", "gss15"], ["bbs8"], ["gsk7"]],
}
BOY_SHIRTS = 0
GIRL_SHIRTS = 1
BOY_SHORTS = 2
GIRL_BOTTOMS = 3
HAT = 1
GLASSES = 2
BACKPACK = 4
SHOES = 8
MakeAToonBoyBottoms = []
MakeAToonBoyShirts = []
MakeAToonGirlBottoms = []
MakeAToonGirlShirts = []
MakeAToonGirlSkirts = []
MakeAToonGirlShorts = []
for style in TailorCollections[MAKE_A_TOON][BOY_SHORTS]:
    index = BottomStyles[style][0]
    MakeAToonBoyBottoms.append(index)

for style in TailorCollections[MAKE_A_TOON][BOY_SHIRTS]:
    index = ShirtStyles[style][0]
    MakeAToonBoyShirts.append(index)

for style in TailorCollections[MAKE_A_TOON][GIRL_BOTTOMS]:
    index = BottomStyles[style][0]
    MakeAToonGirlBottoms.append(index)

for style in TailorCollections[MAKE_A_TOON][GIRL_SHIRTS]:
    index = ShirtStyles[style][0]
    MakeAToonGirlShirts.append(index)

for index in MakeAToonGirlBottoms:
    flag = GirlBottoms[index][1]
    if flag == SKIRT:
        MakeAToonGirlSkirts.append(index)
    elif flag == SHORTS:
        MakeAToonGirlShorts.append(index)
    else:
        notify.error("Invalid flag")