import pygame
class Setting : 
    def __init__(self) : 
        #screen setting 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (153, 255, 204)
        
        # dashbroad 
        self.dash_height = 100
        self.dash_width = 1100 
        self.dash_color = (204, 255, 255)

        # change dashboard -> screen 
        self.change_dtosc_x = 50 
        self.change_dtosc_y = self.screen_height - self.dash_height - 50
        
        # Elemet 
        self.element_rad = 40 
        self.element_color = (204, 204, 255)
        self.element_content = [["NaOH", "MgSO4", "SO3", "HCl", "CO2", "KNO3", "NaCl", "MgCl2"], ['H2', 'CO2']]
        self.element_distance = 50
        self.element_text_color = (255, 255, 255)

        # equation dashboard 
        self.equation_dashboard_rad = 250
        self.equation_dashboard_color = (255, 153 , 153)

        # level of game 
        self.target = ["Na2SO4", "HNO3", "SO2"]

        # start button 
        self.start_button_rad = 50 
        self.start_button_center = (600, 300)
        self.start_button_color = (128, 128, 128)
        self.start_button_text_color = (255, 253, 204)

        self.init_equation_dasboard()

        # winner table 
        self.winner_height = 300
        self.winner_width = 600
        self.winner_toscr_x = 300
        self.winner_toscr_y = 200
        self.winner_color = (204, 229, 255)

        self.winner_button_height = 60
        self.winner_button_width = 140


        # title setting
        self.title_header_text_color = (204, 255, 255)


        # dictionary setting
        self.dictionary_table_height = 600
        self.dictionary_table_width = 600
        

        ''' loading asset  '''
        # title asset 
        self.play_button = pygame.image.load('res\\menu\\play.png')
       
        self.about_button = pygame.image.load('res\\menu\\about.png')

        self.setting_button = pygame.image.load('res\\menu\\setting.png')

        self.prize_button = pygame.image.load('res\\menu\\prize.png')

        self.leader_button = pygame.image.load('res\\menu\\leader.png')

        self.title = pygame.image.load('res\\backgound\\Title.png')


        # background_loading 
        self.back_ground_1 = pygame.image.load('res\\backgound\\background_1.png')
        self.back_ground_2 = pygame.image.load('res\\backgound\\background_2.png')
        self.back_ground_3 = pygame.image.load('res\\backgound\\background_3.png')
        self.back_ground_4 = pygame.image.load('res\\backgound\\background_4.png')
        self.back_ground_5 = pygame.image.load('res\\backgound\\background_5.png')
        self.back_ground_6 = pygame.image.load('res\\backgound\\background_6.png')


        # title state loading 
        self.close_2 = pygame.image.load('res\\title_state\\close_2.png')
        self.bg = pygame.image.load('res\\title_state\\bg.png')
        self.table = pygame.image.load('res\\title_state\\table.png')
        self.content_button = pygame.image.load('res\\title_state\\about_state\\btn.png')

        # setting state loading 
        self.setting_header = pygame.image.load('res\\title_state\\settings\\92.png')
        self.setting_sound_1 = pygame.image.load('res\\title_state\\settings\\93.png')
        self.setting_sound_2 = pygame.image.load('res\\title_state\\settings\\94.png')
        self.setting_off = pygame.image.load('res\\title_state\\settings\\95.png')
        self.setting_on = pygame.image.load('res\\title_state\\settings\\96.png')
        self.setting_plus = pygame.image.load('res\\title_state\\settings\\97.png')
        self.setting_subtract = pygame.image.load('res\\title_state\\settings\\98.png')

        # prizing state loading 
        self.prize_header = pygame.image.load('res\\title_state\\prize_state\\header.png')
        self.prize_bg_1 = pygame.image.load('res\\title_state\\prize_state\\bg_1.png')
        self.prize_table = pygame.image.load('res\\title_state\\prize_state\\table_1.png')
        self.prize_dot = pygame.image.load('res\\title_state\\prize_state\\dot.png')
        self.prize_face = pygame.image.load('res\\title_state\\prize_state\\face.png')
        self.prize_scroll = pygame.image.load('res\\title_state\\prize_state\\scroll.png')
        self.prize_btn = pygame.image.load('res\\title_state\\prize_state\\btn.png')

        # Level select state
        self.level_select_bg = pygame.image.load('res\\level_select\\bg.png')
        self.level_select_close = pygame.image.load('res\\level_select\\close_2.png')
        self.level_select_dot_1 = pygame.image.load('res\\level_select\\dot_a.png')
        self.level_select_dot_2 = pygame.image.load('res\\level_select\\dot_d.png')
        self.level_select_header = pygame.image.load('res\\level_select\\header.png')
        self.level_select_tb_2 = pygame.image.load('res\\level_select\\table2.png')
        
        # level
        self.level_tb = pygame.image.load('res\\level_select\\table.png')
        self.level_star_1 = pygame.image.load('res\level_select\star_1.png')
        self.level_star_2 = pygame.image.load('res\\level_select\\star_2.png')
        self.level_star_3 = pygame.image.load('res\\level_select\\star_3.png')
        self.level_star_4 = pygame.image.load('res\\level_select\\star_4.png')
        self.level_lock = pygame.image.load('res\\level_select\\lock.png')


        # btn 
        self.next_button = pygame.image.load('res\\btn\\next.png')
        self.prew_button = pygame.image.load('res\\btn\\prew.png')

    # Init_equation_position 
    def init_equation_dasboard(self) : 
        arr = [[200, 0], [0, -200], [0, 200], [-200, 0], [200, -200], [-200, 200], [200, 200], [-200, -200]]
        self.equation_position = []
        for i in range(len(arr)) : 
            self.equation_position.append([self.start_button_center[0] + arr[i][0], self.start_button_center[1] + arr[i][1]])

        