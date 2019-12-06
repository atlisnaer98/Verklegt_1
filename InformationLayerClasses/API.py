from InformationLayerClasses.Airplane_repository import Airplane_repository
from InformationLayerClasses.Destination_repository import Destination_repository
from InformationLayerClasses.Employee_repository import Employee_repository
from InformationLayerClasses.Voyage_repository import Voyage_repository

class Data_main:
    def __init__(self):
        self.aDL = Airplane_repository()
        self.dDL = Destination_repository()
        self.eDL = Employee_repository()
        self.vDL = Voyage_repository()
    
    def get_airplane(self):
        return self.aDL.get_airplane()

    def add_plane(self, plane):
        self.aDL.add_plane(plane)
    
    def get_all_dest(self):
        return self.dDL.get_all_dest()

    def add_dest(self, dest):
        self.dDL.add_dest(dest)
    
    def get_all_employee(self):
        return self.eDL.get_all_employees()

    def get_all_employees_dict(self):
        return self.eDL.get_all_employees_dict()

    def add_employee(self,emp):
        self.eDL.add_employee(emp)

    def get_all_voyages(self):
        return self.vDL.get_all_voyages()