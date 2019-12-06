from Models.Voyage import Voyage
import datetime
import dateutil.parser

class VoyageLL():
        
    def __init__(self, sending):
        self.dl = sending
    

    def get_all_voyages(self, from_date, to_date):
        employee_list = []
        all_voyage_list = self.dl.get_all_voyages()
        for line in all_voyage_list:
            sting = str(line)
            lis = sting.split(',')
            parseddate =dateutil.parser.parse(lis[3])
            if from_date <= parseddate and parseddate <= to_date:
                employee_list.append(lis)
        return employee_list
        

    def get_voyages_for_employee(self,ID):
        ''' takes staff ID and returns all the voyages for a specific employee'''
        employee_list = []
        all_voyage_list = self.dl.get_all_voyages()
        for line in all_voyage_list:
            sting = str(line)
            lis = sting.split(',')
            if ID in line:
                employee_list.append(lis)
        return employee_list
