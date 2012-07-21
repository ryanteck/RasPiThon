import pygame, math, random

class Player(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ship.png").convert_alpha()
        self.imagecp = self.image.copy()
        self.rect = self.image.get_rect(center=(320,240))
        self.startx = 320
        self.starty = 240
        self.angle = 180
        self.image = pygame.transform.rotate(self.imagecp, self.angle)
        
    def turnRight(self):
        self.angle -= 5
        self.image = pygame.transform.rotate(self.imagecp, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        print(self.angle)

    def turnLeft(self):
        self.angle += 5
        self.image = pygame.transform.rotate(self.imagecp, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        print(self.angle)
        

class Alien(pygame.sprite.Sprite):
    def __init__(self,screen,clock):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("alien.png").convert_alpha()
        self.imagecp = self.image.copy()
        self.x = ['620','20', '620', '20']
        self.y = ['15', '465', '15', '465']
        self.alieny = int(random.choice(self.x))
        self.alienx = int(random.choice(self.y))
        self.rect = self.image.get_rect(center=(self.alieny, self.alienx))
        self.angle = 0
        self.image = pygame.transform.rotate(self.imagecp, self.angle)
        self.tickclock = 0
        self.count = 0
        
    def add(self):
        self.alienspeed = 50
        print(self.tickclock)
        self.tickclock += 1
        if self.tickclock == 30:
            self.count += 1
            self.alieny = int(random.choice(self.x))
            self.alienx = int(random.choice(self.y))
            self.rect = self.image.get_rect(center=(self.alieny, self.alienx))
            self.tickclock = 0