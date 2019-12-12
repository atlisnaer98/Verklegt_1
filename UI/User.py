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
import string

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
        dest.set_airport(input("Airport(XXX): "))
        dest.set_flight_time(input("Time of flight (HH:MM): "))
        dest.set_distance(input("Distance: "))
        dest.set_name_of_contact(input("Emergency contact: "))
        dest.set_emergency_phone_number(input("Emergency contact number: "))
        self.ll.add_dest(dest)

    def get_all_dest(self):
        dest_obj = self.ll.get_all_dest()
        self.app.print_get_all_dest()
        print("{:<20}{:<20}{:<20}".format("Airport","Country","Distance(km)"))
        for destination in dest_obj:
            #sting = str(line)
            #lis = sting.split(",")
            #print("{:<20}{:<20}{:<20}".format(lis[2], lis[1], lis[4]+'km')) 
            self.app.print_list_dest_info(destination)
    
    def add_plane(self):
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
        self.app.print_get_all_employess()
        print("{:<20}{:<20}{:<20}".format("Name","SSN","Role"))
        for employee in employee_list:
            self.app.print_get_all_employess_role(employee)

    def add_employee(self):
        #self.app.print_add_employee()                          Búa til þetta í apperance
        plane_list = []
        role_list = ["Pilot","Cabincrew"]
        pilot_rank_list = ["Captain","Copilot"]
        cabincrew_rank_list = ["Flight Service Manager", "Flight Attendant"]
        emp = Employee()
        emp.set_ssn(input("ID number: "))
        emp.set_name(input("Name: "))
        emp.set_address(input("Adress: "))
        emp.set_home_phone(input("Home phone: "))
        emp.set_mobile_number(input("Mobile number: "))
        emp.set_email_address(input("Email: "))
        print("role:")
        self.app.print_selection_list(role_list)
        role_selection = self.validate_selection(input("Select a role: "),2)
        for role_index in range(len(role_list)):
            if role_selection == str(role_index+1) and int(role_selection)==1:
                role_selection = role_list[role_index]
                selected_rank_list = pilot_rank_list
            elif role_selection == str(role_index+1) and int(role_selection)==2:
                role_selection = role_list[role_index]
                selected_rank_list = cabincrew_rank_list
        emp.set_role(role_selection)
        self.app.print_selection_list(selected_rank_list)
        rank_selection = self.validate_selection(input("select a rank: "),2)
        if role_selection == "Cabincrew":
            if rank_selection == "1":
                rank_selection = "Flight Service Manager"
            elif rank_selection == "2":
                rank_selection = "Flight Attendant"
        elif role_selection == "Pilot":
            if rank_selection == "1":
                rank_selection = "Captain"
            elif rank_selection == "2":
                rank_selection = "Copilot"
        emp.set_rank(rank_selection)
        airplane_obj = self.ll.get_all_airplanes()
        for index in range(len(airplane_obj)):
            plane = airplane_obj[index]
            plane_type = plane.get_planeID()
            if plane_type not in plane_list:
                plane_list.append(plane_type)
        if role_selection == "Cabincrew":
            plane_selection = "N/A"
        elif role_selection == "Pilot":
            self.app.print_selection_list(plane_list)
            plane_selection = self.validate_selection(input("Select a licence: "),len(plane_list))
            for selected_numb in range(len(plane_list)):
                if plane_selection == str(selected_numb+1):
                    plane_selection = plane_list[selected_numb]
        emp.set_licence(plane_selection)
        emp.set_activity(1)
        self.ll.add_employee(emp)



    def validate_selection(self,action,limit):
        validation = True
        while validation == True:
            try:
                if int(action) > 0 and int(action) < limit+1:
                    validation = False
                    return action
                else:
                    action = input("Invalid input, please re-enter: ")
            except ValueError:
                action = input("Invalid input, please re-enter: ")

    def change_employee_info(self):
        self.app.print_change_employee_info()
        employee_list = self.ll.get_all_employees()
        action = input("Enter ID number: ")
        for index in range(len(employee_list)):
            emp = employee_list[index]
            if action == emp.get_ssn():
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
        
    def get_cabin_crew(self): #Laga og bæta 
        cabin_crew_list = self.ll.get_cabin_crew()
        self.app.print_get_all_cabincrew()
        print("{:<20}{:<20}{:<20}".format("Name","SSN","Rank"))
        for employee in cabin_crew_list:
            #sting = str(line)
            #lis = sting.split(",")
            #print("{:<20}{:<20}{:<20}".format(lis[1],lis[0],lis[7]))
            self.app.print_get_all_employess_rank(employee)

    def get_pilots(self):
        self.app.select_license()
        license = ''
        while license not in QUIT:
            license = self.back_quit(license,4)
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
                print("{:<20}{:<20}{:<20}".format(lis[1],lis[0],lis[8]))        #Nota model föllin og færa í apperance

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
        print("[1]Date     [2] Employee")
        action = input("Select an option: ")
        if action == '1':
            print("[1]Available     [2] Working")
            action = input("Select an option: ")
            temp_date = input("Enter from date: YYYY-MM-DD:")
            from_date = dateutil.parser.parse(temp_date)
            to_date = from_date + timedelta(days=1)
            if action == '1':
                self.get_available_emp_date_schedule(from_date,to_date)
            elif action == '2':
                self.get_working_emp_date_schedule(from_date,to_date)
        elif action == '2':
            ID = input("Enter ID number: ")
            self.get_voyages_for_employee(ID)

    def get_available_emp_date_schedule(self, date,action):
        available_list = self.ll.get_emp_date_schedule(date,action)
        print("{:<20}{:<20}{:<20}".format("Name","SSN","Role"))
        for emp in available_list:
            self.app.print_get_all_employess_role(emp)


    def get_working_emp_date_schedule(self,from_date, to_date):
        time_voyage_list = self.ll.get_voyages_on_date(from_date,to_date)
        employee_dict = self.ll.get_all_employees_dict()
        self.app.print_working_employee()
        print("{:<20}{:<20}{:<20}".format("Name","SSN","Destination"))
        for voyage in time_voyage_list:
            print(str(voyage))
            #self.app.print_working_emps(voyage,employee_dict)
            
    def add_voyage(self):
        voyage = Voyage()
        voyage_list = self.ll.get_all_voyages()
        last_booking_ref = int(voyage_list[-1].get_booking_reference())
        voyage.set_booking_reference(last_booking_ref+1)
        dest_list = self.ll.get_all_dest()
        self.app.print_selection_list(dest_list)
        dest_number = int(input("Please select destination: ")) - 1
        dest = dest_list[dest_number].get_destination()
        voyage.set_arriving_at(dest)
        voyage.set_flight_number_away("NA0500")
        voyage.set_flight_number_home("NA0501")
        depart = input("Departure date (YYYY-MM-DD): ") + "T" + input("Departure time(HH:MM): ")
        departure = dateutil.parser.parse(depart)
        voyage.set_departure(depart)
        arrival = departure + timedelta(hours=4)
        voyage.set_arrival(arrival.isoformat())
        plane_list = self.ll.get_available_planes(departure,arrival)
        self.app.print_selection_list(plane_list)
        plane_number = int(input("Select an airplane: ")) - 1
        plane = plane_list[plane_number].get_registration_number()
        voyage.set_aircraft_id(plane)
        self.ll.add_voyage(voyage)

    def change_voyage(self):
        #self.app.print_change_voyage()                     Búa til þetta method í apperance
        voyage_list = self.ll.get_all_voyages()
        action = input("Enter booking reference: ")
        for index in range(len(voyage_list)):
            voyage = voyage_list[index]
            if action == voyage.get_booking_reference():
                #self.app.print_changing_voyage_information(voyage)
                departure = dateutil.parser.parse(voyage.get_departure())
                arrival = dateutil.parser.parse(voyage.get_arrival())
                plane_list = self.ll.get_available_planes(departure,arrival)
                self.app.print_selection_list(plane_list)
                plane_number = int(input("Select an airplane: ")) - 1
                plane = plane_list[plane_number].get_registration_number()
                voyage.set_aircraft_id(plane)
                self.ll.change_voyage(voyage_list,index,plane)

    def assign_crew(self):
        available_fa = []
        self.app.print_assign_crew()
        voyage_list = self.ll.get_all_voyages()
        employee_list = self.ll.get_all_employees()
        airplane_list = self.ll.get_all_airplanes()
        print("{}{:>15}{:>20}".format("Booking referance","Destination","Departure"))
        for voyage in voyage_list:
            if voyage.get_captain() == "" or voyage.get_copilot() == "" or voyage.get_fsm() == "":
                highest_selection = int(voyage.get_booking_reference())
                self.app.print_voyage_selection_list(voyage)
        action = self.back_quit("",highest_selection)
        for index in range(len(voyage_list)):
            voyage = voyage_list[index]
            if action == voyage.get_booking_reference():
                self.clear_voyage_crew(voyage_list,index)
                for airplane in airplane_list:
                    if voyage.get_aircraft_id() == airplane.get_registration_number():
                        licence = airplane.get_planeID()             
                self.set_captain(voyage,employee_list,licence,)
                self.set_copilot(voyage,employee_list,licence)
                self.set_fsm(voyage,employee_list)
                voyage.set_fa1(input("Flight attendant: "))
                voyage.set_fa2(input("Flight attendat: "))
                voyage_list[index] = voyage
                self.ll.assign_crew(voyage_list)

    def clear_voyage_crew(self,voyage_list,index):
        voyage = voyage_list[index]
        voyage.set_captain("")
        voyage.set_copilot("")
        voyage.set_fsm("")
        voyage.set_fa1("")
        voyage.set_fa2("")
        voyage_list[index] = voyage
        self.ll.assign_crew(voyage_list)

    def available_empoyees(self,voyage):
        available_emp_list = []
        voyage_date_from = dateutil.parser.parse(voyage.get_departure())
        voyage_date_to = dateutil.parser.parse(voyage.get_arrival())
        emp_obj = self.ll.get_emp_date_schedule(voyage_date_from,voyage_date_to)
        for emp in emp_obj:
            available_emp_list.append(emp.get_ssn())
        return available_emp_list

    def set_captain(self,voyage,employee_list,licence):
        available_captain_list = []
        available_emp_list = self.available_empoyees(voyage)   
        for captain in employee_list:
            if captain.get_rank() == "Captain" and captain.get_activity() == "1" and licence == captain.get_licence() and captain.get_ssn() in available_emp_list:
                available_captain_list.append(captain.get_name())
        self.app.print_selection_list(available_captain_list)
        captain_selection = self.back_quit("",len(available_captain_list))
        for captain_index in range(len(available_captain_list)):
            if captain_index+1 == int(captain_selection):
                for emp in employee_list:
                    if emp.get_name() == available_captain_list[captain_index]:
                        voyage.set_captain(emp.get_ssn())

    def set_copilot(self,voyage,employee_list,licence):
        available_copilot_list = []
        available_emp_list = self.available_empoyees(voyage)
        for copilot in employee_list:
            if copilot.get_rank() == "Copilot" and copilot.get_activity() == "1" and licence == copilot.get_licence() and copilot.get_ssn() in available_emp_list:
                available_copilot_list.append(copilot.get_name())
        self.app.print_selection_list(available_copilot_list)
        copilot_selection = self.back_quit("",len(available_copilot_list))
        for copilot_index in range(len(available_copilot_list)):
            if copilot_index+1 == int(copilot_selection):
                for emp in employee_list:
                    if emp.get_name() == available_copilot_list[copilot_index]:
                        voyage.set_copilot(emp.get_ssn())

    def set_fsm(self,voyage,employee_list):
        available_fsm_list = []
        available_emp_list = self.available_empoyees(voyage)
        for fsm in employee_list:
            if fsm.get_rank() == "Flight Service Manager" and fsm.get_activity() =="1" and fsm.get_ssn() in available_emp_list:
                available_fsm_list.append(fsm.get_name())
        self.app.print_selection_list(available_fsm_list)
        fsm_selection = self.back_quit("",len(available_fsm_list))
        for fsm_index in range(len(available_fsm_list)):
            if fsm_index + 1 == int(fsm_selection):
                for emp in employee_list:
                    if emp.get_name() == available_fsm_list[fsm_index]:
                        voyage.set_fsm(emp.get_ssn())

    def get_date_voyages(self, from_date, to_date):
        voyage_list = self.ll.get_date_voyages(from_date, to_date)
        #print("{:<20}{:<20}{:<20}".format("Name","SSN","Role"))
        for voyage in voyage_list:
            print(voyage.get_booking_reference())

