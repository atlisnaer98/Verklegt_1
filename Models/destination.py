class Destination():

    def __init__(self, country, airport, flight_time, distance, name_of_contact, emergency_phone_number,  ):
        self.__country = country
        self.__airport = airport
        self.__flight_time = flight_time
        self.__distance = distance
        self.__name_of_contact = name_of_contact
        self.__emergency_phone_number = emergency_phone_number

    def __str__(self):
        return "{},{},{},{},{},{}".format(self.__country, self.__airport, self.__flight_time, self.__distance, self.__name_of_contact, self.__emergency_phone_number)

    def get_country(self):
        return self.__country
    
    def get_airport(self):
        return self.__airport

    def get_flight_time(self):
        return self.__flight_time
    
    def get_distance(self):
        return self.__distance

    def get_name_of_contact(self):
        return self.__name_of_contact

    def get_emergency_phone_number(self):
        return self.__emergency_phone_number