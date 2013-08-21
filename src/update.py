def doUpdate(main):
    main.player.tick()
    
    #Draw projectiles
    for index, projectile in enumerate(main.projectilesList):
        projectile.move()
        
        #Delete projectiles that has vanished off the screen (posY < 0)
        if(projectile.pos[1] < -100):
            del main.projectilesList[index]
            
    #Draw asteroids
    for index, asteroid in enumerate(main.asteroidsList):
        asteroid.move()
        
        #Delete asteroids that has vanished off the screen 
        if(asteroid.pos[0] > main.screenSize[0] or #Vanished to the right
                              asteroid.pos[0] < (0 - asteroid.size) or # vanished to the left
                              asteroid.pos[1] > (main.screenSize[1])): #Vanished at the bottom of screen
            del main.asteroidsList[index]
            
    
    #Scroll background
    main.backgroundScroller.scroll()
            

