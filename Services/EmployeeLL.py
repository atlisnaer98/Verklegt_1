from Models.Employee import Employee
from InformationLayerClasses.API import Data_main
import datetime
import dateutil.parser
from Services.VoyageLL import VoyageLL

class EmployeeLL():
        
    def __init__(self, sending):
        self.dl = sending
        self.vLL = VoyageLL(sending)
    
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

    def change_employee(self,employee_list,index,option,changed):
        emp = employee_list[index]
        if option == 1:
            emp.set_address(changed)
        elif option == 2:
            emp.set_home_phone(changed)
        elif option == 3:
            emp.set_mobile_number(changed)
        elif option == 4:
            emp.set_email_address(changed)
        elif option == 5:
            current_activity = emp.get_activity()
            if current_activity == "1":
                changed = "0"
                print()
                print("{} is now Inactive".format(emp.get_name()))
                print()
            elif current_activity == "0":
                changed = "1"
                print()
                print("{} is now Active".format(emp.get_name()))
                print()

            emp.set_activity(changed)
        else: 
            return False
        employee_list[index] = emp
        self.dl.update_employee_file(employee_list)

    def get_cabin_crew(self):
        cabin_crew_list = []
        all_employee_list = self.dl.get_all_employee()
        for line in all_employee_list:
            sting = str(line)
            lis = sting.split(',')
            if lis[6] == "Cabincrew":
                cabin_crew_list.append(sting)
        return cabin_crew_list
    
    def get_pilots(self, license):
        pilot_list = []
        all_employee_list = self.dl.get_all_employee()
        for line in all_employee_list:
            sting = str(line)
            lis = sting.split(',')
            if license == "All" and lis[6] == 'Pilot':
                pilot_list.append(line)
            elif lis[8] == license:
                pilot_list.append(line)
        
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
        temp_list = []
        print(date)
        all_voyage_list = self.dl.get_all_voyages() 
        for voyage in all_voyage_list:
            parseddate = dateutil.parser.parse(voyage.get_departure())
            if date.year == parseddate.year and date.month == parseddate.month and date.day == parseddate.day:
                temp_list.append(voyage)   
        action = input("[1]available, [2]working")
        final_list = self.available_employees(temp_list,action)
        return final_list

    def available_employees(self, voyage_list,action):
        all_employees = self.get_all_employees()
        list_of_available = []
        list_of_working = []
        for employee in all_employees:
            id_numb = employee.get_ID_number()
            for voyage in voyage_list:
                crew = self.vLL.get_crew(voyage)
                if id_numb in crew and employee not in list_of_working:
                    list_of_working.append(employee)
            if employee not in list_of_working:
                list_of_available.append(employee)
        if action == "1":
            return list_of_available
        elif action == "2":
            return list_of_working
            

        
