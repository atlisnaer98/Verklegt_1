import string

class Validation:
    def __init__(self):
        pass

    def validate_distance(self,distance_input):
        # The method will check if the input of distance is valid, only number allowed. 
        distance_repeater = True
        while distance_repeater == True:
            try:
                if int(distance_input) <= 0:
                    distance_input = input("Invalid input, please re-enter distance: ")
                else:
                    return distance_input
            except ValueError:
                distance_input = input("Invalid input, please re-enter distance: ")

    def validate_airport(self,airport_input):
        airport_repeater = True
        numb_list = ["0","1","2","3","4","5","6","7","8","9"]
        while airport_repeater == True:
            if len(airport_input) != 3:
                airport_input = input("Invalid input, please re-enter airport(XXX)")
            else:
                counter = 0
                for letter in airport_input:
                    if letter in numb_list or letter in string.punctuation:
                        airport_input = input("Invalid input, please re-enter airport(XXX)")
                        break
                    else:
                        counter += 1
            if counter == len(airport_input):
                airport_repeater = False
        return airport_input.upper()

    def validate_name(self,name_input):
        counter = 0
        name_repeater = True
        while name_repeater == True:
            splitted_name  = name_input.split(" ")
            name_len = len(splitted_name)
            for name in splitted_name:
                if name.isalpha():
                    counter += 1
                else:
                    name_input = input("The name has to only contain letters, please re-enter name: ")
                    counter = 0
                    break 
            if counter == name_len: 
                name_repeater = False        
        return name_input.title()

    def validate_phone_number(self,phone_number):
        true_check = True
        while true_check == True:
            if phone_number.isdigit():
                true_check = False
                return phone_number
            else:
                phone_number = input("Invalid input,  please re-enter (only integers) phone number:")

    def validate_time(self,time_input):
        time_repeater = True
        while time_repeater == True:
            #time_input = str(time_input)
            try:
                hour = int(time_input[:2])
                minute = int(time_input[3:])
                if hour >= 0 and hour <= 24 and minute >= 0 and minute <= 60 and time_input[2] == ":":
                    #time_repeater = False
                    return time_input
                else:
                    time_input = input("Invalid input, please re-enter (HH:MM): ")
            except ValueError:
                time_input = input("Invalid input, please re-enter (HH:MM): ")

    def validate_home(self,address_input):
        address_repeater = True
        while address_repeater == True:
            counter = 0
            for letter in address_input:
                if  letter in string.punctuation:
                    print("The home address can only contain numbers and letters,")
                    address_input = input("Please re-enter address: ")
                    counter = 0
                else:
                    counter += 1
            if counter == len(address_input):
                address_repeater = False
        return address_input

    def validate_email(self, email_address):
        true_condition = True
        while true_condition == True:
            try:
                first, last = email_address.split('@')
                true_condition = False
                return email_address
            except ValueError:
                email_address = input("Invalid input, pleaes re-enter email address: ")

    def validate_selection(self,action,limit):
        validation = True
        while validation == True:
            try:
                temp_action = int(action)
                if temp_action > 0 and temp_action < limit+1:
                    validation = False
                    return action
                else:
                    action = input("Invalid input, please re-enter: ")
            except ValueError:
                action = input("Invalid input, please re-enter: ")

    def validate_date(self,date_input):
        date_repeater = True
        while date_repeater == True:
            try:
                year = int(date_input[:4])
                month = int(date_input[5:7])
                day = int(date_input[8:10])
                if year > 0 and date_input[4] == "-" and date_input[7] == "-" and month > 0 and month <= 12 and day > 0 and day < 32:
                    return date_input
                else:
                    date_input = input("Invalid input, please re-enter (YYYY-MM-DD):")
            except ValueError:
                date_input = input("Invalid input, please re-enter (YYYY-MM-DD):")

    def validate_reg(self,reg_input):
        # The method will check if the registration number is valid. The number has to start with TF- to be valid and contain 3 letters.
        reg_repeater = True
        while reg_repeater == True:
            if reg_input[:3] != "TF-":
                print("""The registration number has to start with "TF-""")
                reg_input = input("please re-enter: ")
            else:
                last_three = reg_input.split("-")
                for name in last_three[1:]:
                    if name.isalpha() and len(last_three) == 3:
                        reg_repeater = False
                    else:
                        reg_input = input("Invalid input, please re-enter:")
                    break
        return reg_input.upper()

    def validate_ssn(self,ssn_input):
        ssn_repeater = True
        while ssn_repeater == True:
            try:
                if int(ssn_input) > 0 and len(ssn_input) == 10:
                    ssn_repeater = False
                else:
                    print("The SSN has to be exactly 10 numbers,")
                    ssn_input = input("please re-enter SSN: ")
            except ValueError:
                print("The SSN can only contain numbers,")
                ssn_input = input("please re-enter SSN: ")
        return ssn_input

    def validate_existing_emp(self,ssn_input,employee_list):
        #validates wether the employee is in the company, if not you have to reenter ssn
        ssn_repeater = True
        while ssn_repeater == True:
            ssn_input = self.validate_ssn(ssn_input)
            counter = 1
            for emp in employee_list:
                if emp.get_ssn() == ssn_input:
                    return ssn_input
                else:
                    counter += 1
            if counter > len(employee_list):
                print("This employee is not in the company,")
                ssn_input = input("please re-enter SSN: ")
            
    def validate_already_emp(self,ssn_input,employee_list):
        #Validate if the ssn input is already in the company if so then reenter ssn
        employees_in_company = []
        for emp in employee_list:
            employees_in_company.append(emp.get_ssn())
        ssn_repeater = True
        while ssn_repeater == True:
            ssn_input = self.validate_ssn(ssn_input)
            if ssn_input in employees_in_company:
                print("This employee is already in the company,")
                ssn_input = input("please re-enter SSN: ")
            else:
                return ssn_input
            
    def validate_dest(self,dest_input,dest_list):
        #checks if the destination is already in the data
        taken_dest_list = []
        dest_repeater = True
        for dest in dest_list:
            taken_dest_list.append(dest.get_destination())
        while dest_repeater == True:
            dest_input = self.validate_name(dest_input)
            if dest_input in taken_dest_list:
                print("\nThis destination is already in the system,")
                dest_input = input("please re-enter destination: ")
            else:
                return dest_input