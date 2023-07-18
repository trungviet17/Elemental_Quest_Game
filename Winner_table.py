import pygame.font

class Winner_table : 
    def __init__(self, c_game) : 
        self.setting = c_game.setting 
        self.screen = c_game.winner_table
        self.rect = c_game.winner_table.get_rect()
        
        self.winner_content = "Winner !!!"
        self.winner_content_color = (255, 153, 204)
        self.button_color = (204, 255, 153)
        self.prep_header()
        self.prep_next_playbutton()
        self.prep_quit_button()
    
    def prep_header(self) : 
        self.header_font = pygame.font.SysFont(None, 96)
        self.header_text = self.header_font.render("Winner!!!", True, self.winner_content_color)

        self.header_rect = self.header_text.get_rect()
        self.header_rect.top = self.rect.top + 20
        self.header_rect.centerx = self.rect.centerx

    def prep_next_playbutton (self) : 
        self.next_button_font = pygame.font.SysFont(None, 36)
        self.next_button_text = self.next_button_font.render("Next level", True,self.winner_content_color)
        self.next_button_text_rect = self.next_button_text.get_rect()

        self.next_button_rect = pygame.Rect(0, 0, self.setting.winner_button_width, self.setting.winner_button_height)
        self.next_button_rect.bottom = self.rect.bottom - 20 
        self.next_button_rect.right = self.rect.right - 30
        self.next_button_text_rect.center = self.next_button_rect.center

    def prep_quit_button(self) : 
        self.quit_button_font = pygame.font.SysFont(None, 36)
        self.quit_button_text = self.quit_button_font.render("Quit", True, self.winner_content_color)
        self.quit_button_text_rect = self.quit_button_text.get_rect()

        self.quit_button_rect = pygame.Rect(0, 0, self.setting.winner_button_width, self.setting.winner_button_height)
        self.quit_button_rect.bottom = self.rect.bottom - 20
        self.quit_button_rect.left = self.rect.left + 30 
        self.quit_button_text_rect.center = self.quit_button_rect.center

    def showing(self) : 
        self.screen.blit(self.header_text, self.header_rect )
        self.screen.fill(self.button_color, self.next_button_rect)
        self.screen.blit(self.next_button_text, self.next_button_text_rect)

        self.screen.fill(self.button_color, self.quit_button_rect)
        self.screen.blit(self.quit_button_text, self.quit_button_text_rect)

         


