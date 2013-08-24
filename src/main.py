import pygame, os, init, render, event, update

from entities.Player import Player
from entities.AmmoType import AmmoType
from entities.Asteroid import Asteroid
from level.BackgroundScroller import BackgroundScroller
from Controllers.AsteroidController import AsteroidController

# TODO: Add start up text, like "Try to clear the asteroid field!"
# TODO: Add a counter for number of asteroids hit
# TODO: Add death animations for asteroids as well as player
# TODO: Add game over text

#Cannot play the sound files that I want.. maybe I should try and create sound explosions my self.

class Main():
    
    screenSize = (640, 480)
    
    mypath = os.path.dirname( os.path.realpath( __file__ ) )

    shipImage = pygame.image.load(os.path.join('..\gfx', 'ship2.png'))
    ammoLaserImage = pygame.image.load(os.path.join('..\gfx', 'greenlaserbeam.png'))
    asteroidImage = pygame.image.load(os.path.join('..\gfx', 'asteroid.png'))
    
    #The players ammo type, only 1 for now
    ammoType = AmmoType(15, ammoLaserImage, (4, 32), 350)
    
    def __init__(self):

        self.gameOver = False
        
        self.screen = init.init(self.screenSize)
        
        #pygame.mixer.init(frequency=44100, size=16, channels=2, buffer=2000)
        pygame.mixer.init()
        pygame.font.init()
        print(pygame.font.get_fonts())
        
        #Init sounds
        self.laserShotSound = pygame.mixer.Sound(os.path.join('..\sounds\lasershot.wav'))
        self.asteroidExplosion = pygame.mixer.Sound(os.path.join('..\sounds\snare003.wav'))
        self.playerDies = pygame.mixer.Sound(os.path.join('..\sounds\Noise001.wav'))
        
        #Init fonts
        self.fontScoreHeight = 25
        self.fontScoreColor = (0, 210, 30)
        self.fontScorePos = (25, 450)
        self.scoreFont = pygame.font.Font(os.path.join('..\gfx\chintzy.ttf'), self.fontScoreHeight)
        
        #Projectiles
        self.projectilesList = []
        
        #Create main player
        self.player = Player(self, self.shipImage, (32,32), (300, 420), self.ammoType, self.screenSize) 
        
        self.asteroidController = AsteroidController(self, (32, 32), self.asteroidImage)
        
        self.backgroundScroller = BackgroundScroller(self.screenSize)
        
        #Score system
        self.score = 0 #Initial score
        self.scoreAsteroidHit = 80
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



