import pygame as game
from pygame.locals import *
from config import *
from sprite import *
from text import *

game.init()


screen = game.display.set_mode((config.SPACE, config.SPACE))

game.display.set_caption(config.get_caption())

# Cursor
game.mouse.set_visible(False)
cursor = Sprite("src/cursor.png", screen)

bg = Sprite("src/bg.png", screen)
settings = Sprite("src/settings.png", screen)
settings.rect.center = (48,48)
font = Text(screen, "My tamagochi", (config.SPACE / 2 - 120, 16, 240, 64))
dialogframe = Sprite("src/dialogframe.gif", screen)
dialogframe.rect.center = (config.SPACE / 2, 560)
def refresh_static_objects():
    # Background
    bg.draw()
    # Tamagochi
    game.draw.rect(screen, (0,0,0), (config.SPACE / 2 - 100, config.SPACE / 2 - 100, 200 ,200), 1)
    # Poop
    game.draw.rect(screen, (0,0,0), (config.SPACE / 2 + 150, config.SPACE / 2, 100 ,100), 1)
    # Settings
    settings.draw()
    # Shop
    game.draw.rect(screen, (0,0,0), (config.SPACE - 80,16, 64, 64), 1)
    # Tamagochi name
    font.draw()
    # Dialog frame
    dialogframe.draw()

while True:

    screen.fill((0,0,0))
    refresh_static_objects()

    for event in game.event.get():

        if event.type == game.QUIT:
            game.quit()



    cursor.rect.center = game.mouse.get_pos()
    cursor.draw()
    game.display.flip()

    game.time.Clock().tick(60)