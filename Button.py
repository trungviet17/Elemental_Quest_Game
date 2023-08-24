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
            


class Start_button(Title_Button) : 

    def __init__(self,x, y, img, surface, scale, img2) :
        Title_Button.__init__(self, x, y, img, surface, scale)
        self.trans_img = img2
        self.ori_img = img

    def draw(self):
        pos = pygame.mouse.get_pos()
        self.action = False

        if self.img_rect.collidepoint(pos) : 
            if pygame.mouse.get_pressed()[0] == 1 and self.isPress == False : 
                self.action = True
                self.isPress = True
                self.set_img(self.trans_img)
            if pygame.mouse.get_pressed()[0] == 0 : 
                self.isPress = False
                self.set_img(self.ori_img)
        self.screen.blit(self.img_to_screen, self.img_rect)
        
    



