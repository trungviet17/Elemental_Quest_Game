import pygame
import sys
from Setting import Setting
from Element import Element
from Start_button import Start_button
from Game_Logic import Game_Logic



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
        

        
        
    def game_play(self) : 
        while(True) : 
            # check event 
            self.check_event()

            #setting screen  
            self.update_screen()
            
            #element update
            self.elements_update()
             
            pygame.display.flip()

    # check event from player
    def check_event(self) : 
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT :
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                mouse_pos = pygame.mouse.get_pos()
                self.check_element_onclick(mouse_pos)
                self.check_equation_table_onclick(mouse_pos)
                self.check_combine_element(mouse_pos)

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
        self.start.draw()

        # init dash board 
        self.dash_board.fill(self.setting.dash_color)

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

    #check 
    def check_combine_element(self, mouse_pos) : 
        mouse_x, mouse_y = mouse_pos
        pos_x, pos_y = self.setting.start_button_center
        if (((pos_x - mouse_x)**2 + (pos_y - mouse_y)**2 <= self.setting.start_button_rad **2) ) :
            if (self.game_logic.check_for_new_element(self)) : 
                self.element_for_equa.empty()
                for i in self.game_logic.name_after_combine : 
                    e = Element(i, self)
                    self.elements.add(e)
            else : 
                for i in self.element_for_equa.sprites() : 
                    self.elements.add(i)
                self.element_for_equa.empty()


if __name__ == '__main__' : 
    ai = Chemistry_game()
    ai.game_play()