import pygame.font
from State import State 
from Button import Title_Button
from Chemistry_equation import Chemistry_game
# Surface của button và title có thể xảy ra lỗi khi được truyền vào 2 biến khác nhau

class Title(State) : 
    def __init__(self, game) : 
        State.__init__(self, game)
        self.play_button = Title_Button(0, 0, self.setting.play_button, self.screen)
        self.about_button = Title_Button(0, 0, self.setting.about_button, self.screen)
        self.setting_button = Title_Button(0, 0, self.setting.setting_button, self.screen)
        self.prize_button = Title_Button(0, 0, self.setting.prize_button, self.screen)
        self.leader_button = Title_Button(0, 0, self.setting.leader_button, self.screen)
        self.surface_rect = self.screen.get_rect()
        
        
    def update(self):
        if self.play_button.isPress : 
            ai = Chemistry_game(self.game)
            ai.enter_state()
            self.play_button.isPress = False

    def render(self):
        #surface_rect = surface.get_rect()
        self.surface_rect = self.screen.get_rect()
        # setting play_button 
        self.play_button.img_rect.centerx = self.surface_rect.centerx
        self.play_button.img_rect.centery = self.surface_rect.centery + 150

        # setting about_button 
        self.about_button.img_rect.right = self.surface_rect.right - 20
        self.about_button.img_rect.top = self.surface_rect.top + 20 

        # #setting button 
        self.setting_button.img_rect.right = self.surface_rect.right - 20 
        self.setting_button.img_rect.bottom = self.surface_rect.bottom - 20

        # prize button 
        self.prize_button.img_rect.left = self.surface_rect.left + 20
        self.prize_button.img_rect.top = self.surface_rect.top + 20

        # leader button 
        self.leader_button.img_rect.left = self.surface_rect.left + 20 
        self.leader_button.img_rect.bottom = self.surface_rect.bottom - 20


        self.screen.blit(self.game.title_img, (0, 0))
        self.play_button.draw()
        self.about_button.draw()
        self.leader_button.draw()
        self.prize_button.draw()
        self.setting_button.draw()
        
    


    
        

