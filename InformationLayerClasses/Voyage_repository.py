from Models.Voyage import Voyage
import csv

HEADER = "bookingReference,flightNumberAway,flightNumberHome,arrivingAt,departure,arrival,aircraftID,captain,copilot,fsm,fa1,fa2"
class Voyage_repository:

    def add_all_upcoming_flights(self,all_voyages,counter):
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

    def update_voyage_file(self,voyage_list):
        with open("./DATA/Voyage.csv", "w+", newline="") as voyages:
            voyages.write("{}\n".format(HEADER))
            for voyage in voyage_list:
                voyages.write("{}\n".format(str(voyage)))

    def get_all_past_flights(self):
        all_voyages_list = []
        with open("./DATA/PastFlights.csv","r",newline="") as all_flights:
            reader = csv.DictReader(all_flights)
            counter = 0
            for line in reader:
                if line["departingFrom"] == "Keflavik":
                    counter +=1
                    voyages = Voyage(counter,line["flightNumber"],line["flightNumber"],line["arrivingAt"],line["departure"],line["arrival"],line["aircraftID"],line["captain"],line["copilot"],line["fsm"],line["fa1"],line["fa2"])
                    all_voyages_list.append(voyages)
        return all_voyages_list

    def get_all_voyages(self):
        """gets all the voyages"""
        all_voyages_list = []
        with open("./DATA/Voyage.csv","r",newline="") as voyages:
            reader = csv.DictReader(voyages)
            for line in reader:
                voyage = Voyage(line["bookingReference"],line["flightNumberAway"],line["flightNumberHome"],line["arrivingAt"],line["departure"],line["arrival"],line["aircraftID"],line["captain"],line["copilot"],line["fsm"],line["fa1"],line["fa2"])
                all_voyages_list.append(voyage)
        return all_voyages_list

    def add_voyage(self, voyage):
        with open("./DATA/Voyage.csv", "a", newline="") as voyages:
            voyages.write("{}\n".format(str(voyage)))

    def add_captains_to_voyage(self):
        ''' adds captains to a specific voyage, each captain can only go on one voyage each day,
        each voyage should at least have two pilots of which one should be a captain'''
        pass

    
    def add_cabin_crew_to_voyage(self):
        ''' adds cabin crew members to a specific voyage and at least one cabin crew member should be 
        a flight manager each cabin crew member can only go on one voyage each day'''
        pass

    
    
    


    