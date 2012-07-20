
#test

import pygame, random, time, player_info
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,480), 0)
screensize = screen.get_size()
center = [320,240]
centership = [288,226]
pygame.display.set_caption("Raspithon Game")

font = pygame.font.Font(None, 50)

fps = 60
clock = pygame.time.Clock()

black = [0,0,0]
white = [255,255,255]

background = pygame.Surface(screensize)
background = background.convert()
background.fill(black)

logo = "rptlogo.png"
logoload = pygame.image.load(logo)

running = True
playtime = 0.0
bgmusic = pygame.mixer.music.load("backgroundmusic.mp3")
pygame.mixer.init()
pygame.mixer.music.play(-1)


#Display the ship
player = player_info.Player(screen)
allSprites = pygame.sprite.Group(player)
#Display Life
lifeimg = "life.png"
lifeimage = pygame.image.load(lifeimg).convert_alpha()

while running:
    screen.blit(background,(0,0))
    pygame.display.flip()
    milliseconds = clock.tick(fps)
    playtime += milliseconds / 1000.0
    text = font.render("Frame rate: %.2f Playtime: %.2fs" % (clock.get_fps(),playtime), 1, white)
    background.fill(black)
    background.blit(text, (0,0))
    background.blit(lifeimage, center)
    allSprites.clear(screen,background)
    allSprites.update()
    allSprites.draw(screen)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                
    keysdown = pygame.key.get_pressed()
    if keysdown[pygame.K_RIGHT]:   
        shipangle +=1

    

    