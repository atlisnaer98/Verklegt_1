class Destination():

    def __init__(self, destination="",country="", airport="", flight_time="", distance=0, name_of_contact="", emergency_phone_number=""):
        self.__destination = destination
        self.__country = country
        self.__airport = airport
        self.__flight_time = flight_time
        self.__distance = distance
        self.__name_of_contact = name_of_contact
        self.__emergency_phone_number = emergency_phone_number

    def __str__(self):
        return "{},{},{},{},{},{},{}".format(self.__destination,self.__country, self.__airport, self.__flight_time, self.__distance, self.__name_of_contact, self.__emergency_phone_number)

    def get_destination(self):
        return self.__destination
    
    def set_destination(self, new_dest):
        self.__destination = new_dest
    
    def get_country(self):
        return self.__country

    def set_country(self, new_country):
        self.__country = new_country
    
    def get_airport(self):
        return self.__airport

    def set_airport(self, new_airport):
        self.__airport = new_airport

    def get_flight_time(self):
        return self.__flight_time

    def set_flight_time(self, new_flight_time):
        self.__flight_time = new_flight_time
    
    def get_distance(self):
        return self.__distance
    
    def set_distance(self, new_dist):
        self.__distance = new_dist

    def get_name_of_contact(self):
        return self.__name_of_contact

    def set_name_of_contact(self, new_contact):
        self.__name_of_contact = new_contact

    def get_emergency_phone_number(self):
        return self.__emergency_phone_number

    def set_emergency_phone_number(self, new_phone):
        self.__emergency_phone_number = new_phone