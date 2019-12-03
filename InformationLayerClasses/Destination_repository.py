from InformationLayerClasses.API import Destination
import csv

class Destination_repository():

    def __init__(self):
        self.__destination = []

    def add_destination(self,new_dest):
        with open("./DATA/Destination.csv", "a+") as f_object:
            country = new_dest.get_country()
            airport = new_dest.get_airport()
            flight_time = new_dest.get_flight_time()
            distance = new_dest.get_distance()
            name_of_contact = new_dest.get_name_of_contact()
            emergency_phone_number = new_dest.get_emergency_phone_number()
            

