from Models.Employee import Employee
from InformationLayerClasses.API import Data_main
import datetime
import dateutil.parser
from datetime import timedelta
from Services.VoyageLL import VoyageLL

class EmployeeLL():
        
    def __init__(self, sending):
        self.dl = sending
        self.vLL = VoyageLL(sending)
    
    def get_all_employees(self):
        ''' Calls the data layer and returns a list of all the employees in the company '''
        return self.dl.get_all_employee()

    def get_all_employees_dict(self):
        ''' Calls the data layer and returns a dictionary of all the employees in the company '''
        return self.dl.get_all_employees_dict()

    def get_employee(self, action):
        '''Compares the SSN input by the user and sees if it matches the SSN of an existing employee working for the company'''
        employee_list = []
        all_employee_list = self.dl.get_all_employee()
        for emp in all_employee_list:
            ssn = emp.get_ssn()
            if ssn == action:
                employee_list.append(emp)
        return employee_list

    def add_employee(self,emp):
        ''' forwards the information input by the user about a new employee and creates a new employee'''
        self.dl.add_employee(emp)

    def change_employee(self,employee_list,index,option,changed):
        '''Changes a specific information about the employee selected by the user, forwards the information
        to the dl where the information is changed'''
        emp = employee_list[index]
        if option == 1:
            emp.set_address(changed)
        elif option == 2:
            emp.set_home_phone(changed)
        elif option == 3:
            emp.set_mobile_number(changed)
        elif option == 4:
            emp.set_email_address(changed)
        elif option == 5:
            current_activity = emp.get_activity()
            if current_activity == "1":
                changed = "0"
                print()
                print("{} is now Inactive".format(emp.get_name()))
                print()
            elif current_activity == "0":
                changed = "1"
                print()
                print("{} is now Active".format(emp.get_name()))
                print()

            emp.set_activity(changed)
        else: 
            return False
        employee_list[index] = emp
        self.dl.update_employee_file(employee_list)

    def get_cabin_crew(self):
        '''Fetches a list of cabin crew from the data layer'''
        cabin_crew_list = []
        all_employee_list = self.dl.get_all_employee()
        for emp in all_employee_list:
            role = emp.get_role()
            if role == "Cabincrew":
                cabin_crew_list.append(emp)
        return cabin_crew_list
    
    def get_pilots(self, license):
        ''' fetches a list of pilots from the data layer'''
        pilot_list = []
        all_employee_list = self.dl.get_all_employee()
        for emp in all_employee_list:
            role = emp.get_role()
            if license == "All" and role == 'Pilot':
                pilot_list.append(emp)
            elif emp.get_licence() == license:
                pilot_list.append(emp)
        
        return pilot_list


    def get_date_schedule(self,from_date,to_date):
        '''fetches a list of all voyages and compares all of them to the timperiod input by the user and returns
        only the voyages that are within that timeframe and sees'''
        temp_list = []
        all_voyage_list = self.dl.get_all_voyages() 
        for voyage in all_voyage_list:
            dep_date = dateutil.parser.parse(voyage.get_departure())
            arr_date = dateutil.parser.parse(voyage.get_arrival())
            if (from_date <= dep_date and dep_date < to_date) or (from_date <= arr_date and arr_date < to_date):
                temp_list.append(voyage)
        final_list = self.available_employees(temp_list)
        return final_list

    def available_employees(self, voyage_list):
        ''' fetches a list of all employees and checks what employees are available for a specific voyage'''
        all_employees = self.get_all_employees()
        list_of_available = []
        list_of_working = []
        for employee in all_employees:
            ssn = employee.get_ssn()
            for voyage in voyage_list:
                crew = self.vLL.get_crew(voyage)
                if ssn in crew and employee not in list_of_working:
                    list_of_working.append(employee)
            if employee not in list_of_working and employee.get_activity() == "1":
                list_of_available.append(employee)
        return list_of_available
            

        
