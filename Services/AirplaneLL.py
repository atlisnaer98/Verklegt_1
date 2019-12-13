from Models.Airplane import Airplane
from InformationLayerClasses.API import Data_main
import datetime
import dateutil.parser
from datetime import timedelta

class AirplaneLL():

    def __init__(self, sending):
        self.dl = sending

    def get_all_airplanes(self):
        '''fetches all airplanes from the data layers and returns the lsit'''
        return self.dl.get_airplane()
    
    def get_available_planes(self,from_date,to_date):
        '''returns a list of available planes'''
        busy_list = []
        all_voyage_list = self.dl.get_all_voyages() 
        for voyage in all_voyage_list:
            dep_parsed_date = dateutil.parser.parse(voyage.get_departure())
            arr_parsed_date = dateutil.parser.parse(voyage.get_arrival())
            if (dep_parsed_date < to_date and arr_parsed_date > from_date) or (arr_parsed_date > from_date and dep_parsed_date < from_date):
                busy_list.append(voyage)   
        final_list = self.check_available_planes(busy_list)
        return final_list

    def check_available_planes(self,voyage_list):
        '''Returns a list of available planes'''
        all_plane_list = self.dl.get_airplane()
        list_of_available = []
        list_of_working = []
        for plane in all_plane_list:
            reg_num = plane.get_registration_number()
            for voyage in voyage_list:
                string = str(voyage)
                list_of_voyage_attributes = string.split(",")
                if reg_num == list_of_voyage_attributes[6] and plane not in list_of_working:
                    list_of_working.append(plane)
            if plane not in list_of_working:
                list_of_available.append(plane)
        return list_of_available
    
    def add_plane(self, plane):
        '''forwards the information about anew plane to the data layer where it is created'''
        self.dl.add_plane(plane)

    def change_plane(self,airplane_list,index):
        ''' forwards the updated information about a plane to the data layer where it is updated'''
        plane = airplane_list[index]
        if plane.get_active() == "1":
            plane.set_active(0)
        elif plane.get_active() == "0":
            plane.set_active(1)
        airplane_list[index] = plane
        self.dl.update_plane_file(airplane_list)