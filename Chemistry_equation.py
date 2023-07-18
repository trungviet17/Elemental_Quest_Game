import pygame
import sys
from Setting import Setting
from Element import Element
from Start_button import Start_button
from Game_Logic import Game_Logic
from aboard import Aboard
from Winner_table import Winner_table


class Chemistry_game : 

    def __init__(self) :
        pygame.init()
        
        # setting attribute of game 
        self.setting = Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Chemistry Demo Game")
        self.back_ground = pygame.image.load('back_ground.png').convert()

        # dash board 
        self.dash_board = self.screen.subsurface(pygame.Rect(self.setting.change_dtosc_x, self.setting.change_dtosc_y, self.setting.dash_width, self.setting.dash_height))

        # element of game on dashboard
        self.elements = pygame.sprite.Group()
        self.default_element()

        # element of game on 
        self.element_for_equa = pygame.sprite.Group()

        # start button 
        self.start = Start_button(self)

        # check game logic 
        self.game_logic = Game_Logic()
        
        # target element 
        self.target = "H2SO3"
        self.aboard = Aboard(self)

        # running 
        self.running = True

        # winner notice 
        self.winner_table = self.screen.subsurface(pygame.Rect(self.setting.winner_toscr_x, self.setting.winner_toscr_y, self.setting.winner_width, self.setting.winner_height))
        
        self.winner = Winner_table(self)

        
    def game_play(self) : 
        while(True) : 

            # check event 
            self.check_event()

            #setting screen  
            self.update_screen()

        
            if (self.running) : 
                #element update
                self.elements_update()
            else : 
                self.winning_notice()

            pygame.display.flip()

    # check event from player
    def check_event(self) : 
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT :
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN :
                mouse_pos = pygame.mouse.get_pos()
                if self.running : 
                    self.check_element_onclick(mouse_pos)
                    self.check_equation_table_onclick(mouse_pos)
                    self.check_combine_element(mouse_pos)
                else : 
                    self.check_winning_next_button(mouse_pos)
                    self.check_winning_quit_button(mouse_pos)
                


    # click to element
    def check_element_onclick(self, mouse_pos) : 
        mouse_x, mouse_y = mouse_pos
        for i in self.elements.sprites() : 
            e_x, e_y = i.center_point
            if ((e_x + self.setting.change_dtosc_x - mouse_x)**2 + (e_y + self.setting.change_dtosc_y - mouse_y)**2 <= self.setting.element_rad **2) : 
                #i.onclick = True
                self.element_for_equa.add(i)
                self.elements.remove(i)

    # update screen 
    def update_screen(self) : 
        # init background
        #self.screen.fill(self.setting.bg_color)
        self.screen.blit(self.back_ground, (0,0))

        self.update_equation_table()
        # init start button
        if(self.running) : self.start.draw()

        self.aboard.prep_score()
        self.aboard.showing()
        # init dash board 
        if (self.running) : self.dash_board.fill(self.setting.dash_color)

    # print element to dashboard 
    def elements_update(self) : 
        max_element = self.setting.dash_width / self.setting.element_distance 
        pos_y = self.setting.dash_height // 2
        pos_x = 50
        if (len(self.elements) < max_element) : 
            for i in self.elements.sprites() : 
                i.draw(pos_x, pos_y, self.dash_board)
                pos_x += 100
                
    # default_element          
    def default_element(self) : 
        for i in self.setting.element_content : 
            e = Element(i, self)
            self.elements.add(e)


    # add element to equation table 
    def update_equation_table(self) : 
        for i in range( len(self.element_for_equa.sprites()) ) : 
            new_position = (self.setting.equation_position[i][0], self.setting.equation_position[i][1])
            pygame.draw.line(self.screen, self.setting.start_button_color, self.setting.start_button_center, new_position, 6)
            self.element_for_equa.sprites()[i].draw(self.setting.equation_position[i][0], self.setting.equation_position[i][1], self.screen)


    # remove element from equation table 
    def check_equation_table_onclick(self, mouse_pos) : 
        mouse_pos_x, mouse_pos_y = mouse_pos
        for i in self.element_for_equa.sprites() : 
            e_x, e_y = i.center_point
            if ((e_x - mouse_pos_x) ** 2 + (e_y - mouse_pos_y)**2 <= self.setting.element_rad** 2 ) : 
                self.elements.add(i)
                self.element_for_equa.remove(i)

    # check the new element after click start  
    def check_combine_element(self, mouse_pos) : 
        mouse_x, mouse_y = mouse_pos
        pos_x, pos_y = self.setting.start_button_center
        if (((pos_x - mouse_x)**2 + (pos_y - mouse_y)**2 <= self.setting.start_button_rad **2) ) :
            if (self.game_logic.check_for_new_element(self)) : 
                self.element_for_equa.empty()
                self.aboard.score += len(self.game_logic.name_after_combine) * 100
                for i in self.game_logic.name_after_combine : 
                    # find target element 
                    e = Element(i, self)
                    self.elements.add(e)
                    if (i == self.target) : self.running = False
            else : 
                for i in self.element_for_equa.sprites() : 
                    self.elements.add(i)
                self.element_for_equa.empty()


    def winning_notice(self) : 
        self.winner_table.fill(self.setting.winner_color)
        self.winner.showing()


    def check_winning_next_button(self, mouse_pos) : 
        if self.winner.next_button_rect.collidepoint(mouse_pos) : 
            self.running = True


    def check_winning_quit_button(self, mouse_pos) : 
        mouse_pos = self.change_mouse_pos(mouse_pos)
        print(mouse_pos)
        if self.winner.quit_button_rect.collidepoint(mouse_pos) : 
            sys.exit()

    def change_mouse_pos(self, mouse_pos) : 
        mouse_pos_x, mouse_pos_y = mouse_pos
        print(mouse_pos)
        return (mouse_pos_x - self.setting.winner_toscr_x, mouse_pos_y - self.setting.winner_toscr_y)


if __name__ == '__main__' : 
    ai = Chemistry_game()
    ai.game_play()