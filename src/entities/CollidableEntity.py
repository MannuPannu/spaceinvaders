import pygame, Entity

from pygame import Rect

class CollidableEntity(Entity.Entity):
    
    def __init__(self, image, size, pos):
         super(CollidableEntity, self).__init__(image, size, pos)
        
    #Calculates if this entity collides with other entities
    def checkCollision(self, entityList):
        
        doCollide = False
        entityIndex = 0
        
        for index, entity in enumerate(entityList):
            entityIndex = index
            #Create Rect of self
            selfRect = Rect((self.pos[0], self.pos[1]), (self.size[0], self.size[1]))
            
            #Create Rect of other entity
            otherEntityRect = Rect((entity.pos[0], entity.pos[1]), (entity.size[0], entity.size[1]))
            
            if(selfRect.colliderect(otherEntityRect)):
                print (doCollide)
                doCollide = True
                break
        
        return (doCollide, (entityIndex))
        