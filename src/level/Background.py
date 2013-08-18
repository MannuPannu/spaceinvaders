import pygame

from Star import Star

#Generates a moving star background
class Background():
    
    starList = []
    
    #Generates initial stars
    def generateInitialStars(self):
        
        for i in range(self.starAmount):
            self.star = Star(self.starSize, self.screenSize)
            self.starList.append(self.star) 
    
    def draw(self, screen):
        for star in self.starList:
            star.draw(screen)
    
    def __init__(self, starAmount, starSize, screenSize):
        self.starAmount = starAmount
        self.starSize = starSize
        self.screenSize = screenSize
        
        self.generateInitialStars()
    
        
