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
        self.action = False

    def set_img(self, img) : 
        self.img = img
        self.img_to_screen = pygame.transform.scale(self.img, (int(self.width * self.scale), int(self.height * self.scale)))
        self.img_scacle = pygame.transform.scale(self.img, (self.scaled_width, self.scaled_height))

    def draw(self) : 
        pos = pygame.mouse.get_pos()
        self.action = False

        if self.img_rect.collidepoint(pos) : 
            self.screen.blit(self.img_scacle, ((self.img_rect.left + self.img_rect.right - self.scaled_width) // 2, (self.img_rect.top + self.img_rect.bottom - self.scaled_height) // 2))
            if pygame.mouse.get_pressed()[0] == 1 and self.isPress == False : 
                self.action = True
                self.isPress = True
            if pygame.mouse.get_pressed()[0] == 0 : self.isPress = False
        else : 
            self.screen.blit(self.img_to_screen, self.img_rect)
            


class Start_button : 

    def __init__(self, c_game) : 
        self.screen = c_game.screen 
        self.setting = c_game.setting

        self.font = pygame.font.SysFont(None, 48)
        self.text = self.font.render("Start", True, self.setting.start_button_text_color)
        self.onclick = False
        self.text_rect = self.text.get_rect()

        self.scale = 0.5
        self.bg = pygame.transform.scale(self.setting.element_simp_rect, (int(self.setting.element_simp_rect.get_width() * self.scale), int(self.setting.element_simp_rect.get_height() * self.scale)))

        self.set_position()
    def draw(self) : 
        

        self.screen.blit(self.bg, self.bg_rect)
        self.screen.blit(self.text, self.text_rect)

    def set_position(self) : 
        screen_rect = self.screen.get_rect()
        self.bg_rect = self.bg.get_rect()
        self.bg_rect.center = screen_rect.center

        self.text_rect.center = self.bg_rect.center



