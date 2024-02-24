import pygame as game
import sys
from pygame.locals import *
from sprite import *
from text import *
from button import *
from dialogframe import *
from scene import *

# --- INITIALIZING PYGAME ---

SPACE = 640
game.init()
screen = game.display.set_mode((SPACE, SPACE))
game.display.set_caption("Retrogochi")

# --- MODAL ---
isModalActive = False

modalbg = game.Surface((640,640))
modalbg.set_alpha(128)
modalbg.fill((0,29,42))

modalimg = Sprite("src/modalimg.png", screen)
modalimg.move(SPACE / 8, SPACE / 4)

modaltext = Text(screen, "Give your pet a name:", (SPACE / 8 + 30, SPACE / 4 + 30, 100, 100))

# --- SCENES ---

home = Scene((
    Sprite("src/bg.png", screen, (SPACE / 2, SPACE / 2)), # Background
    Button(Sprite("src/poop.png", screen, (SPACE / 2 + 160, SPACE / 2 + 64))), # Poop
    Button(Sprite("src/settings.png", screen, (48,48))), # Settings
    Text(screen, "My tamagochi", (SPACE / 2 - 120, 16, 240, 64)), # Tamagochi's name
    DialogFrame(screen, "Hey! I'm.. well, I don't have a name, but I'm your retrogochi. I know! \nYou can give me a name.") # Dialog Frame
))


scenes = [home]
scene_pointer = 0
# --- UPDATING EVERY FRAME ---

while True:
    screen.fill((0,0,0))

    scenes[scene_pointer].render()

    if isModalActive:
        screen.blit(modalbg, (0,0))
        modalimg.draw()
        modaltext.draw()

    for event in game.event.get():

        if event.type == game.QUIT:
            game.quit()
            sys.exit(0)


    game.display.flip()