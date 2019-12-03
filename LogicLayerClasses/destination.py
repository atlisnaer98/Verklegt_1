class Destination():

    def __init__(self, country, airport, flight_time, distance, name_of_contact, emergency_phone_number,  ):
        self.__country = country
        self.__airport = airport
        self.__flight_time = flight_time
        self.__distance = distance
        self.__name_of_contact = name_of_contact
        self.__emergency_phone_number = emergency_phone_number

    def __str__(self):
        return "{},{},{},{},{},{}".format(self.country, self.airport, self.flight_time, self.distance, self.name_of_contact, self.emergency_phone_number)

    def get_country(self):
        return self.__country
    
    def 