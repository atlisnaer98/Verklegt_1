from Models.Employee import Employee
import csv


HEADER = "ssn,name,address,home_phone,mobile_phone,email_address,role,rank,licence,active"
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

    def add_employee(self, emp):
        with open("./DATA/Crew.csv", "a", newline="") as employees:
            employees.write("{}\n".format(str(emp)))

    def update_employee_file(self,emp_list):
        with open("./DATA/Crew.csv", "w+", newline="") as employees:
            employees.write("{}\n".format(HEADER))
            for emp in emp_list:
                employees.write("{}\n".format(str(emp)))

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

    def get_all_employees_dict(self):
        all_employee_dict = {}
        with open("./DATA/Crew.csv","r",newline="") as all_crew:
            reader = csv.DictReader(all_crew)
            for line in reader:
                lis = []
                lis.append(line["name"])
                lis.append(line["address"])
                lis.append(line["home_phone"])
                lis.append(line["mobile_phone"])
                lis.append(line["email_address"])
                lis.append(line["role"])
                lis.append(line["rank"])
                lis.append(line["licence"])
                lis.append(line["active"])
                all_employee_dict[line["ssn"]] = lis
        return all_employee_dict

    def get_all_employees_dict(self):
        all_employee_dict = {}
        with open("./DATA/Crew.csv","r",newline="") as all_crew:
            reader = csv.DictReader(all_crew)
            for line in reader:
                emp = Employee(line["ssn"], line["name"], line["address"], line["home_phone"],line["mobile_phone"], line["email_address"], line["role"], line["rank"], line["licence"], line["active"])
                all_employee_dict[line["ssn"]] = emp
        return all_employee_dict