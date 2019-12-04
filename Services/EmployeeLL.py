from Models.Employee import Employee
from InformationLayerClasses.API import Data_main

class EmployeeLL():
        
    def __init__(self, sending):
        self.dl = sending
    
    def get_all_employees(self):
        return self.dl.get_all_employee()

    def get_cabin_crew(self):
        