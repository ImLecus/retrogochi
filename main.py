import pygame as game
from pygame.locals import *
from config import *
from sprite import *

game.init()

screen = game.display.set_mode((config.SPACE, config.SPACE))

# Background

bg = Sprite("src/bg.png", screen)
bg.draw()

game.display.set_caption(config.get_caption())

# Tamagochi
game.draw.rect(screen, (0,0,0), (config.SPACE / 2 - 100, config.SPACE / 2 - 100, 200 ,200), 1)

# Poop
game.draw.rect(screen, (0,0,0), (config.SPACE / 2 + 150, config.SPACE / 2, 100 ,100), 1)

# Settings

settings = Sprite("src/settings.png", screen)
settings.rect.center = (48,48)
settings.draw()

# Shop
game.draw.rect(screen, (0,0,0), (config.SPACE - 80,16, 64, 64), 1)

# Tamagochi name
game.draw.rect(screen, (0,0,0), (config.SPACE / 2 - 120, 16, 240, 64), 1)

game.display.update()
while True:
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()