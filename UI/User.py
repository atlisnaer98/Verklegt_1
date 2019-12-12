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
        # The method will add destinations and ask for needed information as input to make a new destination.
        dest = Destination()
        dest.set_destination(self.validate_name(input("Destination: ")))
        dest.set_country(self.validate_name(input("Country: ")))
        dest.set_airport(self.validate_airport(input("Airport(XXX): ")))
        dest.set_flight_time(self.validate_time(input("Time of flight (HH:MM): ")))
        dest.set_distance(self.validate_distance(input("Distance: ")))
        dest.set_name_of_contact(self.validate_name(input("Emergency contact: ")))
        dest.set_emergency_phone_number(self.validate_phone_number(input("Emergency contact number: ")))
        dest.set_flight_number(self.ll.get_dest_flight_number())
        self.ll.add_dest(dest)

    def validate_distance(self,distance_input):
        # The method will check if the input of distance is valid, only number allowed. 
        distance_repeater = True
        while distance_repeater == True:
            try:
                if int(distance_input) <= 0:
                    distance_input = input("Invalid input, please re-enter distance: ")
                else:
                    return distance_input
            except ValueError:
                distance_input = input("Invalid input, please re-enter distance: ")

    def validate_airport(self,airport_input):
        # The method checks the airport is validate. User is only allowed to enter letters. It is invalid if user put in for example numbers. 
        airport_repeater = True
        numb_list = ["0","1","2","3","4","5","6","7","8","9"]
        while airport_repeater == True:
            if len(airport_input) > 3 or len(airport_input) < 3:
                airport_input = input("Invalid input, please re-enter airport(XXX)")
            else:
                for letter in airport_input:
                    if letter in numb_list or letter in string.punctuation:
                        airport_input = input("Invalid input, please re-enter airport(XXX)")
                    else:
                        return airport_input.upper()

    def validate_name(self,name_input):
        # The method will check if the name is validate, user can only put in letters to proceed. 
        counter = 0
        name_repeater = True
        while name_repeater == True:
            splitted_name  = name_input.split(" ")
            name_len = len(splitted_name)
            for name in splitted_name:
                if name.isalpha():
                    counter += 1
                else:
                    name_input = input("The name has to only contain letters, please re-enter name: ")
                    break 
            if counter == name_len: 
                name_repeater = False        
        return name_input.title()
    
    def validate_phone_number(self,phone_number):
        # The method will check if the user put in number as a phone number. 
        true_check = True
        while true_check == True:
            if phone_number.isdigit():
                true_check = False
                return phone_number
            else:
                phone_number = input("Invalid input,  please re-enter (only integers) Emergency contact number:")

    def get_all_dest(self):
        # The method will print out all listed destinations, the output will be Airport, Country and Distance from Reykjavik in km.
        dest_obj = self.ll.get_all_dest()
        self.app.print_get_all_dest()
        print("{:<20}{:<20}{:<20}".format("Airport:","Country:","Distance(km):"))
        for destination in dest_obj:
            self.app.print_list_dest_info(destination)
    
    def add_plane(self):
        # The method will add new aircraft, you will have to give the plane a registration number and choose model, when model is choosen it will automacly put how many passenger can trave
        plane = Airplane()
        plane.set_registration_number(self.validate_reg(input("Registration number(TF-XXX): ")))
        self.app.print_add_plane_vol2()
        option = self.validate_selection(input("Model: "),3)
        self.set_plane_model(plane,option)
        plane.set_active(1)
        self.ll.add_plane(plane)

    def validate_reg(self,reg_input):
        # The method will check if the registration number is valid. The number has to start with TF- to be valid and contain 3 letters.
        reg_repeater = True
        while reg_repeater == True:
            if reg_input[:3] != "TF-":
                print("""The registration number has to start with "TF-""")
                reg_input = input("please re-enter: ")
            else:
                last_three = reg_input.split("-")
                for name in last_three[1:]:
                    if name.isalpha():
                        reg_repeater = False
                    else:
                        reg_input = input("Invalid input, please re-enter:")
                    break
        return reg_input.upper()

    def set_plane_model(self,plane,option):
        # The method will add certain information when certain number is chosen
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
        # The method will print out all employess, the output will be theire name, social security number and theire role.
        employee_list = self.ll.get_all_employees()
        self.app.print_get_all_employess()
        print("{:<20}{:<20}{:<20}".format("Name:","SSN:","Role:"))
        for employee in employee_list:
            self.app.print_get_all_employess_role(employee)

    def add_employee(self):
        # The method will add new employee to the Crew.csv file. 
        # User have to input SSN number, Name, Adress, Home and Mobile number, Email and chose role and rank for the employee.
        # If pilot is chosen then the user has to enter a licence number for the aircraft that he is allowed to fly. 
        self.app.print_create_employee()
        plane_list = []
        role_list = ["Pilot","Cabincrew"]
        pilot_rank_list = ["Captain","Copilot"]
        cabincrew_rank_list = ["Flight Service Manager", "Flight Attendant"]
        emp = Employee()
        emp.set_ssn(input("SSN number: "))
        emp.set_name(self.validate_name(input("Name: ")))
        emp.set_address(input("Adress: "))
        emp.set_home_phone(self.validate_phone_number(input("Home phone: ")))
        emp.set_mobile_number(self.validate_phone_number(input("Mobile number: ")))
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
        # The method will change employee information. The user is not able to change SSN number, Name, Rank or Role. 
        self.app.print_change_employee_info()
        employee_list = self.ll.get_all_employees()
        action = input("Enter SSN number: ")
        for index in range(len(employee_list)):
            emp = employee_list[index]
            if action == emp.get_ssn():
                self.app.print_employee_information(emp)
                print("Would you like to change any information?")
                self.app.print_yes_no()
                change_selection = self.back_quit(action,2)
                if change_selection == "1":
                    self.app.print_changing_employee_information(emp)
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
        # The method will change destination information. User is only able to change Emergency contact and Emergency phonenumber.
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
                if action == '1':
                    changed = self.validate_name(input("Enter new input: "))
                elif action == '2':
                    changed = self.validate_phone_number(input("Enter new input: "))
                self.ll.change_dest(dest_list,index,int(action),changed)
        
    def get_cabin_crew(self):
        # The method will print out all cabin crew employees, the output will be their Name, SSN number and Rank. 
        cabin_crew_list = self.ll.get_cabin_crew()
        self.app.print_get_all_cabincrew()
        print("{:<20}{:<20}{:<20}".format("Name:","SSN:","Rank:"))
        for employee in cabin_crew_list:
            self.app.print_get_all_employess_rank(employee)

    def get_pilots(self):
        # The method will print out all pilots, you can choose if you want all pilots or you want to print pilot with licence on surten aircraft.
        self.app.print_choose_aircraft()
        self.app.select_licence()
        licence = ''
        while licence not in QUIT:
            licence = self.back_quit(licence,4)
            if licence == '1':
                licence = 'NAFokkerF100'
            elif licence == '2':
                licence = 'NABAE146'
            elif licence == '3':
                licence = 'NAFokkerF28'
            elif licence == '4':
                licence = 'All'
            pilot_list = self.ll.get_pilots(licence)
            self.app.print_get_all_pilots()
            print("{:<20}{:<13}{:<13}{:<13}".format("Name:","SSN:","Licence:","Model:"))
            for employee in pilot_list:
                self.app.print_get_all_pilot_rank_and_licence(employee)

    def printing_picture(self):
        self.app.picture()

    def dest_menu(self,action):
        # The method will give you options in destinations menu, user has to choose number to deside what he want to do.
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
            action = input("\nSelect an option:")
            print()
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
        # The method will give you options in employee menu, user has to choose number to deside what he want to do.
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
        # The method will show you employee schedule. User has to choose between to give Date og SSN number as a input.
        self.app.print_employee_schedule()
        action = self.back_quit(action, 2)
        if action == '1':
            self.app.print_employee_available_or_working()
            action = self.back_quit(action, 2)
            temp_date = self.validate_date(input("Enter from date (YYYY-MM-DD):"))
            from_date = dateutil.parser.parse(temp_date)
            to_date = from_date + timedelta(days=1)
            if action == '1':
                self.get_available_emp_date_schedule(from_date,to_date)
            elif action == '2':
                self.get_working_emp_date_schedule(from_date,to_date)
        elif action == '2':
            ID = input("Enter ID number: ")
            self.get_voyages_for_employee(ID)

    def get_available_emp_date_schedule(self,from_date,to_date):
        # The method will print out all available employees, their SSN number and role
        available_list = self.ll.get_emp_date_schedule(from_date,to_date)
        print("{:<20}{:<20}{:<20}".format("Name:","SSN:","Role:"))
        for emp in available_list:
            self.app.print_get_all_employess_role(emp)

    def get_working_emp_date_schedule(self,from_date, to_date):
        counter = 0
        time_voyage_list = self.ll.get_voyages_on_date(from_date,to_date)
        employee_dict = self.ll.get_all_employees_dict()
        self.app.print_working_employee()
        if len(time_voyage_list) == 0:
            print("There are no flights on this date")
        else:
            for voyage in time_voyage_list:
                if len(voyage.get_captain()) < 1 and len(voyage.get_copilot()) < 1 and len(voyage.get_fsm()) < 1:
                    counter += 1
                    if counter == len(time_voyage_list):
                        print("No employee has been assigned to a voyage on that date")
                else:
                    print("{:<20}{:<20}{:<20}".format("Name","SSN","Destination"))
                    self.app.print_working_emps(voyage,employee_dict)
   
    def add_voyage(self):
        voyage = Voyage()
        voyage_list = self.ll.get_all_voyages()
        last_booking_ref = int(voyage_list[-1].get_booking_reference())
        voyage.set_booking_reference(last_booking_ref+1)
        dest_list = self.ll.get_all_dest()
        self.app.print_selection_list(dest_list)
        dest_number = int(input("Please select destination: ")) - 1
        dest = dest_list[dest_number]
        destination_place = dest.get_destination()
        voyage.set_arriving_at(destination_place)
        voyage.set_flight_number_away("NA0500") #PLANE NUMBEEER!!!!!!!!!!!
        voyage.set_flight_number_home("NA0501")
        depart = self.validate_date(input("Departure date (YYYY-MM-DD): ")) + "T" + self.validate_time(input("Departure time(HH:MM): ")) + ":00"
        departure = dateutil.parser.parse(depart)
        voyage.set_departure(depart)
        one_way_flight_time = dateutil.parser.parse(dest.get_flight_time())
        arrival = departure + timedelta(hours=one_way_flight_time.hour * 2 + 1, minutes=one_way_flight_time.minute*2)
        voyage.set_arrival(arrival.isoformat())
        plane_list = self.ll.get_available_planes(departure,arrival)
        self.app.print_selection_list(plane_list)
        plane_number = int(input("Select an airplane: ")) - 1
        plane = plane_list[plane_number].get_registration_number()
        voyage.set_aircraft_id(plane)
        self.ll.add_voyage(voyage)
            
    def change_voyage(self):
        self.app.print_change_voyage()
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
        self.app.print_assign_crew()
        voyage_list = self.ll.get_all_voyages()
        employee_list = self.ll.get_all_employees()
        airplane_list = self.ll.get_all_airplanes()
        print("{:<20}{:<20}{:<20}\n{}".format("Booking","Destination:","Departure:","referance:"))
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
                self.set_captain(voyage,employee_list,licence)
                self.save_crew(voyage,voyage_list,index)
                self.set_copilot(voyage,employee_list,licence)
                self.save_crew(voyage,voyage_list,index)
                self.set_fsm(voyage,employee_list)
                self.save_crew(voyage,voyage_list,index)
                fa1 = self.set_fa(voyage,employee_list)
                voyage.set_fa1(fa1)
                self.save_crew(voyage,voyage_list,index)
                fa2 = self.set_fa(voyage,employee_list)
                voyage.set_fa2(fa2)
                self.save_crew(voyage,voyage_list,index)

    def save_crew(self,voyage,voyage_list,index):
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

    def available_employees(self,voyage):
        available_emp_list = []
        departure_time = dateutil.parser.parse(voyage.get_departure())
        year,month,day = departure_time.year, departure_time.month, departure_time.day
        voyage_date_from = datetime.datetime(year,month,day)
        arrival_time = dateutil.parser.parse(voyage.get_arrival())
        year,month,day = arrival_time.year, arrival_time.month, arrival_time.day
        voyage_date_to = datetime.datetime(year,month,day) + timedelta(days=1)
        emp_obj = self.ll.get_emp_date_schedule(voyage_date_from,voyage_date_to)
        for emp in emp_obj:
            available_emp_list.append(emp.get_ssn())
        return available_emp_list

    def set_captain(self,voyage,employee_list,licence):
        available_captain_list = []
        available_emp_list = self.available_employees(voyage)   
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
        available_emp_list = self.available_employees(voyage)
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
        available_emp_list = self.available_employees(voyage)
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

    def set_fa(self,voyage,employee_list):
        available_fa_list = []
        available_emp_list = self.available_employees(voyage)
        for fa in employee_list:
            if fa.get_rank() == "Flight Attendant" and fa.get_activity() =="1" and fa.get_ssn() in available_emp_list:
                available_fa_list.append(fa.get_name())
        self.app.print_selection_list(available_fa_list)
        fa_selection = self.back_quit("",len(available_fa_list))
        for fa_index in range(len(available_fa_list)):
            if fa_index + 1 == int(fa_selection):
                for emp in employee_list:
                    if emp.get_name() == available_fa_list[fa_index]:
                        return emp.get_ssn()

    def get_date_voyages(self, from_date, to_date):
        voyage_list = self.ll.get_date_voyages(from_date, to_date)
        #print("{:<20}{:<20}{:<20}".format("Name","SSN","Role"))
        for voyage in voyage_list:
            print(voyage.get_booking_reference())

