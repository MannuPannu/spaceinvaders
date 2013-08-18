import pygame, os, init, render, event, update

from entities.Player import Player
from entities.AmmoType import AmmoType
from level.BackgroundScroller import BackgroundScroller

class Main():
    
    screenSize = (640, 480)

    shipImage = pygame.image.load("C:\Users\Magnus\git\spaceinvaders\gfx\ship.png")
    ammoLaser = pygame.image.load("C:\Users\Magnus\git\spaceinvaders\gfx\laser.png")
    
    #init sounds
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    
    laserShotSound = pygame.mixer.Sound("C:\Users\Magnus\git\spaceinvaders\sounds\lasershot.wav")
    #The players ammo type, only 1 for now
    
    ammoType = AmmoType(0, -25, ammoLaser, 350)
    
    def __init__(self):

        self.gameOver = False
        
        self.screen = init.init(self.screenSize)
        
        #Projectiles
        self.projectilesList = []
        
        #Create main player
        self.player = Player(self, self.shipImage, 64, (300, 420), self.ammoType, self.screenSize)
        
        self.backgroundScroller = BackgroundScroller(self.screenSize) 
        self.startGameLoop()

    def startGameLoop(self):
    #Main game loop
        while True:
            event.doEvent(self)

            if self.gameOver == True: 
                break

            update.doUpdate(self) 
    
            render.doRender(self)

            pygame.time.delay(40)

    pygame.quit()
    

game = Main()

