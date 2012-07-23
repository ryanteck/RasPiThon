import pygame
screen = pygame.display.set_mode((640,480), 0)
screensize = screen.get_size()
image = pygame.image.load("ship.png").convert_alpha()
rect = image.get_rect()
print(rect)