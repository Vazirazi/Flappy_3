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
        self.tlo=pygame.image.load('resources/images/background.png')
        self.pozycja=1
        self.pozycja2=1
        self.czas3=pygame.time.get_ticks()
        self.color1=(255,255,255)
        self.color0=(0,255,255)
        self.loop()
        
    def loop(self):
        
        
        pygame.mixer.music.load('resources/sounds/nature_sketch.wav')
        pygame.mixer.music.play(-1)
        
        while self.gamestate==1:
            for event in pygame.event.get():
                if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                    self.gamestate = 0
              
            
            keys = pygame.key.get_pressed() # odczytujemy stan klawiszy
            if (pygame.time.get_ticks()-self.czas3>100):
                if keys[pygame.K_UP]:
                    self.pozycja -= 1
                if keys[pygame.K_DOWN]:
                    self.pozycja += 1
                self.czas3=pygame.time.get_ticks()
                if keys[pygame.K_RETURN]:
                    if self.pozycja == 1:
                        exec(open('resources/Flappy.py').read())
                    if self.pozycja ==2:
                        exec(open('resources/ustawienia.py').read())
                    if self.pozycja ==3:
                        exec(open('resources/rekordy.py').read())
                    if self.pozycja ==4:
                        pygame.display.quit()
                        sys.exit(0) 
                        pygame.quit()
                        self.game_exit()
                        
            if self.pozycja > 4:
                self.pozycja =1
            if self.pozycja < 1:
                self.pozycja =4
            if self.pozycja == 1:
                start = self.basicFont.render("start", 1, self.color0)
                
            else:
                start = self.basicFont.render("start", 1, self.color1)
            if self.pozycja == 2:
                ustawienia=self.basicFont.render("ustawienia", 1, self.color0)
            else:
                ustawienia=self.basicFont.render("ustawienia", 1, self.color1)
            if self.pozycja== 3:
                rekordy=self.basicFont.render("rekordy", 1, self.color0)
            else:
                rekordy=self.basicFont.render("rekordy", 1, self.color1)
            if self.pozycja== 4:
                exit=self.basicFont.render("exit", 1, self.color0)
            else:
                exit=self.basicFont.render("exit", 1, self.color1)




            #self.surface.fill((0,0,0))  # czyscimy ekran, malo wydajne ale wystarczy
            self.surface.blit(self.tlo, (0,0)) 
            self.surface.blit(start,(200,150))
            self.surface.blit(ustawienia,(200,200))
            self.surface.blit(rekordy, (200,250))
            self.surface.blit(exit,(200,300))
            
            pygame.display.flip() 
            
            

        self.game_exit()    
if __name__ == '__main__':
   menu()
    
    

