import pygame

class Level : 
    def __init__(self, setting, tag) : 
        self.scale = 0.5
        self.setting = setting

        # level_select infor
        self.table = self.img_scale(self.setting.level_tb, self.scale)
        self.star = 0
        self.tag = tag


        


    def img_scale(self, img, scale) : 
        res = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        return res