from Models.Employee import Employee
from InformationLayerClasses.API import Data_main
import datetime
import dateutil.parser

class EmployeeLL():
        
    def __init__(self, sending):
        self.dl = sending
    
    def get_all_employees(self):
        return self.dl.get_all_employee()

    def get_employee(self, action):
        employee_list = []
        all_employee_list = self.dl.get_all_employee()
        for line in all_employee_list:
            sting = str(line)
            lis = sting.split(',')
            if lis[0] == action:
                cabin_crew_list.append(sting)
        return employee_list

        

    def add_employee(self,emp):
        self.dl.add_employee(emp)

    def get_cabin_crew(self):
        cabin_crew_list = []
        all_employee_list = self.dl.get_all_employee()
        for line in all_employee_list:
            sting = str(line)
            lis = sting.split(',')
            if lis[6] == "Cabincrew":
                cabin_crew_list.append(sting)
        return cabin_crew_list
    
    def get_pilots(self):
        pilot_list = []
        all_employee_list = self.dl.get_all_employee()
        for line in all_employee_list:
            sting = str(line)
            lis = sting.split(',')
            if lis[6] == "Pilot":
                pilot_list.append(sting)
        return pilot_list

    def get_schedule(self, ID, from_date, to_date):
        voyage_list = []
        employee_list = []
        all_voyage_list = self.dl.get_all_voyages()
        for voyage in all_voyage_list:
            parseddate = dateutil.parser.parse(voyage.get_departure())
            if from_date <= parseddate and parseddate <= to_date:
                voyage_list.append(voyage)
        #voyage_list = check_id_in_voyage(voyage_list, ID)
        #return voyage_list
        for line in voyage_list:
            sting = str(line)
            lis = sting.split(',')
            if ID in line:
                employee_list.append(lis)
        return employee_list

    def check_id_in_voyage(self, voyage_list, ID):
        employee_list = []
        for line in voyage_list:
            sting = str(line)
            lis = sting.split(',')
            if ID in line:
                employee_list.append(lis)
        return employee_list