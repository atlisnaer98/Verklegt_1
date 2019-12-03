class User:
    def __init__(self):
        pass

    def start(self):
        pass

    def add_destination(self):
        country = input("Country: ")
        airport = input("Airport: ")
        flight_time = input("Time of flight: ")
        name_of_contact = input("Emergency contact: ")
        emergency_phone_number = input("Emergency contact number: ")
        return country, airport, flight_time, name_of_contact, emergency_phone_number
