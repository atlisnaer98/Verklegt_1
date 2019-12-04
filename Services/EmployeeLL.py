from Models.Employee import Employee
from InformationLayerClasses.API import Data_main

class EmployeeLL():
        
    def __init__(self, sending):
        self.dl = sending
    
    def get_all_employees(self):
        return self.dl.get_all_employee()

    def get_cabin_crew(self):
        cabin_crew_list = []
        all_employee_list = self.dl.get_all_employee()
        for line in all_employee_list:
            if line[6] == "Cabincrew":
                cabin_crew_list.append(line)
        return cabin_crew_list