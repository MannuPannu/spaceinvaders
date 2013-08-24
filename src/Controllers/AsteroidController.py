import pygame, random

from entities.Asteroid import Asteroid

#Class for generating asteroids
class AsteroidController():
    
    asteroidsList = []
    
    asteroidCoolDownTimer = 0
    asteroidCoolDown = 1500
    
    def createAsteroid(self):
        
        #Create a random direction but that is pointing downwards
        speedX = float(random.randint(-5, 5)) /10
        speedY = 1.6
        
        #Create random start pos
        pos = (random.randint(0, self.mainObj.screenSize[0]-self.asteroidSize[0]), -self.asteroidSize[1])
        
        newAsteroid = Asteroid(self.asteroidImage, self.asteroidSize, pos, speedX, speedY)
        
        self.asteroidsList.append(newAsteroid)
    
    def __init__(self, mainObj, asteroidSize, asteroidImage):
        self.mainObj = mainObj
        self.asteroidSize = asteroidSize
        self.asteroidImage = asteroidImage
        
        #Create initial asteroid
        self.createAsteroid()
    
    #Handles the asteroids
    def tick(self):
        
        #moves the asteroids
        for index, asteroid in enumerate(self.asteroidsList):
            asteroid.move()
            
            #Delete asteroids that has vanished off the screen 
            if(asteroid.pos[0] > self.mainObj.screenSize[0] or #Vanished to the right
                                  asteroid.pos[0] < (0 - asteroid.size[0]) or # vanished to the left
                                  asteroid.pos[1] > (self.mainObj.screenSize[1])): #Vanished at the bottom of screen
                del self.asteroidsList[index]
                
        
        #Create asteroid
        if((self.asteroidCoolDownTimer + self.asteroidCoolDown) < pygame.time.get_ticks()):
            self.createAsteroid()
            self.asteroidCoolDownTimer = pygame.time.get_ticks() #Reset timer
                
    def draw(self, screen):
        for asteroid in self.asteroidsList:
            asteroid.draw(screen)
    
                
        
                
           
        
    