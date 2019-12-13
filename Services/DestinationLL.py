from Models.Destination import Destination
from InformationLayerClasses.API import Data_main
from Services.VoyageLL import VoyageLL
class DestinationLL():
   
    def __init__(self, sending):
        self.dl = sending

    def add_dest(self, dest):
        self.dl.add_dest(dest) 
        
    def get_all_dest(self): #Returns a list of all destinations
        return self.dl.get_all_dest()

    def change_dest(self,dest_list,index,option,changed):
        """Changes a destination's contact and phone number"""
        dest = dest_list[index]
        if option == 1:
            dest.set_name_of_contact(changed)
        elif option == 2:
            dest.set_emergency_phone_number(changed)
        else:
            return False
        dest_list[index] = dest
        self.dl.update_dest_file(dest_list) #Updates the CSV file

    def get_flight_number(self): #Creates a specific number to use in flights to a location
        dest_list = self.dl.get_all_dest()
        last_flight_numb = int(dest_list[-1].get_flight_number()) #Gets the last number and  then adds 1
        next_flight_numb = last_flight_numb + 1 
        if next_flight_numb < 10:
            return "0" + str(next_flight_numb)
        else:
            return str(next_flight_numb)