from enum import Enum

DEBUGGING = 1

CANVAS_SIZE = 256
CANVAS_PADDING = 20
TILE_PADDING_MIN = 2
TILE_PADDING_MAX = 16
# HOVER_SCALE = 1.1
# TWEEN_SPEED = .08
CHAR_WIDTH = 4
CHAR_HEIGHT = 5
PALETTE_START = 2
PALETTE_END = 15

# 0 = cursor outline
# 7 = cursor fill
# 6 = cursor fill shadow
PALETTE = [
    0xFFFFFF, # WHITE - 0
    0xababab, # GRAY
    0x7b27ab, # PURPLE - 2
    0xdb2e9f, # MAGENTA
    0x00ebb4, # TEAL
    0x66e8e8, # CYAN
    0x99540f, # BROWN
    0xdb84d8, # PINK
    0xffa312, # ORANGE
    0x8979d4, # LAVENDER
    0xfa4d3c, # RED
    0x29a329, # DARK GREEN
    0x83f789, # BRIGHT GREEN
    0xf5f056, # YELLOW
    0x3850eb, # DEEP BLUE
    0xd6f3ff, # SKY BLUE - 15
]
OG_PALETTE = [
    0xFFFFFF, # WHITE - 0
    0xababab, # GRAY
    0xA200FF, # PURPLE - 2
    0xFF0097, # MAGENTA
    0x008D6D, # TEAL
    0x8CBF26, # LIME
    0xA05000, # BROWN
    0xE671B8, # PINK
    0xF09609, # ORANGE
    0x1BA1E2, # BLUE
    0xE51400, # RED
    0x339933, # GREEN - 11
]
PASTEL_PALETTE = [
    0xFFFFFF, # WHITE - 0
    0xababab, # GRAY
    0xFDF39A,
    0xFEC278,
    0xF7977A,
    0xF6B5C4,
    0xD9D8EC,
    0xC2AFD5,
    0xA1BBE1,
    0xD4EFFD,
    0xC0E0C7,
    0xF1F3E3,
    0xC7B899,
    0xFAB9AA,
    0xBFD1DD,
    # 0xCEE197,
    0xB7DAF5,
]

class Scene(Enum):
    GAME = 1
    TITLE = 2
