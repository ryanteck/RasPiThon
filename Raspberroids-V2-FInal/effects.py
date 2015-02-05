import pygame

effects = []

def update():
    toremove = []
    for i in range(len(effects)):
        effects[i].update()
        if effects[i].shouldRemove:
            toremove.append(i)
    for i in range(len(toremove)):
        effects.pop(toremove[i-1])

def draw(surface):
    for i in range(len(effects)):
        effects[i].draw(surface)

class Explosion():
    
    animdelay = 5
    shouldRemove = False
    
    def __init__(self, x, y):
        self.imgpaths = ["expl/expl1.gif", "expl/expl2.gif", "expl/expl3.gif", "expl/expl4.gif", "expl/expl5.gif", "expl/expl6.gif"]
        self.imgs = []
        for i in range(len(self.imgpaths)):
            self.imgs.append(pygame.image.load(self.imgpaths[i]).convert_alpha())
        
        self.animframe = 0
        self.animtime = 0
        self.image = self.imgs[0]
        self.position = pygame.Rect(x, y, 0, 0)
        self.rect = self.image.get_rect()
        effects.append(self)
        
    def update(self):
        self.animtime += 1
        if self.animtime%self.animdelay==0:
            self.animframe += 1
            
        if self.animframe==len(self.imgs):
            self.shouldRemove = True
        else:
            self.image = self.imgs[self.animframe]
            
    def draw(self, surface):
        surface.blit(self.image, self.position)
