from chemlib import Compound
import pygame , sys
from Setting import Setting
from Element import Element

class Dictionary : 
    def __init__(self) : 
        pygame.init()

        self.setting = Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Dictionary Demo")

        self.background = pygame.image.load('res\\backgound\\background_5.png')

        self.table = pygame.Rect(100, 100, self.setting.dictionary_table_width, self.setting.dictionary_table_height)

        self.sub_table = pygame.Rect(750, 100, 400, 400)

        self.elements = pygame.sprite.Group()
        self.set_defaut()

    def loop(self) : 
        while(True) :
            self.screen.blit(self.background, (0,0)) 
            pygame.draw.rect(self.screen,self.setting.dash_color, self.table, 5 )
            pygame.draw.rect(self.screen, self.setting.equation_dashboard_color, self.sub_table, 5)
            self.check_event()
            self.print_element_toscr()

            pygame.display.flip()


    def print_element_toscr(self) : 
        max_w = self.setting.dictionary_table_width // (self.setting.element_distance * 2)
        max_h = self.setting.dictionary_table_height // (self.setting.element_distance * 2) 
        c = 0
        for i in range(max_h) : 
            for  k in range(max_w) : 
                if c == len(self.elements) : return
                self.elements.sprites()[c].draw(150 + 2 *k * self.setting.element_distance, 150 + 2 * i * self.setting.element_distance, self.screen)
                c += 1

    def print_information(self, element) : 
        e = Compound(element.tag_name)
        


    def check_event(self) : 
        for event in pygame.event.get() : 
            if (event.type == pygame.QUIT) : 
                sys.exit()

    def set_defaut(self) : 
        for i in self.setting.element_content[0] : 
            e = Element(i, self)
            self.elements.add(e)

if __name__ == '__main__' : 
    ai = Dictionary()
    ai.loop()