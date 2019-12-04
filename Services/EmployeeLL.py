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
        for i in range(0,len(all_employee_list)+1):
            if all_employee_list[i][6] == "Cabincrew":
                cabin_crew_list.append(all_employee_list[i][6])
        return cabin_crew_list