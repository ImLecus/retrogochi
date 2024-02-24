import pygame as game
from pygame.locals import *

SPACE = 640


game.init()
screen = game.display.set_mode((SPACE, SPACE))
screen.fill((56,216,142))

caption = "Retrogochi"
game.display.set_caption(caption)
game.display.update()
while True:
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()