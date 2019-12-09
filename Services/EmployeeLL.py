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

    """def get_schedule(self, ID, from_date, to_date):
        voyage_list = []
        employee_list = []
        all_voyage_list = self.dl.get_all_voyages()
        for voyage in all_voyage_list:
            parseddate = dateutil.parser.parse(voyage.get_departure())
            if from_date <= parseddate and parseddate <= to_date:
                voyage_list.append(voyage)

        for line in voyage_list:
            sting = str(line)
            lis = sting.split(',')
            print(lis[0], ID, lis[7])
            if ID == lis[11] or ID == lis[7] or ID == lis[8] or ID == lis[9] or ID == lis[10]:
                print("yes")
                employee_list.append(lis)
        return employee_list"""

    # def check_id_in_voyage(self, voyage_list, ID):
    #     ''' LANGAR AÐ KALLA Í ÞETTA FALL ÚR FALLINU GET_SCHEDULE EN ÞAÐ VIRKAR EKKI'''
    #     employee_list = []
    #     for line in voyage_list:
    #         sting = str(line)
    #         lis = sting.split(',')
    #         if ID in line:
    #             employee_list.append(lis)
    #     return employee_list


    def get_date_schedule(self, date):
        same_year_list = []
        same_month_list = []
        same_day_list = []
        print(date)
        all_voyage_list = self.dl.get_all_voyages() 
        for voyage in all_voyage_list:
            parseddate = dateutil.parser.parse(voyage.get_departure())
            if date.year == parseddate.year:
                same_year_list.append(voyage)


        for month in same_year_list:
            parseddate = dateutil.parser.parse(month.get_departure())
            if date.month == parseddate.month:
                same_month_list.append(month)

        for day in same_month_list:
            parseddate = dateutil.parser.parse(day.get_departure())
            if date.day == parseddate.day:
                same_day_list.append(day)
        action = input("[1]available, [2]working")
        if action == '1':
            self.available_employees(same_day_list)
        elif action == '2':
            self.working_employees(same_day_list)
        
        
        return same_day_list

    def available_employees(self, same_day_list):
        all_employees = self.get_all_employees()
        for i in all_employees:
            if i in same_day_list:
                print("yesss")

    def working_employees(self):
        all_employees = self.get_all_employees()

            

        
