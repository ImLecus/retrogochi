import pygame as game
class Text:
    def __init__(self,screen, text = "New Text", rect = (0,0,0,0)):
        self.text = text
        self.rect = rect
        self.screen = screen
    def draw(self):
        font = game.font.Font("src/PixCon.ttf", 18)
        img = font.render(self.text, True, (0,0,0))
        self.screen.blit(img, self.rect)