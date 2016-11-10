import pygame, sys
from pygame.locals import *
screen_size = (500,600)      # ustalamy rozmiar ekranu









class menu(object):

    def __init__(self):
        #self.myfont = pygame.font.SysFont("monospace", 16)
        self.gamestate=1
        self.basicFont=pygame.font.SysFont(None, 30)
        
        start = self.basicFont.render("start", 1, (0,255,255))
        ustawienia=self.basicFont.render("ustawienia", 1, (0,255,255))
                                         
        rekordy=self.basicFont.render("rekordy= ", 1, (0,255,255))
        exit=self.basicFont.render("exit= ", 1, (0,255,255))
        self.surface.blit(start,punkty.get_rect())
        self.surface.blit(ustawienia,punkty.get_rect())
        self.surface.blit(rekordy,punkty.get_rect())
        self.surface.blit(exit,punkty.get_rect())
        pygame.display.flip() 
        
        self.loop()
    def loop():
    
    
        
        if self.gamestate ==0:
            pygame.display.quit()
            sys.exit(0) 
            pygame.quit()
            self.game_exit()
    
        self.game_exit()    
if __name__ == '__main__':
   menu()
    
    

