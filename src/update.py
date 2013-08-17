def doUpdate(main):
    main.player.tick()
    
    #Draw projectiles
    for projectile in main.projectilesList:
        projectile.move()

