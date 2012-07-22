#test

import pygame, random, time, player_info, moveable_dude, gun, math
from pygame.locals import *
from math import sqrt

def startGame():
    

    pygame.init()
    
    screen = pygame.display.set_mode((640,480), 0)
    screensize = screen.get_size()
    
    
    
    
    center = [320,240]
    centership = [288,226]
    pygame.display.set_caption("Raspberroids")
    lifeimg = pygame.image.load("life.png").convert_alpha()
    pygame.display.set_icon(lifeimg)
    
    font = pygame.font.Font(None, 32)
    
    fps = 100
    clock = pygame.time.Clock()
    
    black = [0,0,0]
    white = [255,255,255]
    
    background = pygame.Surface(screensize)
    background = background.convert()
    backgroundimg = pygame.image.load("bg.png")
    background.blit(backgroundimg,(0,0))
    
    logo = "rptlogo.png"
    logoload = pygame.image.load(logo)
    
    running = True
    playtime = 0.0
    bgmusic = pygame.mixer.music.load("backgroundmusic.mp3")
    pygame.mixer.init()
    pygame.mixer.music.play(-1) 
    
    
    #Display the ship
    #player = player_info.Player(screen)
    move = moveable_dude.MoveableDude()
    #allSprites = pygame.sprite.Group(player)
    
    moveable_dude.addDudes(1) #Creds to Cakez0r for helping me out with this
    
    
    gunnew = gun.Gun(screen)
    pygame.display.init()
    
    while running:
        
        screen.blit(background,(0,0)) # comment
        pygame.display.flip() # comment
        milliseconds = clock.tick(fps) # comment
        hp = 5
        playtime += milliseconds / 1000.0 # comment
        text = font.render("Frame rate: %.2f Playtime: %.2fs Lives: %.2f" % (clock.get_fps(),playtime,hp), 1, white) # comment
        background.blit(backgroundimg,(0,0))
        background.blit(text, (0,0)) # comment
        moveable_dude.updateAndDrawDudes(background)
      
        move.timer()
        
        gunnew.update(float(milliseconds) / 1000)
        gunnew.draw(background)
        
        toremove = []
        
        if len(moveable_dude.dudes) > 0:
            for y in range(len(moveable_dude.dudes)):
                if len(gunnew.bullets) > 0:
                    for i in range(len(gunnew.bullets)):
                        if gunnew.bullets[i].alive:
                            posx = gunnew.bullets[i].position.left
                            posy = gunnew.bullets[i].position.top
                            pozx = moveable_dude.dudes[y-1].position.left
                            pozy = moveable_dude.dudes[y-1].position.top
                            difx = pozx - posx
                            dify = pozy - posy
                            magn = sqrt((difx*difx) + (dify*dify))
                            if (magn < 10):
                                
                                toremove.append(moveable_dude.dudes[y])
                        #else:
                            #Blah
        
        for y in range(len(toremove)):
            print
            moveable_dude.dudes.remove(toremove[y])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    
    
        if hp == 0:
            import mainmenu
            mainmenu.showMenu()
        
        #On keypress        
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:      
            gunnew.turnRight()
        if keystate[pygame.K_LEFT]:
            gunnew.turnLeft()
        if keystate[pygame.K_z]:
            gunnew.fire()
        if keystate[pygame.K_SPACE]:
            gunnew.fire()
            
        if keystate[pygame.K_q]:
            pygame.quit()
        
            
            
    
        