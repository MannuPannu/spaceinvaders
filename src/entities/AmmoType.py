#Defines an ammunition type 

class AmmoType():
    
    def __init__(self, projectileSpeed, image, imageSize, coolDown):
        self.projectileSpeed = projectileSpeed
        self.image = image
        self.imageSize = imageSize
        self.coolDown = coolDown #A time interval between shots for this ammo type, in ms