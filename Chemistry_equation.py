import pygame
import sys
from Element import Element
from Button import Title_Button
from Game_Logic import Game_Logic
from aboard import Aboard
from Winner_table import Winner_table
from State import State
from Level import Level
import random

"""
- State game play 
    - Đầu vào là dữ liệu từ level 
    - Tính toán điểm, sao cho game 
    - Bổ trợ thêm phép bổ trợ cho game 
    - Pause game 
    - Bộ đếm thời gian
"""

class Chemistry_game(State) : 

    def __init__(self, game, level) :
        State.__init__(self, game)
        self.game = game
        bgr_img = random.randint(0, len(self.setting.back_ground) - 1)
        self.back_ground = self.setting.back_ground[bgr_img]
        # game data 
        self.level = level
        # element of game on 
        self.element_in_equa = []
        self.element_in_board = []

        # check game logic 
        self.game_logic = Game_Logic()
        
        # target element 
        self.target = self.level.level_target

        # aboard
        self.aboard = Aboard(self)

        # running 
        self.running = True

        # element of game on dashboard
        self.elements = {}

    
        self.default_element()
        
    def render(self) : 
        # check event 
        self.check_event()

        #setting screen  
        self.update_screen()

        


    # check event from player
    def check_event(self) : 
        pass
                
                

    
    # update screen 
    def update_screen(self) : 
        # init background
        self.screen.blit(self.back_ground, (0,0))

        self.update_equation_table()
       
        
        self.aboard.draw()
        
       
    # print element to dashboard 
    def elements_update(self) : 
        pass
                
    # default_element          
    def default_element(self) : 
        for i in self.setting.element_content[int(self.aboard.game_level) - 1] : 
            if i in self.elements : 
                self.elements[i] += 1
            else : 
                e = Element(i, self)
                self.elements[i] = 1
                self.element_in_board.append(e)
        


    # add element to equation table 
    def update_equation_table(self) : 
        # for i in range( len(self.element_for_equa.sprites()) ) : 
        #     new_position = (self.setting.equation_position[i][0], self.setting.equation_position[i][1])
        #     pygame.draw.line(self.screen, self.setting.start_button_color, self.setting.start_button_center, new_position, 6)
        #     self.element_for_equa.sprites()[i].draw(self.setting.equation_position[i][0], self.setting.equation_position[i][1], self.screen)
        pass

    # remove element from equation table 
    def check_equation_table_onclick(self, mouse_pos) : 
        pass

    
    # TODO : FIX IT 
    # check the new element after click start  
    def check_combine_element(self, mouse_pos) : 
        # mouse_x, mouse_y = mouse_pos
        # pos_x, pos_y = self.setting.start_button_center
        # if (((pos_x - mouse_x)**2 + (pos_y - mouse_y)**2 <= self.setting.start_button_rad **2) ) :
        #     if (self.game_logic.check_for_new_element(self)) : 
        #         self.element_for_equa.empty()
        #         self.aboard.score += len(self.game_logic.name_after_combine) * 100
        #         for i in self.game_logic.name_after_combine : 
        #             e = Element(i, self)
        #             self.elements.add(e)
        #             if (i == self.target) : self.running = False
        #         # clear all game_logic
        #         self.game_logic.name_after_combine.clear()
        #     else : 
        #         for i in self.element_for_equa.sprites() : 
        #             self.elements.add(i)
        #         self.element_for_equa.empty()
        pass


   
    # TODO : FIX IT 
    def change_mouse_pos(self, mouse_pos) : 
        pass
    

    def update(self) : 
        pass




# if __name__ == '__main__' : 
#     ai = Chemistry_game()
#     ai.game_play()