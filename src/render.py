import pygame

def doRender(main):

    black = 0, 0, 0

    main.screen.fill(black)
    
    main.backgroundScroller.draw(main.screen)
    
    #Draw projectiles
    for projectile in main.projectilesList:
        projectile.draw(main.screen)
    
    #Draw asteroids
    for asteroid in main.asteroidsList:
        asteroid.draw(main.screen)
    
    #Draw player
    main.player.draw(main.screen)
       
    pygame.display.flip()
