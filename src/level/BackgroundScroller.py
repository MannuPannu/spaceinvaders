from Background import Background

#Responsible for scrolling the backgrounds

class BackgroundScroller():
    
    backgroundList = []
    starAmount = 40
    starSizeMax = 3
    starSizeMin = 1
    starSpeed = 5
    
    def __init__(self, screenSize):
        
        self.screenSize = screenSize
        
        #Create two backgrounds to alternate with when scrolling them        
        self.backgroundList.append(Background(self.starAmount, self.starSizeMin, self.starSizeMax, self.screenSize, self.starSpeed, 0, (0, 0)))
        
        self.backgroundList.append(Background(self.starAmount, self.starSizeMin, self.starSizeMax, self.screenSize, self.starSpeed, -self.screenSize[1], (0, -self.screenSize[1])))
        
    def scroll(self):
        self.backgroundList[0].scroll()
        self.backgroundList[1].scroll()
        
        if(self.backgroundList[0].pos[1] > self.screenSize[1]):
            self.backgroundList[0] = Background(self.starAmount, self.starSizeMin, self.starSizeMax, self.screenSize, self.starSpeed, -self.screenSize[1], (0, -self.screenSize[1]))
            
        if(self.backgroundList[1].pos[1] > self.screenSize[1]):
            self.backgroundList[1] = Background(self.starAmount, self.starSizeMin, self.starSizeMax, self.screenSize, self.starSpeed, -self.screenSize[1], (0, -self.screenSize[1]))
        
    def draw(self, screen):
        self.backgroundList[0].draw(screen)
        self.backgroundList[1].draw(screen)
        
        
        