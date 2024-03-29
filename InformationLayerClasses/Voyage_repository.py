from Models.Voyage import Voyage
import csv

HEADER = "bookingReference,flightNumberAway,flightNumberHome,arrivingAt,departure,arrival,aircraftID,captain,copilot,fsm,fa1,fa2"
class Voyage_repository:

    def update_voyage_file(self,voyage_list):
        ''' opens the csv voyage file and allows us to rewrite it'''
        with open("./DATA/Voyage.csv", "w+", newline="") as voyages:
            voyages.write("{}\n".format(HEADER))
            for voyage in voyage_list:
                voyages.write("{}\n".format(str(voyage)))

    def get_all_voyages(self):
        """fetches all the voyages and returns them"""
        all_voyages_list = []
        with open("./DATA/Voyage.csv","r",newline="") as voyages:
            reader = csv.DictReader(voyages)
            for line in reader:
                voyage = Voyage(line["bookingReference"],line["flightNumberAway"],line["flightNumberHome"],line["arrivingAt"],line["departure"],line["arrival"],line["aircraftID"],line["captain"],line["copilot"],line["fsm"],line["fa1"],line["fa2"])
                all_voyages_list.append(voyage)
        return all_voyages_list

    def add_voyage(self, voyage):
        ''' appends a new voyage to the voyage csv file'''
        with open("./DATA/Voyage.csv", "a", newline="") as voyages:
            voyages.write("{}\n".format(str(voyage)))

    def get_all_past_flights(self):
        '''This method Was used to create the Voyage.csv file it was only uesd once'''
        all_voyages_list = []
        with open("./DATA/PastFlights.csv","r",newline="") as all_flights:
            reader = csv.DictReader(all_flights)
            counter = 0
            for line in reader:
                if line["departingFrom"] == "Keflavik":
                    counter +=1
                    voyages = Voyage(counter,line["flightNumber"],line["flightNumber"],line["arrivingAt"],line["departure"],line["arrival"],line["aircraftID"],line["captain"],line["copilot"],line["fsm"],line["fa1"],line["fa2"])
                    all_voyages_list.append(voyages)
        return all_voyages_list , counter

    def add_all_upcoming_flights(self,all_voyages,counter):
        '''This method was used to create the Voyage.csv file it was only uesd once'''
        all_voyages_list = all_voyages
        with open("./DATA/UpcomingFlights.csv","r",newline="") as all_flights:
            reader = csv.DictReader(all_flights)
            counter = counter
            for line in reader:
                if line["departingFrom"] == "Keflavik":
                    counter +=1
                    voyages = Voyage(counter,line["flightNumber"],line["flightNumber"],line["arrivingAt"],line["departure"],line["arrival"],line["aircraftID"],line["captain"],line["copilot"],line["fsm"],line["fa1"],line["fa2"])
                    all_voyages_list.append(voyages)
        return all_voyages_list