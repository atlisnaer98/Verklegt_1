from Models.Airplane import Airplane
from Models.Destination import Destination
from Models.Employee import Employee
from Models.Voyage import Voyage
import csv
from Services.API import LLApi
from UI.Appearance import Appearance
import datetime

QUIT = ["q","Q"]
BACK = ["b","B"]
class User:
    def __init__(self):
        self.ll = LLApi()
        self.app = Appearance()

    def start(self):
        pass

    def add_dest(self):
        dest = Destination()
        dest.set_destination(input("Destination: "))
        dest.set_country(input("Country: "))
        dest.set_airport(input("Airport: "))
        dest.set_flight_time(input("Time of flight: "))
        dest.set_distance(input("Distance: "))
        dest.set_name_of_contact(input("Emergency contact: "))
        dest.set_emergency_phone_number(input("Emergency contact number: "))
        #print(dest)
        self.ll.add_dest(dest)
        #return country, airport, flight_time, name_of_contact, emergency_phone_number

    def get_all_dest(self):
        print("{:<20}{:<20}{:<20}".format("Airport","Country","Distance(km)"))
        dest_obj = self.ll.get_all_dest()
        for line in dest_obj:
            sting = str(line)
            lis = sting.split(",")
            print("{:<20}{:<20}{:<20}".format(lis[2], lis[1], lis[4]+'km'))

    def get_all_airplane(self):
        airplane_obj = self.ll.get_all_airplanes()
        for line in airplane_obj:
            print(line)
    
    def add_plane(self):
        #self.app.print_add_plane()
        plane = Airplane()
        plane.set_registration_number(input("Registration number: "))
        plane.set_model(input("Model: "))
        self.ll.add_plane(plane)

    def get_all_employee(self):
        employee_list = self.ll.get_all_employees()
        print("{:<20}{:<20}{:<20}".format("Name","SSN","Role"))
        for line in employee_list:
            sting = str(line)
            lis = sting.split(",")
            print("{:<20}{:<20}{:<20}".format(lis[1],lis[0],lis[6]))

    def add_employee(self):
        #self.app.print_add_employee()
        emp = Employee()
        emp.set_ssn(input("ID number: "))
        emp.set_name(input("Name: "))
        emp.set_address(input("Adress: "))
        emp.set_home_phone(input("Home phone: "))
        emp.set_mobile_number(input("Mobile number: "))
        emp.set_email_address(input("Email: "))
        emp.set_job_title(input("Job title: "))
        emp.set_rank(input("Rank: "))
        emp.set_licence(input("Licence: "))
        emp.set_activity(input("Activity: "))
        self.ll.add_employee(emp)

    def change_employee_info(self):
        self.app.print_change_employee_info()
        employee_list = self.ll.get_all_employees()
        action = input("Enter ID number: ")
        for index in range(len(employee_list)):
            emp = employee_list[index]
            if action == emp.get_ID_number():
                print("ID Number: {}\nName: {}\nAddress: {}\nHome phone: {}\nMobile number: {}\nEmail address: {}\nJob title: {}\nRank: {}\nLicence: {}\nActivity: {}\n"
                .format(emp.get_ID_number(), emp.get_name(), emp.get_address(), emp.get_home_phone(), emp.get_mobile_number(), 
                emp.get_email_address(), emp.get_job_title(), emp.get_rank(), emp.get_licence(), emp.get_activity()))
                option = int(input("What do you want to change? "))
                changed = input("Enter new input: ")
                self.ll.change_employee(employee_list,index,option,changed)
                #print("tippi")
            """def change_employee_info(self): # ef við viljum nota dicts
            self.app.print_change_employee_info()
            employee_dic = self.ll.get_all_employees_dict()
            action = input("Enter ID number: ")
            for key in employee_dic:
                if key == action:
                    print(employee_dic[key]) """

    def change_dest_info(self):
        self.app.print_change_dest_info()
        dest_list = self.ll.get_all_dest()
        self.app.print_selection_list(dest_list)
        action = input("select an option: ")
        for index in range(0,len(dest_list)):
            if int(action) == (index+1):
                self.app.print_change_dest_info()
                dest = str(dest_list[index]).split(",")              
                print("You chose {}, what do you want to change?".format(dest[0]))
                aciton = input("blbla")
        
    def get_cabin_crew(self):
        cabin_crew_list = self.ll.get_cabin_crew()
        print("{:<20}{:<20}{:<20}".format("Name","SSN","Role"))
        for line in cabin_crew_list:
            sting = str(line)
            lis = sting.split(",")
            print("{:<20}{:<20}{:<20}".format(lis[1],lis[0],lis[6]))

    def get_pilots(self):
        pilot_list = self.ll.get_pilots()
        print("{:<20}{:<20}{:<20}".format("Name","SSN","Licence"))
        for line in pilot_list:
            sting = str(line)
            lis = sting.split(",")
            print("{:<20}{:<20}{:<20}".format(lis[1],lis[0],lis[8]))

    def printing_picture(self):
        self.app.picture()

    def dest_menu(self,action):
        self.app.print_dest_menu()
        while action not in QUIT:
            action = input("select an option: ")
            if action == "1": #create new dest
                self.app.print_add_dest()
                self.add_dest()
                print()
                print("You have created a new destination!")
                print()
                self.dest_menu(action)
            elif action == "2": #change dest
                self.change_dest_info()
            elif action == "3": #list dest
                self.get_all_dest()
                action = self.back_quit(action)
                """self.app.back_quit()
                action = input("select an option: ")
                if action in BACK:
                    self.dest_menu(action)
                elif action in QUIT:
                    return action
                else:
                    action = input("not a valid input, please re-enter: ")
                    self.dest_menu(action)"""
            elif action in BACK:
                self.main_menu()
                    
    def back_quit(self,action):
        self.app.back_quit()
        action = input("select an option: ")
        if action in BACK:
            self.dest_menu(action)
        elif action in QUIT:
            return action
        else:
            action = input("not a valid input, please re-enter: ")
            self.dest_menu(action)
            return action

    def employee_menu(self,action):
        self.app.print_employee_menu()
        while action not in QUIT:
            action = input("select an option: ")
            if action == "1":
                self.add_employee()
            elif action == "2":
                self.change_employee_info()
            elif action == "3":
                pass
            elif action == "4":
                self.app.print_select_employee_menu()
                action = input("select an option: ")
                if action == "1":
                    self.get_all_employee()
                elif action == "2":
                    self.get_pilots()
                elif action == "3":
                    self.get_cabin_crew()
            
    def add_voyage(self):
        dest = Destination()
        dest.set_destination(input("date of departure: "))
        dest.set_country(input("time of departure: "))
        dest.set_airport(input("destination: "))
        
        #print(dest)
        self.ll.add_dest(dest)
        #return country, airport, flight_time, name_of_contact, emergency_phone_number

    def get_all_voyages(self, from_date, to_date):
        voyage_list = self.ll.get_all_voyages(from_date, to_date)
        #print("{:<20}{:<20}{:<20}".format("Name","SSN","Role"))
        for voyage in voyage_list:
            print(str(voyage))

    def get_voyages_for_employee(self, ID):
        employee_list = self.ll.get_voyages_for_employee(ID)
        for line in employee_list:
            print(line[0],line[1],line[2])
            
    def Voyage_menu(self,action):
        self.app.print_voyage_menu()
        action = ""
        while action not in QUIT:
            action = input("select an option: ")
            if action == "1":
                self.app.print_add_voyage()
                
            # elif action == "2":
            #     #assign crew
            elif action == "3":
                self.app.print_voyage_selection()
                action = input("select an option: ")
                if action =="1": 
                    #from_date = input("Enter date: YYYY-MM-DD:") 2019-11-24T14:43:00
                    year,month,day,hour,minute = 2019,11,10,6,0
                    from_date = datetime.datetime(year,month,day,hour,minute,0)
                    #to_date = input("to YYYY-MM-DD:") 2019-11-24T03:00:00
                    year,month,day,hour,minute = 2019,12,20,6,0
                    to_date = datetime.datetime(year,month,day,hour,minute,0)
                    self.get_all_voyages(from_date, to_date)
                elif action == "2":
                    ID = input("Enter ID number")
                    print("Enter timeperiod")
                    # from_date = input("From YYYY-MM-DD:")
                    # to_date = input("to YYYY-MM-DD:")
                    self.get_voyages_for_employee(ID)
            # elif action == "4":
            #     #change voyage
    
    def change_plane_status(self): #VINNA Í ÞESSU!
        self.app.print_change_plane_status()
        airplane_list = self.ll.get_all_airplanes()
        for index in range(0,len(airplane_list)):
            sting = str(airplane_list[index])
            lis = sting.split(",")
            numb = index + 1
            plane = lis[0]
            activity = lis[2]
            self.app.test_print_selection_list(numb,plane,activity)

    def airplane_menu(self,action):
        self.app.print_airplane_menu()
        while action not in QUIT:
            action = input("select an option: ")
            if action == "1":
                self.app.print_add_plane()
                self.add_plane()
                print()
                print("You have added a new airplane!")
                print()
            elif action == "2":
                self.change_plane_status()
                
            elif action == "3":
                self.app.print_list_plane()
                
                
        '''
        self.app.print_airplane()
        while action not in QUIT:
            action = input("select an option: ")
            if action == "1":
                self.app.print_add_plane()
                self.add_plane()
                print()
                print("You have added a new airplane!")
                print()
                self.dest_menu(action)
            elif action == "2": #Change satus
                pass
            elif action == "3": #List airplane
                pass
        '''

    def main_menu(self):
        action = ""
        while action not in QUIT:
            self.app.print_main_menu()
            action = input("select an option: ") # muna að villutjékka þetta
            if action == "1":
                self.employee_menu(action)  
            elif action == "2":
                self.Voyage_menu(action)
                action = input("select an option: ")
            elif action == "3": #DESTINATION
                self.dest_menu(action)
            elif action == "4":
                self.airplane_menu(action)

            
