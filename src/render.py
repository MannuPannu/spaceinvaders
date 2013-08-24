import pygame

def doRender(main):

    black = 0, 0, 0

    main.screen.fill(black)
    
    main.backgroundScroller.draw(main.screen)
    
    #DrawScore
    main.screen.blit(main.scoreSurface, main.fontScorePos)
    
    #Draw projectiles
    for projectile in main.projectilesList:
        projectile.draw(main.screen)
    
    #Draw asteroids
    main.asteroidController.draw(main.screen)
    
    #Draw player
    main.player.draw(main.screen)
    
    #Draw animation
    main.animationController.drawAnimations(main.screen)
    
    pygame.display.flip()
