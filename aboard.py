import pygame
from Button import Title_Button
"""
- Thanh tính điểm, thời gian , level
"""


class Aboard : 
    def __init__ (self, c_game) : 
        self.screen = c_game.screen 
        self.setting = c_game.setting
        self.game_level = c_game.level.tag_name
        self.screen_rect = self.screen.get_rect()


        self.scale = 0.5
        # aboard setting
        self.aboard_up = self.set_scale(self.setting.match_up_board, self.scale)
        self.aboard_down = self.set_scale(self.setting.match_down_board, self.scale)
        self.aboard_left = self.set_scale(self.setting.match_targetbar, self.scale)

        self.loading_bar = self.set_scale(self.setting.match_loading_bar, self.scale)
        self.loading = self.set_scale(self.setting.match_loading,self.scale)

        self.pause_button = Title_Button(0, 0, self.setting.match_pause_but, self.screen, self.scale)

        self.star_1 = self.set_scale(self.setting.match_star_1, self.scale)
        self.star_2 = self.set_scale(self.setting.match_star_2, self.scale)
        self.star_3 = self.set_scale(self.setting.match_star_3, self.scale)

        self.time_tb = self.set_scale(self.setting.match_table, self.scale)
        self.score_tb = self.set_scale(self.setting.match_table, self.scale)
        self.move_tb = self.set_scale(self.setting.match_table, self.scale)

        self.start = Title_Button(0, 0, self.setting.element_shi_rect, self.screen, self.scale)
        
        self.score = 0
        self.num_move = 0
        self.font = pygame.font.Font('res\\font\\SpeedRushItalic-GOYoa.ttf', 40)
        self.font_num = pygame.font.Font('res\\font\\SpeedRushItalic-GOYoa.ttf', 60)

        self.level_text = []
        for i in str(self.game_level) : 
            self.level_text.append(self.setting.number_img[int(i)])
        self.level_bg = self.set_scale(self.setting.match_level_board, self.scale)
        self.level_banner = self.set_scale(self.setting.match_level, self.scale - 0.2)

        self.score_nt = self.font.render(str(self.score), True, (255, 255, 255))
        self.move = self.font.render(str(self.num_move), True, (255, 255, 255))

        self.heart_button = Title_Button(0, 0, self.setting.match_help_bg, self.screen, self.scale )
        self.luck_button = Title_Button(0, 0, self.setting.match_help_bg, self.screen, self.scale )
        self.time_button = Title_Button(0, 0, self.setting.match_help_bg, self.screen, self.scale )

        self.heart = self.set_scale(self.setting.help_heart, self.scale - 0.25)
        self.time = self.set_scale(self.setting.help_time, self.scale - 0.25)
        self.luck = self.set_scale(self.setting.help_luck, self.scale - 0.25)
        self.clock = self.set_scale(self.setting.match_clock, self.scale)
        self.score_icon = self.set_scale(self.setting.match_score_icon, self.scale - 0.1)
        self.move_icon = self.set_scale(self.setting.match_move_icon, self.scale - 0.2)

        self.start_text = self.font.render('Start', True, (0, 255, 255))


        self.element_up_but = Title_Button(0, 0, self.setting.btn_up, self.screen, self.scale - 0.15)
        self.element_down_but = Title_Button(0, 0, self.setting.btn_down, self.screen, self.scale - 0.15)

        
        self.close_target_but = Title_Button(0, 0, self.setting.next_button, self.screen, self.scale - 0.15)
        self.isOpen = False
        self.set_position()
        self.prep_move()
        self.prep_score()

    def set_scale(self, img, scale) : 
        res = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        return res

    def set_position(self) : 

        self.aboard_up_rect = self.aboard_up.get_rect()
        self.aboard_up_rect.midtop = self.screen_rect.midtop

        self.aboard_down_rect = self.aboard_down.get_rect()
        self.aboard_down_rect.midbottom = self.screen_rect.midbottom

        self.aboard_left_rect = self.aboard_left.get_rect()
        self.aboard_left_rect.midleft = self.screen_rect.midleft

        self.loading_bar_rect = self.loading_bar.get_rect()
        self.loading_bar_rect.centerx = self.aboard_up_rect.centerx
        self.loading_bar_rect.centery = self.aboard_up_rect.centery - 20

        self.score_tb_rect = self.score_tb.get_rect()
        self.score_tb_rect.centery = self.loading_bar_rect.centery + 20
        self.score_tb_rect.right = self.aboard_up_rect.right - 70
        

        self.time_tb_rect = self.time_tb.get_rect()
        self.time_tb_rect.centery = self.score_tb_rect.centery
        self.time_tb_rect.left = self.aboard_up_rect.left + 70


        self.clock_rect = self.clock.get_rect()
        self.clock_rect.center = self.time_tb_rect.midleft

        self.star_1_rect = self.star_1.get_rect()
        self.star_1_rect.centerx = self.loading_bar_rect.left + 30
        
        self.star_2_rect = self.star_2.get_rect()
        self.star_2_rect.centerx = self.loading_bar_rect.centerx

        self.star_3_rect = self.star_3.get_rect()
        self.star_3_rect.centerx = self.loading_bar_rect.right - 30

        self.star_1_rect.centery = self.loading_bar_rect.centery
        self.star_2_rect.centery = self.loading_bar_rect.centery
        self.star_3_rect.centery = self.loading_bar_rect.centery

        self.score_nt_rect = self.score_nt.get_rect()
        self.move_rect = self.move.get_rect()
        

        self.pause_button.img_rect.centery = self.aboard_down_rect.centery + 15
        self.pause_button.img_rect.right = self.aboard_down_rect.right - 50


        self.heart_button.img_rect.centery = self.pause_button.img_rect.centery
        self.heart_button.img_rect.left = self.aboard_down_rect.left + 50
        self.heart_rect = self.heart.get_rect()
        self.heart_rect.centerx = self.heart_button.img_rect.centerx
        self.heart_rect.centery = self.heart_button.img_rect.centery +2
        

        self.luck_button.img_rect.centery = self.pause_button.img_rect.centery
        self.luck_button.img_rect.centerx = self.heart_button.img_rect.centerx + 70
        self.luck_rect = self.luck.get_rect()
        self.luck_rect.center = self.luck_button.img_rect.center

        self.time_button.img_rect.centery = self.pause_button.img_rect.centery
        self.time_button.img_rect.centerx = self.heart_button.img_rect.centerx + 140
        self.time_rect = self.time.get_rect()
        self.time_rect.center = self.time_button.img_rect.center

        self.start.img_rect.center = self.screen_rect.center

        self.start_text_rect = self.start_text.get_rect()
        self.start_text_rect.center = self.start.img_rect.center

        self.move_tb_rect = self.move_tb.get_rect()
        self.move_tb_rect.right = self.pause_button.img_rect.left - 20
        self.move_tb_rect.centery = self.pause_button.img_rect.centery


        self.move_icon_rect = self.move_icon.get_rect()
        self.move_icon_rect.center = self.move_tb_rect.midleft

        self.score_icon_rect = self.score_icon.get_rect()
        self.score_icon_rect.center = self.score_tb_rect.midleft

        self.level_bg_rect = self.level_bg.get_rect()
        self.level_bg_rect.midtop = self.loading_bar_rect.center

        self.level_banner_rect = self.level_banner.get_rect()
        self.level_banner_rect.centerx = self.level_bg_rect.centerx
        self.level_banner_rect.centery = self.level_bg_rect.centery - 30

        self.element_down_but.img_rect.bottom = self.aboard_down_rect.top + 1
        self.element_down_but.img_rect.left = self.aboard_down_rect.right + 70

        self.element_up_but.img_rect.top = self.aboard_up_rect.bottom - 1
        self.element_up_but.img_rect.left = self.element_down_but.img_rect.left

       

        self.close_target_but.img_rect.center = self.aboard_left_rect.midright


    def prep_score(self) : 
        self.score_nt = self.font.render(str(self.score), True, (255, 255, 255))
        self.score_nt_rect.center = self.score_tb_rect.center


    def prep_move(self) : 
        self.move = self.font.render(str(self.num_move), True, (255, 255, 255))
        self.move_rect.center = self.move_tb_rect.center


    def draw(self): 
        

        self.screen.blit(self.aboard_up, self.aboard_up_rect)
        self.screen.blit(self.aboard_down, self.aboard_down_rect)
        
        self.screen.blit(self.level_bg, self.level_bg_rect)
        self.screen.blit(self.loading_bar, self.loading_bar_rect)
        self.screen.blit(self.star_1, self.star_1_rect)
        self.screen.blit(self.star_2, self.star_2_rect)
        self.screen.blit(self.star_3, self.star_3_rect)


        self.screen.blit(self.score_tb, self.score_tb_rect)
        self.screen.blit(self.time_tb, self.time_tb_rect)
        self.screen.blit(self.move_tb, self.move_tb_rect)
        self.screen.blit(self.level_banner, self.level_banner_rect)

        
        self.screen.blit(self.score_nt, self.score_nt_rect)
        self.screen.blit(self.move, self.move_rect)
        

        self.start.draw()
        self.screen.blit(self.start_text, self.start_text_rect)
        self.pause_button.draw()
        self.heart_button.draw()
        self.time_button.draw()
        self.luck_button.draw()

        self.screen.blit(self.clock, self.clock_rect)
        self.screen.blit(self.time, self.time_rect)
        self.screen.blit(self.heart, self.heart_rect)
        self.screen.blit(self.luck, self.luck_rect)
        self.screen.blit(self.score_icon, self.score_icon_rect)
        self.screen.blit(self.move_icon, self.move_icon_rect)

        self.element_down_but.draw()
        self.element_up_but.draw()

        if self.close_target_but.action and not self.isOpen : 
            self.close_target_but.set_img(self.setting.prew_button)
            self.isOpen = True
        elif self.close_target_but.action and self.isOpen : 
            self.close_target_but.set_img(self.setting.next_button)
            self.isOpen = False

        if self.isOpen : 
            self.screen.blit(self.aboard_left, self.aboard_left_rect)

        self.close_target_but.draw()

