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
        lis = []
        with open("./DATA/Aircraft.csv", "r", newline="") as aircraft:
            reader = csv.DictReader(aircraft)
            #next(reader)
            for line in reader:
                plane = Airplane(line["planeInsignia"], line["planeTypeId"], line["active"])
                lis.append(plane)
        return lis

    def add_dest(self,plane):
        with open("./DATA/Destination.csv", "a", newline="") as airplanes:
            airplanes.write(str(plane))

