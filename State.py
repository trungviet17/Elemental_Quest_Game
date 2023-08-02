
class State : 
    def __init__(self, game) : 
        self.game = game
        self.prev_game = None
        self.setting = game.setting
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

    def update(self) : 
        pass 

    def render(self, surface) : 
        pass 

    def enter_state(self) : 
        if (len(self.game.state_stack) > 1) : 
            self.prev_game = self.game.state_stack[-1]
        self.game.state_stack.append(self) 

    def exit_state(self) : 
        self.game.state_stack.pop()

    