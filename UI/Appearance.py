from Models.Destination import Destination
from Models.Employee import Employee



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
CEI = 'Change Employee Info'
CNE = 'Create new Employee'
CND = 'Create new Destination'
CNV = 'Create new Voyage'
CNA = 'Create new Airplane'
CV = 'Change voyage'
A = 'Airplanes'
AC = 'Assign crew'
E = "Employees"
V = "Voyage"
S = "Show schedule "
L = "List employee"
LA = "List airplane"
LD = 'List destination'
LV = 'List voyage'
GA = "Get all employees"
GP = "Get all pilots"
GC = "Get all cabincrew"
CE = "Change employee"
CV = "Change voyage"
CS = "Change status"
CDI = 'Change destination info'
WC = "What would you like to change?"
DOE = "Are you looking for a specific date or a specific employee?"
DATE = "Date"
EM = "Employee"
ASS = "Assign crew"
F100 = "Fokker F100"
BAE146 = "BAE 146"
F28 = "Fokker F28"


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
    def back_quit(self):
        print("{:15}{}".format(EMPTY,DASH*30))
        print("{:17}{}{:10}{}".format(EMPTY,B,EMPTY,Q))
        print("{:15}{}".format(EMPTY,DASH*30))
    
    def print_main_menu(self):
        print(DASH*LENGTH)
        print("{:^60}".format(M))
        print(DASH*LENGTH)
        print("{:>5} {:<27}{} {} ".format('[1]', E, '[2]', V))
        print("{:>5} {:<27}{} {} ".format('[3]', D, '[4]', A))
        print("{:15}{}".format(EMPTY,DASH*30))
        print("{:^60}".format(Q))
        print("{:15}{}".format(EMPTY,DASH*30))
 

    def print_employee_menu(self):
        print(DASH*LENGTH)
        print("{:^60}".format(E))
        print(DASH*LENGTH)
        print("{:>5} {:<27}{} {} ".format('[1]', C, '[2]', CH))
        print("{:>5} {:<27}{} {} ".format('[3]', S, '[4]', L))
        self.back_quit()

    def print_select_employee_menu(self):
        print(DASH*LENGTH)
        print("{:^60}".format(E))
        print(DASH*LENGTH)
        print("{:>5} {:<27}{} {} ".format('[1]', GA, '[2]', GP))
        print("{:>5} {:<27}".format('[3]', GC, ))
        print("{:15}{}".format(EMPTY,DASH*30))
        print("{:17}{}{:10}{}".format(EMPTY,B,EMPTY,Q))
        print("{:15}{}".format(EMPTY,DASH*30))


    def print_create_employee(self):
        print(DASH*LENGTH)
        print("{:^60}".format(CNE))
        print(DASH*LENGTH)
        print("Please input necessary information:")
        #Input upplýsingar
        self.back_quit()

    def print_show_schedule(self):
        print(DASH*LENGTH)
        print("{:^60}".format(S))
        print(DASH*LENGTH)
        
    
    def print_change_employee_info(self):
        print(DASH*LENGTH)
        print("{:^60}".format(CE))
        print(DASH*LENGTH)

    def print_what_to_change_employee(self):
        print(DASH*LENGTH)
        print("{}".format(WC))

    def print_changing_employee_information(self, emp):
        print("ID Number: {}\nName: {}\nAddress: {}\nHome phone: {}\nMobile number: {}\nEmail address: {}\nJob title: {}\nRank: {}\nLicence: {}\nActivity: {}\n"
        .format(emp.get_ID_number(), emp.get_name(), emp.get_address(), emp.get_home_phone(), emp.get_mobile_number(),
        emp.get_email_address(), emp.get_job_title(), emp.get_rank(), emp.get_licence(), emp.get_activity()))

    def print_employee_list(self):
        pass

    def print_dest_menu(self):
        print(DASH*LENGTH)
        print("{:^60}".format(D))
        print(DASH*LENGTH)
        print("{:>5} {:<27}{} {} ".format('[1]', C, '[2]', CH))
        print("{:>5} {} ".format('[3]', LD ))
        self.back_quit()

    def print_dest_info(self,dest_list):
        print("Destination: {}\nCountry: {}\nAirport: {}\nflight time(one-way): {}\nDistance from Reykjavik: {}\nContact: {}\nContact phonenumber: {}"
                .format(dest_list.get_destination(),dest_list.get_country(),dest_list.get_airport(),dest_list.get_flight_time()
                ,dest_list.get_distance(),dest_list.get_name_of_contact(),dest_list.get_emergency_phone_number()))
        print(DASH*LENGTH)
        print("What would you like to change?")
        print()
        print("{:>5} {:<27}{} {} ".format('[1]', "Emergency contact", '[2]', "Emergency phonenumber"))
        print()


    def print_add_dest(self): 
        print(DASH*LENGTH)
        print("{:^60}".format(CND))
        print(DASH*LENGTH)
        print("Please input necessary information:")
        # Input Upplýsingar


    def print_change_dest_info(self):
        print(DASH*LENGTH)
        print("{:^60}".format(CDI))
        print(DASH*LENGTH)

    def print_voyage_menu(self):
        print(DASH*LENGTH)
        print("{:^60}".format(V))
        print(DASH*LENGTH)
        print("{:>5} {:<27}{} {} ".format('[1]', C, '[2]', AC))
        print("{:>5} {:<27}{} {}".format('[3]', LV, '[4]',CV ))
        print("{:15}{}".format(EMPTY,DASH*30))
        print("{:17}{}{:10}{}".format(EMPTY,B,EMPTY,Q))
        print("{:15}{}".format(EMPTY,DASH*30))
        

    def print_add_voyage(self):
        print(DASH*LENGTH)
        print("{:^60}".format(CNV))
        print(DASH*LENGTH)
        print("Please input necessary information:")
        #Input upplýsingar
        self.back_quit()
    
    def print_voyage_selection(self):
        print(DASH*LENGTH)
        print("{:^60}".format(S))
        print(DASH*LENGTH)
        print("{}".format(DOE))
        print("{:>5} {:<27}{} {} ".format('[1]', DATE, '[2]',E ))

    def print_selection_list(self,selected_list):
        print("Please select an option: ")
        for i in range(0,len(selected_list)):
            sting = str(selected_list[i])
            lis = sting.split(",")
            numb = i+1
            selected = lis[0]
            #self.app.print_selection_list(numb,dest)
            #print("[{}] {}".format(numb,dest))
            print("[{}] {}".format(numb,selected))
        
    def print_plane_activity_list(self,numb,selected,activity=""):
        if activity == "1":
            activity = "Active"
        elif activity == "0":
            activity = "Inactive"
        print("[{}] {}\t{}".format(numb,selected,activity))

    def print_assign_crew(self):
        print(DASH*LENGTH)
        print("{:^60}".format(ASS))
        print(DASH*LENGTH)
        

    def print_voyage_list(self):
        pass

    def print_change_voyage(self):
        pass

    def print_airplane_menu(self):
        print(DASH*LENGTH)
        print("{:^60}".format(A))
        print(DASH*LENGTH)
        print("{:>5} {:<27}{} {} ".format('[1]', C, '[2]', CS))
        print("{:>5} {} ".format('[3]', LA ))
        self.back_quit()
    
    def print_add_plane(self):
        print(DASH*LENGTH)
        print("{:^60}".format(CNA))
        print(DASH*LENGTH)
        print("Please select the registration number and aircraft model")
        print("Aircraft models:")
        print("{:>5} {:<27}{} {} ".format('[1]', BAE146, '[2]', F28))
        print("{:>5} {} ".format('[3]', F100 )) 
        
 
        
    def print_change_plane_status(self):
        print(DASH*LENGTH)
        print("{:^60}".format(CS))
        print(DASH*LENGTH)
        print()
        '''
        print("{:>5} {:<27}{} {} ".format('[1]', C, '[2]', CS)) #Laga þetta 
        print("{:>5} {} ".format('[3]', LA )) #Laga þetta 
        '''
        self.back_quit()

    def print_list_plane(self):
        print(DASH*LENGTH)
        print("{:^60}".format(LA))
        print(DASH*LENGTH)
        print("Laga og bæta hér :), hehehehe")

        

    
