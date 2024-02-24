class Scene:
    def __init__(self, elements) -> None:
        self.elements = elements
    def render(self):
        for e in self.elements:
            e.draw()