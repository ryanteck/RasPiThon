import pygame, math, random

global rect

dudes = []
def addDudes(count):
    for i in range(count):
        dudes.append(MoveableDude())

def updateAndDrawDudes(surface):
    for i in range(len(dudes)):
        dudes[i].update()
        
    for i in range(len(dudes)):
        dudes[i].draw(surface)

class MoveableDude(pygame.sprite.Sprite):
    x = ['620','20', '620', '20', '320']
    y = ['15', '465', '15', '465', '15']
    alieny = int(random.choice(x))
    alienx = int(random.choice(y))
    target = pygame.Rect(320, 240, 0, 0)
    position = pygame.Rect(alienx, alieny, 0, 0)
    movement_speed = 5
    tickclock = 0
    dudes = []
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("life.png").convert_alpha()
        self.imagecp = pygame.image.load("life.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.angle = 0
        moveablerec = self.rect
        
        

    def addDudes(self,count):
        if len(dudes) <20:
            for i in range(count):
                dudes.append(MoveableDude())

    def updateAndDrawDudes(self,surface):
        for i in range(len(dudes)):
            dudes[i].update()
            
        for i in range(len(dudes)):
            dudes[i].draw(surface)
            
    def update(self):
        dx = self.target.x - self.position.x
        dy = self.target.y - self.position.y
        self.image = pygame.transform.rotate(self.imagecp, self.angle)
        #print(self.angle)
        self.angle += 3
        # Home towards the target if we are more than 10 pixels away
        if (math.fabs(dx) > 10 or math.fabs(dy) > 10):
            magnitude = math.sqrt((dx*dx) + (dy*dy))
            
            dx_norm = dx / magnitude
            dy_norm = dy / magnitude
        
            self.position = self.position.move(dx_norm * self.movement_speed, dy_norm * self.movement_speed)
        else:
            self.setTarget(random.randint(0, 640), random.randint(0, 480))
        
    def setTarget(self, x, y):
        self.target = pygame.Rect(x, y, 0, 0)
    
    def draw(self, surface):
        surface.blit(self.image, self.position)
        
    def timer(self):
        
        self.alienspeed = 30
        self.tickclock += 1
        if self.tickclock == 100:
            self.addDudes(1)
            self.tickclock = 0
    