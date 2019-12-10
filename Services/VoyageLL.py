from Models.Voyage import Voyage
import datetime
import dateutil.parser
from datetime import timedelta
from InformationLayerClasses.API import Data_main
class VoyageLL():
        
    def __init__(self, sending):
        self.dl = sending
    
    def get_all_voyages(self):
        all_voyage_list = self.dl.get_all_voyages()
        return all_voyage_list


    def get_date_voyages(self,from_date,to_date):
        voyage_list = []
        all_voyage_list = self.dl.get_all_voyages()
        for voyage in all_voyage_list:
            parseddate =dateutil.parser.parse(voyage.get_departure())
            if from_date <= parseddate and parseddate < to_date:
                voyage_list.append(voyage)
        return voyage_list  

    def get_voyages_for_employee(self,ID):
        ''' takes staff ID and returns all the voyages for a specific employee'''
        voyage_list_for_emp = []
        all_voyage_list = self.dl.get_all_voyages()
        for voyage in all_voyage_list:
            if ID == voyage.get_captain() or ID == voyage.get_copilot() or ID == voyage.get_fsm() or ID == voyage.get_fa1 or ID == voyage.get_fa2():
                voyage_list_for_emp.append(voyage)
        return voyage_list_for_emp

    def add_voyage(self,voyage):
        self.dl.add_voyage(voyage)

    def assign_crew(self,voyage_list):
        self.dl.update_voyage_file(voyage_list)

    def change_voyage(self,voyage_list,index,option,changed):
        voyage = voyage_list[index]
        if option == 1:
            voyage.set_flight_number_away(changed)
        elif option == 2:
            voyage.set_aircraft_id(changed)
        else:
            return False
        voyage_list[index] = voyage
        self.dl.update_voyage_file(voyage_list)