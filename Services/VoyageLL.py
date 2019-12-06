from Models.Voyage import Voyage

class VoyageLL():
        
    def __init__(self, sending):
        self.dl = sending
    

    def get_all_voyages(self):
        return self.dl.get_all_voyages()

    def get_voyages_for_employee(self,ID):
        ''' takes staff ID and returns all the voyages for a specific employee'''
        employee_list = []
        all_voyage_list = self.dl.get_all_voyages()
        for line in all_voyage_list:
            sting = str(line)
            lis = sting.split(',')
            if lis[6] or lis[7] or lis[8] or lis[9] or lis[10] == ID:
                employee_list.append(lis)
        return employee_list
        