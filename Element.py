from pygame.sprite import Sprite
import pygame 
import pygame.font
"""  The element class can do:
    - Round shape, color, with chemical name written on it
    - Subclass of Sprite . class
"""
class Element(Sprite) : 
    
    def __init__(self, c_tag, c_game) :
        super().__init__()
        self.screen = c_game.screen 
        self.screen_rect = c_game.screen.get_rect()
        
        self.dash_board_screen = c_game.dash_board
        self.setting = c_game.setting

        # setting font and img
        self.font = pygame.font.SysFont(None, 30)
        self.text = self.font.render(c_tag, True, self.setting.element_text_color)
        #self.onclick = False
        self.center_point = (0, 0)
        self.text_rect = self.text.get_rect(center = self.center_point)
        
        # setting 
        self.tag_name = c_tag

    def draw(self, x, y, screen) : 
        self.center_point = (x, y)
        self.text_rect = self.text.get_rect(center = (x, y))
        pygame.draw.circle(screen, self.setting.element_color, (x, y), self.setting.element_rad)
        screen.blit(self.text, self.text_rect)
        
