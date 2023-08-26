import bs4, requests

class Game_Logic : 
    def __init__(self) :
        self.name_after_combine = []

    def check_for_new_element(self, c_game) : 
        if (len(c_game.element_in_equa) == 0) : return False
        link = 'https://chemequations.com/en/?s='
        for i in c_game.element_in_equa : 
            link  = link  + i.tag_name + '+%2B+'
        link  += '&ref=input'
        res = requests.get(link)
        soup = bs4.BeautifulSoup(res.text, features='html.parser')
        title = soup.select_one('title')
        if (title.get_text() == 'Chemical Equations online!') : return False
        res_arr = title.get_text().split(' ')
        begin = False
        for i in res_arr : 
            if (i == '→') : 
                begin = True 
            elif (i == '-') : 
                break 
            elif (i == '?:') :
                self.name_after_combine.clear()
                break
            elif ( begin and not i.isdigit() and (not i.endswith(":-") or not i.endswith(":+")) and i != '+') : 
                self.name_after_combine.append(i)
            
        
        if len(self.name_after_combine) == 0 : return False
        return True

