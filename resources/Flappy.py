import pygame, sys
from pygame.locals import *
import random
screen_size = (500,600)      # ustalamy rozmiar ekranu









class IsoGame(object):
    import random 
    def __init__(self):
        #self.myfont = pygame.font.SysFont("monospace", 16)
        self.czas=pygame.time.get_ticks()
        self.czas2=pygame.time.get_ticks()
        import random 
        pygame.init()       # incjalizujemy biblioteke pygame
        flag = DOUBLEBUF    # wlaczamy tryb podwojnego buforowania
        
        self.czas3=pygame.time.get_ticks()
        self.trudnosc = open('resources/trudnosc.txt','r')
        self.ustawienia_trudnosci= self.trudnosc.readline().strip('\n\r') 
        self.trudnosc.close()
        self.diff=int(self.ustawienia_trudnosci)
        if self.diff==1:
            self.player_x = 70   # pozycja x duszka na ekranie
            self.player_y = 300
            self.predkosc=4
            self.korektor=30
        if self.diff ==2:
            self.player_x = 100   # pozycja x duszka na ekranie
            self.player_y = 300
            self.predkosc =5
            self.korektor=15
        if self.diff==3:
            self.player_x = 100   # pozycja x duszka na ekranie
            self.player_y = 300
            self.predkosc =7
            self.korektor=0
            
        # tworzymy bufor na  grafike
        self.surface = pygame.display.set_mode(screen_size,flag)

        # zmienna stanu gry
        self.gamestate = 1  # 1 - run, 0 - exit
        self.przegrana=0
        self.tlo=pygame.image.load('resources/images/layer-1-sky.png')
        grafika1=pygame.image.load('resources/images/ptak1.png')
        grafika2=pygame.image.load('resources/images/ptak2.png')
        grafika3=pygame.image.load('resources/images/ptak3.png')
        self.gover=pygame.image.load('resources/images/Game_over.png')
        frame_rect = pygame.Rect(1,0,125,47)
        self.player_image = [None] * 3 
        self.player_image[0]=grafika1
        self.player_image[1]=grafika2
        self.player_image[2]=grafika3
        
        self.basicFont = pygame.font.SysFont(None, 30)
        
        
        
        self.counter=0
        self.player_frame = 1 # numer klatki animacji
        self.speed = 1.2     # szybkosc poruszania duszka
        # pozycja y duszka na ekranie
        self.rura1 = pygame.image.load('resources/images/rura1.png')
        self.rura2 = pygame.image.load('resources/images/rura2.png') 
        self.h=-600
        self.h1=300+self.korektor
        self.x=800
        self.grawitacja =4
        self.ciagptaka=3.5
        self.loop()                             # glowna petla gry
    def move(self,dirx,diry):
       """ poruszanie duszkiem """
       self.player_x = self.player_x + (dirx * self.speed)
       self.player_y = self.player_y + (diry * self.speed)

    def game_exit(self):
        """ funkcja przerywa dzialanie gry i wychodzi do systemu"""
        exit()

    def loop(self):
        """ glowna petla gry """
        self.counter=0
        punkty = self.basicFont.render("Score = "+str(self.counter), 1, (0,0,0))
        textRect = punkty.get_rect()
        textRect.topleft=[20,20]
        self.surface.blit(punkty,textRect)
        pygame.display.flip()
        self.color0=(0,255,255)
        self.basicFont = pygame.font.SysFont(None, 30)
        pygame.mixer.music.load('resources/sounds/nature_sketch.wav')
        pygame.mixer.music.play(-1)
        
        
        
        while self.gamestate==1:
            while self.przegrana==0:
                player_anim = 0
                for event in pygame.event.get():
                    if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                        self.gamestate=0
                keys = pygame.key.get_pressed() # odczytujemy stan klawiszy

                if keys[K_SPACE]:
                    self.move(0,-1)  
                    player_anim = 1
                    pygame.mixer.music.load('resources/sounds/jump.wav')
                    pygame.mixer.music.play(0)
                    self.player_y-=self.ciagptaka
                if keys[K_ESCAPE]:
                    self.przegrana=1
                if player_anim == 1:
                    self.player_frame+=1
                    if self.player_frame>1:
                        self.player_frame = 0
            
                if (pygame.time.get_ticks()-self.czas2>20):
                    if self.x<=-60:   
                        self.counter+=1
                        
                        punkty = self.basicFont.render("Score = "+str(self.counter), 1, (0,0,0))
                        self.surface.blit(punkty,punkty.get_rect())
                        pygame.display.flip() 
                        
                    #if self.x< -100:
                    #if self.x<=-60:  
                        self.x=500
                        self.h=self.random.randint(-600,-400)
                        self.h1=self.h+900+self.korektor
                        self.czas=pygame.time.get_ticks()
                    


                    self.player_y+=self.grawitacja    
                    self.x=self.x-self.predkosc # ustawienie trudnosci
                    self.czas2=  pygame.time.get_ticks()
  


                if  (self.x<= self.player_x<=(self.x+66) or keys[K_ESCAPE] ):
                    if( self.player_y<= self.h + 800 or self.player_y >= (self.h1-30) ):
                        self.player_frame = 2
                        self.surface.blit(self.player_image[self.player_frame],(self.player_x,self.player_y))
                        pygame.display.flip()   # przenosimy bufor na ekran
                        self.surface.blit(self.gover, (0,0)) 
                        pygame.display.flip()   # przenosimy bufor na ekran
                        self.przegrana=1
                        ##################Zapisywanie rekordow#####################
                        if self.diff==1:
                            self.p1='resources/rekordy1.txt'
                        if self.diff==2:
                            self.p1='resources/rekordy2.txt'
                        if self.diff==3:
                            self.p1='resources/rekordy3.txt'
                        self.r = open(self.p1,'r')
                        self.a = []
                        self.a.append(self.r.readline().strip('\n\r'))
                        self.a.append(self.r.readline().strip('\n\n\r'))
                        self.a.append(self.r.readline().strip('\n\n\n\r'))
                        self.a.append(self.r.readline().strip('\n\n\n\n\r'))
                        self.a.append(self.r.readline().strip('\n\n\n\n\n\r'))
                        self.a.append(self.r.readline().strip('\n\n\n\n\n\n\r'))
                        self.a.append(self.r.readline().strip('\n\n\n\n\n\n\n\r'))
                        self.a.append(self.r.readline().strip('\n\n\n\n\n\n\n\n\r'))
                        self.b=self.a.copy()
                        for i in range(len(self.a)):
                            if (self.counter>int(self.a[i])):
                                self.a[i]=str(self.counter)
                                i+=1
                          
                                while i<=(len(self.a)-1):
                                    self.a[i]=self.b[i-1]
                                    i+=1
                                break
                        self.r = open(self.p1,'w')
                        for i in range(len(self.a)):
                            #b=str(self.a[i])
                            self.r.write(self.a[i] + '\n') 
                            if (i==(len(self.a)-1)):
                                self.r.close()
                    
                        


            
        
                self.surface.fill((0,0,0))  # czyscimy ekran, malo wydajne ale wystarczy
                self.surface.blit(self.tlo, (0,0)) 
                self.surface.blit(self.rura2, (self.x,self.h)) 
                self.surface.blit(self.rura1, (self.x,self.h1)) 
        
           # umieszczamy gracza
                self.surface.blit(punkty,punkty.get_rect())
                self.surface.blit(self.player_image[self.player_frame],(self.player_x,self.player_y))
                pygame.display.flip()   # przenosimy bufor na ekran
            
            while self.przegrana==1:
                con = self.basicFont.render("enter zeby kontynuować", 1, self.color0)
                wyjscie = self.basicFont.render("esc zeby wyjść do menu", 1, self.color0)
                con1 = self.basicFont.render("Przegraleś!", 1, self.color0)
                #self.surface.fill((0,0,0))
                self.surface.blit(con,(100,100))
                self.surface.blit(con1,(100,200))
                self.surface.blit(wyjscie,(100,300))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                        self.gamestate=0
                keys = pygame.key.get_pressed() # odczytujemy stan klawiszy
              
                #self.czas3=pygame.time.get_ticks()
                if keys[pygame.K_RETURN]:
                    exec(open('resources/Flappy.py').read())
                if keys[pygame.K_ESCAPE]:
                    exec(open('game.py').read())
                    

if __name__ == '__main__':
   IsoGame()
    
    

