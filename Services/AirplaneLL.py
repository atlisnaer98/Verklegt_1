from Models.Airplane import Airplane
from InformationLayerClasses.API import Data_main

class AirplaneLL():

    def __init__(self, sending):
        self.dl = sending

    def get_all_airplanes(self):
        return self.dl.get_airplane()
    """
    def get_plane_schedule(self,from_date,to_date):
        busy_list = []
        all_voyage_list = self.dl.get_all_voyages() 
        for voyage in all_voyage_list:
            dep_parsed_date = dateutil.parser.parse(voyage.get_departure())
            arr_parsed_date = dateutil.parser.parse(voyage.get_arrival())
            if (dep_parsed_date < to_date and arr_parsed_date > from_date) or (arr_parsed_date > from_date and dep_parsed_date < from_date):
                busy_list.append(voyage)   
        final_list = self.available_employees(busy_list)
        return final_list

    def get_available_planes(self,voyage_list):
        all_plane_list = self.dl.get_airplane()
        list_of_available = []
        list_of_working = []
        for plane in all_plane_list:
            reg_num = plane.get_registration_number()
            for voyage in voyage_list:
                if reg_num = voyage.get_plane_id() and employee not in list_of_working:
                    list_of_working.append(employee)
            if employee not in list_of_working:
                list_of_available.append(plane)
        return list_of_available
    """
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