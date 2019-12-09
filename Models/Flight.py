class Flight():

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