import pyxel

from game import Game
from constants import *

class App:
    def __init__(self):
        pyxel.init(CANVAS_SIZE, CANVAS_SIZE, caption=TITLE, palette=PALETTE, scale=4)
        pyxel.load('assets/sounds.pyxres')
        pyxel.mouse(True)
        self.input_enabled = True
        self.sound = bool(SOUND)

        self.new_game()

        pyxel.run(self.update, self.draw)

    def update(self):
        self.check_input()
        scene_map = {
            Scene.GAME: self.game.update,
            Scene.TITLE: Title(self).update
        }
        scene_map[self.scene]()

    def draw(self):
        pyxel.cls(0)
        scene_map = {
            Scene.GAME: self.game.draw,
            Scene.TITLE: Title(self).draw
        }
        scene_map[self.scene]()

        if DEBUG:
            text = f'level {self.game.level_n}'
            pyxel.text(0,0, text, 1)

    @property
    def input_enabled(self):
        return self._input_enabled

    @input_enabled.setter
    def input_enabled(self, value):
        self._input_enabled = value

    def new_game(self):
        self.scene = Scene.TITLE
        self.game = Game(self)

    def check_input(self):
        self.check_debug_input()
        if pyxel.btnr(pyxel.KEY_S):
            self.sound = not self.sound


    def check_debug_input(self):
        if not DEBUG: return
        key = 0
        if pyxel.btnr(pyxel.KEY_0):
            self.scene = Scene.GAME
            self.game.goto_level(12)
        if pyxel.btnr(pyxel.KEY_1): key = 1
        if pyxel.btnr(pyxel.KEY_2): key = 2
        if pyxel.btnr(pyxel.KEY_3): key = 3
        if pyxel.btnr(pyxel.KEY_4): key = 4
        if key:
            self.scene = Scene.GAME
            self.game.goto_level(LEVELS_PER_BATCH * (key - 1) + 1)
        
class Title:
    def __init__(self, app):
        self.app = app

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.app.scene = Scene.GAME
            self.app.game.level_n = 1

    def draw(self):
        text = TITLE
        pyxel.text(CANVAS_SIZE / 2 - (len(text) * pyxel.FONT_WIDTH) / 2, CANVAS_SIZE / 2 - pyxel.FONT_HEIGHT / 2, text, 1)

        # controls
        text = '[s] toggle sound'
        pyxel.text(CANVAS_SIZE - len(text) * pyxel.FONT_WIDTH - 1, CANVAS_SIZE - (pyxel.FONT_HEIGHT + 1) * 1, text, 1)

        # credits
        pyxel.text(1, CANVAS_SIZE - (pyxel.FONT_HEIGHT + 1) * 2, '@DesmondWeindorf', 1)
        pyxel.text(1, CANVAS_SIZE - (pyxel.FONT_HEIGHT + 1) * 1, 'desmondw.com', 1)


app = App()
