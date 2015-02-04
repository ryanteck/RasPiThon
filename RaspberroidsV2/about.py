#Alpha Code

import pygame

pygame.init()

def showAbout(screen):

    running = True

    screensize = screen.get_size()
    
    background = pygame.Surface(screensize)
    background = background.convert()
    backgroundimg = pygame.image.load("about.png").convert()
    background.blit(backgroundimg,(0,0))
    screen.blit(background,(0,0)) # comment
    
    pygame.display.flip()
    
    while running:
      
        for event in pygame.event.get():
            if event.type == pygame.constants.KEYDOWN:
                if event.key == pygame.constants.K_BACKSPACE:
                    running = False
            
        pygame.time.wait(8)
       
            
            
    
        