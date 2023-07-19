
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
        self.element_content = [["NaOH", "NaOH", "SO3", "HCl", "CO2"], ['H2', 'CO2']]
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


    # Init_equation_position 
    def init_equation_dasboard(self) : 
        arr = [[200, 0], [0, -200], [0, 200], [-200, 0], [200, -200], [-200, 200], [200, 200], [-200, -200]]
        self.equation_position = []
        for i in range(len(arr)) : 
            self.equation_position.append([self.start_button_center[0] + arr[i][0], self.start_button_center[1] + arr[i][1]])

        