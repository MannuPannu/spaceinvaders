import pygame

from CollidableEntity import CollidableEntity

#Representing a laser beam/etc from the player
class Projectile(CollidableEntity):
    
    #Physics
    maxSpeed = 10
    acceleration = 10
    breakSpeed = 0
    
    #Set the speed and direction of the projectile
    def __init__(self, ammoType, pos, direction):
        self.maxSpeed = ammoType.projectileSpeed
        self.acceleration = ammoType.projectileSpeed
        
        if(direction == "UP"):
            self.moveY = -self.maxSpeed
            self.moveX = 0
            
        super(Projectile,self).__init__(ammoType.image, ammoType.imageSize, pos)
                     
    def tick(self):
        self.move()    
    
    def draw(self, screen):
        screen.blit(self.image, self.pos)
        
  
    
        
        
    