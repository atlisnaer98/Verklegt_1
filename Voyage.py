class Voyage():

    def __init__(self, airplane, destination, employees, time, flight_numbers, booking_reference):
        self.airplane = airplane
        self.destination = destination
        self.employees = employees
        self.time = time
        self.flight_numbers = flight_numbers
        self.booking_reference = booking_reference


    def __str__(self):
        return "{},{},{},{},{},{},".format(self.airplane, self.destination, self.employees, self.time, self.flight_numbers, self.booking_reference)



