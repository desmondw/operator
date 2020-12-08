import pyxel
import random

from tile import Tile
from constants import *

class Level:
    def __init__(self, app, colors, mods=[]):
        self.app = app

        self.grid = []
        self.grid_size = len(colors)

        # determine values for drawing/collision
        tile_padding = self.get_tile_padding()
        tile_size = self.get_tile_size()
        play_area_padding = self.get_play_area_padding()

        # generate all tiles (colors, grid position)
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                # add a random color tile (excluding the new color)
                tile = Tile(self.app, random.choice(colors[:-1]), i, j, tile_size, tile_padding, play_area_padding)
                row.append(tile)
            self.grid.append(row)

        
        # change one of the tiles to the new color
        tile = Tile(self.app,
                    colors[-1],
                    random.randrange(self.grid_size),
                    random.randrange(self.grid_size),
                    tile_size,
                    tile_padding,
                    play_area_padding)
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

    def get_tile_padding(self):
        return max(TILE_PADDING_MIN, min(TILE_PADDING_MAX, PLAY_AREA_SIZE / (self.grid_size - 1) * .1)) // 1

    def get_tile_size(self):
        tile_padding = self.get_tile_padding()
        return (PLAY_AREA_SIZE - (self.grid_size - 1) * tile_padding) // self.grid_size

    def get_play_area_padding(self):
        tile_padding = self.get_tile_padding()
        tile_size = self.get_tile_size()
        return (PLAY_AREA_SIZE - ((tile_size + tile_padding) * self.grid_size - tile_padding)) // 2
    