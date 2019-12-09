class Voyage():

    def __init__(self,booking_ref=0, flight_number_away = "", flight_number_home = "", arriving_at = "", departure ="", arrival="", aircraft_id="",captain="",copilot="",fsm="",fa1="",fa2=""):
        self.__booking_reference = booking_ref
        self.__flight_number_away = flight_number_away
        self.__flight_number_home = flight_number_home
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
        return "{},{},{},{},{},{},{},{},{},{},{},{}".format(self.__booking_reference,self.__flight_number_away,self.__flight_number_home,self.__arriving_at,self.__departure,self.__arrival,self.__aircraft_id,self.__captain,self.__copilot,self.__fsm,self.__fa1,self.__fa2)

    def get_booking_reference(self):
        return self.__booking_reference

    def set_booking_reference(self, new_booking_reference):
        self.__booking_reference = new_booking_reference

    def get_flight_number_away(self):
        return self.__flight_number_away

    def set_flight_number_away(self,new_number):
        self.__flight_number_away = new_number

    def get_flight_number_home(self):
        return self.__flight_number_home

    def set_flight_number_home(self,new_number):
        self.__flight_number_home = new_number

    def get_arriving_at(self):
        return self.__arriving_at

    def set_arriving_at(self,new_location):
        self.__arriving_at = new_location
    
    def get_departure(self):
        return self.__departure

    def set_departure(self,new_time):
        self.__departure = new_time

    def get_arrival(self):
        return self.__arrival

    def set_arrival(self,new_time):
        self.__arrival = new_time
    
    def get_aircraft_id(self):
        return self.__aircraft_id

    def set_aircraft_id(self, new_ID):
        self.__aircraft_id = new_ID

    def get_captain(self):
        return self.__captain

    def set_captain(self,new_capt):
        self.__captain = new_capt
    
    def get_copilot(self):
        return self.__copilot

    def set_copilot(self,new_copilot):
        self.__copilot = new_copilot

    def get_fsm(self):
        return self.__fsm

    def set_fsm(self, new_fsm):
        self.__fsm = new_fsm

    def get_fa1(self):
        return self.__fa1

    def set_fa1(self, new_fa):
        self.__fa1 = new_fa

    def get_fa2(self):
        return self.__fa2

    def set_fa2(self,new_fa):
        self.__fa2 = new_fa

        
        
        