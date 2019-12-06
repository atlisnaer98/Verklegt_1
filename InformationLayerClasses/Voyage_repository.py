from Models.Voyage import Voyage
import csv

class Voyage_repository:


    def get_all_voyages(self):
        """gets all the voyages"""
        all_voyages_list = []
        with open("./DATA/PastFlights.csv","r",newline="") as all_flights:
            reader = csv.DictReader(all_flights)
            for line in reader:
                voyages = Voyage(line["flightNumber"],line["departingFrom"],line["arrivingAt"],line["departure"],line["arrival"],line["aircraftID"],line["captain"],line["copilot"],line["fsm"],line["fa1"],line["fa2"])
                all_voyages_list.append(voyages)
        return all_voyages_list

    def add_captains_to_voyage(self):
        ''' adds captains to a specific voyage, each captain can only go on one voyage each day,
        each voyage should at least have two pilots of which one should be a captain'''
        pass

    
    def add_cabin_crew_to_voyage(self):
        ''' adds cabin crew members to a specific voyage and at least one cabin crew member should be 
        a flight manager each cabin crew member can only go on one voyage each day'''
        pass

    
    
    


    