from text import *
from sprite import *
from config import *
class DialogFrame:
    def __init__(self, screen ,text):
        self.sprite = Sprite("src/dialogframe.gif", screen)
        self.text = Text(screen, text, (16, 510, 608, 160) )
    def draw(self):
        self.sprite.draw()
        self.text.draw()