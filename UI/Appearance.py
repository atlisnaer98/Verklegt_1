from Models.Destination import Destination
from Models.Employee import Employee
from Models.Airplane import Airplane
from Models.Voyage import Voyage

DASH = "-"
LENGTH = 60

M = "Menu"
D = "Destination"
C = 'Create'
CH = 'Show info'
CEI = 'Change Employee Info'
CNE = 'Create new Employee'
CND = 'Create new Destination'
CNV = 'Create new Voyage'
CNA = 'Create new Airplane'
CV = 'Change voyage'
A = 'Airplanes'
AC = 'Assign crew'
AD = "All destinations"
AV = "Available"
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
DOE = "Are you looking for a specific date, employee or timeperiod?"
DATE = "Date"
EM = "Employee"
ASS = "Assign crew"
F100 = "Fokker F100"
BAE146 = "BAE 146"
F28 = "Fokker F28"
AC = "Active"
IAC = "Inactive"
W = "Working"
MP = "Show most popular"
B = "[B] Back"
Q = "[Q] Quit"
EMPTY = ''


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
        print()
        print("{:>10} {:<30}{} {}".format('[1]',E,'[2]',V))
        print()
        print("{:>10} {:<30}{} {}".format('[3]',D,'[4]',A))
        print()
        print("{:15}{}".format(EMPTY,DASH*30))
        print("{:^60}".format(Q))
        print("{:15}{}".format(EMPTY,DASH*30))
        print()
 

    def print_employee_menu(self):
        print()
        print(DASH*LENGTH)
        print("{:^60}".format(E))
        print(DASH*LENGTH)
        print()
        print("{:>10} {:<30}{} {} ".format('[1]', C, '[2]', CH))
        print()
        print("{:>10} {:<30}{} {} ".format('[3]', S, '[4]', L))
        print()

    def print_select_employee_menu(self):
        print(DASH*LENGTH)
        print("{:^60}".format(E))
        print(DASH*LENGTH)
        print()
        print("{:>10} {:<30}{} {} ".format('[1]', GA, '[2]', GP))
        print()
        print("{:>10} {:<30}".format('[3]', GC, ))
        print()


    def print_create_employee(self):
        print(DASH*LENGTH)
        print("{:^60}".format(CNE))
        print(DASH*LENGTH)
        print()


    def print_show_schedule(self):
        print(DASH*LENGTH)
        print("{:^60}".format(S))
        print(DASH*LENGTH)
        print()
        
    
    def print_change_employee_info(self):
        print(DASH*LENGTH)
        print("{:^60}".format(CE))
        print(DASH*LENGTH)

    def print_what_to_change_employee(self):
        print(DASH*LENGTH)
        print("{}".format(WC))
    
    def print_employee_schedule(self):
        print("{:>10} {:<30}{} {} ".format('[1]', DATE, '[2]', EM))
        print()
    
    def print_employee_available_or_working(self):
        print()
        print(DASH*LENGTH)
        print()
        print("Are you looking for available or working employees?")
        print()
        print("{:>10} {:<30}{} {} ".format('[1]', AV ,'[2]', W))
        print()

    def print_employee_information(self, emp):
        print("\nID Number: {}\nName: {}\nJob title: {}\nRank: {}\nLicence: {}\nAddress: {}\nHome phone: {}\nMobile number: {}\nEmail address: {}\nActivity: {}\n"
        .format(emp.get_ssn(), emp.get_name(), emp.get_role(), emp.get_rank(), emp.get_licence(), emp.get_address(), emp.get_home_phone(), emp.get_mobile_number(),
        emp.get_email_address(), emp.get_activity()))

    def print_changing_employee_information(self, emp):
        print("\n[1] Address: {}\n[2] Home phone: {}\n[3] Mobile number: {}\n[4] Email address: {}\n[5] Activity: {}\n"
        .format(emp.get_address(), emp.get_home_phone(), emp.get_mobile_number(),
        emp.get_email_address(), emp.get_activity()))

    def print_get_all_employess(self):
        print()
        print(DASH*LENGTH)
        print("{:^60}".format("All Employees"))
        print(DASH*LENGTH)

    def print_get_all_employess_role(self,employee):
        print("{:<20}{:<20}{:<20}".format(employee.get_name(), employee.get_ssn(), employee.get_role()))
    
    def print_get_all_employess_rank(self,employee):
        print("{:<20}{:<20}{:<20}".format(employee.get_name(), employee.get_ssn(), employee.get_rank()))
    
    def print_get_all_pilot_rank_and_licence(self,employee):
        print("{:<20}{:<13}{:<13}{:<13}".format(employee.get_name(), employee.get_ssn(), employee.get_rank(), employee.get_licence()))

    def print_choose_aircraft(self):
        print(DASH*LENGTH)
        print("{:^60}".format("Choose Aircraft Model"))
        print(DASH*LENGTH)  
    
    
    def print_get_all_pilots(self):
        print()
        print(DASH*LENGTH)
        print("{:^60}".format("Pilots"))
        print(DASH*LENGTH)    
    
    def print_get_all_cabincrew(self):
        print()
        print(DASH*LENGTH)
        print("{:^60}".format("All Cabin Crew"))
        print(DASH*LENGTH)
    
    def print_dest_menu(self):
        print()
        print(DASH*LENGTH)
        print("{:^60}".format(D))
        print(DASH*LENGTH)
        print("\n{:>10} {:<30}{} {} ".format('[1]', C, '[2]', CH))
        print("\n{:>10} {:<30}{} {} ".format('[3]', MP, '[4]', LD))

    def print_dest_info(self,dest_list):
        print("\nDestination: {}\nCountry: {}\nAirport(XXX): {}\nflight time(one-way, HH:MM): {}\nDistance from Reykjavik: {}\nContact: {}\nContact phonenumber(+xxx...): {}"
                .format(dest_list.get_destination(),dest_list.get_country(),dest_list.get_airport(),dest_list.get_flight_time()
                ,dest_list.get_distance(),dest_list.get_name_of_contact(),dest_list.get_emergency_phone_number()))
        print(DASH*LENGTH)
        print("What would you like to change?")
        print()
        print("{:>10} {:<30}{} {} ".format('[1]', "Emergency contact", '[2]', "Emergency phonenumber"))
        print()
    
    def print_list_dest(self):
        print()
        print(DASH*LENGTH)
        print("{:^60}".format(LD))
        print(DASH*LENGTH)
    
    def print_get_all_dest(self):
        print()
        print(DASH*LENGTH)
        print("{:^60}".format(AD))
        print(DASH*LENGTH) 
  
    def print_list_dest_info(self,dest):
        print("{:<20}{:<20}{:<20}".format(dest.get_airport(), dest.get_country(), dest.get_distance()+' km'))

    def print_plane_info(self,plane_list):
        print("Registration number: {}\nPlane Type: {}\nModel: {}\nCapictity: {}\nActivity: {}".format(plane_list.get_registration_number(),plane_list.get_plane_type(),plane_list.get_model(),plane_list.get_capacity(),plane_list.get_active()))


    def print_add_dest(self): 
        print()
        print(DASH*LENGTH)
        print("{:^60}".format(CND))
        print(DASH*LENGTH)
        print()
        print("Please input necessary information:")
        print()



    def print_change_dest_info(self):
        print()
        print(DASH*LENGTH)
        print("{:^60}".format(CDI))
        print(DASH*LENGTH)

    def print_voyage_menu(self):
        print()
        print(DASH*LENGTH)
        print("{:^60}".format(V))
        print(DASH*LENGTH)
        print()
        print("{:>10} {:<30}{} {} ".format('[1]', C, '[2]', ASS))
        print()
        print("{:>10} {:<30}{} {}".format('[3]', LV, '[4]',CV ))
        print()

    def print_add_voyage(self):
        print(DASH*LENGTH)
        print("{:^60}".format(CNV))
        print(DASH*LENGTH)
        print("Please input necessary information:")


    def print_voyage_info(self, voyage):
        print("Booking Refrence: {}\nDestination: {}\nDeparture Time: {}\nArrival Time: {}\n".format(voyage.get_booking_reference(), voyage.get_arriving_at(),voyage.get_departure(),voyage.get_arrival()))
    
    def print_voyage_selection(self):
        print(DASH*LENGTH)
        print("{:^60}".format(S))
        print(DASH*LENGTH)
        print("\n{}\n".format(DOE))
        print("{:>10} {:<30}{} {} \n".format('[1]', DATE, '[2]',E ))
        print("{:>10} {:<30}\n".format('[3]', 'time period'))
    
    def print_voyage_list_with_crew(self, voyage,manned,status):
        print("Booking Refrence: {}\nDestination: {}\nFlight number away: {}\nFlight number home: {}\nDeparture Time: {}\nArrival Time: {}\nStatus: {}\nUn/Manned: {}\n".format(voyage.get_booking_reference(), voyage.get_arriving_at(),voyage.get_flight_number_away(),voyage.get_flight_number_home(),voyage.get_departure(),voyage.get_arrival(),status,manned))

    def print_selection_list(self,selected_list):
        print()
        for i in range(0,len(selected_list)):
            sting = str(selected_list[i])
            lis = sting.split(",")
            numb = i+1
            selected = lis[0]
            print("[{}] {}".format(numb,selected))
        print()
        
    def print_plane_activity_list(self,numb,selected,activity=""):
        if activity == "1":
            activity = "Active"
        elif activity == "0":
            activity = "Inactive"
        print("{:<15}{:<15}{:<15}".format("["+str(numb)+"]",selected,activity))

    def print_assign_crew(self):
        print(DASH*LENGTH)
        print("{:^60}".format(ASS))
        print(DASH*LENGTH)
        

    def print_voyage_selection_list(self,voyage):
        print("{:<20}{:<20}{:<20}".format("["+ voyage.get_booking_reference()+ "]",voyage.get_arriving_at(),voyage.get_departure()))

    def print_change_voyage(self):
        print(DASH*LENGTH)
        print("{:^60}".format(CV))
        print(DASH*LENGTH)
    
    def print_changing_voyage_information(self,emp):
        print(DASH*LENGTH)
        print("{:^60}".format("What would you like to change?"))
        print(DASH*LENGTH)
        print()
        
        print("{:>10} {:<30}{} {} ".format('[1]', "Flight Number", '[2]', "Aircraft ID"))

    def print_airplane_menu(self):
        print(DASH*LENGTH)
        print("{:^60}".format(A))
        print(DASH*LENGTH)
        print("\n{:>10} {:<30}{} {} \n".format('[1]', C, '[2]', CS))
        print("{:>10} {} \n".format('[3]', LA ))
    
    def print_add_plane(self):
        print(DASH*LENGTH)
        print("{:^60}".format(CNA))
        print(DASH*LENGTH)
        print("\nPlease select the registration number and aircraft model\n")
        
    
    def print_add_plane_vol2(self):
        print("\nAircraft models:")
        print("\n{:>10} {:<30}{} {} ".format('[1]', BAE146, '[2]', F28))
        print("\n{:>10} {} \n".format('[3]', F100 ))
        
 
        
    def print_change_plane_status(self,airplane_list):
        print(DASH*LENGTH)
        print("{:^60}".format(CS))
        print(DASH*LENGTH)
        print()
        counter = 0
        print("{:<15}{:<15}{:<15}".format("Select", "Registration","Activity:"))
        print("{:<15}{:<15}\n".format("number:", "number:"))
        for plane in airplane_list:
            counter += 1
            plane_reg = plane.get_registration_number()
            activity = plane.get_active()
            self.print_plane_activity_list(counter,plane_reg,activity)

    def print_list_plane(self):
        print()
        print(DASH*LENGTH)
        print("{:^60}".format(LA))
        print(DASH*LENGTH)
        print()
        print("Select an airplane to see availability at\na specific date and time:")
    
    def print_list_plane_info(self,plane):
        print("{:<20}{:<13}{:<13}{:<13}".format(plane.get_registration_number(), plane.get_plane_type(), plane.get_model(), plane.get_capacity()))
        
    def print_yes_no(self):
        print()
        print("{:>10} {:<30}{} {} ".format('[1]', "Yes", '[2]',"No" ))
        print()

    def select_licence(self):
        print()
        print("{:>10} {:<30}{} {} ".format('[1]', "NAFokkerF100", '[2]',"NABAE146" ))
        print()
        print("{:>10} {:<30}{} {} ".format('[3]', "NAFokkerF28", '[4]',"All Pilots" ))
        print()
        
    def print_working_employee(self):
        print()
        print(DASH*LENGTH)
        print("{:^60}".format("Working employee schedule"))
        print(DASH*LENGTH)
    
    def print_working_emps(self, voyage,employee_dict):
        print("\n{:<20}{:<20}{:<20}\n{:<20}{:<20}{:<20}\n{:<20}{:<20}{:<20}\n{:<20}{:<20}{:<20}\n{:<20}{:<20}{:<20}\n".format(employee_dict[voyage.get_captain()].get_name(),voyage.get_captain(),voyage.get_arriving_at(),
        employee_dict[voyage.get_copilot()].get_name(),voyage.get_copilot(),voyage.get_arriving_at(),
        employee_dict[voyage.get_fsm()].get_name(),voyage.get_fsm(),voyage.get_arriving_at(),
        employee_dict[voyage.get_fa1()].get_name(),voyage.get_fa1(),voyage.get_arriving_at(),
        employee_dict[voyage.get_fa2()].get_name(),voyage.get_fa2(),voyage.get_arriving_at()))
    

    def print_in_air_away(self,plane,voyage,status):
        print("\nPlane ID: {}\nPlane Type: {}\nPlane model: {}\nStatus: {}\nDestination: {}\nFlight number: {}\nAvailable again: {}\n".format(plane.get_registration_number(),plane.get_plane_type(),plane.get_model(),status,voyage.get_arriving_at(),voyage.get_flight_number_away(),voyage.get_arrival()))

    def print_in_air_home(self,plane,voyage,status):
        print("\nPlane ID: {}\nPlane Type: {}\nPlane model: {}\nStatus: {}\nDestination: {}\nFlight number: {}\nAvailable again: {}\n".format(plane.get_registration_number(),plane.get_plane_type(),plane.get_model(),status,voyage.get_arriving_at(),voyage.get_flight_number_away(),voyage.get_arrival()))

    def print_plane_busy(self,plane,voyage,status):
        print("\nPlane ID: {}\nPlane Type: {}\nPlane model: {}\nStatus: {}\nDestination: {}\nAvailable again: {}\n".format(plane.get_registration_number(),plane.get_plane_type(),plane.get_model(),status,voyage.get_arriving_at(),voyage.get_arrival()))

    def print_plane_available(self,plane):
        print("\nPlane ID: {}\nPlane Type: {}\nPlane model: {}\nPlane is available\n".format(plane.get_registration_number(),plane.get_plane_type(),plane.get_model()))

    def get_pop_dest(self,dest,counter):
        print("\nMost popular destination: {}\nNumber of assigned voyages: {}\n".format(dest.get_destination(),counter))