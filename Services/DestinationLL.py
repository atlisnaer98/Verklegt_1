from Models.Destination import Destination
from InformationLayerClasses.API import Data_main
class DestinationLL():
   
    def __init__(self, sending):
        self.dl = sending

    def add_dest(self, dest):
        self.dl.add_dest(dest)
        
    def get_all_dest(self):
        return self.dl.get_all_dest()

    def change_dest(self,dest_list,index,option,changed):
        