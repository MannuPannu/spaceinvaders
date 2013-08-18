#Defines an ammunition type 

class AmmoType():
    
    def __init__(self, speedX, speedY, image, coolDown):
        self.speedX = speedX
        self.speedY = speedY
        self.image = image
        self.coolDown = coolDown #A time interval between shots for this ammo type, in ms