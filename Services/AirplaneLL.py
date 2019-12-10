from Models.Airplane import Airplane
from InformationLayerClasses.API import Data_main

class AirplaneLL():

    def __init__(self, sending):
        self.dl = sending

    def get_all_airplanes(self):
        return self.dl.get_airplane()

    def add_plane(self, plane):
        self.dl.add_plane(plane)

    def change_plane(self,airplane_list,index):
        plane = airplane_list[index]
        if plane.get_active() == "1":
            plane.set_active(0)
        elif plane.get_active() == "0":
            plane.set_active(1)
        airplane_list[index] = plane
        self.dl.update_plane_file(airplane_list)