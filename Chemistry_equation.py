import pygame
import sys
from Element import Element
from Button import Title_Button
from Game_Logic import Game_Logic
from aboard import Aboard
from Winner_table import Winner_table
from State import State
from Level import Level
from Background_Scrolling import Background_Scrolling
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
        bgr_img = random.randint(1, len(self.setting.bg_lst) - 1)
        self.back_ground = Background_Scrolling(self, bgr_img)
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

        self.element_board_long = self.aboard.element_up_but.img_rect.centery - self.aboard.element_down_but.img_rect.centery
        self.element_board_indx = 0

    
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
        self.back_ground.draw()

        self.element_draw(self.element_board_indx)
        self.update_equation_table()
       
        
        self.aboard.draw()
        
       
    # print element to dashboard 
    def element_draw(self, indx) : 
        end =   min(len(self.element_in_board), indx + 4) 
        for i in range(indx, end ) : 
            self.element_in_board[i].img_to_scr_rect.centerx = self.aboard.element_down_but.img_rect.centerx
            self.element_in_board[i].img_to_scr_rect.centery = self.aboard.element_up_but.img_rect.centery - (i + 1 - indx) * self.element_board_long // 5
            self.element_in_board[i].draw()
                
    # default_element          
    def default_element(self) : 
        for i in self.level.level_element : 
            if i in self.elements : 
                self.elements[i] += 1
            else : 
                e = Element(i, self)
                self.elements[i] = 1
                self.element_in_board.append(e)
        


    # all update of element
    def update_equation_table(self) : 
        # for i in range( len(self.element_for_equa.sprites()) ) : 
        #     new_position = (self.setting.equation_position[i][0], self.setting.equation_position[i][1])
        #     pygame.draw.line(self.screen, self.setting.start_button_color, self.setting.start_button_center, new_position, 6) 
        #     self.element_for_equa.sprites()[i].draw(self.setting.equation_position[i][0], self.setting.equation_position[i][1], self.screen)
        self.update_element(self.element_in_board, self.element_in_equa)
        if (self.aboard.element_up_but.action and self.element_board_indx - 1 >= 0) : 
            self.element_board_indx -= 1

        if (self.aboard.element_down_but.action and self.element_board_indx + 4 < len(self.element_in_board)) : 
            self.element_board_indx += 1

        self.element_draw(self.element_board_indx)

    def update_element(self, arr1, arr2) : 
        if len(arr1) == 0 : return 
        for i in arr1 :
            if i.action : 
                arr2.append(i) 
                arr1.remove(i)
                

    
    # TODO : FIX IT 
    # check the new element after click start  
    def check_combine_element(self, mouse_pos) : 
        pass


    def update(self) : 
        pass




