import CollidableEntity, pygame

from Projectile import Projectile

class Player(CollidableEntity.CollidableEntity):
    """ The player class """

    #Player physics
    maxSpeed = 6
    acceleration = 5
    breakSpeed = 0.2
    
    coolDownTimer = 0
    
    def __init__(self, mainObj, image, size, pos, ammoType, screenSize):
        self.ammoType = ammoType
        self.mainObj = mainObj
        self.screenSize = screenSize
        
        super(Player, self).__init__(image, size, pos)

    def tick(self):
    
        #Set screen limit for player move horizontally
        movePosX = self.getMovePos()[0]
        
        if(movePosX < (self.screenSize[0] - self.size) and movePosX > 0 ):
            self.move()
        else: 
            #Stop player move and align it with the screen border
            if (self.moveX > 0): #Player went to the right
                self.pos = (self.screenSize[0] - self.size - 1, self.pos[1])
            elif (self.moveX < 0):
                self.pos = (0, self.pos[1])
            
            self.moveX = 0
            self.move() #Move in y-axis
            
        #Set screen limit for player moving vertically
        movePosY = self.getMovePos()[1]
        
        if(movePosY > 0 and (movePosY + self.size) < self.screenSize[1]):
            self.move()
        else:
        #Stop player move and align it with the screen border
            if (self.moveY > 0): #Player is going down
                self.pos = (self.pos[0], self.screenSize[1] - self.size )
            elif (self.moveY < 0):
                self.pos = (self.pos[0], 0)
            
            self.moveY = 0
            self.move() #Move in x-axis
            
            
    def shoot(self):
        #Shoot and wait for gun cool down before we can shoot again!
        if((self.coolDownTimer + self.ammoType.coolDown) < pygame.time.get_ticks()):
            self.mainObj.laserShotSound.play()
                     
            projectile = Projectile(self.ammoType, (self.pos[0], self.pos[1]), "UP")
            self.mainObj.projectilesList.append(projectile) #Put in a global list, for render/updating purposes
            
            self.coolDownTimer = pygame.time.get_ticks() #Reset timer
            
        
            
            
            