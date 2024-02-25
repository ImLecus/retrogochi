import pygame as game
import sys
from pygame.locals import *
from sprite import *
from text import *
from button import *
from dialogframe import *
from scene import *
from dialogs import *
import random
from gochi import *
# --- INITIALIZING PYGAME ---

SPACE = 640
game.init()
screen = game.display.set_mode((SPACE, SPACE))
game.display.set_caption("Retrogochi")
gochi = Gochi()

# --- MODAL ---
isModalActive = False

modalbg = game.Surface((640,640))
modalbg.set_alpha(128)
modalbg.fill((0,29,42))

modalimg = Sprite("src/modalimg.png", screen)
modalimg.move(SPACE / 8, SPACE / 4)

modaltext = Text(screen, "Give your pet a name:", (SPACE / 8 + 30, SPACE / 4 + 30, 100, 100))

# --- SCENES ---
dialogtext = ""
# NOTE: Background element must be the first in the list
home = Scene([
    Sprite("src/bg.png", screen, (SPACE / 2, SPACE / 2)), # Background
    Sprite("src/bg.png", screen, (SPACE / 2, SPACE + SPACE / 2)), # Background top
    Button(Sprite("src/settings.png", screen, (48,48))), # Settings
    Text(screen, "Gochi", (SPACE / 2 - 48, 32, 240, 64)), # Tamagochi's name
    DialogFrame(screen, dialogtext), # Dialog Frame
    Button(Sprite("src/gochi.png", screen, (SPACE / 2, SPACE / 2 - 32))), # Tamagochi
    Sprite("src/bars.png",screen ,(0 + 100,SPACE / 2 - 100))
])

settings = Scene([
    Sprite("src/bg.png", screen, (SPACE / 2, SPACE / 2)), # Background
    Sprite("src/bg.png", screen, (SPACE / 2, SPACE + SPACE / 2)), # Background top
    Button(Sprite("src/back.png", screen, (48,48))), # Return home
    Text(screen, "Settings", (SPACE / 2 - 120, 16, 240, 64)), # "Settings" text
])


scenes = [home, settings]
scene_pointer = 0
# --- UPDATING EVERY FRAME ---

def mouse_under_settings_btn():
    pos = game.mouse.get_pos()
    return  (16 < pos[0] < 80) and (16 < pos[1] < 80) and not isModalActive

def mouse_under_gochi():
    pos = game.mouse.get_pos()
    return (SPACE / 2 - 64 < pos[0] < SPACE / 2 + 64) and (200 < pos[1] < 400) and not isModalActive
square = game.draw.rect(screen, (255,0,0), (SPACE / 2 - 120, 16, 240, 64))

while True:
    # --- RE-RENDER THE SCENE ---
    screen.fill((0,190,145))
    scenes[scene_pointer].render()
    #game.draw.rect(screen, (255,0,0), (SPACE / 2 - 120, 16, 240, 64), 1)
    # --- MOVING THE BACKGROUND ---
    scenes[scene_pointer][0].move(0,-1)
    scenes[scene_pointer][1].move(0,-1)
    if scenes[scene_pointer][0].rect[1] < -SPACE:
        scenes[scene_pointer][0].set_position(0, SPACE)
    if scenes[scene_pointer][1].rect[1] < -SPACE:
        scenes[scene_pointer][1].set_position(0, SPACE)

    if isModalActive:
        screen.blit(modalbg, (0,0))
        modalimg.draw()
        modaltext.draw()

    for event in game.event.get():

        if event.type == game.QUIT:
            game.quit()
            sys.exit(0)

        # --- HOVER EFFECTS ---
        if event.type == game.MOUSEMOTION:
            pos = game.mouse.get_pos()

            if mouse_under_settings_btn() or mouse_under_gochi(): 
                game.mouse.set_cursor( game.cursors.Cursor(game.SYSTEM_CURSOR_HAND) )
            else:
                 game.mouse.set_cursor( game.cursors.Cursor(game.SYSTEM_CURSOR_ARROW) )
        if event.type == game.MOUSEBUTTONDOWN:
            pos = game.mouse.get_pos()
            # SETTINGS BUTTON and GO BACK BUTTON
            if mouse_under_settings_btn(): 
                if scene_pointer == 0:
                    scene_pointer = 1
                elif scene_pointer == 1:
                    scene_pointer = 0
            elif mouse_under_gochi:
                print(dialogs[random.randint(0, len(dialogs) - 1)])
                dialogtext = dialogs[random.randint(0, len(dialogs) - 1)]

    game.display.flip()