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

        self._x = CANVAS_PADDING + self.grid_x * (tile_size + tile_padding) + play_area_padding
        self._y = CANVAS_PADDING + self.grid_y * (tile_size + tile_padding) + play_area_padding
        self._w = tile_size
        self._h = tile_size

        # animating
        self.x = self._x + self._w // 2
        self.y = self._y + self._h // 2
        self.w = 0
        self.h = 0

        self.was_hovering = self.is_hovering()

    def update(self):
        if self.is_hovering():
            if not self.was_hovering:
                self.mouse_over()
            self.was_hovering = True

            if self.app.input_enabled and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                self.app.game.level.animating_out = True
                if self.correct:
                    if self.app.sound:
                        if self.app.game.level_n == len(self.app.game.levels)-1:
                            pyxel.play(1, Sfx.GAME_WON.value)
                        else:
                            pyxel.play(1, Sfx.TILE_CLICK_CORRECT.value)
                    self.app.game.level.post_animation_level = 1
                else:
                    if self.app.sound:
                        pyxel.play(1, Sfx.TILE_CLICK_WRONG.value)
                    self.app.game.level.post_animation_level = -1
        else:
            self.was_hovering = False

    def draw(self, animating_in, animating_out, anim_step=1):
        if animating_in:
            self.w += 2 * anim_step
            self.h += 2 * anim_step
            self.x -= 1 * anim_step
            self.y -= 1 * anim_step
        elif animating_out:
            self.w -= 2 * anim_step
            self.h -= 2 * anim_step
            self.x += 1 * anim_step
            self.y += 1 * anim_step
        else:
            self.w = self._w
            self.h = self._h
            self.h = self._h
            self.x = self._x
            self.x = self._x
            self.y = self._y
        if self.is_hovering():
            growth = math.ceil(self.app.game.level.get_tile_padding() / 4)
            pyxel.rect(self.x - growth,
                        self.y - growth,
                        self.w + growth * 2,
                        self.h + growth * 2,
                        self.color)
        else:
            color = self.app.game.level.check_for_mod(Mod.HOVER_ONLY) or self.color
            pyxel.rect(self.x, self.y, self.w, self.h, color)

        if DEBUG and self.correct:
            pyxel.rect(self.x, self.y, 6, 6, 0)
    
    def mouse_over(self):
        if self.app.sound:
            pyxel.play(0, Sfx.TILE_HOVER.value)
    
    def is_hovering(self):
        return (self.app.input_enabled
                and self.x <= pyxel.mouse_x and pyxel.mouse_x <= self.x + self.w
                and self.y <= pyxel.mouse_y and pyxel.mouse_y <= self.y + self.h)
