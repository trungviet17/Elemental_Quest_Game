import pygame


class Background_Scrolling : 
    def __init__(self, game) : 
        self.screen = game.screen 
        self.back_ground_lst = []
        self.back_ground_sc1 = pygame.image.load('res\\backgound\\Scrolling\\sky.png').convert_alpha()
        self.back_ground_lst.append(self.back_ground_sc1)
        self.back_ground_sc2 = pygame.image.load('res\\backgound\\Scrolling\\rocks_1.png').convert_alpha()
        self.back_ground_lst.append(self.back_ground_sc2)
        self.back_ground_sc3 = pygame.image.load('res\\backgound\\Scrolling\\rocks_2.png').convert_alpha()
        self.back_ground_lst.append(self.back_ground_sc3)
        self.back_ground_sc4 = pygame.image.load('res\\backgound\\Scrolling\\clouds_1.png').convert_alpha()
        self.back_ground_lst.append(self.back_ground_sc4)
        self.back_ground_sc5 = pygame.image.load('res\\backgound\\Scrolling\\clouds_2.png').convert_alpha()
        self.back_ground_lst.append(self.back_ground_sc5)
        self.back_ground_sc6 = pygame.image.load('res\\backgound\\Scrolling\\clouds_3.png').convert_alpha()
        self.back_ground_lst.append(self.back_ground_sc6)
        self.back_ground_sc7 = pygame.image.load('res\\backgound\\Scrolling\\clouds_4.png').convert_alpha()
        self.back_ground_lst.append(self.back_ground_sc7)

        self.clock = pygame.time.Clock()
        self.bg_width = self.back_ground_sc1.get_width()
        self.scroll = 0 

    def draw(self) : 
        self.scroll += 1
        for k in range(0, 20) : 
            speed = 1
            for i in self.back_ground_lst : 
                self.screen.blit(i, (k * self.bg_width - self.scroll * speed, 0))
                speed += 0.1
        if (self.scroll * speed > 5 * self.bg_width) : self.scroll = 0
    

        