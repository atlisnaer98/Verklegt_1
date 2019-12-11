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
    
    def change_plane_status(self,airplane_list,index):
        self.aLL.change_plane(airplane_list,index)

    def add_dest(self, dest):
        self.dLL.add_dest(dest)

    def get_all_dest(self):
        return self.dLL.get_all_dest()

    def change_dest(self,dest_list,index,option,changed):
        self.dLL.change_dest(dest_list,index,option,changed)
    
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

    
    def get_all_voyages(self):
        return self.vLL.get_all_voyages()

    def get_date_voyages(self,from_date,to_date):
        return self.vLL.get_date_voyages(from_date,to_date)

    def add_voyage(self,voyage):
        self.vLL.add_voyage(voyage)

    def change_voyage(self,voyage_list,index,option,changed):
        self.vLL.change_voyage(voyage_list,index,option,changed)

    def get_crew(self,voyage):
        self.vLL.get_crew(voyage)

    def assign_crew(self,voyage_list):
        self.vLL.assign_crew(voyage_list)

    def get_voyages_for_employee(self,ID,voyage_list):
        ''' takes staff ID and returns all the voyages for a specific employee'''
        return self.vLL.get_voyages_for_employee(ID,voyage_list)
    
    def get_emp_schedule(self, ID, from_date, to_date):
        return self.eLL.get_schedule(ID, from_date, to_date)
    
    def get_emp_date_schedule(self, date):
        return self.eLL.get_date_schedule(date) 