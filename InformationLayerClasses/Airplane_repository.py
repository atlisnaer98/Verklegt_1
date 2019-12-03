from Models.Airplane import Airplane
import csv

class Airplane_repository:

    def __init__(self):
        self.__airplanes = []

    def add_airplane(self, airplane):
        with open("Aircraft.csv", "a+") as aircraft:
            registration_number = airplane.get_registration_number
            model = airplane.get_model

        aircraft.write("{},{}".format(registration_number, model))

    def get_airplane(self):
        with open("./DATA/Aircraft.csv", "r") as aircraft:
            reader = csv.reader(aircraft)
            next(reader)
            return reader


