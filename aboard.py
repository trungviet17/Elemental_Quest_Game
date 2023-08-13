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
        self.aboard_up = self.set_scale(self.setting.match_up_board)
        self.aboard_down = self.set_scale(self.setting.match_down_board)

        self.move_tb = self.set_scale(self.setting.match_move_tbl)
        self.loading_bar = self.set_scale(self.setting.match_loading_bar)
        self.loading = self.set_scale(self.setting.match_loading)

        self.pause_button = Title_Button(0, 0, self.setting.match_pause_but, self.screen, self.scale)

        self.star_1 = self.set_scale(self.setting.match_star_1)
        self.star_2 = self.set_scale(self.setting.match_star_2)
        self.star_3 = self.set_scale(self.setting.match_star_3)

        self.level_tb = self.set_scale(self.setting.match_level_tb)
        self.score_tb = self.set_scale(self.setting.match_score_tb)
        
        self.score = 0
        self.num_move = 0
        self.font = pygame.font.Font('res\\font\\SpeedRushItalic-GOYoa.ttf', 40)
        self.font_num = pygame.font.Font('res\\font\\SpeedRushItalic-GOYoa.ttf', 60)

        self.level = self.font.render('Level :' + str(self.game_level), True, (255, 255, 255))
        self.score_nt = self.font.render('Score :' + str(self.score), True, (255, 255, 255))
        self.move = self.font.render(str(self.num_move), True, (255, 255, 255))

        self.heart = Title_Button(0, 0, self.setting.help_heart, self.screen, self.scale)
        self.luck = Title_Button(0, 0, self.setting.help_luck, self.screen, self.scale)
        self.time = Title_Button(0, 0, self.setting.help_time, self.screen, self.scale)

        self.set_position()
        self.prep_move()
        self.prep_score()

    def set_scale(self, img) : 
        res = pygame.transform.scale(img, (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))
        return res

    def set_position(self) : 

        self.aboard_up_rect = self.aboard_up.get_rect()
        self.aboard_up_rect.midtop = self.screen_rect.midtop

        self.aboard_down_rect = self.aboard_down.get_rect()
        self.aboard_down_rect.midbottom = self.screen_rect.midbottom

        self.loading_bar_rect = self.loading_bar.get_rect()
        self.loading_bar_rect.centerx = self.aboard_up_rect.centerx
        self.loading_bar_rect.centery = self.aboard_up_rect.centery - 30

        self.move_tb_rect = self.move_tb.get_rect()
        self.move_tb_rect.midtop = self.loading_bar_rect.midbottom

        self.level_tb_rect = self.level_tb.get_rect()
        self.level_tb_rect.left = self.loading_bar_rect.left + 10
        self.level_tb_rect.top = self.loading_bar_rect.bottom + 10

        self.level_rect = self.level.get_rect()
        self.level_rect.left = self.level_tb_rect.left + 10
        self.level_rect.centery = self.level_tb_rect.centery - 5


        self.score_tb_rect = self.score_tb.get_rect()
        self.score_tb_rect.right = self.loading_bar_rect.right - 10
        self.score_tb_rect.top = self.level_tb_rect.top

        self.star_1_rect = self.star_1.get_rect()
        self.star_1_rect.centerx = self.loading_bar_rect.left + 200
        
        self.star_2_rect = self.star_2.get_rect()
        self.star_2_rect.centerx = self.loading_bar_rect.left + 400 

        self.star_3_rect = self.star_3.get_rect()
        self.star_3_rect.centerx = self.loading_bar_rect.right - 100

        self.star_1_rect.centery = self.loading_bar_rect.centery
        self.star_2_rect.centery = self.loading_bar_rect.centery
        self.star_3_rect.centery = self.loading_bar_rect.centery

        self.score_nt_rect = self.score_nt.get_rect()
        self.move_rect = self.move.get_rect()

        self.pause_button.img_rect.centery = self.aboard_down_rect.centery + 20
        self.pause_button.img_rect.right = self.aboard_down_rect.right - 50

    def prep_score(self) : 
        self.score_nt = self.font.render('Score :' + str(self.score), True, (255, 255, 255))
        self.score_nt_rect.centery = self.score_tb_rect.centery - 5
        self.score_nt_rect.left = self.score_tb_rect.left + 10


    def prep_move(self) : 
        self.move = self.font_num.render(str(self.num_move), True, (255, 255, 255))
        self.move_rect.centery = self.move_tb_rect.centery
        self.move_rect.centerx = self.move_tb_rect.centerx


    def draw(self): 
        self.screen.blit(self.aboard_up, self.aboard_up_rect)
        self.screen.blit(self.aboard_down, self.aboard_down_rect)
        self.screen.blit(self.loading_bar, self.loading_bar_rect)
        self.screen.blit(self.star_1, self.star_1_rect)
        self.screen.blit(self.star_2, self.star_2_rect)
        self.screen.blit(self.star_3, self.star_3_rect)

        self.screen.blit(self.move_tb, self.move_tb_rect)
        self.screen.blit(self.move, self.move_rect)

        self.screen.blit(self.score_tb, self.score_tb_rect)
        self.screen.blit(self.score_nt, self.score_nt_rect)

        self.screen.blit(self.level_tb, self.level_tb_rect)
        self.screen.blit(self.level, self.level_rect)

        self.pause_button.draw()
