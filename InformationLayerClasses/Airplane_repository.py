from Models.Airplane import Airplane
import csv

HEADER = "planeInsignia,planeTypeId,planeType,model,capacity,active"
class Airplane_repository:

    def __init__(self):
        self.__airplanes = []

    def add_plane(self, plane):
        """Adds a plane to the CSV file"""
        with open("./DATA/Aircraft.csv", "a", newline="") as airplanes:
            airplanes.write("{}\n".format(str(plane)))

    def get_airplane(self):
        """Reads the Aircraft CSV file and returns a list whith all planes """
        lis = [] #list of planes
        with open("./DATA/Aircraft.csv", "r", newline="") as aircraft:
            reader = csv.DictReader(aircraft)
            for line in reader: #each line is a plane
                plane = Airplane(line["planeInsignia"], line["planeTypeId"],line["planeType"],line["model"],line["capacity"],line["active"])
                lis.append(plane) #adds the plane to a list
        return lis

    def update_plane_file(self,plane_list):
        """Reads a list and uses it to rewrite the whole aircraft CSV file"""
        with open("./DATA/Aircraft.csv", "w+", newline="") as planes:
            planes.write("{}\n".format(HEADER))
            for plane in plane_list:
                planes.write("{}\n".format(str(plane)))