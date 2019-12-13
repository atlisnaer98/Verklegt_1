from Models.Destination import Destination
import csv
HEADER = "Destination,country,airport,flight time (one-way),distance from Reykjavik,contact,contact phonenumber,flight number"
class Destination_repository():

    def __init__(self):
        self.__destination = []

    def get_all_dest(self):
        "Reads the whole csv file and returns a list of destination clases"
        lis = [] #list of destinations
        with open("./DATA/Destination.csv", "r", newline="") as destinations:
            reader = csv.DictReader(destinations)
            for line in reader: #Creates a dest class for each line of the csv file
                dest = Destination(line["Destination"], line["country"], line["airport"], line["flight time (one-way)"], line["distance from Reykjavik"], line["contact"], line["contact phonenumber"],line["flight number"])
                lis.append(dest) #appends the destination to a list
        return lis

    def add_dest(self,dest): #Adds a new destination to the CSV file
        with open("./DATA/Destination.csv", "a", newline="") as destinations:
            destinations.write("{}\n".format(str(dest)))

    def update_dest_file(self, dest_list):
        """Uses a list to rewrite the CSV file where each line is a destiantion""" 
        with open("./DATA/Destination.csv", "w+", newline="") as destinations:
            destinations.write("{}\n".format(HEADER))
            for dest in dest_list:
                destinations.write("{}\n".format(str(dest)))