import pygame
from State import State 
from Button import Title_Button
from Chemistry_equation import Chemistry_game
from Background_Scrolling import Background_Scrolling
from About_title import About_title
from Setting_title import Setting_title
# Surface của button và title có thể xảy ra lỗi khi được truyền vào 2 biến khác nhau

class Title(State) : 
    def __init__(self, game) : 
        State.__init__(self, game)
        self.play_button = Title_Button(0, 0, self.setting.play_button, self.screen,0.3)
        self.about_button = Title_Button(0, 0, self.setting.about_button, self.screen, 0.3)
        self.setting_button = Title_Button(0, 0, self.setting.setting_button, self.screen, 0.3)
        self.prize_button = Title_Button(0, 0, self.setting.prize_button, self.screen, 0.3)
        self.leader_button = Title_Button(0, 0, self.setting.leader_button, self.screen, 0.3)
        self.surface_rect = self.screen.get_rect()
        self.title = self.setting.title
        self.background = Background_Scrolling(game)

        self.set_position()
        
        
    def update(self):
        if self.play_button.isPress : 
            ai = Chemistry_game(self.game)
            ai.enter_state()
            self.play_button.isPress = False
        elif self.about_button.isPress : 
            about = About_title(self.game)
            about.enter_state()
            self.about_button.isPress = False
        elif self.setting_button.isPress : 
            setting = Setting_title(self.game)
            setting.enter_state()
            self.setting_button.isPress = False

    def render(self):
        
        self.background.draw()
        self.screen.blit(self.title, self.title_rect)
        self.play_button.draw()
        self.about_button.draw()
        self.leader_button.draw()
        self.prize_button.draw()
        self.setting_button.draw()


    def set_position(self) : 
        #surface_rect = surface.get_rect()
        self.surface_rect = self.screen.get_rect()
        
        # setting play_button 
        self.play_button.img_rect.centerx = self.surface_rect.centerx
        self.play_button.img_rect.centery = self.surface_rect.centery + 150

        # setting about_button 
        self.about_button.img_rect.right = self.surface_rect.right - 40
        self.about_button.img_rect.top = self.surface_rect.top + 40 

        # #setting button 
        self.setting_button.img_rect.right = self.surface_rect.right - 40 
        self.setting_button.img_rect.bottom = self.surface_rect.bottom - 40

        # prize button 
        self.prize_button.img_rect.left = self.surface_rect.left + 40
        self.prize_button.img_rect.top = self.surface_rect.top + 40

        # leader button 
        self.leader_button.img_rect.left = self.surface_rect.left + 40 
        self.leader_button.img_rect.bottom = self.surface_rect.bottom - 40

        self.title_rect = self.title.get_rect()
        self.title_rect.centerx = self.surface_rect.centerx
        self.title_rect.centery = self.surface_rect.centery - 120
        
    


    
        

