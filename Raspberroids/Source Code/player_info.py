import pygame, math, random, time, moveable_dude

class Player(pygame.sprite.Sprite):
    def __init__(self,screen):
        global rect;
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ship.png").convert_alpha()
        self.imagecp = self.image.copy()
        self.rect = self.image.get_rect(center=(320,240))
        self.startx = 320
        self.starty = 240
        self.angle = 0
        self.image = pygame.transform.rotate(self.imagecp, self.angle)
        self.hp = 100
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
    def __init__(self,screen,playerrect):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("alien.png").convert_alpha()
        self.imagecp = self.image.copy()
        self.x = ['20', random.randint(20,620), '620', random.randint(20,620)]
        self.y = [random.randint(15,465), '15', random.randint(15,465), '465']
        self.alieny = int(random.choice(self.x))
        self.alienx = int(random.choice(self.y))
        self.rect = self.image.get_rect(center=(320,240))
        self.angle = 0
        self.image = pygame.transform.rotate(self.imagecp, self.angle)
        self.tickclock = 0
        self.count = 0
    def timer(self):
        self.alienspeed = 30
        self.tickclock += 1
        if self.tickclock == 100:
           moveable_dude.addDudes(1)
           self.tickclock = 0