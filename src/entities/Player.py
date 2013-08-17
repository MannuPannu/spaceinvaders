import Entity

from Projectile import Projectile

class Player(Entity.Entity):
    """ The player class """

    #Player speed
    maxSpeed = 15
    acceleration = 5
    breakSpeed = 2 
    
    #List of projectiles that player has fired
    projectilesList = []

    def __init__(self, mainObj, image, size, pos, ammoType):
        self.pos = pos
        self.ammoType = ammoType
        self.mainObj = mainObj

        super(Player, self).__init__(image, size)

    def tick(self):
        self.move()   
        
    def shoot(self):
        #Shoot and wait for gun cooldown before can shoot again!
        projectile = Projectile(self.ammoType, self.pos)
        self.mainObj.projectilesList.append(projectile)
        
        
