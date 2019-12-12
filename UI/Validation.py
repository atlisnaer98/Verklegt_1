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
            if len(airport_input) > 3 or len(airport_input) < 3:
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
                phone_number = input("Invalid input,  please re-enter (only integers) Emergency contact number:")

    def validate_time(self,time_input):
        time_repeater = True
        while time_repeater == True:
            #time_input = str(time_input)
            try:
                hour = int(time_input[:2])
                minute = int(time_input[4:])
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
        first, last = email_address.split('@')
        if '@' in email_address and False == first.isdigit() and False == last.isdigit():
            if first.isalpha() or first in '.':
                if last.isalpha() or '.' in last:
                    return email_address
                else:
                    email_address = input("invalid input, please re-enter:")
                email_address = input("invalid input, please re-enter:")
        else:
            email_address = input("invalid input, please re-enter:")

    def validate_selection(self,action,limit):
        validation = True
        while validation == True:
            try:
                if int(action) > 0 and int(action) < limit+1:
                    validation = False
                    return action
            except ValueError:
                action = input("Invalid input, please re-enter: ")

    def validate_date(self,date_input):
        date_repeater = True
        while date_repeater == True:
            try:
                year = int(date_input[:4])
                month = int(date_input[5:7])
                day = int(date_input[8:10])
                if year > 0 and date_input[4] == "-" and date_input[7] == "-" and month > 0 and month <= 12 and day > 0 and day < 31:
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
                    if name.isalpha():
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
                    ssn_input = input("please re-enter SSN:")
            except ValueError:
                print("The SSN can only contain numbers,")
                ssn_input = input("please re-enter SSN:")
        return ssn_input

