from Models.Airplane import Airplane
import csv

class Airplane_repository:

    def __init__(self):
        self.__airplanes = []

    def add_airplane(self, airplane):
        with open("Aircraft.csv", "a+") as airplanes:
            airplanes.write(str(plane))

    def get_airplane(self):
        lis = []
        with open("./DATA/Aircraft.csv", "r", newline="") as aircraft:
            reader = csv.DictReader(aircraft)
            #next(reader)
            for line in reader:
                plane = Airplane(line["planeInsignia"], line["planeTypeId"], line["active"])
                lis.append(plane)
        return lis


