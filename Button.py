import pygame

class Button : 
    def __init__(self, x, y, img, surface) : 
        self.width = img.get_width()
        self.height = img.get_height()
        self.screen = surface
        self.img = img
        self.img_rect = img.get_rect()
        self.img_rect.topleft = (x,y)
        self.isPress = False


   


    def draw(self) : 
        pos = pygame.mouse.get_pos()

        if self.img_rect.collidepoint(pos) : 
            if pygame.mouse.get_pressed()[0] == 1 : self.isPress = True
            scaled_width = int(self.width * 1.2)
            scaled_height = int(self.height * 1.2)
            img_scacle = pygame.transform.scale(self.img, (scaled_width, scaled_height))
            self.screen.blit(img_scacle, ((self.img_rect.left + self.img_rect.right - scaled_width) // 2, (self.img_rect.top + self.img_rect.bottom - scaled_height) // 2))
        else : 
            self.screen.blit(self.img, self.img_rect)


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