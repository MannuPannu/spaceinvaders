import Entity, pygame

from Projectile import Projectile

class Player(Entity.Entity):
    """ The player class """

    #Player speed
    maxSpeed = 15
    acceleration = 5
    breakSpeed = 2
    
    coolDownTimer = 0
    
    def __init__(self, mainObj, image, size, pos, ammoType, screenSize):
        self.pos = pos
        self.ammoType = ammoType
        self.mainObj = mainObj
        self.screenSize = screenSize
        
        super(Player, self).__init__(image, size)

    def tick(self):
        movePosX = self.getMovePos()[0]
        
        print(str(movePosX))
        
        #Set screen limit for player move horizontally
        if(movePosX < (self.screenSize[0] - self.size) and movePosX > 0 ):
            self.move()
        else: 
            #Stop player move and align it with the screen border
            if (self.moveX > 0): #Player went to the right
                self.pos = (self.screenSize[0] - self.size, self.pos[1])
            elif (self.moveX < 0):
                self.pos = (0, self.pos[1])
            
            self.moveX = 0
            
    def shoot(self):
        #Shoot and wait for gun cool down before we can shoot again!
        if((self.coolDownTimer + self.ammoType.coolDown) < pygame.time.get_ticks()):
            self.mainObj.laserShotSound.play()
                     
            projectile = Projectile(self.ammoType, (self.pos[0] + (float(self.size)/3), self.pos[1]))
            self.mainObj.projectilesList.append(projectile) #Put in a global list, for render/updating purposes
            
            self.coolDownTimer = pygame.time.get_ticks() #Reset timer
            
        
            
            
            