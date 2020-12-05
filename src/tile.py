import pyxel

from constants import *

class Tile:
    def __init__(self, app, color, x, y, tile_size, tile_padding, play_area_padding):
        self.app = app

        self.color = color
        self.grid_x = x
        self.grid_y = y
        self.correct = False

        self.x = CANVAS_PADDING + self.grid_x * (tile_size + tile_padding) + play_area_padding
        self.y = CANVAS_PADDING + self.grid_y * (tile_size + tile_padding) + play_area_padding
        self.w = tile_size
        self.h = tile_size

    def update(self):
        # if hovering
        if (self.x <= pyxel.mouse_x and pyxel.mouse_x <= self.x + self.w and
            self.y <= pyxel.mouse_y and pyxel.mouse_y <= self.y + self.h):

            if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON):
                if self.correct:
                    self.app.game.next_level()
                else:
                    self.app.game.prev_level()

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.color)
        if DEBUGGING and self.correct:
            pyxel.rect(self.x, self.y, 6, 6, 0)
