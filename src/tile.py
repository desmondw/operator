import pyxel
import math

from constants import *

class Tile:
    def __init__(self, app, color, x, y, tile_size, tile_padding, play_area_padding):
        self.app = app

        self.color = color
        self.grid_x = x
        self.grid_y = y
        self.correct = False
        self.hovering = False

        self.x = CANVAS_PADDING + self.grid_x * (tile_size + tile_padding) + play_area_padding
        self.y = CANVAS_PADDING + self.grid_y * (tile_size + tile_padding) + play_area_padding
        self.w = tile_size
        self.h = tile_size

    def update(self):
        if self.is_hovering():
            if not self.hovering:
                self.mouse_over()
            self.hovering = True

            if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON):
                if self.correct:
                    self.app.game.next_level()
                else:
                    self.app.game.prev_level()
        else:
            self.hovering = False

    def draw(self):
        if self.is_hovering():
            growth = math.ceil(self.app.game.level.get_tile_padding() / 4)
            pyxel.rect(self.x - growth,
                        self.y - growth,
                        self.w + growth * 2,
                        self.h + growth * 2,
                        self.color)
        else:
            pyxel.rect(self.x, self.y, self.w, self.h, self.color)

        if DEBUGGING and self.correct:
            pyxel.rect(self.x, self.y, 6, 6, 0)

    def mouse_over(self):
        pass # add click sound
    
    def is_hovering(self):
        return (self.x <= pyxel.mouse_x and pyxel.mouse_x <= self.x + self.w and
            self.y <= pyxel.mouse_y and pyxel.mouse_y <= self.y + self.h)
