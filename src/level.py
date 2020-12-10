import pyxel
import random

from tile import Tile
from constants import *

class Level:
    def __init__(self, app, colors, mods=Mod.VANILLA):
        self.app = app

        self.grid = []
        self.grid_size = len(colors)
        self.colors = colors
        self.mods = mods
        self.animating_in = True
        self.animating_out = False
        self.app.input_enabled = False
        self.post_animation_level = 0

        # determine values for drawing/collision
        self.tile_padding = self.get_tile_padding()
        self.tile_size = self.get_tile_size()
        self.play_area_padding = self.get_play_area_padding()

        # generate all tiles (colors, grid position)
        self.gen_tiles()

    def update(self):
        if self.animating_in and self.grid[0][0].w >= self.grid[0][0]._w:
            self.animating_in = False
            self.app.input_enabled = True
        if self.animating_out and self.grid[0][0].w <= 0:
            self.app.input_enabled = True
            if self.post_animation_level == -1:
                self.app.game.prev_level()
            else:
                self.app.game.next_level()

        for row in self.grid:
            for tile in row:
                tile.update()

    def draw(self):
        for row in self.grid:
            for tile in row:
                tile.draw(self.animating_in, self.animating_out, self.grid[0][0]._w / 16)

    def get_tile_padding(self):
        return max(TILE_PADDING_MIN, min(TILE_PADDING_MAX, PLAY_AREA_SIZE / (self.grid_size - 1) * .1)) // 1

    def get_tile_size(self):
        tile_padding = self.get_tile_padding()
        return (PLAY_AREA_SIZE - (self.grid_size - 1) * tile_padding) // self.grid_size

    def get_play_area_padding(self):
        tile_padding = self.get_tile_padding()
        tile_size = self.get_tile_size()
        return (PLAY_AREA_SIZE - ((tile_size + tile_padding) * self.grid_size - tile_padding)) // 2
    
    def gen_tiles(self):
        # assure the target color is in there
        color_pile = [self.colors[-1]]
        for color in self.colors[:-1]:
            # assure each color has at least 3 tiles
            color_pile += [color]*2
        while len(color_pile) < self.grid_size**2:
            # add a random color tile (excluding the new color)
            color_pile.append(random.choice(self.colors[:-1]))
        random.shuffle(color_pile)

        if DEBUG:
            color_map = {}
            for c in color_pile:
                if not c in color_map:
                    color_map[c] = 0
                color_map[c] +=1
            print(color_map)

        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                c = color_pile.pop()
                tile = Tile(self.app,
                            c,
                            i,
                            j,
                            self.tile_size,
                            self.tile_padding,
                            self.play_area_padding)
                if c == self.colors[-1]:
                    tile.correct = True

                row.append(tile)
            self.grid.append(row)

    def check_for_mod(self, mod):
        return self.mods & mod
