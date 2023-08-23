import pygame
from State import State
from Button import Title_Button
from Background_Scrolling import Background_Scrolling


"""
- State prize : 
    - Lưu thông tin điểm cao nhất của người chơi 


"""

class Prize_title(State) :
    def __init__(self, game) : 
        State.__init__(self, game) 

        self.scale = 0.5
        self.close = Title_Button(0, 0, self.setting.close_2, self.screen, self.scale)
        self.prize_bg = pygame.transform.scale(self.setting.prize_bg_1, (int(self.setting.prize_bg_1.get_width() * 0.47), int(self.setting.prize_bg_1.get_height() * 0.45)))
        self.prize_table = pygame.transform.scale(self.setting.prize_table, (int(self.setting.prize_table.get_width() * self.scale), int(self.setting.prize_table.get_height() * self.scale)))
        self.prize_header = pygame.transform.scale(self.setting.prize_header, (int(self.setting.prize_header.get_width() * self.scale), int(self.setting.prize_header.get_height() * self.scale)))
        self.prize_scroll = pygame.transform.scale(self.setting.prize_scroll, (int(self.setting.prize_scroll.get_width() * self.scale), int(self.setting.prize_scroll.get_height() * (self.scale - 0.1))) )
        self.prize_content = []
        self.back_ground = Background_Scrolling(game,0)
        self.prize_dot = Title_Button(0, 0, self.setting.prize_dot, self.screen, self.scale)

        self.set_position()

    def set_position(self) : 
        self.screen_rect = self.screen.get_rect()
        
        self.prize_bg_rect = self.prize_bg.get_rect()
        self.prize_bg_rect.center = self.screen_rect.center

        self.prize_table_rect = self.prize_table.get_rect()
        self.prize_table_rect.center = self.screen_rect.center

        self.prize_header_rect = self.prize_header.get_rect()
        self.prize_header_rect.centery = self.prize_bg_rect.top
        self.prize_header_rect.centerx = self.prize_bg_rect.centerx

        self.close.img_rect.center = self.prize_table_rect.topright
        
        self.prize_scroll_rect = self.prize_scroll.get_rect()
        self.prize_scroll_rect.right = self.prize_bg_rect.right - self.prize_bg.get_width() // 12
        self.prize_scroll_rect.centery = self.prize_bg_rect.centery

        self.prize_dot.img_rect.center = self.prize_scroll_rect.midtop

    def render(self) : 
        self.back_ground.draw()
        self.screen.blit(self.prize_bg, self.prize_bg_rect)
        self.screen.blit(self.prize_table, self.prize_table_rect)
        self.screen.blit(self.prize_header, self.prize_header_rect)
        self.screen.blit(self.prize_scroll, self.prize_scroll_rect)
        self.prize_dot.draw()
        self.close.draw()


    def update(self) : 
        if self.close.action : 
            self.exit_state()
           
        pos = pygame.mouse.get_pos()
        if self.prize_dot.action and pos[1] <= self.prize_scroll_rect.bottom and pos[1] >= self.prize_scroll_rect.top: 
            self.prize_dot.img_rect.centery = pos[1] 
        if self.prize_scroll_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] : 
            self.prize_dot.img_rect.centery = pos[1]
            


class Prize_element : 
    def __init__(self, scale) : 
        self.scale = scale
        self.prize_face = pygame.transform.scale(self.setting.prize_face , (int(self.setting.prize_face.get_width() * self.scale), int(self.setting.prize_face.get_height() * self.scale))) 
        self.prize_btn = Title_Button(0, 0, self.setting.prize_btn, self.screen, self.scale)

    def set_position(self, x, y) : 
        pass
