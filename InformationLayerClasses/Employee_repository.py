from Models.Employee import Employee

class Employee_repository:

    def create_employee_list(self):
        '''creates a list of all employees working for the company'''
        pass

    def get_pilots(self):
        ''' gets all the pilots working in the company and returns a list of them '''
        pass

    def get_cabin_crew(self):
        ''' gets all the cabin crew members and returns a list of them'''
        pass

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