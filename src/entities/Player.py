import Entity

class Player(Entity.Entity):
    """ The player class """

    #Player speed
    maxSpeed = 15
    acceleration = 5
    breakSpeed = 2 

    def __init__(self, image, size, pos):
        self.pos = pos

        super(Player, self).__init__(image, size)

    def tick(self):
        self.move()
