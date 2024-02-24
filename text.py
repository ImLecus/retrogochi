import pygame as game
class Text:
    def __init__(self,screen, text = "New Text", rect = (0,0,0,0)) -> None:
        self.text = text
        self.rect = rect
        self.screen = screen
    def draw(self) -> None:
        """Draws the text on the screen"""
        font = game.font.Font("src/PixCon.ttf", 16)
        img = font.render(self.text, True, (0,29,42))
        self.screen.blit(img, self.rect)