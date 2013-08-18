import pygame, random

class Star():
    
    def __init__(self, starSize, screenSize):
        
        #Set star size
        self.starSize = starSize
        
        #Create color for star
        val = random.randint(165, 255)
        self.starColor = pygame.Color(val, val, val)
        
        #Create start position for star
        self.pos = (random.randint(0, screenSize[0]), random.randint(0, screenSize[1]))
        
    def draw(self, screen):
        rect = pygame.Rect(self.pos[0], self.pos[1], self.starSize, self.starSize)
        pygame.draw.rect(screen, self.starColor, rect)
        
        