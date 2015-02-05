#Raspberroids V2,
#Re Written to remove some weight from it and to make it run fast on the Pi

import pygame, random, time, moveable_dude, gun, math, pygame.mixer, effects
from moveable_dude import *

from pygame.locals import *

if not pygame.display.get_init():
    pygame.display.init()

if not pygame.font.get_init():
    pygame.font.init()
surface = pygame.display.set_mode((640,480))

from math import sqrt

from random import randint

randnum = randint(1,5) # 1 to 4, code is inclusive
#Select a Title
if randnum == 1:    # Divinite added randomised titles.
    rand = "Oh no, not the Aliens!"

if randnum == 2:    # Divinite added randomised titles.
    rand = "Spaaaccceee!"

if randnum == 3:    # Divinite added randomised titles.
    rand = "Developed by the RasPi Community!"

if randnum == 4:    # Divinite added randomised titles.
    rand = "Cheeseburgers are tasty."

if randnum == 5:
    rand = "Now with more FPS!"

#Define the game
#@profile
def startGame(screen):
    #Reset all dudes
    #moveable_dude.reset()

    screensize = screen.get_size()
    
    score = 0
    
    center = [320,240]
    centership = [288,226]
    pygame.display.set_caption("Raspberroids | A collaborative Project | " + rand) # Divinite added randomised titles.
    lifeimg = pygame.image.load("life.gif").convert_alpha()
    pygame.display.set_icon(lifeimg)
    
    font = pygame.font.Font(None, 32)
    
    fps = 600
    clock = pygame.time.Clock()
    
    black = [0,0,0]
    white = [255,255,255]
    
    background = pygame.Surface(screensize)
    background = background.convert()
    backgroundimg = pygame.image.load("bgCompress.gif")
    background.blit(backgroundimg,(0,0))
    
    logo = "rptlogo.png"
    logoload = pygame.image.load(logo)
    pygame.mixer.pre_init(44100,-16)
    pygame.mixer.init()
    running = True
    playtime = 0.0
    pygame.mixer.set_num_channels(4)
    bgmusic = pygame.mixer.music.load("backgroundmusic.mp3")
    sfx = pygame.mixer.Channel(1)
    explode = pygame.mixer.Sound("explode.ogg")
    explode.set_volume(1.0)
    shot = pygame.mixer.Sound("8bit1up.ogg")
    shot.set_volume(1.0)
    gameover = pygame.mixer.Sound("game_over.ogg")
    gameover.set_volume(1.0)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1) 
    
    #Display the ship
    #player = player_info.Player(screen)
    move = moveable_dude.MoveableDude()
    #allSprites = pygame.sprite.Group(player)
    
    #moveable_dude.addDudes(1) #Creds to Cakez0r for helping me out with this
    dead = 0
    
    gunnew = gun.Gun(screen)
    pygame.display.init()
    screen.blit(background,(0,0))
    pygame.display.update()   
    fpsLast = 0.00 
    counter = 0
    
    while running:
		if(clock.get_fps()>fpsLast):
			print clock.get_fps()
			fpsLast = clock.get_fps()
		screen.blit(background,(0,0)) # comment
		pygame.display.update()   

		milliseconds = clock.tick() # comment
		hp = gunnew.hp
		playtime =0 # comment
		text = font.render("Frame rate: %.2f Playtime: %.2fs Lives: %d" % (clock.get_fps(),playtime,hp), 1, white) # comment
		
		scoretext = font.render("Score: %d" % (score), 1, white)
		background.blit(backgroundimg,(0,0))
		background.blit(text, (10,15)) # comment
		background.blit(scoretext, (240,450))
		#pygame.display.update([10,15,450,25]) 
		moveable_dude.updateAndDrawDudes(background)
        
		effects.update()
		effects.draw(background)
        
		move.timer()
        
		gunnew.update(float(milliseconds) / 1000)
		gunnew.draw(background)
        
		toremove = []
        
		if len(moveable_dude.dudes) > 0:
			for y in range(len(moveable_dude.dudes)):
				remove = False
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
							if (magn < 15):
								pygame.init()
								shot.play()
								remove = True
								effects.Explosion(posx, posy)
								score = score + 50
                        #else:
                        
                            #Blah
				if gunnew.hp > 0:
						posx = gunnew.position.left
						posy = gunnew.position.top
						pozx = moveable_dude.dudes[y-1].position.left
						pozy = moveable_dude.dudes[y-1].position.top
						difx = pozx - posx
						dify = pozy - posy
						magn = sqrt((difx*difx) + (dify*dify))
						if (magn < 15):
							gunnew.hp -= 1
							remove = True
							effects.Explosion(pozx, pozy)
							explode.play()
				else:
					if dead != 1:
						gameover.play()
						dead = 1
						running = False
						pygame.time.wait(2000)
                
				if remove:
					toremove.append(y-1)
                
		for i in range(len(toremove)):
			moveable_dude.dudes.pop(toremove[i])
        
        
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		        
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
            
                    
        #On key press        
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
			running = False
		
		
        
        
            
            
    
        
startGame(surface)
