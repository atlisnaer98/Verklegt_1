from Models.Employee import Employee
from InformationLayerClasses.API import Data_main

class EmployeeLL():
        
    def __init__(self, sending):
        self.dl = sending
    
    def get_all_employees(self):
        return self.dl.get_all_employee()

    def get_employee(self, action):
        employee_list = []
        all_employee_list = self.dl.get_all_employee()
        for line in all_employee_list:
            sting = str(line)
            lis = sting.split(',')
            if lis[0] == action:
                cabin_crew_list.append(sting)
        return employee_list

        

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