import pygame
from State import State
from Button import Title_Button

class Prize_title(State) :
    def __init__(self, game) : 
        State.__init__(self, game) 

        self.scale = 0.5
        self.close = Title_Button(0, 0, self.setting.close_2, self.screen, self.scale)
        self.prize_bg = pygame.transform.scale(self.setting.prize_bg_1, (int(self.setting.prize_bg_1.get_width() * self.scale), int(self.prize_bg_1.get_height() * self.scale)))
        self.prize_table = pygame.transform.scale(self.setting.prize_table, (int(self.setting.prize_table.get_width() * self.scale), int(self.setting.prize_table.get_height() * self.scale)))
        self.prize_header = pygame.transform.scale(self.setting.prize_header, (int(self.setting.prize_header.get_width() * self.scale), int(self.setting.prize_header.get_height() * self.scale)))
        self.prize_face = pygame.transform.scale(self.setting.prize_face , (int(self.setting.prize_face.get_width() * self.scale), int(self.setting.prize_face.get_height() * self.scale))) 
        self.prize_scroll = pygame.transform.scale(self.setting.prize_scroll, (int(self.setting.prize_scroll.get_width() * self.scale), int(self.setting.prize_scroll.get_height() * self.scale))) 
        self.prize_btn = Title_Button(0, 0, self.setting.prize_btn, self.screen, self.scale)
