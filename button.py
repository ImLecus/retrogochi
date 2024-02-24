class Button:
    def __init__(self, sprite) -> None:
        self.sprite = sprite
    def draw(self) -> None:
        """Draws the button sprite on the screen"""
        self.sprite.draw()