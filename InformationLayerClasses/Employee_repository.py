from Models.Employee import Employee
import csv


HEADER = "ssn,name,address,home_phone,mobile_phone,email_address,role,rank,licence,active"
class Employee_repository:

    def get_all_employees(self):
        """gets all the crew member"""
        all_employee_list = []
        NAFokkerF100_list = []
        NABAE146_list = []
        NAFokkerF28_list = []
        N_A_list = []
        final_list = []


        with open("./DATA/Crew.csv","r",newline="") as all_crew:
            reader = csv.DictReader(all_crew)
            for line in reader:
                crew = Employee(line["ssn"], line["name"], line["address"], line["home_phone"],line["mobile_phone"], line["email_address"], line["role"], line["rank"], line["licence"], line["active"])
                all_employee_list.append(crew)
            for employee in all_employee_list:
                if employee.get_licence() == 'NAFokkerF100':
                    NAFokkerF100_list.append(employee)
                elif employee.get_licence() == 'NABAE146':
                    NABAE146_list.append(employee)
                elif employee.get_licence() == 'NAFokkerF28':
                    NAFokkerF28_list.append(employee)
                elif employee.get_licence() == 'N/A':
                    N_A_list.append(employee)
        final_list.extend(NAFokkerF100_list)
        final_list.extend(NABAE146_list) 
        final_list.extend(NAFokkerF28_list)
        final_list.extend(N_A_list)

        return final_list

    def add_employee(self, emp):
        with open("./DATA/Crew.csv", "a", newline="") as employees:
            employees.write("{}\n".format(str(emp)))

    def update_employee_file(self,emp_list):
        with open("./DATA/Crew.csv", "w+", newline="") as employees:
            employees.write("{}\n".format(HEADER))
            for emp in emp_list:
                employees.write("{}\n".format(str(emp)))

    def get_all_employees_dict(self):
        all_employee_dict = {}
        with open("./DATA/Crew.csv","r",newline="") as all_crew:
            reader = csv.DictReader(all_crew)
            for line in reader:
                emp = Employee(line["ssn"], line["name"], line["address"], line["home_phone"],line["mobile_phone"], line["email_address"], line["role"], line["rank"], line["licence"], line["active"])
                all_employee_dict[line["ssn"]] = emp
        return all_employee_dict