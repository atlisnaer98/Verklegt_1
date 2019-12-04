from InformationLayerClasses.Airplane_repository import Airplane_repository
from InformationLayerClasses.Destination_repository import Destination_repository
from InformationLayerClasses.Employee_repository import Employee_repository
from InformationLayerClasses.Voyage_repository import Voyage_repository

class Data_main:
    def __init__(self):
        self.aDL = Airplane_repository()
    
    def get_airplane(self):
        return self.aDL.get_airplane()
    
    def get_all_dest(self):
        return self.dDL.get_all_dest()