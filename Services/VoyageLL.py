from Models.Voyage import Voyage

class VoyageLL():
        
    def __init__(self, sending):
        self.dl = sending
    

    def get_all_voyages(self):
        return self.dl.get_all_voyages()