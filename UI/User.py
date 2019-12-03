from Models.Destination import Destination

from Services.API import LLApi

class User:
    def __init__(self):
        self.ll = LLApi()

    def start(self):
        pass

    def add_destination(self):
        dest = Destination()
        dest.setCountry(input("Country: "))
        airport = input("Airport: ")
        flight_time = input("Time of flight: ")
        name_of_contact = input("Emergency contact: ")
        emergency_phone_number = input("Emergency contact number: ")
        self.ll.add_destination(dest)
        return country, airport, flight_time, name_of_contact, emergency_phone_number
