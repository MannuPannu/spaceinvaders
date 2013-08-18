import pygame

#Representing a laser beam/etc from the player
class Projectile():
    
    speedX = 0
    speedY = 0
    pos = (0, 0)
    
    #Set the speed and direction of the projectile
    def __init__(self, ammoType, pos):
        self.speedX = ammoType.speedX
        self.speedY = ammoType.speedY
        self.pos = pos
        self.image = ammoType.image
        
    def draw(self, screen):
        screen.blit(self.image, self.pos)
        
    def move(self):
        (x, y) = self.pos
        self.pos = (x + self.speedX, y + self.speedY)
  
  
    
        
        
    