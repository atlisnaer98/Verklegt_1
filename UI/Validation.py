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
