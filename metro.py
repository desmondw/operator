import pyxel
from enum import Enum
from random import *

DEBUGGING = 1

CANVAS_SIZE = 256;
CANVAS_PADDING = 20;
TILE_PADDING_MIN = 2;
TILE_PADDING_MAX = 16;
# HOVER_SCALE = 1.1;
# TWEEN_SPEED = .08;
PALETTE_START = 1
PALETTE_END = 15
PALETTE = [
    0xFFFFFF, # WHITE - 0
    0xA200FF, # PURPLE - 1
    0xFF0097, # MAGENTA
    0x008D6D, # TEAL
    0x8CBF26, # LIME
    0xA05000, # BROWN
    0xE671B8, # PINK
    0xF09609, # ORANGE
    0x1BA1E2, # BLUE
    0xE51400, # RED
    0x339933, # GREEN - 11 (original limit)
    0xa3ff78, # NEON GREEN
    0xfcf50f, # YELLOW
    0x788aff, # SKY BLUE
    0xababab, # GRAY
    0x8dd1f0, # SKY BLUE - 15
]

class Scene(Enum):
    GAME = 1
    GAME_OVER = 2

class App:
    def __init__(self):
        pyxel.init(CANVAS_SIZE, CANVAS_SIZE, caption="metro", palette=PALETTE, scale=4)
        pyxel.mouse(True)

        self.new_game()

        pyxel.run(self.update, self.draw)

    def new_game(self):
        global scene, game
        scene = Scene.GAME
        game = Game()

    def update(self):
        scene_map = {
            Scene.GAME: game.update,
            Scene.GAME_OVER: self.new_game
        }
        scene_map[scene]()

    def draw(self):
        pyxel.cls(0)
        scene_map = {
            Scene.GAME: game.draw,
            Scene.GAME_OVER: lambda: None
        }
        scene_map[scene]()
        

class Game:
    def __init__(self):
        self.color_order = [c for c in range(PALETTE_START, PALETTE_END+1)]
        shuffle(self.color_order)
        self.used_colors = [self.color_order[0]]
        del self.color_order[0]
        self.new_level()
    
    def new_level(self):
        # finished last level, restart
        if len(self.color_order) == 0:
            global scene
            scene = Scene.GAME_OVER
            return
        
        self.used_colors.append(self.color_order[0])
        del self.color_order[0]
        self.level = Level(self.used_colors)

    def update(self):
        self.level.update()

    def draw(self):
        self.level.draw()

class Level:
    def __init__(self, colors):
        self.grid = []
        self.grid_size = len(colors)

        # determine values for drawing/collision
        play_area = CANVAS_SIZE - CANVAS_PADDING * 2
        tile_padding = max(TILE_PADDING_MIN, min(TILE_PADDING_MAX, play_area / (self.grid_size - 1) * .1)) // 1
        tile_size = (play_area - (self.grid_size - 1) * tile_padding) // self.grid_size
        play_area_padding = (play_area - ((tile_size + tile_padding) * self.grid_size - tile_padding)) // 2

        # generate all tiles (colors, grid position)
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                # add a random color tile (excluding the new color)
                tile = Tile(choice(colors[:-1]), i, j, tile_size, tile_padding, play_area_padding)
                row.append(tile)
            self.grid.append(row)
        
        # change one of the tiles to the new color
        tile = Tile(colors[-1], randrange(self.grid_size), randrange(self.grid_size), tile_size, tile_padding, play_area_padding)
        tile.correct = True
        self.grid[tile.grid_x][tile.grid_y] = tile

    def update(self):
        for row in self.grid:
            for tile in row:
                tile.update()

    def draw(self):
        for row in self.grid:
            for tile in row:
                tile.draw()

class Tile:
    def __init__(self, color, x, y, tile_size, tile_padding, play_area_padding):
        self.color = color
        self.grid_x = x
        self.grid_y = y
        self.correct = False

        self.x = CANVAS_PADDING + self.grid_x * (tile_size + tile_padding) + play_area_padding
        self.y = CANVAS_PADDING + self.grid_y * (tile_size + tile_padding) + play_area_padding
        self.w = tile_size
        self.h = tile_size

    def update(self):
        if (self.correct):
            if (self.x <= pyxel.mouse_x and pyxel.mouse_x <= self.x + self.w and
                self.y <= pyxel.mouse_y and pyxel.mouse_y <= self.y + self.h):
                if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON):
                    game.new_level()

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.color)
        if DEBUGGING and self.correct:
            pyxel.rect(self.x, self.y, 6, 6, 0)

app = App()
