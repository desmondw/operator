import pyxel

from constants import *
from game import *

class App:
    def __init__(self):
        pyxel.init(CANVAS_SIZE, CANVAS_SIZE, caption="metro", palette=PALETTE, scale=4)
        pyxel.mouse(True)

        self.new_game()

        pyxel.run(self.update, self.draw)

    def new_game(self):
        self.scene = Scene.TITLE
        self.game = Game(self)

    def update(self):
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
        
class Title:
    def __init__(self, app):
        self.app = app

    def update(self):
        if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON):
            self.app.scene = Scene.GAME

    def draw(self):
        text = "metro"
        text = "METRO"
        pyxel.text(CANVAS_SIZE / 2 - (len(text) * CHAR_WIDTH) / 2, CANVAS_SIZE / 2 - CHAR_HEIGHT / 2, text, 1)


app = App()
