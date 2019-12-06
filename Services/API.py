from Services.AirplaneLL import AirplaneLL
from Services.DestinationLL import DestinationLL
from Services.EmployeeLL import EmployeeLL
from Services.VoyageLL import VoyageLL
from InformationLayerClasses.API import Data_main

class LLApi:
    def __init__(self):
        self.dl = Data_main()
        self.aLL = AirplaneLL(self.dl)
        self.dLL = DestinationLL(self.dl)
        self.eLL = EmployeeLL(self.dl)
        self.vLL = VoyageLL(self.dl)

    def get_all_airplanes(self):
        return self.aLL.get_all_airplanes()

    def add_plane(self, plane):
        self.aLL.add_plane(plane)

    def add_dest(self, dest):
        self.dLL.add_dest(dest)

    def get_all_dest(self):
        return self.dLL.get_all_dest()
    
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

    def get_pilots(self):
        return self.eLL.get_pilots()

    
    def get_all_voyages(self, from_date, to_date):
        return self.vLL.get_all_voyages(from_date, to_date)

    def get_voyages_for_employee(self, ID):
        ''' takes staff ID and returns all the voyages for a specific employee'''
        return self.vLL.get_voyages_for_employee(ID)
    
