from Models.Employee import Employee
import csv

class Employee_repository:

    

    def get_all_employees(self):
        """gets all the crew member"""
        all_employee_list = []
        with open("./DATA/Crew.csv","r",newline="") as all_crew:
            reader = csv.DictReader(all_crew)
            for line in reader:
                crew = Employee(line["ssn"], line["name"], line["address"], line["home_phone"],line["mobile_phone"], line["email_address"], line["role"], line["rank"], line["licence"], line["active"])
                all_employee_list.append(crew)
        return all_employee_list


    def change_employee_attribute(self):
        ''' changes a specific attribute for an employee'''
        pass

    def get_available_employees(self):
        '''returns a list of all available employees on a specific date'''
        pass

    def get_unavailable_employees(self):
        '''returns a list of all employees working on a specific date and the destination'''
        pass

    def employee_working_schedudule(self):
        '''returns working schedule for a specific employee for a specific week'''
        pass