import pygame, Entity

class CollidableEntity(Entity.Entity):
    
    def __init__(self, image, size, pos):
         super(CollidableEntity, self).__init__(image, size, pos)
        
        
    #Calculates if this entity collides with another entity
    def isCollision(self, entity):
        
        return false
        