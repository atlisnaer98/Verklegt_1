from Models.Airplane import Airplane
from InformationLayerClasses.API import Data_main

class AirplaneLL():

    def __init__(self, sending):
        self.dl = sending

    def get_all_airplanes(self):
        return self.dl.get_airplane()

    def add_plane(self, plane):
        self.dl.add_plane(plane)