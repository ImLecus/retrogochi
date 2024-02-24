from sprite import Sprite
class Scene:
    def __init__(self, elements) -> None:
        self.elements = elements
    def render(self) -> None:
        """Draws all the elements on the screen"""
        for e in self.elements:
            e.draw()
    def bg(self) -> Sprite:
        """Returns the background image element"""
        return self.elements[0]