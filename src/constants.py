from enum import Enum, IntFlag, auto

DEBUG = 0
SOUND = 1

TITLE = 'operator'
CANVAS_SIZE = 256
CANVAS_PADDING = 20
PLAY_AREA_SIZE = CANVAS_SIZE - CANVAS_PADDING * 2
TILE_PADDING_MIN = 2
TILE_PADDING_MAX = 16
PALETTE_START = 2
PALETTE_END = 15
LEVELS_PER_BATCH = PALETTE_END - PALETTE_START

# 0 = cursor outline
# 7 = cursor fill
# 6 = cursor fill shadow
PALETTE = [
    0xFFFFFF, # WHITE - 0
    0xababab, # GRAY
    0x7b27ab, # PURPLE - 2
    0xdb2e9f, # MAGENTA
    0x29ffb8, # TEAL
    0x66e8e8, # CYAN
    0x99540f, # BROWN
    0xdb84d8, # PINK
    0xffa312, # ORANGE
    0x8979d4, # LAVENDER
    0xfa4d3c, # RED
    0x29a329, # DARK GREEN
    0xa6ffaa, # LIGHT GREEN
    0xf5f056, # YELLOW
    0x3850eb, # DEEP BLUE
    0xd6f3ff, # SKY BLUE - 15
]

class Sfx(Enum):
    TILE_HOVER = 0
    TILE_CLICK_CORRECT = 1
    TILE_CLICK_WRONG = 2
    GAME_WON = 3


class Scene(Enum):
    GAME = auto()
    TITLE = auto()

# Modifiers to gameplay
class Mod(IntFlag):
    VANILLA = 0
    HOVER_ONLY = auto() # tiles only show their color on hover
    TEST = auto()
