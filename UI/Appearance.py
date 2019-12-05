DASH = "-"
LENGTH = 60
#Len af forritinu er 54!!!
# hastag = "#"


# Role = "Select a Role"
# option = "Select an option"
M = "Menu"
D = "Destination"
# C = 'Create'
# CH = 'Change info'
# CV = 'Change voyage'
A = 'Airplanes'
# AC = 'Assign crew'
E = "Employees"
V = "Voyage"
# S = "Show schedule "
L = "List employee"
# LD = 'List destination'
# LV = 'list voyage'



B = "Back"
Q = "Quit"
EMPTY = ''


# print(DASH*LENGTH)
# print("{:>30} ".format(M))
# print(DASH*LENGTH)
# print("{} {:<30}{} {} ".format('[1]', E, '[2]', V))
# print("{} {:<30}{} {} ".format('[3]', D, '[4]', L))
# print("{:<16} {}".format(empty, DASH*24))
# print("{:<18} {} {} {} {} ".format(empty, '[B]',B, '[Q]',Q))
# print("{:<16} {}".format(empty, DASH*24))
class Appearance:
    def __init__(self):
        pass

    def picture(self):
        print(""" 
           ______
            _\ _~-\___
    =  = ==(____AA____D
                \_____\___________________,-~~~~~~~`-.._
                /     o O o o o o O O o o o o o o O o  |\_
                `~-.__        ___..----..                  )
                      `---~~\___________/------------`````
                      =  ===(_________D                      
                    _   __      _   _____    _     
                   / | / /___ _/ | / /   |  (_)____
                  /  |/ / __ `/  |/ / /| | / / ___/
                 / /|  / /_/ / /|  / ___ |/ / /    
                /_/ |_/\__,_/_/ |_/_/  |_/_/_/     
                                   
            """)

    def print_main_menu(self):
        print(DASH*LENGTH)
        print("{:>32}".format(M))
        print(DASH*LENGTH)
        print("{:>8} {:<30}{} {} ".format('[1]', E, '[2]', V))
        print("{:>8} {:<30}{} {} ".format('[3]', D, '[4]', A))
        print("{:15}{}".format(EMPTY,DASH*30))
        print("{:20}{}{}{:5}{}{}".format(EMPTY,'[B]',B,EMPTY,'[Q]',Q))
        print("{:15}{}".format(EMPTY,DASH*30))

    def print_employee_menu(self):
        pass

    def print_dest_menu(self):
        pass

    def print_add_dest(self):
        pass