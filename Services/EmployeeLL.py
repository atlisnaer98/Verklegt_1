from Models.Employee import Employee
from InformationLayerClasses.API import Data_main

class EmployeeLL():
        
    def __init__(self, sending):
        self.dl = sending
    
    def get_all_employees(self):
        return self.dl.get_all_employee()

    def get_all_employees_dict(self):
        return self.dl.get_all_employees_dict()

    def list_to_dict(self):
        big_list = self.dl.get_all_employee()
        for emp in big_list:
            lis = []
            lis.append(emp)
    
    def change_employee(self,emp,option,changed):
        if option == 1:
            emp.set_address(changed)
        elif option == 2:
            emp.set_home_phone(changed)
        elif option == 3:
            emp.set_mobile_number(changed)
        elif option == 4:
            emp.set_email_address(changed)
        elif option == 5:
            emp.set_job_title(changed)
        elif option == 6:
            emp.set_rank(changed)
        elif option == 7:
            emp.set_licence(changed)
        elif option == 8:
            emp.set_activity(changed)
        else: 
            return False
        print(emp)

    def add_employee(self,emp):
        self.dl.add_employee(emp)

    def get_cabin_crew(self):
        cabin_crew_list = []
        all_employee_list = self.dl.get_all_employee()
        for line in all_employee_list:
            sting = str(line)
            lis = sting.split(',')
            if lis[6] == "Cabincrew":
                cabin_crew_list.append(sting)
        return cabin_crew_list
    
    def get_pilots(self):
        pilot_list = []
        all_employee_list = self.dl.get_all_employee()
        for line in all_employee_list:
            sting = str(line)
            lis = sting.split(',')
            if lis[6] == "Pilot":
                pilot_list.append(sting)
        return pilot_list