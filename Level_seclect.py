from State import State
from Button import Title_Button
from Background_Scrolling import Background_Scrolling
from Level import Level
import pygame 

"""
- State chứa menu của game 
    - Ô lưới 9 ô với mỗi ô là 1 đối tượng level của game 
    - chứa các button update và store
"""
class Level_select(State) : 
    def __init__(self, game) :
        State.__init__(self, game) 
        
        self.scale = 0.4 
        self.header = self.img_scale(self.setting.level_select_header, self.scale + 0.05)
        self.bg = self.img_scale(self.setting.level_select_bg, self.scale)
        self.bg_table = self.img_scale(self.setting.level_select_tb_2, self.scale)
        self.close = Title_Button(0, 0, self.setting.close_2, self.screen, self.scale)
        self.next = Title_Button(0, 0, self.setting.next_button, self.screen, self.scale)
        self.prew = Title_Button(0, 0, self.setting.prew_button,self.screen, self.scale)
        self.background = Background_Scrolling(game)
        self.dot = []
        self.content = [[],[],[]]


        self.set_dot()
        self.set_content()

        self.set_position()

        self.level_position()
    
    def img_scale(self, img, scale) : 
        res = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        return res
    
    def set_dot(self) : 
        for i in range(3) : 
            tmp = self.img_scale(self.setting.level_select_dot_2, self.scale)
            self.dot.append(tmp)
        self.dot[0] = self.img_scale(self.setting.level_select_dot_1, self.scale)
        self.index_dot = 0

    def set_content(self) : 
        for i in range (3) : 
            for j in range(3) : 
                tag = i * 3 + j + 1
                level = Level(self.setting, str(tag), self.screen)
                self.content[i].append(level)

    def render(self):
        self.background.draw()
        self.screen.blit(self.bg, self.bg_rect)
        self.screen.blit(self.bg_table, self.bg_table_rect)
        self.screen.blit(self.header, self.header_rect)
        self.close.draw()
        self.next.draw()
        self.prew.draw()

        for i in range(len(self.dot)) : 
            self.screen.blit(self.dot[i], self.dot_rect[i])

        for i in range(len(self.content)) : 
            for j in range (len(self.content[0])) : 
                self.content[i][j].draw()
            
    
    def update(self):
        if self.close.action : 
            self.exit_state()

        if self.next.action and self.index_dot < len(self.dot) - 1  : 
            self.dot[self.index_dot] = self.img_scale(self.setting.level_select_dot_2, self.scale)
            self.index_dot += 1
            self.dot[self.index_dot] = self.img_scale(self.setting.level_select_dot_1, self.scale)

        if self.prew.action and self.index_dot > 0 : 
            self.dot[self.index_dot] = self.img_scale(self.setting.level_select_dot_2, self.scale)
            self.index_dot -= 1
            self.dot[self.index_dot] = self.img_scale(self.setting.level_select_dot_1, self.scale)
            
            
    
    def set_position(self) : 
       
        self.bg_rect = self.bg.get_rect()
        self.bg_rect.center = self.screen_rect.center

        self.bg_table_rect = self.bg_table.get_rect()
        self.bg_table_rect.centerx = self.screen_rect.centerx
        self.bg_table_rect.centery = self.screen_rect.centery - 50

        self.close.img_rect.center = self.bg_table_rect.topright

        self.header_rect = self.header.get_rect()
        self.header_rect.center = self.bg_rect.midtop

        self.next.img_rect.top = self.bg_table_rect.bottom 
        self.next.img_rect.right = self.bg_rect.right - self.bg.get_width() // 6
        
        self.prew.img_rect.top = self.next.img_rect.top
        self.prew.img_rect.left = self.bg_rect.left + self.bg.get_width() // 6
        
        self.dot_position()


    def dot_position(self) :
        # dot setting
        center = len(self.dot) // 2 
        self.dot_rect = []

        for i in range(len( self.dot)) : 
            tmp = self.dot[i].get_rect()
            self.dot_rect.append(tmp) 

        self.dot_rect[center].centerx = self.bg_table_rect.centerx
        self.dot_rect[center].centery = self.next.img_rect.centery
        l = r = center
        while l > 0 and r < len(self.dot_rect) - 1 : 
            l -= 1
            self.dot_rect[l].centerx = self.dot_rect[center].centerx - (center - l) * 30
            self.dot_rect[l].centery = self.dot_rect[center].centery
           
            
            r += 1
            self.dot_rect[r].centerx = self.dot_rect[center].centerx + (r - center) * 30
            self.dot_rect[r].centery = self.dot_rect[center].centery

    def level_position(self) : 
        self.content_rect = [[],[],[]]
        for i in range(len(self.content)) : 
            for j in range(len(self.content[0])) :
                tmp = self.content[i][j].game_start.img_rect
                self.content_rect[i].append(tmp)

        center = len(self.content) // 2
        self.content_rect[center][center].centerx = self.bg_table_rect.centerx 
        self.content_rect[center][center].centery = self.bg_table_rect.centery
        self.content[center][center].set_position()

        dx = [1, -1, 0, 0, 1, -1, 1, -1]
        dy = [1, 1, 1, -1, -1, -1, 0, 0]

        self.content[0][0].isOpen = True

        for i in range(8) : 
            self.content_rect[center + dx[i]][center + dy[i]].centerx = self.content_rect[center][center].centerx + 120 * dx[i]
            self.content_rect[center + dx[i]][center + dy[i]].centery = self.content_rect[center][center].centery + 120 * dy[i]
            self.content[center + dx[i]][center + dy[i]].set_position()

        


        







    

