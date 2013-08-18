import Entity, pygame

from Projectile import Projectile

class Player(Entity.Entity):
    """ The player class """

    #Player speed
    maxSpeed = 15
    acceleration = 5
    breakSpeed = 2
    
    coolDownTimer = 0
    
    def __init__(self, mainObj, image, size, pos, ammoType):
        self.pos = pos
        self.ammoType = ammoType
        self.mainObj = mainObj
        
        super(Player, self).__init__(image, size)

    def tick(self):
        self.move()   
        
    def shoot(self):
        #Shoot and wait for gun cool down before we can shoot again!
        #print("Time since last shot:" + str(self.coolDown.tick()))
        #print("CoolDown:" + str(self.ammoType.coolDown))     
        
        if((self.coolDownTimer + self.ammoType.coolDown) < pygame.time.get_ticks()):         
            projectile = Projectile(self.ammoType, self.pos)
            self.mainObj.projectilesList.append(projectile) #Put in a global list, for render/updating purposes
            
            self.coolDownTimer = pygame.time.get_ticks() #Reset timer
            
            
            