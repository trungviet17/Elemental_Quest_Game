import pygame


class Background_Scrolling : 
    def __init__(self, game, num) : 
        self.screen = game.screen 
        self.setting = game.setting
        self.back_ground_lst = self.setting.bg_lst[num]
        for i in range(len(self.back_ground_lst)) : 
            self.back_ground_lst[i] = self.back_ground_lst[i].convert_alpha()

        self.clock = pygame.time.Clock()
        self.bg_width = self.back_ground_lst[0].get_width()
        self.scroll = 0 

    def draw(self) : 
        self.scroll += 1.5
        for k in range(10) : 
            speed = 1.5
            for i in self.back_ground_lst : 
                self.screen.blit(i, (k * self.bg_width - int(self.scroll * speed), 0))
                speed += 0.5
        if (self.scroll * speed > 10 * self.bg_width) : self.scroll = 0
    

        