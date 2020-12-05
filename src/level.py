import pyxel
from random import *

from constants import *
from tile import *

class Level:
    def __init__(self, app, colors):
        self.app = app

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
                tile = Tile(self.app, choice(colors[:-1]), i, j, tile_size, tile_padding, play_area_padding)
                row.append(tile)
            self.grid.append(row)
        
        # change one of the tiles to the new color
        tile = Tile(self.app, colors[-1], randrange(self.grid_size), randrange(self.grid_size), tile_size, tile_padding, play_area_padding)
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
