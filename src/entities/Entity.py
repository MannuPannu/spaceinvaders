class Entity(object):
    """ A movable object """
    
    moveX = 0
    moveY = 0
    pos = (0, 0)
    
    def __init__(self, image, size, pos):
        self.image = image
        self.size = size
        self.pos = pos

    def draw(self, screen):
        screen.blit(self.image, self.pos)
        
    def moveLeft(self):
        self.moveX -= self.acceleration 

    def moveRight(self):
        self.moveX += self.acceleration
        
    def moveUp(self):
        self.moveY -= self.acceleration
        
    def moveDown(self):
        self.moveY += self.acceleration
    
    # Breaks the speed of entity    
    def breakMove(self, breakSpeed):
        if self.moveX > 0:
            self.moveX = self.moveX - breakSpeed
            if self.moveX < 0: 
                self.moveX = 0 
        elif self.moveX < 0:
            self.moveX = self.moveX + breakSpeed
            if self.moveX > 0:
                self.moveX = 0

        if self.moveY > 0:
            self.moveY = self.moveY - breakSpeed
            if self.moveY < 0:
                self.moveY = 0
        elif self.moveY < 0:
            self.moveY = self.moveY + breakSpeed
            if self.moveY > 0:
                self.moveY = 0
        
    #Moves the entity
    def move(self):
        x, y = self.pos

        #Cap speed if movement speed is above max
        if self.moveX > self.maxSpeed:
            self.moveX = self.maxSpeed
        if self.moveX < -self.maxSpeed:
            self.moveX = -self.maxSpeed
        if self.moveY > self.maxSpeed:
            self.moveY = self.maxSpeed
        if self.moveY < -self.maxSpeed:
            self.moveY = -self.maxSpeed

        #move entity
        (x, y) = self.pos
        
        self.pos = (x + self.moveX, y + self.moveY)
        self.breakMove(self.breakSpeed)
        
    #Get the position an entity will end up in after a move
    def getMovePos(self):
        x, y = self.pos

        #Cap speed if movement speed is above max
        if self.moveX > self.maxSpeed:
            self.moveX = self.maxSpeed
        if self.moveX < -self.maxSpeed:
            self.moveX = -self.maxSpeed
        if self.moveY > self.maxSpeed:
            self.moveY = self.maxSpeed
        if self.moveY < -self.maxSpeed:
            self.moveY = -self.maxSpeed

        return (x + self.moveX, y + self.moveY)

        
