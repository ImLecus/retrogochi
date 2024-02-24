import pygame as game
class Sprite:
    def __init__(self, path, screen):
        self.img = game.image.load(path)
        self.rect = self.img.get_rect()
        self.screen = screen
    def draw(self):
        self.screen.blit(self.img, self.rect)