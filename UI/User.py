from Models.Destination import Destination
import csv
from Services.API import LLApi

class User:
    def __init__(self):
        self.ll = LLApi()

    def start(self):
        pass

    def add_destination(self):
        dest = Destination()
        dest.set_Country(input("Country: "))
        airport = input("Airport: ")
        flight_time = input("Time of flight: ")
        name_of_contact = input("Emergency contact: ")
        emergency_phone_number = input("Emergency contact number: ")
        self.ll.add_dest(dest)
        return country, airport, flight_time, name_of_contact, emergency_phone_number

    def get_all_dest(self):
        dest_obj = self.ll.get_all_dest()
        for line in dest_obj:
            print(line)

    def get_airplane(self):
        airplane_obj = self.ll.get_all_airplanes()
        for line in airplane_obj:
            print(line)

    def get_employee(self):
        employee_list = self.ll.get_all_employees()
        for line in employee_list:
            print(line)