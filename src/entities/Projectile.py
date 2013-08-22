import pygame

from CollidableEntity import CollidableEntity

#Representing a laser beam/etc from the player
class Projectile(CollidableEntity):
    
    #Physics
    maxSpeed = 10
    acceleration = 10
    breakSpeed = 0
    
    hasCollided = False
    
    #Set the speed and direction of the projectile
    def __init__(self, mainObj, ammoType, pos, direction):
        self.mainObj = mainObj
        self.maxSpeed = ammoType.projectileSpeed
        self.acceleration = ammoType.projectileSpeed
        
        if(direction == "UP"):
            self.moveY = -self.maxSpeed
            self.moveX = 0
            
        super(Projectile,self).__init__(ammoType.image, ammoType.imageSize, pos)
                     
    def tick(self):
        
        #Check for collisions on different entities
        (doCollide, entityIndex) = self.checkCollision(self.mainObj.asteroidController.asteroidsList)
         
        if(doCollide):
            self.mainObj.asteroidController.asteroidsList.pop(entityIndex)  
            self.hasCollided = True
            self.mainObj.laserShotSound.play()  
            
        self.move()    
    
    def draw(self, screen):
        screen.blit(self.image, self.pos)
        
  
    
        
        
    