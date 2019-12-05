DASH = "-"
LENGTH = 60
#Len af forritinu er 54!!!
# hastag = "#"


# Role = "Select a Role"
# option = "Select an option"
M = "Menu"
D = "Destination"
C = 'Create'
CH = 'Change info'
# CV = 'Change voyage'
A = 'Airplanes'
# AC = 'Assign crew'
E = "Employees"
V = "Voyage"
S = "Show schedule "
L = "List employee"
# LD = 'List destination'
# LV = 'list voyage'



B = "[B] Back"
Q = "[Q] Quit"
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
        print("{:^60}".format(M))
        print(DASH*LENGTH)
        print("{:>8} {:<30}{} {} ".format('[1]', E, '[2]', V))
        print("{:>8} {:<30}{} {} ".format('[3]', D, '[4]', A))
        print("{:15}{}".format(EMPTY,DASH*30))
        print("{:17}{}{:10}{}".format(EMPTY,B,EMPTY,Q))
        print("{:15}{}".format(EMPTY,DASH*30))

    def print_employee_menu(self):
        print(DASH*LENGTH)
        print("{:^60}".format(E))
        print(DASH*LENGTH)
        print("{:>8} {:<30}{} {} ".format('[1]', C, '[2]', CH))
        print("{:>8} {:<30}{} {} ".format('[3]', S, '[4]', L))
        print("{:15}{}".format(EMPTY,DASH*30))
        print("{:17}{}{:10}{}".format(EMPTY,B,EMPTY,Q))
        print("{:15}{}".format(EMPTY,DASH*30))

    def print_create_employee(self):
        pass

    def print_show_schedule(self):
        pass
    
    def print_change_employee_info(self):
        pass

    def print_employee_list(self):
        pass

    def print_dest_menu(self):
        #DASH
        print("destination")
        #DASH
        print("[1] Create [2] change info")
        print("[3] list")
        #SUBDASH
        #BACK OG QUIT
        #SUBDASH

    def print_add_dest(self):
        pass

    
    def print_voyage_menu(self):
        print(DASH*LENGTH)
        print("{:^60}".format(V))
        print(DASH*LENGTH)
        print("{:>8} {:<30}{} {} ".format('[1]', C, '[2]', AC))
        print("{:>8} {:<30}{} {} ".format('[3]', LV, '[4]', CV))
        print("{:15}{}".format(EMPTY,DASH*30))
        print("{:17}{}{:10}{}".format(EMPTY,B,EMPTY,Q))
        print("{:15}{}".format(EMPTY,DASH*30))
        

    def print_add_voyage(self):
        pass

    def print_assign_crew(self):
        pass

    def print_voyage_list(self):
        pass

    def print_change_voyage(self):
        pass
