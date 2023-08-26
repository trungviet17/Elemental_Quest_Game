from pygame.sprite import Sprite
import pygame 
import pygame.font
import random
"""  The element class can do:
    - Round shape, color, with chemical name written on it
    - Subclass of Sprite . class
"""
class Element : 
    
    def __init__(self, c_tag, c_game) :
        
        self.screen = c_game.screen 
        self.setting = c_game.setting
        self.scale = 0.35
        self.tag_name = c_tag

        # setting img
        self.bgr_int = random.randint(0, len(self.setting.element_simp) - 1)
        self.img_to_scr = self.trans_img(self.setting.element_simp[self.bgr_int])

        self.img_simp = self.trans_img(self.setting.element_simp[self.bgr_int])
        self.img_shine = self.trans_img(self.setting.element_shi[self.bgr_int])
        
        # setting information
        self.font = pygame.font.Font('res\\font\\SuperBubble-Rpaj3.ttf', 20)
        self.text = self.font.render(c_tag, True, self.setting.element_text_color)
        self.sub_font = pygame.font.Font('res\\font\\SpeedRushItalic-GOYoa.ttf', 30)
        self.num_vis = self.sub_font.render(str(1), True, (255,255,255))
       # self.update_num()

        self.isPress = False
        self.action = False

        self.set_position()
        

    def draw(self) :    
        pos = pygame.mouse.get_pos()
        self.action = False
        self.text_rect.center = self.img_to_scr_rect.center
        if self.img_to_scr_rect.collidepoint(pos) : 
            self.img_to_scr = self.img_shine
            self.screen.blit(self.img_to_scr, self.img_to_scr_rect)
            if pygame.mouse.get_pressed()[0] == 1 and self.isPress == False : 
                self.action = True
                self.isPress = True
            if pygame.mouse.get_pressed()[0] == 0 : self.isPress = False
        else : 
            self.img_to_scr = self.img_simp
            self.screen.blit(self.img_to_scr, self.img_to_scr_rect)
        self.screen.blit(self.text, self.text_rect)
       

    def trans_img(self, img) : 
        res = pygame.transform.scale(img, (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))
        return res
    
    # def update_num(self) :
    #     self.num_text = self.sub_font.render(str(self.num), True, self.setting.element_text_color)

    def set_position(self) : 
        self.img_to_scr_rect = self.img_to_scr.get_rect()

        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.img_to_scr_rect.center

        self.num_vis_rect = self.num_vis.get_rect()
        self.num_vis_rect.centerx = self.img_to_scr_rect.centerx 
        self.num_vis_rect.centery = self.img_to_scr_rect.centery

    def draw_infor(self, num) : 
        self.num_vis = self.sub_font.render(str(num), True, (255,255,255))
        self.num_vis_rect.centerx = self.img_to_scr_rect.centerx + 30
        self.num_vis_rect.centery = self.img_to_scr_rect.centery + 30
        pygame.draw.circle(self.screen, (204, 204, 255), self.num_vis_rect.center, 15)
        self.screen.blit(self.num_vis, self.num_vis_rect)
    
