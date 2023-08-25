
    def update_screen(self) : 
        self.state_stack[-1].render()
        self.state_stack[-1].update()


    def check_event(self) : 
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT : 
                self.running = False    
                sys.exit()
           

    # load asset
    def load_asset(self) : 