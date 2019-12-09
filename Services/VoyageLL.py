from Models.Voyage import Voyage
import datetime
import dateutil.parser

class VoyageLL():
        
    def __init__(self, sending):
        self.dl = sending
    

    def get_all_voyages(self, from_date, to_date):
        voyage_list = []
        all_voyage_list = self.dl.get_all_voyages()
        for voyage in all_voyage_list:
            parseddate =dateutil.parser.parse(voyage.get_departure())
            if from_date <= parseddate and parseddate <= to_date:
                voyage_list.append(voyage)
        return voyage_list
        

    def get_voyages_for_employee(self,ID):
        ''' takes staff ID and returns all the voyages for a specific employee'''
        employee_list = []
        all_voyage_list = self.dl.get_all_voyages()
        for line in all_voyage_list:
            sting = str(line)
            lis = sting.split(',')
            if ID == lis[6] or ID == lis[7] or ID == lis[8] or ID == lis[9] or ID == lis[10]:
                employee_list.append(lis)
        return employee_list
