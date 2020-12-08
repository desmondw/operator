import pyxel
import random
from enum import IntFlag, auto

from level import Level
from constants import *

LEVEL_MODS = [
    Mod.VANILLA,
    Mod.HOVER_ONLY,
    Mod.TEST,
    Mod.HOVER_ONLY | Mod.TEST,
]
levels = []

class Game:
    def __init__(self, app):
        self.app = app
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
                levels.append({
                    'mods': mod_set,
                    'colors': color_order[:i]
                })
        
        # Example checking of mods:

        # for level in levels:
        #     # print(level['mods'])
        #     text = ''
        #     if level['mods'] is 0: text += 'vanilla '
        #     if level['mods'] & Mod.HOVER_ONLY: text += 'hover '
        #     if level['mods'] & Mod.TEST: text += 'test '
        #     print(text)
        #     # print(level['mods'])

    def goto_level(self, num):
        if (num < 0 or len(levels) <= num): return False

        self.level_n = num
        level_data = levels[self.level_n - 1]
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
        if self.level_n == len(levels) - 1:
            self.app.new_game()
            return
        
        self.goto_level(self.level_n + 1)
    