#self.app.print_voy_lsfasldf(voyage_list,"Manned")
    def get_voyages_for_employee(self, ID):
        temp_date = self.validate_date(input("Enter date from (YYYY-MM-DD):"))
        from_date= dateutil.parser.parse(temp_date)
        temp_date = self.validate_date(input("Enter to date (YYYY-MM-DD):"))
        to_date= dateutil.parser.parse(temp_date) + timedelta(days=1)
        time_voyage_list = self.ll.get_date_voyages(from_date,to_date)
        voyage_list = self.ll.get_voyages_for_employee(ID,time_voyage_list)
        self.print_voyages_manned_and_status(voyage_list)

    def validate_date(self,date_input):
        date_repeater = True
        while date_repeater == True:
            try:
                year = int(date_input[:4])
                month = int(date_input[5:7])
                day = int(date_input[8:10])
                if year > 0 and date_input[4] == "-" and date_input[7] == "-" and month > 0 and month <= 12 and day > 0 and day < 31:
                    return date_input
                else:
                    date_input = input("Invalid input, please re-enter (YYYY-MM-DD):")
            except ValueError:
                date_input = input("Invalid input, please re-enter (YYYY-MM-DD):")

    def validate_time(self,time_input):
        time_repeater = True
        while time_repeater == True:
            #time_input = str(time_input)
            try:
                hour = int(time_input[:2])
                minute = int(time_input[4:])
                if hour >= 0 and hour <= 24 and minute >= 0 and minute <= 60 and time_input[2] == ":":
                    #time_repeater = False
                    return time_input
                else:
                    time_input = input("Invalid input, please re-enter (HH:MM): ")
            except ValueError:
                time_input = input("Invalid input, please re-enter (HH:MM): ")
                

    def Voyage_menu(self,action):
        action = ""
        while action not in QUIT:
            self.app.print_voyage_menu()
            action = self.back_quit(action,4)
            if action == "1":
                self.app.print_add_voyage()
                self.add_voyage()
            elif action == "2":
                self.assign_crew()
            elif action == "3":
                self.app.print_voyage_selection()
                action = self.back_quit(action,3)
                if action =="1":
                    self.get_voyages_for_single_date()
                elif action == "2":
                    ID = input("Enter ID number")#ef ekki í fyrirtækinu     self.validate_ssn(
                    self.get_voyages_for_employee(ID)
                elif action == "3":
                    self.get_voyages_for_timeperiod()
            elif action == "4":
                self.change_voyage()
    
    def get_voyages_for_single_date(self):
        the_date = self.validate_date(input("Enter date (YYYY-MM-DD): "))                    
        from_date = dateutil.parser.parse(the_date)
        to_date = from_date + timedelta(days=1)
        voyage_list = self.ll.get_date_voyages(from_date,to_date)
        self.print_voyages_manned_and_status(voyage_list)
    
    def get_voyages_for_timeperiod(self): #Þarf að vera valkostur fyrir þetta í apperance
        temp_date = self.validate_date(input("Enter from date (YYYY-MM-DD): "))                    
        from_date = dateutil.parser.parse(temp_date)
        temp_date = self.validate_date(input("Enter to date (YYYY-MM-DD): "))     
        to_date = dateutil.parser.parse(temp_date)
        voyage_list = self.ll.get_date_voyages(from_date,to_date)
        self.print_voyages_manned_and_status(voyage_list)

    def print_voyages_manned_and_status(self,voyage_list):
        for voyage in voyage_list:
            status = self.ll.get_voyage_status(voyage)
            if len(voyage.get_captain()) == 10 and len(voyage.get_copilot()) == 10 and len(voyage.get_fsm()) == 10:
                self.app.print_voyage_list_with_crew(voyage,"Manned",status)
            else:
                self.app.print_voyage_list_with_crew(voyage,"Unmanned",status)

    def change_plane_status(self,action):
        # The method will print out all airplanes in a list with information if the airplane is active or inactive.
        # You are able to make airplane active or inactive in this method.
        airplane_list = self.ll.get_all_airplanes()
        #app.fall(airplane_list) svipað fall og print selection list
        self.app.print_change_plane_status(airplane_list)
        action = self.back_quit(action,len(airplane_list))
        for index in range(0,len(airplane_list)):
            if int(action) == (index+1):
                self.ll.change_plane_status(airplane_list,index)
                print("\nYou have changed the plane status\n")
        self.main_menu()
    
    def get_all_plane(self):
        # The method will print out all airplanes in a list with certain information. 
        # The output will tell you if the plain is heading or landed in the destination or in Reykjavik.
        plane_list = self.ll.get_all_airplanes()
        voyage_list = self.ll.get_all_voyages()
        self.app.print_list_plane()
        #self.app.print_all_planes()
        #print("{:<20}{:<13}{:<13}{:<13}".format("Registration Number","Plane Type","Model","Capacity"))
        #for plane in plane_list:
        #   self.app.print_list_plane_info(plane)
        self.app.print_selection_list(plane_list)
        index = int(input("Select an airplane: ")) - 1
        plane = plane_list[index]
        reg_num = plane.get_registration_number()
        busy = 0
        for voyage in voyage_list:
            if voyage.get_aircraft_id() == reg_num:
                status = self.ll.get_voyage_status(voyage)
                if status == "On the way to the destination" or status == "On the way to Reykjavik":
                    busy = 1
                    self.app.print_in_air(plane,voyage,status) #Vantar bæta þetta fall
                elif status == "Landed in destination":
                    busy = 1
                    self.app.print_plane_busy(plane,voyage,status) #Vantar bæta þetta fall
        if busy == 0:
            self.app.print_plane_available(plane) #Vantar bæta þetta fall

            
                    

    
    def airplane_menu(self,action):
        # The method will give you options in airplane menu, user has to choose number to deside what he want to do.
        self.app.print_airplane_menu()
        while action not in QUIT:
            action = self.back_quit(action,3)
            if action == "1":
                self.app.print_add_plane()
                self.add_plane()
                print("\nYou have added a new airplane!\n")
            elif action == "2":
                self.change_plane_status(action)

            elif action == "3":
                self.get_all_plane()
                action = self.back_quit(action,3)

    def main_menu(self,action = ""):
        while action not in QUIT:
            self.app.print_main_menu()
            action = input("Select an option: ") # muna að villutjékka þetta
            if action == "1":
                self.employee_menu(action)  
            elif action == "2":
                self.Voyage_menu(action)
                action = input("Select an option: ")
            elif action == "3": #DESTINATION
                self.dest_menu(action)
            elif action == "4":
                self.airplane_menu(action)
        quit()

            
