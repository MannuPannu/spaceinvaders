import pygame

#Inits the game
def init(screenSize):
    pygame.init()

    screen=pygame.display.set_mode(screenSize)

    pygame.display.set_caption("Space invaders!")

    return screen
