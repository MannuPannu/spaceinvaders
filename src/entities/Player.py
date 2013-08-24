import CollidableEntity, pygame

from Projectile import Projectile

class Player(CollidableEntity.CollidableEntity):
    """ The player class """

    #Player physics
    maxSpeed = 7
    acceleration = 5
    breakSpeed = 0.4
    
    coolDownTimer = 0
    
    def __init__(self, mainObj, image, size, pos, ammoType, screenSize):
        self.ammoType = ammoType
        self.mainObj = mainObj
        self.screenSize = screenSize
        
        super(Player, self).__init__(image, size, pos)

    def tick(self):
    
        moveTargetPos = self.getMovePos() #Target position after next move
        
        #Set screen limit for player move horizontally
        movePosX = moveTargetPos[0]
        
        if(movePosX < 0 or (movePosX + self.size[0]) > self.screenSize[0]):
            self.moveX = 0
            
        #Set screen limit for player moving vertically
        movePosY = moveTargetPos[1]
            
        if(movePosY < 0 or (movePosY + self.size[1]) > self.screenSize[1]):
            self.moveY = 0
            
        #Check for collisions on different entities
        (doCollide, entityIndex) = self.checkCollision(self.mainObj.asteroidController.asteroidsList) 
        
        if(not doCollide): 
            self.move()
        else:
            clock = pygame.time.Clock()
            
            self.mainObj.playerDies.play()
            while pygame.mixer.get_busy():
                clock.tick(30)

            print("Game over")
            self.mainObj.gameOver = True
            
    def shoot(self):
        #Shoot and wait for gun cool down before we can shoot again!
        if((self.coolDownTimer + self.ammoType.coolDown) < pygame.time.get_ticks()):
            self.mainObj.laserShotSound.play()
                     
            projectile = Projectile(self.mainObj, self.ammoType, (self.pos[0] + float(self.size[0])/2, self.pos[1]), "UP")
            self.mainObj.projectilesList.append(projectile) #Put in a global list, for render/updating purposes
            
            self.coolDownTimer = pygame.time.get_ticks() #Reset timer
            
        
            
            
            