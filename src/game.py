import pyxel
import random
from enum import IntFlag, auto

from level import Level
from constants import *

class Game:
    def __init__(self, app):
        self.app = app
        self.levels = []
        self.level_n = 0

        self.gen_levels()
        self.goto_level(1)

    def update(self):
        self.level.update()

    def draw(self):
        self.level.draw()
    
    def gen_levels(self):
        for mod_set in LEVEL_MODS:
            color_order = [c for c in range(PALETTE_START, PALETTE_END+1)]
            random.shuffle(color_order)

            for i in range(2, len(color_order)+1):
                self.levels.append({
                    'mods': mod_set,
                    'colors': color_order[:i]
                })

    def goto_level(self, num):
        if (num < 0 or len(self.levels) <= num): return False

        self.level_n = num
        level_data = self.levels[self.level_n - 1]
        self.level = Level(self.app, level_data['colors'], level_data['mods'])
    
    def prev_level(self):
        # return to title if on first level
        if self.level_n == 1:
            self.app.scene = Scene.TITLE
            self.goto_level(1)
            return
        
        self.goto_level(self.level_n - 1)
    
    def next_level(self):
        # send to title after complete
        if self.level_n == len(self.levels) - 1:
            self.app.new_game()
            return
        
        self.goto_level(self.level_n + 1)
    