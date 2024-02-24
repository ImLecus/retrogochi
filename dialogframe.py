from text import Text
from sprite import Sprite
class DialogFrame:
    def __init__(self, screen ,text) -> None:
        self.sprite = Sprite("src/dialogframe.gif", screen, (320, 560))
        self.text = Text(screen, text, (16, 510, 608, 160) )
    def draw(self) -> None:
        """Draws the text and the sprite on the screen"""
        self.sprite.draw()
        self.text.draw()