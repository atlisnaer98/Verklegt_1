from Services.AirplaneLL import AirplaneLL
from Services.DestinationLL import DestinationLL
from Services.EmployeeLL import EmployeeLL
from Services.VoyageLL import VoyageLL
from InformationLayerClasses.API import Data_main
from Services.Validation import Validation

class LLApi:
    def __init__(self):
        self.dl = Data_main()
        self.aLL = AirplaneLL(self.dl)
        self.dLL = DestinationLL(self.dl)
        self.eLL = EmployeeLL(self.dl)
        self.vLL = VoyageLL(self.dl)
        self.valLL = Validation()

    def get_all_airplanes(self):
        return self.aLL.get_all_airplanes()

    def get_available_planes(self,from_date,to_date):
        return self.aLL.get_available_planes(from_date,to_date)

    def add_plane(self, plane):
        self.aLL.add_plane(plane)
    
    def change_plane_status(self,airplane_list,index):
        self.aLL.change_plane(airplane_list,index)

    def add_dest(self, dest):
        self.dLL.add_dest(dest)

    def get_all_dest(self):
        return self.dLL.get_all_dest()

    def change_dest(self,dest_list,index,option,changed):
        self.dLL.change_dest(dest_list,index,option,changed)

    def get_dest_flight_number(self):
        return self.dLL.get_flight_number()

    def get_all_employees(self):
        return self.eLL.get_all_employees()

    def get_all_employees_dict(self):
        return self.eLL.get_all_employees_dict()

    def change_employee(self,employee_list,index,option,changed):
        self.eLL.change_employee(employee_list,index,option,changed)
    
    def add_employee(self, emp):
        self.eLL.add_employee(emp)
    
    def get_cabin_crew(self):
        return self.eLL.get_cabin_crew()

    def get_pilots(self, license):
        return self.eLL.get_pilots(license)

    def get_all_voyages(self):
        return self.vLL.get_all_voyages()

    def get_date_voyages(self,from_date,to_date):
        return self.vLL.get_date_voyages(from_date,to_date)
    
    def get_voyages_on_date(self,from_date,to_date):
        return self.vLL.get_date_voyages(from_date,to_date)

    def add_voyage(self,voyage):
        self.vLL.add_voyage(voyage)

    def change_voyage(self,voyage_list,index,plane):
        self.vLL.change_voyage(voyage_list,index,plane)

    def get_crew(self,voyage):
        self.vLL.get_crew(voyage)

    def assign_crew(self,voyage_list):
        self.vLL.assign_crew(voyage_list)

    def get_voyages_for_employee(self,ID,voyage_list):
        ''' takes staff ID and returns all the voyages for a specific employee'''
        return self.vLL.get_voyages_for_employee(ID,voyage_list)

    def get_voyage_status(self,voyage,date):
        return self.vLL.get_voyage_status(voyage,date)
    
    def get_emp_date_schedule(self, from_date, to_date):
        return self.eLL.get_date_schedule(from_date,to_date)     
        
    def count_dest_flights(self,dest,place,time):
        return self.vLL.count_dest_flights(dest,place,time)

    def update_flight_nums(self):
        return self.vLL.update_flight_nums()
    
    def get_departure(self):
        return self.vLL.get_departure()

    def validate_distance(self,distance_input):
        return self.valLL.validate_distance(distance_input)
    
    def validate_airport(self,airport_input):
        return self.valLL.validate_airport(airport_input)
    
    def validate_name(self,name_input):
        return self.valLL.validate_name(name_input)
    
    def validate_phone_number(self,phone_number):
        return self.valLL.validate_phone_number(phone_number)
    
    def validate_time(self,time_input):
        return self.valLL.validate_time(time_input)

    def validate_home(self,address_input):
        return self.valLL.validate_home(address_input)
    
    def validate_email(self, email_address):
        return self.valLL.validate_email(email_address)

    def validate_selection(self,action,limit):
        return self.valLL.validate_selection(action,limit)
    
    def validate_date(self,date_input):
        return self.valLL.validate_date(date_input)
    
    def validate_reg(self,reg_input):
        return self.valLL.validate_reg(reg_input)
    
    def validate_existing_reg(self,reg_input,plane_list):
        return self.valLL.validate_existing_reg(reg_input,plane_list)
    
    def validate_ssn(self,ssn_input):
        return self.valLL.validate_ssn(ssn_input)

    def validate_existing_emp(self,ssn_input,employee_list):
        return self.valLL.validate_existing_emp(ssn_input,employee_list)
    
    def validate_already_emp(self,ssn_input,employee_list):
        return self.valLL.validate_already_emp(ssn_input,employee_list)
    
    def validate_dest(self,dest_input,dest_list):
        return self.valLL.validate_dest(dest_input,dest_list)

    def validate_period(self,from_date,to_date):
        return self.valLL.validate_period(from_date,to_date)