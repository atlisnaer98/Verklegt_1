from Models.Airplane import Airplane
from Models.Destination import Destination
from Models.Employee import Employee
from Models.Voyage import Voyage
import csv
from Services.API import LLApi
from UI.Appearance import Appearance
import datetime
import dateutil.parser
from datetime import timedelta

QUIT = ["q","Q"]
BACK = ["b","B"]
YES = ["y","Y"]
NO = ["n","N"]
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
    
    def add_plane(self):
        #self.app.print_add_plane()
        plane = Airplane()
        plane.set_registration_number(input("Registration number: "))
        self.app.print_add_plane_vol2()
        option = int(input("Model: "))
        self.set_plane_model(plane,option)
        plane.set_active(1)
        self.ll.add_plane(plane)

    def set_plane_model(self,plane,option):
        if option == 1:
            plane.set_planeID("NABAE146")
            plane.set_plane_type("BAE")
            plane.set_model("146")
            plane.set_capacity(82)
        elif option == 2:
            plane.set_planeID("NAFokkerF28")
            plane.set_plane_type("Fokker")
            plane.set_model("F28")
            plane.set_capacity(65)
        elif option == 3:
            plane.set_planeID("NAFokkerF100")
            plane.set_plane_type("Fokker")
            plane.set_model("F100")
            plane.set_capacity(100)

    def get_all_employee(self):
        employee_list = self.ll.get_all_employees()
        print("{:<20}{:<20}{:<20}".format("Name","SSN","Role"))
        for line in employee_list:
            sting = str(line)
            lis = sting.split(",")
            print("{:<20}{:<20}{:<20}".format(lis[1],lis[0],lis[6]))

    def add_employee(self):
        #self.app.print_add_employee()
        job_title_list = ["Pilot","Cabincrew"]
        pilot_rank_list = ["Captain","Copilot"]
        cabincrew_rank_list = ["Flight Service Manager", "Flight Attendant"]
        emp = Employee()
        emp.set_ssn(input("ID number: "))
        emp.set_name(input("Name: "))
        emp.set_address(input("Adress: "))
        emp.set_home_phone(input("Home phone: "))
        emp.set_mobile_number(input("Mobile number: "))
        emp.set_email_address(input("Email: "))
        print("Job title:")
        self.app.print_selection_list(job_title_list)
        job_title_selection = self.back_quit("",2)
        if job_title_selection == "1":
            job_title_selection = "Pilot"
            selected_rank_list = pilot_rank_list
        elif job_title_selection == "2":
            job_title_selection = "Cabincrew"
            selected_rank_list = cabincrew_rank_list
        emp.set_job_title(job_title_selection)
        self.app.print_selection_list(selected_rank_list)
        rank_selection = self.back_quit("",2)
        if job_title_selection == "Cabincrew":
            if rank_selection == "1":
                rank_selection = "Flight Service Manager"
            elif rank_selection == "2":
                rank_selection = "Flight Attendant"
        elif job_title_selection == "Pilot":
            if rank_selection == "1":
                rank_selection = "Captain"
            elif rank_selection == "2":
                rank_selection = "Copilot"
        emp.set_rank(rank_selection)
        emp.set_licence(input("Licence: "))
        emp.set_activity(input("Activity: "))
        self.ll.add_employee(emp)

    def validate_selection():
        selection = ""

    def change_employee_info(self):
        self.app.print_change_employee_info()
        employee_list = self.ll.get_all_employees()
        action = input("Enter ID number: ")
        for index in range(len(employee_list)):
            emp = employee_list[index]
            if action == emp.get_ID_number():
                self.app.print_changing_employee_information(emp)
                print("Would you like to change any information?")
                self.app.print_yes_no()
                change_selection = self.back_quit(action,2)
                if change_selection == "1":
                    option = int(input("What do you want to change? "))
                    if option == 5:
                        changed = ""
                        self.ll.change_employee(employee_list,index,option,changed)
                        self.employee_menu(action)
                    else:
                        changed = input("Enter new input: ")
                        self.ll.change_employee(employee_list,index,option,changed)
                        self.employee_menu(action)
                elif change_selection == "2":
                    self.employee_menu(action)

    def change_dest_info(self,action):
        self.app.print_change_dest_info()
        dest_list = self.ll.get_all_dest()
        self.app.print_selection_list(dest_list)
        action = self.back_quit(action,len(dest_list))
        for index in range(0,len(dest_list)):
            if int(action) == (index+1):
                self.app.print_change_dest_info()
                dest = dest_list[index]
                self.app.print_dest_info(dest)
                action = self.back_quit(action,len(dest_list))
                changed = input("Enter new input: ")
                self.ll.change_dest(dest_list,index,int(action),changed)
        
    def get_cabin_crew(self):
        cabin_crew_list = self.ll.get_cabin_crew()
        print("{:<20}{:<20}{:<20}".format("Name","SSN","Rank"))
        for line in cabin_crew_list:
            sting = str(line)
            lis = sting.split(",")
            print("{:<20}{:<20}{:<20}".format(lis[1],lis[0],lis[7]))

    def get_pilots(self):
        self.app.select_license()
        license = ''
        while license not in QUIT:
            license = self.back_quit(license,4)
            license = input("select aircraft license:")
            if license == '1':
                license = 'NAFokkerF100'
            elif license == '2':
                license = 'NABAE146'
            elif license == '3':
                license = 'NAFokkerF28'
            elif license == '4':
                license = 'All'
            pilot_list = self.ll.get_pilots(license)
            print("{:<20}{:<20}{:<20}".format("Name","SSN","Licence"))
            for line in pilot_list:
                sting = str(line)
                lis = sting.split(",")
                print("{:<20}{:<20}{:<20}".format(lis[1],lis[0],lis[8]))

    def printing_picture(self):
        self.app.picture()

    def dest_menu(self,action):
        while action not in QUIT:
            self.app.print_dest_menu()
            action = self.back_quit(action,3)
            if action == "1": #create new dest
                self.app.print_add_dest()
                self.add_dest()
                print()
                print("You have created a new destination!")
                print()
                self.dest_menu(action)
            elif action == "2": #change dest
                self.change_dest_info(action)
            elif action == "3": #list dest
                self.get_all_dest()
                action = self.back_quit(action,3)
            elif action in BACK:
                return action
                    
    def back_quit(self,action,limit):
        action_test = True
        self.app.back_quit()
        while action_test == True:
            action = input("Select an option: ")
            try:
                if int(action) > 0 and int(action) < limit+1:
                    action_test = False
                    return action
                else:
                    print("Invalid input,")
            except ValueError:
                if action in BACK:
                    self.main_menu()
                elif action in QUIT:
                    quit()
                else:
                    print("Invalid input,")

    def employee_menu(self,action):
        self.app.print_employee_menu()
        while action not in QUIT:
            action = self.back_quit(action,4)
            if action == "1":
                self.add_employee()
            elif action == "2":
                self.change_employee_info()
            elif action == "3":
                self.app.print_show_schedule()
                self.show_emp_schedule(action)
            elif action == "4":
                self.app.print_select_employee_menu()
                action = self.back_quit(action,3)
                if action == "1":
                    self.get_all_employee()
                elif action == "2":
                    self.get_pilots()
                elif action == "3":
                    self.get_cabin_crew()


    def show_emp_schedule(self, action):
        print("[1] Date [2]employee")
        action = input("Select an option: ")
        if action == '1':
            temp_date = input("Enter from date: YYYY-MM-DD:")
            date= dateutil.parser.parse(temp_date)
            self.get_emp_date_schedule(date)
        elif action == '2':
            ID = input("Enter ID number: ")
            self.get_voyages_for_employee(ID)


    def get_emp_date_schedule(self, date):
        available_list = self.ll.get_emp_date_schedule(date)
        for emp in available_list:
            print(str(emp))
            
    def add_voyage(self):
        voyage = Voyage()
        voyage_list = self.ll.get_all_voyages()
        last_booking_ref = int(voyage_list[-1].get_booking_reference())
        voyage.set_booking_reference(last_booking_ref+1)
        voyage.set_arriving_at(input("Destination: "))
        voyage.set_flight_number_away("NA0500")
        voyage.set_flight_number_home("NA0501")
        depart = input("Departure date (YYYY-MM-DD): ") + "T" + input("Departure time(HH:MM): ")
        departure = dateutil.parser.parse(depart)
        voyage.set_departure(departure)
        arrival = departure + timedelta(hours=4)
        voyage.set_arrival(arrival)
        plane_list = self.ll.get_all_airplanes()
        self.app.print_selection_list(plane_list)
        voyage.set_aircraft_id("TF-100")
        self.ll.add_voyage(voyage)

    def change_voyage():
        #self.app.print_change_voyage()
        voyage_list = self.ll.get_all_voyages()
        action = input("Enter ID number: ")
        for index in range(len(voyage_list)):
            voyage = voyage_list[index]
            if action == voyage.get_booking_reference():
                #self.app.print_changing_voyage_information(voyage)
                option = int(input("What do you want to change? "))
                changed = input("Enter new input: ")
                self.ll.change_voyage(voyage_list,index,option,changed)

    def assign_crew(self):
    #self.app.print_assign_crew()
        voyage_list = self.ll.get_all_voyages()
        action = input("Enter booking reference: ")
        for index in range(len(voyage_list)):
            voyage = voyage_list[index]
            if action == voyage.get_booking_reference():
                #self.app.print_changing_voyage_information(voyage)
                voyage.set_captain(input("Captain: "))
                voyage.set_copilot(input("Copilot: "))
                voyage.set_fsm(input("Flight service manager: "))
                voyage.set_fa1(input("Flight attendant: "))
                voyage.set_fa2(input("Flight attendat: "))
                voyage_list[index] = voyage
                self.ll.assign_crew(voyage_list)

    def get_date_voyages(self, from_date, to_date):
        voyage_list = self.ll.get_date_voyages(from_date, to_date)
        #print("{:<20}{:<20}{:<20}".format("Name","SSN","Role"))
        for voyage in voyage_list:
            print(voyage.get_booking_reference())

    def get_voyages_for_employee(self, ID):
        temp_date = input("Enter from date: YYYY-MM-DD:")
        from_date= dateutil.parser.parse(temp_date)
        temp_date = input("Enter to date: YYYY-MM-DD:")
        to_date= dateutil.parser.parse(temp_date) + timedelta(days=1)
        time_voyage_list = self.ll.get_date_voyages(from_date,to_date)
        voyage_list = self.ll.get_voyages_for_employee(ID,time_voyage_list)
        for voyage in voyage_list:
            self.app.print_voyage_info(voyage)
            #print(voyage.get_booking_reference())
            
    def Voyage_menu(self,action):
        self.app.print_voyage_menu()
        action = ""
        while action not in QUIT:
            action = input("select an option: ")
            if action == "1":
                self.app.print_add_voyage()
                self.add_voyage()
            elif action == "2":
                self.assign_crew()
            elif action == "3":
                self.app.print_voyage_selection()
                action = input("select an option: ")
                if action =="1":
                    the_date = input("Enter date: YYYY-MM-DD:")                    
                    from_date= dateutil.parser.parse(the_date)
                    to_date = from_date + timedelta(days=1)
                    voyage_list = self.ll.get_date_voyages(from_date,to_date)
                    for voyage in voyage_list:
                        print(str(voyage))
                elif action == "2":
                    ID = input("Enter ID number")
                    self.get_voyages_for_employee(ID)
            elif action == "4":
                self.change_voyage()
    
    def change_plane_status(self,action): #VINNA Í ÞESSU og nota þenna!
        airplane_list = self.ll.get_all_airplanes()
        #app.fall(airplane_list) svipað fall og print selection list
        self.app.print_change_plane_status(airplane_list)
        action = self.back_quit(action,len(airplane_list))
        for index in range(0,len(airplane_list)):
            if int(action) == (index+1):
                self.ll.change_plane_status(airplane_list,index)
                print("You have changed the plane status")
        self.main_menu()
    
    def get_all_plane(self):
        plane_list = self.ll.get_all_airplanes()
        #self.app.print_all_planes()
        print("{:<20}{:<13}{:<13}{:<13}".format("Registration Number","Plane Type","Model","Capacity"))
        for plane in plane_list:
            sting = str(plane)
            lis = sting.split(",")
            print("{:<20}{:<13}{:<13}{:<13}".format(lis[0], lis[2], lis[3], lis[4]))

    
    def airplane_menu(self,action):
        self.app.print_airplane_menu()
        while action not in QUIT:
            action = self.back_quit(action,3)
            if action == "1":
                self.app.print_add_plane()
                self.add_plane()
                print()
                print("You have added a new airplane!")
                print()
            elif action == "2":
                self.change_plane_status(action)

            elif action == "3":
                self.get_all_plane()
                action = self.back_quit(action,3)

    def main_menu(self,action = ""):
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
        quit()

            
