import pygame.font

class Start_button : 

    def __init__(self, c_game) : 
        self.screen = c_game.screen 
        self.setting = c_game.setting

        self.font = pygame.font.SysFont(None, 48)
        self.text = self.font.render("Start", True, self.setting.start_button_text_color)
        self.onclick = False
        self.text_rect = self.text.get_rect(center = self.setting.start_button_center)

    def draw(self) : 
        pygame.draw.circle(self.screen, self.setting.start_button_color, self.setting.start_button_center, self.setting.start_button_rad)
        self.screen.blit(self.text, self.text_rect)
