from Services.AirplaneLL import AirplaneLL
from Services.DestinationLL import DestinationLL
from Services.EmployeeLL import EmployeeLL
from Services.VoyageLL import VoyageLL
from InformationLayerClasses.API import dataMain

class LLApi:
    def __init__(self):
        self.dl = dataMain()
        self.aLL = AirplaneLL(self.dl)
        self.dLL = DestinationLL(self.dl)
        self.eLL = EmployeeLL(self.dl)
        self.vLL = VoyageLL(self.dl)

    def GetAllAirplanes(self):
        return self.aLL.GetAllAirplanes()

    def add_dest(self, dest):
        self.dLL.add_dest(dest)
