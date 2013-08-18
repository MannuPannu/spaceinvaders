import pygame, random

from Star import Star

#Generates a moving star background
class Background():
    
    starList = []
    
    #Generates initial stars
    def generateInitialStars(self):
        
        for i in range(self.starAmount):
            self.star = Star(random.randint(self.starSizeMin, self.starSizeMax), self.screenSize, self.offset)
            self.starList.append(self.star) 
    
    def draw(self, screen):
        for star in self.starList:
            star.draw(screen)
            
    def scroll(self):
        for star in self.starList:
            star.moveStar(self.scrollingSpeed)
            
        self.pos = (self.pos[0], self.pos[1] + self.scrollingSpeed)
    
    def __init__(self, starAmount, starSizeMin, starSizeMax, screenSize, scrollingSpeed, offset, pos):
        self.starAmount = starAmount
        self.starSizeMin = starSizeMin
        self.starSizeMax = starSizeMax
        self.screenSize = screenSize
        self.scrollingSpeed = scrollingSpeed
        self.offset = offset
        self.pos = pos
        self.starList = []
        
        self.generateInitialStars()
    
        
