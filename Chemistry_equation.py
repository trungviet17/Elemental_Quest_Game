import pygame
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
        
        
        self.target = self.level.level_target

        # aboard
        self.aboard = Aboard(self)

        # running 
        self.running = True
        self.stage = 0
        # element of game on dashboard
        self.elements = {}

        self.element_board_long = self.aboard.element_up_but.img_rect.centery - self.aboard.element_down_but.img_rect.centery
        self.element_board_indx = 0

        
        self.default_element()
        #self.set_target()
        
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
       
        self.update_equation_table()

        self.aboard.draw()
        
    # TODO : update it 
    # print element to dashboard 
    def element_draw_todash(self) : 
        end =   min(len(self.element_in_board), self.element_board_indx + 4) 
        for i in range(self.element_board_indx, end ) : 
            self.element_in_board[i].img_to_scr_rect.centerx = self.aboard.element_down_but.img_rect.centerx
            self.element_in_board[i].img_to_scr_rect.centery = self.aboard.element_up_but.img_rect.centery - (i + 1 - self.element_board_indx) * self.element_board_long // 5
            self.element_in_board[i].draw()
            self.element_in_board[i].draw_infor(self.elements[self.element_in_board[i].tag_name])

    # print element to equa
    def element_draw_toequ(self) : 
        for i in range(len(self.element_in_equa)) : 
            self.element_in_equa[i].img_to_scr_rect.centerx = self.setting.equation_position[i][0]
            self.element_in_equa[i].img_to_scr_rect.centery = self.setting.equation_position[i][1]
            pygame.draw.line(self.screen, self.setting.start_button_color, self.aboard.start.img_rect.center, (self.setting.equation_position[i][0],self.setting.equation_position[i][1]), 4) 
            self.element_in_equa[i].draw()  
            


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
        

        if (self.aboard.element_up_but.action and self.element_board_indx - 1 >= 0) : 
            self.element_board_indx -= 1
           

        if (self.aboard.element_down_but.action and self.element_board_indx + 4 < len(self.element_in_board)) : 
            self.element_board_indx += 1
           
        

        self.element_draw_todash()
        self.update_element_dash_equa()
        self.element_draw_toequ()
        
        self.update_element_equa_dash()
        self.check_combine_element()
        self.element_draw_toequ()
        self.element_draw_todash()

    # TODO: FIX IT 
    # update element 
    def update_element_equa_dash(self) : 
        if len(self.element_in_equa) == 0 : return 
        for i in self.element_in_equa :
            if i.action : 
                if (i.tag_name not in self.elements or self.elements[i.tag_name] <= 0) : 
                    self.element_in_board.insert(self.element_board_indx,i)
                    self.elements[i.tag_name] = 1
                else : self.elements[i.tag_name] += 1 
                self.element_in_equa.remove(i)
                return
            
    def update_element_dash_equa(self) : 
        if len(self.element_in_board) == 0 : return 
        for i in self.element_in_board : 
            if i.action : 
                self.element_in_equa.insert(0, i)
                if (self.elements[i.tag_name] == 1) : self.element_in_board.remove(i)
                self.elements[i.tag_name] -= 1
                return
                

    
   
    # check the new element after click start  
    def check_combine_element(self) : 
        if (len(self.element_in_equa) == 0) : return

        if (self.aboard.start.action) : 
            if (self.game_logic.check_for_new_element(self)) : 
                self.element_in_equa.clear()
                for i in self.game_logic.name_after_combine : 
                    if i not in self.elements : 
                        self.elements[i] = 1
                        e = Element(i, self)
                        self.element_in_board.insert(0,  e)
                    else : 
                        self.elements[i] += 1

            else : 
                for i in self.element_in_equa : 
                    if (i.tag_name not in self.elements or self.elements[i.tag_name] == 0) :
                        self.element_in_board.insert(0,  i)
                        self.elements[i.tag_name] = 1
                    else : 
                        self.elements[i.tag_name] += 1
                self.element_in_equa.clear()

    # TODO : check result 
    def check_result(self, element) : 
        if (element.tag_name in self.target) : 
            self.target.remove(element.tag_name)

            
   



    def update(self) : 
        pass




