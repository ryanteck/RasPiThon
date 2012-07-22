import pygame, math

GRAD = math.pi * 180


class Bullet(pygame.sprite.Sprite):
    position = pygame.Rect(0, 0, 0, 0)
    velocity = pygame.Rect(0, 0, 0, 0)
    
    alive = 1
    def __init__(self, px, py, vx, vy):
        self.position = pygame.Rect(px, py, 0, 0)
        self.velocity = pygame.Rect(vx, vy, 0, 0)
    
    def update(self, dt):
        self.position = self.position.move(float(self.velocity.x) * dt, float(self.velocity.y) * dt)
        self.alive = self.position.x < 810 and self.position.x > -10 and self.position.y > -10 and self.position.y < 610
        
    def draw(self, surface):
        # pygame.draw.circle(surface, pygame.Color("red"), [self.position.x, self.position.y], 3)
        self.laser = pygame.image.load("laser.png").convert_alpha()
        self.lasercp = self.laser.copy
        surface.blit(self.laser,(self.position.x,self.position.y))
       
class Gun(pygame.sprite.Sprite):
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
        self.hp = 5
        self.bullets = []
        self.position = pygame.Rect(320, 240, 0, 0)
        self.bulletSpeed = 500
        self.moveSpeed = 250.0
        self.bullettime = 0
        
    def turnRight(self):
        self.angle -= 4
        self.image = pygame.transform.rotate(self.imagecp, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        #print(self.angle)
        
    def turnLeft(self):
        self.angle += 4
        self.image = pygame.transform.rotate(self.imagecp, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        #print(self.angle)

    
    def update(self, dt):
    
        for i in range(len(self.bullets)):
            self.bullets[i].update(dt)
    
    def draw(self, surface):
        
        
        removeList = []
        
        for i in range(len(self.bullets)):
            if self.bullets[i].alive:
                self.bullets[i].draw(surface)
            else:
                removeList.append(self.bullets[i])
                
        for i in range(len(removeList)):
            self.bullets.remove(removeList[i])
                
        surface.blit(self.image, self.rect)
        
    def fire(self):
        if self.bullettime == 5:
            dx =  -math.cos(math.radians(self.angle)) * self.bulletSpeed
            dy = +math.sin(math.radians(self.angle)) * self.bulletSpeed

           
            
            if math.fabs(dx) > 0 or math.fabs(dy) > 0:
                magnitude = math.sqrt((dx*dx) + (dy*dy))
                    
                dx_norm = dx / magnitude
                dy_norm = dy / magnitude
                
                self.bullets.append(Bullet(self.position.x, self.position.y, dx_norm * self.bulletSpeed, dy_norm * self.bulletSpeed))
            self.bullettime = 0
        else:
            self.bullettime += 1