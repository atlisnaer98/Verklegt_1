from Models.Airplane import Airplane
import csv

HEADER = "planeInsignia,planeTypeId,planeType,model,capacity,active"
class Airplane_repository:

    def __init__(self):
        self.__airplanes = []

    def add_plane(self, plane):
        with open("./DATA/Aircraft.csv", "a", newline="") as airplanes:
            airplanes.write("{}\n".format(str(plane)))

    def get_airplane(self):
        lis = []
        with open("./DATA/Aircraft.csv", "r", newline="") as aircraft:
            reader = csv.DictReader(aircraft)
            #next(reader)
            for line in reader:
                plane = Airplane(line["planeInsignia"], line["planeTypeId"],line["planeType"],line["model"],line["capacity"],line["active"])
                lis.append(plane)
        return lis

    def update_plane_file(self,plane_list):
        with open("./DATA/Aircraft.csv", "w+", newline="") as planes:
            planes.write("{}\n".format(HEADER))
            for plane in plane_list:
                planes.write("{}\n".format(str(plane)))