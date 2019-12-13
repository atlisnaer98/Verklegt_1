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
        return self.dl.get_all_employee()

    def get_all_employees_dict(self):
        return self.dl.get_all_employees_dict()

    def get_employee(self, action):
        employee_list = []
        all_employee_list = self.dl.get_all_employee()
        for emp in all_employee_list:
            ssn = emp.get_ssn()
            if ssn == action:
                employee_list.append(emp)
        return employee_list

    def add_employee(self,emp):
        self.dl.add_employee(emp)

    def change_employee(self,employee_list,index,option,changed):
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
        cabin_crew_list = []
        all_employee_list = self.dl.get_all_employee()
        for emp in all_employee_list:
            role = emp.get_role()
            if role == "Cabincrew":
                cabin_crew_list.append(emp)
        return cabin_crew_list
    
    def get_pilots(self, license):
        pilot_list = []
        all_employee_list = self.dl.get_all_employee()
        for emp in all_employee_list:
            role = emp.get_role()
            if license == "All" and role == 'Pilot':
                pilot_list.append(emp)
            elif emp.get_licence() == license:
                pilot_list.append(emp)
        
        return pilot_list

    # def check_id_in_voyage(self, voyage_list, ID):
    #     ''' LANGAR AÐ KALLA Í ÞETTA FALL ÚR FALLINU GET_SCHEDULE EN ÞAÐ VIRKAR EKKI'''
    #     employee_list = []
    #     for line in voyage_list:
    #         sting = str(line)
    #         lis = sting.split(',')
    #         if ID in line:
    #             employee_list.append(lis)
    #     return employee_list


    def get_date_schedule(self,from_date,to_date):
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
        all_employees = self.get_all_employees()
        list_of_available = []
        list_of_working = []
        for employee in all_employees:
            ssn = employee.get_ssn()
            for voyage in voyage_list:
                crew = self.vLL.get_crew(voyage)
                if ssn in crew and employee not in list_of_working:
                    list_of_working.append(employee)
            if employee not in list_of_working and employee.get_activity() == 1:
                list_of_available.append(employee)
        return list_of_available
            

        
