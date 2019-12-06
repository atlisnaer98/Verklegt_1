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

    def change_employee(self,emp):
        self.eLL.change_employee(emp)
    
    def add_employee(self, emp):
        self.eLL.add_employee(emp)
    
    def get_cabin_crew(self):
        return self.eLL.get_cabin_crew()

    def get_pilots(self):
        return self.eLL.get_pilots()

    
    def get_all_voyages(self):
        return self.vLL.get_all_voyages()
    
