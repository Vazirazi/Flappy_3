import pygame, sys
from pygame.locals import *
screen_size = (500,600)      # ustalamy rozmiar ekranu









class menu(object):

    def __init__(self):
        pygame.init()  
        flag = DOUBLEBUF    # wlaczamy tryb podwojnego buforowania
        
        # tworzymy bufor na  grafike
        self.surface = pygame.display.set_mode(screen_size,flag)
        #self.myfont = pygame.font.SysFont("monospace", 16)
        self.gamestate=1
        
        self.basicFont = pygame.font.SysFont(None, 30)
        
        
        self.czas3=pygame.time.get_ticks()
        self.color1=(255,255,255)
        self.color0=(0,255,255)
        self.trudnosc = open('trudnosc.txt','r')
        self.ustawienia_trudnosci= self.trudnosc.readline().strip('\n\r') 
        
        self.trudnosc.close()
        self.pozycja=int(self.ustawienia_trudnosci)
        
        
        self.loop()
    def loop(self):
        
        
        
        while self.gamestate==1:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.gamestate = 0
              
            
            keys = pygame.key.get_pressed() # odczytujemy stan klawiszy
            if (pygame.time.get_ticks()-self.czas3>150):
                if keys[pygame.K_UP]:
                    self.pozycja -= 1
                if keys[pygame.K_DOWN]:
                    self.pozycja += 1
                self.czas3=pygame.time.get_ticks()
                if keys[pygame.K_RETURN]:
                    if self.pozycja == 4:
                        exec(open('menu.py').read())
                    else:
                        self.trudnosc = open('trudnosc.txt','w')
                        self.trudnosc.write(str(self.pozycja)) 
                        self.trudnosc.close()

            if self.pozycja == 1:
                easy = self.basicFont.render("easy", 1, self.color0)
                
            else:
                easy = self.basicFont.render("easy", 1, self.color1)
            if self.pozycja == 2:
                medium=self.basicFont.render("medium", 1, self.color0)
            else:
                medium=self.basicFont.render("medium", 1, self.color1)
            if self.pozycja== 3:
                hard=self.basicFont.render("hard", 1, self.color0)
            else:
                hard=self.basicFont.render("hard", 1, self.color1)
            if self.pozycja== 4:
                cofnij=self.basicFont.render("cofnij", 1, self.color0)
            else:
                cofnij=self.basicFont.render("cofnij", 1, self.color1)
                
             





            self.surface.blit(easy,(250,100))
            self.surface.blit(medium,(250,150))
            self.surface.blit(hard, (250,200))
            self.surface.blit(cofnij,(250,250))
            
            pygame.display.flip() 
            
            if self.gamestate ==0:
                pygame.display.quit()
                sys.exit(0) 
                pygame.quit()
                self.game_exit()

        self.game_exit()    
if __name__ == '__main__':
   menu()
    
    

