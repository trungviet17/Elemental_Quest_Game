import pygame
from State import State
from Background_Scrolling import Background_Scrolling
from Button import Title_Button
import webbrowser

"""
- State about 
    - chứa thông tin tác giả facebook và github
"""

class About_title(State) : 
    def __init__(self, game):
        State.__init__(self,game)
        self.scale = 0.5
        self.table = pygame.transform.scale(self.setting.table, (int(self.setting.table.get_width() * self.scale), int(self.setting.table.get_height() * self.scale)))
        self.close = Title_Button(0, 0, self.setting.close_2, self.screen, self.scale)
        self.bg = pygame.transform.scale(self.setting.bg, (int(self.setting.bg.get_width() * self.scale), int(self.setting.bg.get_height() * self.scale)))
        self.back_ground = Background_Scrolling(game)
        self.font_header = pygame.font.Font('res\\font\\PressStart2P-vaV7.ttf', 60)
        self.header = self.font_header.render("About", True, (128, 128, 128))
        self.font = pygame.font.SysFont(None, 50)
        self.content_1 = self.font.render("GitHub", True, (0,128,128))
        self.button_1 = Title_Button(0, 0, self.setting.content_button, self.screen, self.scale + 0.2)

        self.content_2 = self.font.render("FaceBook", True, (0, 128, 128))
        self.button_2 = Title_Button(0, 0, self.setting.content_button, self.screen, self.scale + 0.2)



        self.set_position()

    
    def render(self) : 
        self.back_ground.draw()
        self.screen.blit(self.bg, self.bg_rect)
        self.screen.blit(self.table, self.table_rect)
        self.screen.blit(self.header, self.header_rect)
        self.button_1.draw()
        self.screen.blit(self.content_1, self.content_1_rect)

        self.button_2.draw()
        self.screen.blit(self.content_2, self.content_2_rect)
        self.close.draw()

    def update(self):
        if self.close.action : 
            self.exit_state()
            
        if self.button_1.action : 
            webbrowser.open('https://github.com/trungviet17')
           
        if self.button_2.action : 
            webbrowser.open('https://www.facebook.com/gnurt17')
            

    def set_position(self) : 
        self.screen_rect = self.screen.get_rect()
        self.table_rect = self.table.get_rect()
        #self.close_rect = self.close.get_rect()
        self.bg_rect = self.bg.get_rect()

        self.bg_rect.centerx = self.screen_rect.centerx
        self.bg_rect.centery = self.screen_rect.centery

        self.table_rect.centerx = self.screen_rect.centerx
        self.table_rect.centery = self.screen_rect.centery 

        self.close.img_rect.center = self.table_rect.topright

        self.header_rect = self.header.get_rect()
        self.header_rect.centerx = self.table_rect.centerx 
        self.header_rect.top = self.table_rect.top + 50

        self.content_1_rect = self.content_1.get_rect()
        self.content_1_rect.centerx = self.header_rect.centerx
        self.content_1_rect.top = self.header_rect.top + 100

        self.button_1.img_rect.center = self.content_1_rect.center

        self.content_2_rect = self.content_2.get_rect()
        self.content_2_rect.centerx = self.header_rect.centerx
        self.content_2_rect.top = self.content_1_rect.top + 100

        self.button_2.img_rect.center = self.content_2_rect.center
