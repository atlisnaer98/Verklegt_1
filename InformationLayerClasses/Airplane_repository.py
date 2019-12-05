from Models.Airplane import Airplane
import csv

class Airplane_repository:

    def __init__(self):
        self.__airplanes = []

    def add_plane(self, plane):
        with open("./DATA/Aircraft.csv", "a", newline="") as airplanes:
            airplanes.write("\n{}".format(str(plane)))

    def get_airplane(self):
        lis = []
        with open("./DATA/Aircraft.csv", "r", newline="") as aircraft:
            reader = csv.DictReader(aircraft)
            #next(reader)
            for line in reader:
                plane = Airplane(line["planeInsignia"], line["planeTypeId"], line["active"])
                lis.append(plane)
        return lis


