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

    def Get_all_airplanes(self):
        return self.aLL.get_all_airplanes()

    def add_dest(self, dest):
        self.dLL.add_dest(dest)
    
