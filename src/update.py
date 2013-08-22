def doUpdate(main):
    
    main.player.tick()
    
    #update projectiles
    for index, projectile in enumerate(main.projectilesList):
        projectile.tick()
        
        #Delete projectiles that has vanished off the screen (posY < 0) or collided with something
        if(projectile.pos[1] < -100 or projectile.hasCollided):
            del main.projectilesList[index]
            
    main.asteroidController.tick()
    
    #Scroll background
    main.backgroundScroller.scroll()
            

