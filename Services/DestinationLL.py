from Models.Destination import Destination
from InformationLayerClasses.API import Data_main
from Services.VoyageLL import VoyageLL
class DestinationLL():
   
    def __init__(self, sending):
        self.dl = sending

    def add_dest(self, dest):
        self.dl.add_dest(dest)
        
    def get_all_dest(self):
        return self.dl.get_all_dest()

    def change_dest(self,dest_list,index,option,changed):
        dest = dest_list[index]
        if option == 1:
            dest.set_name_of_contact(changed)
        elif option == 2:
            dest.set_emergency_phone_number(changed)
        else:
            return False
        dest_list[index] = dest
        self.dl.update_dest_file(dest_list)

    def get_flight_number(self):
        dest_list = self.dl.get_all_dest()
        last_flight_numb = int(dest_list[-1].get_flight_number())
        next_flight_numb = last_flight_numb + 1
        if next_flight_numb < 10:
            return "0" + str(next_flight_numb)
        else:
            return str(next_flight_numb)