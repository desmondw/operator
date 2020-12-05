import pyxel

from constants import *
from level import *

class Game:
    def __init__(self, app):
        self.app = app

        self.color_order = [c for c in range(PALETTE_START, PALETTE_END+1)]
        shuffle(self.color_order)
        self.used_colors = self.color_order[:2]
        del self.color_order[0]
        del self.color_order[0]
        self.shuffle_grid()

    def update(self):
        self.level.update()

    def draw(self):
        self.level.draw()
    
    def prev_level(self):
        # return to title
        if len(self.used_colors) == 2:
            self.app.scene = Scene.TITLE
            self.shuffle_grid()
            return
        
        self.color_order.insert(0, self.used_colors.pop())
        self.shuffle_grid()
    
    def next_level(self):
        # finished last level, restart
        if len(self.color_order) == 0:
            self.app.new_game()
            return
        
        self.used_colors.append(self.color_order[0])
        del self.color_order[0]
        self.shuffle_grid()
    
    def shuffle_grid(self):
        self.level = Level(self.app, self.used_colors)
