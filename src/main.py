import pygame, os, init, render, event, update

from entities.Player import Player

class Main():
    
    screenSize = (640, 480)

    shipImage = pygame.image.load("C:\Users\Magnus\git\spaceinvaders\gfx\ship.png")
    
    def __init__(self):

        self.gameOver = False
        
        self.screen = init.init(self.screenSize)
        
          #Create main player
        self.player = Player(self.shipImage, 162, (300, 420))
        
        self.startGameLoop()

    def startGameLoop(self):
    #Main game loop
        while True:
            event.doEvent(self)

            if self.gameOver == True:
                break

            update.doUpdate(self) 
    
            render.doRender(self)

            pygame.time.delay(75)

    pygame.quit()
    

game = Main()

