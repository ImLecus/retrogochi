from text import *
from sprite import *
class DialogFrame:
    def __init__(self, screen ,text):
        self.sprite = Sprite("src/dialogframe.gif", screen, (320, 560))
        self.text = Text(screen, text, (16, 510, 608, 160) )
    def draw(self):
        self.sprite.draw()
        self.text.draw()