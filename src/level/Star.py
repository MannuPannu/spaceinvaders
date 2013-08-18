import pygame, random

class Star():
    
    def __init__(self, starSize, screenSize, offset):
        
        #Set star size
        self.starSize = starSize
        self.offset = offset
        
        #Create color for star
        val = random.randint(125, 255)
        self.starColor = pygame.Color(val, val, val)
        
        #Create start position for star
        self.pos = (random.randint(0, screenSize[0]), random.randint(0 + self.offset, screenSize[1] + self.offset))
        
    def draw(self, screen):
        rect = pygame.Rect(self.pos[0], self.pos[1], self.starSize, self.starSize)
        #circle(Surface, color, pos, radius, width=0)
        #pygame.draw.circle(screen, self.starColor, self.pos, self.starSize)
        pygame.draw.rect(screen, self.starColor, rect)
        
    def moveStar(self, starSpeed):
        self.pos = (self.pos[0], self.pos[1] + starSpeed)
        
        