import pygame as game
from pygame.locals import *
from config import *
from sprite import *
from text import *
from button import *
from dialogframe import *

game.init()

screen = game.display.set_mode((config.SPACE, config.SPACE))

game.display.set_caption(config.get_caption())


bg = Sprite("src/bg.png", screen)
poop = Button(Sprite("src/poop.png", screen))
poop.sprite.rect.center = (config.SPACE / 2 + 160, config.SPACE / 2 + 64)
settings = Button(Sprite("src/settings.png", screen))
settings.sprite.rect.center = (48,48)
font = Text(screen, "My tamagochi", (config.SPACE / 2 - 120, 16, 240, 64))
dialogframe = DialogFrame(screen, "¡Hola! Soy... bueno, no tengo nombre, pero soy tu mascota virtual. ¡Ya sé! \nPuedes ponerme tú un nombre.")
dialogframe.sprite.rect.center = (config.SPACE / 2, 560)
def refresh_static_objects():
    # Background
    bg.draw()
    # Tamagochi
    game.draw.rect(screen, (0,0,0), (config.SPACE / 2 - 100, config.SPACE / 2 - 100, 200 ,200), 1)
    # Poop
    poop.draw()
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


    game.display.flip()