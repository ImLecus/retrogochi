import pygame as game
from pygame.locals import *

SPACE = 640

game.init()

screen = game.display.set_mode((SPACE, SPACE))
screen.fill((56,216,142))
caption = "Retrogochi"
game.display.set_caption(caption)

# Tamagochi
game.draw.rect(screen, (0,0,0), (SPACE / 2 - 100, SPACE / 2 - 100, 200 ,200), 1)

# Poop
game.draw.rect(screen, (0,0,0), (SPACE / 2 + 150, SPACE / 2, 100 ,100), 1)

# Settings
settingsImg = game.image.load("settings.png")
settingsRect = settingsImg.get_rect()
settingsRect.center = (48,48)
screen.blit(settingsImg, settingsRect)
game.draw.rect(screen, (0,0,0) , settingsRect, 1)

# Shop
game.draw.rect(screen, (0,0,0), (SPACE - 80,16, 64, 64), 1)

# Tamagochi name
game.draw.rect(screen, (0,0,0), (SPACE / 2 - 120, 16, 240, 64), 1)

game.display.update()
while True:
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()