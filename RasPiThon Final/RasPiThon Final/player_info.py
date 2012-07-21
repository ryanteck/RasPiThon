import pygame, math

class Player(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ship.png").convert_alpha()
        self.rect = self.image.get_rect()
       
        