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

        self.x = CANVAS_PADDING + self.grid_x * (tile_size + tile_padding) + play_area_padding
        self.y = CANVAS_PADDING + self.grid_y * (tile_size + tile_padding) + play_area_padding
        self.w = tile_size
        self.h = tile_size

        self.hovering = self.is_hovering()

    def update(self):
        if self.is_hovering():
            if not self.hovering:
                self.mouse_over()
            self.hovering = True

            if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON):
                if self.correct:
                    if SOUND:
                        pyxel.play(1, Sfx.TILE_CLICK_CORRECT.value)
                    self.app.game.next_level()
                else:
                    if SOUND:
                        pyxel.play(1, Sfx.TILE_CLICK_WRONG.value)
                    self.app.game.prev_level()
        else:
            self.hovering = False

    def draw(self):
        if self.is_hovering():
            self.draw_tile_hovering()
        else:
            self.draw_tile(self.app.game.level.check_for_mod(Mod.HOVER_ONLY))

        if DEBUG and self.correct:
            pyxel.rect(self.x, self.y, 6, 6, 1)
    
    def draw_tile(self, force_color=False):
        color = force_color or self.color
        pyxel.rect(self.x, self.y, self.w, self.h, color)

    def draw_tile_hovering(self):
        growth = math.ceil(self.app.game.level.get_tile_padding() / 4)
        pyxel.rect(self.x - growth,
                    self.y - growth,
                    self.w + growth * 2,
                    self.h + growth * 2,
                    self.color)

    def mouse_over(self):
        if SOUND:
            pyxel.play(0, Sfx.TILE_HOVER.value)
        pass # add click sound
    
    def is_hovering(self):
        return (self.x <= pyxel.mouse_x and pyxel.mouse_x <= self.x + self.w and
            self.y <= pyxel.mouse_y and pyxel.mouse_y <= self.y + self.h)
