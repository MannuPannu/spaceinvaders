import CollidableEntity, pygame

class Asteroid(CollidableEntity.CollidableEntity):
    
    #Physics
    maxSpeed = 10
    acceleration = 10
    breakSpeed = 0
    
    def __init__(self, image, size, pos, speedX, speedY):   
        
        self.maxSpeed = speedY
        self.acceleration = speedY
        
        self.moveX = speedX
        self.moveY = speedY
            
        super(Asteroid, self).__init__(image, size, pos)
