import pygame as game
class Sprite:
    def __init__(self, path, screen, pos = (0,0)) -> None:
        self.img = game.image.load(path)
        self.rect = self.img.get_rect()
        self.screen = screen
        self.rect.center = pos
    def draw(self) -> None:
        """Draws the sprite on the screen"""
        self.screen.blit(self.img, self.rect)
    def move(self,x, y) -> None:
        """Moves the sprite to a fixed position"""
        self.rect = (self.rect[0] + x, self.rect[1] + y)