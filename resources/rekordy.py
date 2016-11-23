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
            if (pygame.time.get_ticks()-self.czas3>135):
                if keys[pygame.K_ESCAPE]:
                    exec(open('game.py').read())
               
            pygame.display.flip() 
            self.surface.fill((0,0,0))
            self.surface.blit(self.tlo, (0,0)) 
            self.r=open('resources/rekordy1.txt','r')
            w1= self.r.readline().strip('\n\r')
            w2= self.r.readline().strip('\n\n\r')
            w3= self.r.readline().strip('\n\n\n\r')
            w4= self.r.readline().strip('\n\n\n\n\r')
            w5= self.r.readline().strip('\n\n\n\n\n\r')
            w6= self.r.readline().strip('\n\n\n\n\n\n\r')
            w7= self.r.readline().strip('\n\n\n\n\n\n\n\r')
            w8= self.r.readline().strip('\n\n\n\n\n\n\n\n\r')
            w1 = self.basicFont.render(str(w1), 1, self.color1)
            w2 = self.basicFont.render(str(w2), 1, self.color1)
            w3 = self.basicFont.render(str(w3), 1, self.color1)
            w4 = self.basicFont.render(str(w4), 1, self.color1)
            w5 = self.basicFont.render(str(w5), 1, self.color1)
            w6 = self.basicFont.render(str(w6), 1, self.color1)
            w7 = self.basicFont.render(str(w7), 1, self.color1)
            w8 = self.basicFont.render(str(w8), 1, self.color1)
            self.r2=open('resources/rekordy2.txt','r')
            m1= self.r2.readline().strip('\n\r')
            m2= self.r2.readline().strip('\n\n\r')
            m3= self.r2.readline().strip('\n\n\n\r')
            m4= self.r2.readline().strip('\n\n\n\n\r')
            m5= self.r2.readline().strip('\n\n\n\n\n\r')
            m6= self.r2.readline().strip('\n\n\n\n\n\n\r')
            m7= self.r2.readline().strip('\n\n\n\n\n\n\n\r')
            m8= self.r2.readline().strip('\n\n\n\n\n\n\n\n\r')
            m1 = self.basicFont.render(str(m1), 1, self.color1)
            m2 = self.basicFont.render(str(m2), 1, self.color1)
            m3 = self.basicFont.render(str(m3), 1, self.color1)
            m4 = self.basicFont.render(str(m4), 1, self.color1)
            m5 = self.basicFont.render(str(m5), 1, self.color1)
            m6 = self.basicFont.render(str(m6), 1, self.color1)
            m7 = self.basicFont.render(str(m7), 1, self.color1)
            m8 = self.basicFont.render(str(m8), 1, self.color1)
            self.r3=open('resources/rekordy3.txt','r')
            h1= self.r3.readline().strip('\n\r')
            h2= self.r3.readline().strip('\n\n\r')
            h3= self.r3.readline().strip('\n\n\n\r')
            h4= self.r3.readline().strip('\n\n\n\n\r')
            h5= self.r3.readline().strip('\n\n\n\n\n\r')
            h6= self.r3.readline().strip('\n\n\n\n\n\n\r')
            h7= self.r3.readline().strip('\n\n\n\n\n\n\n\r')
            h8= self.r3.readline().strip('\n\n\n\n\n\n\n\n\r')
            h1 = self.basicFont.render(str(h1), 1, self.color1)
            h2 = self.basicFont.render(str(h2), 1, self.color1)
            h3 = self.basicFont.render(str(h3), 1, self.color1)
            h4 = self.basicFont.render(str(h4), 1, self.color1)
            h5 = self.basicFont.render(str(h5), 1, self.color1)
            h6 = self.basicFont.render(str(h6), 1, self.color1)
            h7 = self.basicFont.render(str(h7), 1, self.color1)
            h8 = self.basicFont.render(str(h8), 1, self.color1)
            
            
            w9 = self.basicFont.render("Escape żeby wrócić", 1, self.color1)
            easy= self.basicFont.render("easy", 1, self.color1)
            medium= self.basicFont.render("medium", 1, self.color1)
            hard= self.basicFont.render("hard", 1, self.color1)
            self.surface.blit(w1,(80,40)) 
            self.surface.blit(w2,(80,80))
            self.surface.blit(w3,(80,120))  
            self.surface.blit(w4,(80,160))  
            self.surface.blit(w5,(80,200))  
            self.surface.blit(w6,(80,240))  
            self.surface.blit(w7,(80,280))  
            self.surface.blit(w8,(80,320))
            self.surface.blit(easy,(80,350))
            self.surface.blit(w9,(80,500))  
            
            self.surface.blit(m1,(240,40)) 
            self.surface.blit(m2,(240,80))
            self.surface.blit(m3,(240,120))  
            self.surface.blit(m4,(240,160))  
            self.surface.blit(m5,(240,200))  
            self.surface.blit(m6,(240,240))  
            self.surface.blit(m7,(240,280))  
            self.surface.blit(m8,(240,320))  
            self.surface.blit(medium,(240,350))
            self.surface.blit(h1,(400,40)) 
            self.surface.blit(h2,(400,80))
            self.surface.blit(h3,(400,120))  
            self.surface.blit(h4,(400,160))  
            self.surface.blit(h5,(400,200))  
            self.surface.blit(h6,(400,240))  
            self.surface.blit(h7,(400,280))  
            self.surface.blit(h8,(400,320))  
            self.surface.blit(hard,(400,350))
 
       
       
                
       





           
            
            

        self.game_exit()    
if __name__ == '__main__':
   menu()
    
    

