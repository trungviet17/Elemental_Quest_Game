import pygame

class Title_Button : 
    def __init__(self, x, y, img, surface, scale) : 
        self.width = img.get_width()
        self.height = img.get_height()
        self.screen = surface
        self.img = img
        self.scale = scale
        self.img_to_screen = pygame.transform.scale(self.img, (int(self.width * scale), int(self.height * scale)))
        self.img_rect = self.img_to_screen.get_rect()
        self.img_rect.topleft = (x,y)
        self.isPress = False
        self.scaled_width = int(self.width * (self.scale + 0.05))
        self.scaled_height = int(self.height * (self.scale + 0.05))
        self.img_scacle = pygame.transform.scale(self.img, (self.scaled_width, self.scaled_height))

    def set_img(self, img) : 
        self.img = img
        self.img_to_screen = pygame.transform.scale(self.img, (int(self.width * self.scale), int(self.height * self.scale)))
        self.img_scacle = pygame.transform.scale(self.img, (self.scaled_width, self.scaled_height))

    def draw(self) : 
        pos = pygame.mouse.get_pos()

        if self.img_rect.collidepoint(pos) : 
            self.screen.blit(self.img_scacle, ((self.img_rect.left + self.img_rect.right - self.scaled_width) // 2, (self.img_rect.top + self.img_rect.bottom - self.scaled_height) // 2))
            if pygame.mouse.get_pressed()[0] == 1 : self.isPress = True
            else : self.isPress = False
        else : 
            self.screen.blit(self.img_to_screen, self.img_rect)
            self.isPress = False


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




