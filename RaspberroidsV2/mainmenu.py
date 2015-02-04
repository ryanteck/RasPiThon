import pygame, random, time, player_info, moveable_dude, gun
from pygame.locals import *

if not pygame.display.get_init():
    pygame.display.init()

if not pygame.font.get_init():
    pygame.font.init()
def showMenu():
    
    class Menu:
        list = []
        by = []
        fontsize = 42
        font_path = 'data/coders_crux/coders_crux.ttf'
        font = pygame.font.Font
        dest_surface = pygame.Surface
        ilosc_pol = 0
        color_tla = (102,102,102)
        textcolor =  (255, 255, 153)
        color_selection = (153,50,55)
        position_selection = 0
        position_paste = (0,0)
        menu_width = 0
        menu_height = 0
        class Pole:
            text = ''
            pole = pygame.Surface
            pole_rect = pygame.Rect
            selection_rect = pygame.Rect
        def move_menu(self, top, left):
            self.position_paste = (top,left) 
    
        def set_colors(self, text, selection, background):
            self.color_tla = background
            self.textcolor =  text
            self.color_selection = selection
            
        def set_fontsize(self,font_size):
            self.fontsize = font_size
            
        def set_font(self, path):
            self.font_path = path
            
        def get_position(self):
            return self.position_selection
        
        def init(self, list, dest_surface):
            self.list = list
            self.dest_surface = dest_surface
            self.ilosc_pol = len(self.list)
            self.create_strukture()        
            
        def draw(self,przesun=0):
            if przesun:
                self.position_selection += przesun 
                if self.position_selection == -1:
                    self.position_selection = self.ilosc_pol - 1
                self.position_selection %= self.ilosc_pol
            menu = pygame.Surface((self.menu_width, self.menu_height))
            menu.fill(self.color_tla)
            selection_rect = self.by[self.position_selection].selection_rect
            pygame.draw.rect(menu,self.color_selection,selection_rect)
    
            for i in xrange(self.ilosc_pol):
                menu.blit(self.by[i].pole,self.by[i].pole_rect)
            self.dest_surface.blit(menu,self.position_paste)
            return self.position_selection
    
        def create_strukture(self):
            shift = 0
            self.menu_height = 0
            self.font = pygame.font.Font(self.font_path, self.fontsize)
            for i in xrange(self.ilosc_pol):
                self.by.append(self.Pole())
                self.by[i].text = self.list[i]
                self.by[i].pole = self.font.render(self.by[i].text, 1, self.textcolor)
    
                self.by[i].pole_rect = self.by[i].pole.get_rect()
                shift = int(self.fontsize * 0.2)
    
                height = self.by[i].pole_rect.height
                self.by[i].pole_rect.left = shift
                self.by[i].pole_rect.top = shift+(shift*2+height)*i
    
                width = self.by[i].pole_rect.width+shift*2
                height = self.by[i].pole_rect.height+shift*2            
                left = self.by[i].pole_rect.left-shift
                top = self.by[i].pole_rect.top-shift
    
                self.by[i].selection_rect = (left,top ,width, height)
                if width > self.menu_width:
                        self.menu_width = width
                self.menu_height += height
            x = self.dest_surface.get_rect().centerx - self.menu_width / 2
            y = self.dest_surface.get_rect().centery - self.menu_height / 2
            mx, my = self.position_paste
            self.position_paste = (x+mx, y+my) 
    
    if __name__ == "__main__":
        import sys
        import main
        import about
        surface = pygame.display.set_mode((640,480))
        
        menu = Menu()
        menu.init(['Start','About','Quit'], surface)
        
        pygame.display.set_caption("Raspberroids")
        lifeimg = pygame.image.load("life.png").convert_alpha()
        pygame.display.set_icon(lifeimg)
        pygame.key.set_repeat(199,69)
        while 1:
            surface.fill((51,51,51))
            backgroundimg = pygame.image.load("menubg.png")
            surface.blit(backgroundimg,(0,0))
            menu.draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        menu.draw(-1)
                    if event.key == K_DOWN:
                        menu.draw(1)
                    if event.key == K_RETURN:
                        if menu.get_position() == 0:
                            main.startGame(surface)
                        elif menu.get_position() ==1:
                            about.showAbout(surface)
                            
                        elif menu.get_position() == 2:
                            pygame.display.quit()
                            sys.exit()
                    if event.key == K_ESCAPE:
                        pygame.display.quit()
                        sys.exit()
                    pygame.display.update()
                elif event.type == QUIT:
                    pygame.display.quit()
                    sys.exit()
            pygame.time.wait(8)


showMenu()
        