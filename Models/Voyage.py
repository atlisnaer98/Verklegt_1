class Voyage():

    def __init__(self, flight_number, departing_from, arriving_at, departure, arrival, aircraft_id,captain,copilot,fsm,fa1,fa2):
        self.__flight_number = flight_number
        self.__departing_from = departing_from
        self.__arriving_at = arriving_at
        self.__departure = departure
        self.__arrival = arrival
        self.__aircraft_id = aircraft_id
        self.__captain = captain
        self.__copilot = copilot
        self.__fsm = fsm
        self.__fa1 = fa1
        self.__fa2 = fa2


    def __str__(self):
        return "{},{},{},{},{},{},{},{},{},{},{}".format(self.__flight_number,self.__departing_from,self.__arriving_at,self.__departure,self.__arrival,self.__aircraft_id,self.__captain,self.__copilot,self.__fsm,self.__fa1,self.__fa2)

    def get_flight_number(self):
        return self.__flight_number

    def get_departing_from(self):
        return self.__departing_from

    def get_arriving_at(self):
        return self.__arriving_at
    
    def get_departure(self):
        return self.__departure

    def get_arrival(self):
        return self.__arrival
    
    def get_aircraft_id(self):
        return self.__aircraft_id

    def get_captain(self):
        return self.__captain
    
    def get_copilot(self):
        return self.__copilot

    def get_fsm(self):
        return self.__fsm

    def get_fa1(self):
        return self.__fa1

    def get_fa2(self):
        return self.__fa2

    def set_aircraft_id(self, new_aircraft_id):
        self.__aircraft_id = new_aircraft_id

    def set_destination(self, new_destination):
        self.__destination = new_destination

    def set_time(self, new_time):
        self.__time = new_time
    
    def set_flight_numbers(self, new_flight_numbers):
        self.__flight_numbers = new_flight_numbers 

    def set_booking_reference(self, new_booking_reference):
        self.__booking_reference = new_booking_reference

        
        
        