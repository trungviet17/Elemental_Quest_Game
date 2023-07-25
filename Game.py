import sys, time, pygame
from Setting import Setting 
from Title import Title
class Game : 
    def __init__(self) : 
        pygame.init()
        self.setting = Setting()
        self.state_stack = []
        self.running = True
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Chemistry Alchemy")
        self.load_asset()
        self.load_state()

    # game loop 
    def game_loop(self) : 
        while(self.running) : 
            self.check_event() 
            self.update_screen()

            pygame.display.flip()


    def update_screen(self) : 
        self.state_stack[-1].render()
        self.state_stack[-1].update()


    def check_event(self) : 
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT : 
                self.running = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP : 
                mouse_pos = pygame.mouse.get_pos()

            elif event.type == pygame.MOUSEBUTTONDOWN : 
                mouse_pos = pygame.mouse.get_pos()

    # load asset
    def load_asset(self) : 
        self.title_img = pygame.image.load('res\\backgound\\background_4.png').convert()
        
        

    def load_state(self) : 
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)


if __name__ == '__main__' : 
    g = Game()
    g.game_loop()