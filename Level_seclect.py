from State import State
from Button import Title_Button
import pygame 

class Level_select(State) : 
    def __init__(self, game) :
        State.__init__(self, game) 
        
        self.scale = 0.5 
        self.header = self.img_scale(self.setting.level_select_header, self.scale)
        self.bg = self.img_scale(self.setting.level_select_bg, self.scale)
        self.bg_table = self.img_scale(self.setting.level_select_bg_table, self.scale)
        self.close = Title_Button(0, 0, self.setting.level_select_close, self.screen, self.scale)
        self.next = Title_Button(0, 0, self.setting.next_button, self.scale)
        self.prew = Title_Button(0, 0, self.setting.prew_button, self.scale)
        self.dot = []
        self.content = [[]]
    
    def img_scale(self, img, scale) : 
        res = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        return res
    
    def set_dot(self) : 
        for i in range(3) : 
            tmp = self.img_scale(self.setting.level_select_dot_2, self.scale)
            self.dot.append(tmp)

    def set_content(self) : 
        pass

    def render(self, surface):
        return super().render(surface)
    
    def update(self):
        return super().update()
    

