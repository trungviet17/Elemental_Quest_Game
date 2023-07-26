import pygame
from State import State
from Background_Scrolling import Background_Scrolling

class About_title(State) : 
    def __init__(self, game):
        State.__init__(self,game)
        self.scale = 0.5
        self.table = pygame.transform.scale(self.setting.table, (int(self.setting.table.get_width() * self.scale), int(self.setting.table.get_height() * self.scale)))
        self.close = pygame.transform.scale(self.setting.close_2, (int(self.setting.close_2.get_width() * self.scale), int(self.setting.close_2.get_height() * self.scale)))
        self.bg = pygame.transform.scale(self.setting.bg, (int(self.setting.bg.get_width() * self.scale), int(self.setting.bg.get_height() * self.scale)))
        self.back_ground = Background_Scrolling(game)
        self.set_position()
        

    
    def render(self) : 
        self.back_ground.draw()
        self.screen.blit(self.bg, self.bg_rect)
        self.screen.blit(self.table, self.table_rect)
        self.screen.blit(self.close, self.close_rect)

    def update(self):
        pass

    def set_position(self) : 
        self.screen_rect = self.screen.get_rect()
        self.table_rect = self.table.get_rect()
        self.close_rect = self.close.get_rect()
        self.bg_rect = self.bg.get_rect()

        self.bg_rect.centerx = self.screen_rect.centerx
        self.bg_rect.centery = self.screen_rect.centery

        self.table_rect.centerx = self.screen_rect.centerx
        self.table_rect.centery = self.screen_rect.centery 

        self.close_rect.center = self.table_rect.topright
