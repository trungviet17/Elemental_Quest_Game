from State import State
from Button import Title_Button
from Background_Scrolling import Background_Scrolling
import pygame
class Setting_title(State) : 
    def __init__(self, game) : 
        State.__init__(self, game)

        self.scale = 0.5
        self.table = pygame.transform.scale(self.setting.table, (int(self.setting.table.get_width() * self.scale), int(self.setting.table.get_height() * self.scale)))
        self.close = Title_Button(0, 0, self.setting.close_2, self.screen, self.scale)
        self.bg = pygame.transform.scale(self.setting.bg, (int(self.setting.bg.get_width() * self.scale), int(self.setting.bg.get_height() * self.scale)))
        self.header = pygame.transform.scale(self.setting.setting_header, (int(self.setting.setting_header.get_width() * self.scale), int(self.setting.setting_header.get_height() * self.scale)))
        self.sound_bar = pygame.transform.scale(self.setting.setting_sound_1, (int(self.setting.setting_sound_1.get_width() * self.scale), int(self.setting.setting_sound_2.get_height() * self.scale))) 
        self.sound_change = pygame.transform.scale(self.setting.setting_sound_2, (int(self.setting.setting_sound_2.get_width() * self.scale), int(self.setting.setting_sound_2.get_height() * self.scale)))
        self.setting_music = Title_Button(0, 0, self.setting.setting_on, self.screen, self.scale)
        self.setting_sound = Title_Button(0, 0, self.setting.setting_on, self.screen, self.scale)
        self.setting_plus = Title_Button(0, 0, self.setting.setting_plus, self.screen, self.scale)
        self.setting_subtract = Title_Button(0, 0, self.setting.setting_subtract, self.screen, self.scale)

        self.back_ground = Background_Scrolling(game)
        self.set_position()

    def render(self) : 
        self.back_ground.draw()
        self.screen.blit(self.bg, self.bg_rect)
        self.screen.blit(self.table, self.table_rect)
        self.screen.blit(self.header, self.header_rect)
        self.setting_music.draw()
        self.setting_sound.draw()
        self.close.draw()
        

    def update(self):
        if self.close.isPress : 
            self.exit_state()
            self.close.isPress = False
        # Bug 
        if self.setting_music.isPress : 
            if self.setting_music.img == self.setting.setting_on : 
                self.setting_music.set_img(self.setting.setting_off)
            elif self.setting_music.img == self.setting.setting_off : 
                self.setting_music.set_img(self.setting.setting_on)
            self.setting_music.isPress = False
        # Bug
        if self.setting_sound.isPress : 
            if self.setting_sound.img == self.setting.setting_on : 
                self.setting_sound.set_img(self.setting.setting_off)
            elif self.setting_sound.img == self.setting.setting_off : 
                self.setting_sound.set_img(self.setting.setting_on)
            self.setting_sound.isPress = False

    def set_position(self):
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
        self.header_rect.centerx = self.screen_rect.centerx 
        self.header_rect.centery = self.table_rect.top

        
        self.setting_music.img_rect.right = self.bg_rect.right - int(self.bg.get_width() * self.scale // 4)
        self.setting_music.img_rect.top = self.table_rect.top + int(self.bg.get_height() * self.scale // 4 * 2)

        self.setting_sound.img_rect.right = self.setting_music.img_rect.right
        self.setting_sound.img_rect.top = self.setting_music.img_rect.bottom + 20


        