#self.app.print_voy_lsfasldf(voyage_list,"Manned")
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
                    self.get_voyages_for_single_date()
                elif action == "2":
                    ID = input("Enter ID number")
                    self.get_voyages_for_employee(ID)
                elif action == "3":
                    self.get_voyages_for_timeperiod()
            elif action == "4":
                self.change_voyage()
    
    def get_voyages_for_single_date(self):
        the_date = input("Enter date: YYYY-MM-DD:")                    
        from_date= dateutil.parser.parse(the_date)
        to_date = from_date + timedelta(days=1)
        voyage_list = self.ll.get_date_voyages(from_date,to_date)
        self.print_voyages_manned(voyage_list)
    
    def get_voyages_for_timeperiod(self): #Þarf að vera valkostur fyrir þetta í apperance
        temp_date = input("Enter from date: YYYY-MM-DD:")                    
        from_date = dateutil.parser.parse(temp_date)
        temp_date = input("Enter to date: YYYY-MM-DD:")     
        to_date = dateutil.parser.parse(temp_date)
        voyage_list = self.ll.get_date_voyages(from_date,to_date)
        self.print_voyages_manned(voyage_list)

    def print_voyages_manned(self,voyage_list):
        for voyage in voyage_list:
            if len(voyage.get_captain()) == 10 and len(voyage.get_copilot()) == 10 and len(voyage.get_fsm()) == 10:
                self.app.print_voyage_list_with_crew(voyage,"Manned")
            else:
                self.app.print_voyage_list_with_crew(voyage,"Unmanned")

    
    def change_plane_status(self,action): #VINNA Í ÞESSU og nota þenna!
        # The method will print out all airplanes in a list with information if the airplane is active or inactive.
        # You are able to make airplane active or inactive in this method.
        airplane_list = self.ll.get_all_airplanes()
        #app.fall(airplane_list) svipað fall og print selection list
        self.app.print_change_plane_status(airplane_list)
        action = self.back_quit(action,len(airplane_list))
        for index in range(0,len(airplane_list)):
            if int(action) == (index+1):
                self.ll.change_plane_status(airplane_list,index)
                print()
                print("You have changed the plane status")
                print()
        self.main_menu()
    

    def get_all_plane(self):
        # The method will print out all airplanes in a list with certain information.
        plane_list = self.ll.get_all_airplanes()
        self.app.print_list_plane
        #self.app.print_all_planes()
        print("{:<20}{:<13}{:<13}{:<13}".format("Registration Number","Plane Type","Model","Capacity"))
        for plane in plane_list:
            self.app.print_list_plane_info(plane)

    
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

            
