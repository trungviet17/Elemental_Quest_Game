import pygame

"""
- Thanh tính điểm, thời gian , level
"""


class Aboard : 
    def __init__ (self, c_game) : 
        self.screen = c_game.screen 
        self.setting = c_game.setting
        self.screen_rect = self.screen.get_rect()

        # aboard setting 
        self.text_color = (255, 153, 153)
        self.font = pygame.font.SysFont(None, 48)
        
        #self.target_text = c_game.target
        self.score = 0
        self.level = 1

        self.prep_target()
        self.prep_score()
        self.prep_level()

    def prep_target(self) : 
        target = "Target: " + self.setting.target[self.level - 1]
        self.target_img = self.font.render(target, True, self.text_color)

        self.target_img_rect = self.target_img.get_rect()
        self.target_img_rect.right = self.screen_rect.right - 20 
        self.target_img_rect.top = 20

    def prep_score(self) : 
        score_text = "Score: " + str(self.score)
        self.score_img = self.font.render(score_text, True, self.text_color)

        self.score_img_rect = self.score_img.get_rect()
        self.score_img_rect.left = self.screen_rect.left + 20
        self.score_img_rect.top = 20


    def prep_level(self) : 
        level_text = "Level: " + str(self.level)
        self.level_img = self.font.render(level_text, True, self.text_color)

        self.level_img_rect = self.level_img.get_rect()
        self.level_img_rect.midtop = self.screen_rect.midtop
        self.level_img_rect.top = 20

    def showing(self) : 
        self.screen.blit(self.target_img, self.target_img_rect)
        self.screen.blit(self.score_img, self.score_img_rect)
        self.screen.blit(self.level_img, self.level_img_rect)