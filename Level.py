import pygame
from Button import Title_Button

class Level : 
    def __init__(self, setting, tag, screen) : 
        self.scale = 0.5
        self.setting = setting
        self.screen = screen

        # level_select infor
        self.game_start = Title_Button(0, 0, self.setting.level_tb, self.screen, self.scale)
        self.star = 0
        self.font = pygame.font.Font('res\\font\\SpeedRushItalic-GOYoa.ttf', 20)
        self.tag = self.font.render(tag, True, (153, 76, 0))
        self.lock = self.img_scale(self.setting.level_lock, self.scale)
        self.isOpen = False
        self.set_postion()
        self.star_anni = self.img_scale(self.setting.level_star_1, self.scale)
        


        # game data 
        

    def set_postion(self) : 
        
        self.tag_rect = self.tag.get_rect() 
        self.tag_rect.centerx = self.game_start.img_rect.centerx
        self.tag_rect.centery = self.game_start.img_rect.centery - 20

        self.star_anni_rect = self.star_anni.get_rect()
        self.star_anni_rect.centerx = self.game_start.img_rect.centerx
        self.start_anni_rect.centery = self.game_start.img_rect.bottom
    
        self.lock_rect = self.lock.get_rect()
        self.lock_rect.center = self.game_start.img_rect.center


        


    def img_scale(self, img, scale) : 
        res = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        return res
    
    def draw(self) : 
        self.game_start.draw()
        if self.isOpen: 
            self.screen.blit(self.tag, self.tag_rect)
            self.switch_star()
            self.screen.blit(self.star_anni, self.star_anni_rect)
            
        else : 
            self.screen.blit(self.lock, self.lock_rect)


    def switch_star(self) : 
        if (self.star == 0) : 
            self.star_anni = self.img_scale(self.setting.level_star_1, self.scale)
        elif self.star == 1 : 
            self.star_anni = self.img_scale(self.setting.level_star_2, self.scale)
        elif self.star == 2 : 
            self.star_anni = self.img_scale(self.setting.level_star_3, self.scale)
        elif self.star == 3 : 
            self.star_anni = self.img_scale(self.setting.level_star_4, self.scale)