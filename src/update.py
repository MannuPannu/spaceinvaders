def doUpdate(main):
    main.player.tick()
    
    #Draw projectiles
    for index, projectile in enumerate(main.projectilesList):
        projectile.move()
        
        #Delete projectiles that has vanished off the screen (posY < 0)
        if(projectile.pos[1] < -100):
            del main.projectilesList[index]
            
            

