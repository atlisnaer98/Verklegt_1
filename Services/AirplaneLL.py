from Models.Airplane import Airplane
from InformationLayerClasses.API import Data_main

class AirplaneLL():

    def __init__(self, sending):
        self.dl = sending

    def get_all_airplanes(self):
        return self.dl.get_airplane()
"""
    def get_date_schedule(self, date):
        temp_list = []
        print(date)
        all_voyage_list = self.dl.get_all_voyages() 
        for voyage in all_voyage_list:
            parseddate = dateutil.parser.parse(voyage.get_departure())
            if date.year == parseddate.year and date.month == parseddate.month and date.day == parseddate.day:
                temp_list.append(voyage)   
        action = input("[1]available, [2]working")
        final_list = self.available_employees(temp_list,action)
        return final_list

    def get_available_airplanes(self,to_date,from_date):
        all_plane_list = self.dl.get_airplane()
        list_of_available = []
        list_of_working = []
        for employee in all_employees:
            id_numb = employee.get_ID_number()
            for voyage in voyage_list:
                crew = self.vLL.get_crew(voyage)
                if id_numb in crew and employee not in list_of_working:
                    list_of_working.append(employee)
            if employee not in list_of_working:
                list_of_available.append(employee)
        if action == "1":
            return list_of_available
        elif action == "2":
            return list_of_working
"""
    def add_plane(self, plane):
        self.dl.add_plane(plane)

    def change_plane(self,airplane_list,index):
        plane = airplane_list[index]
        if plane.get_active() == "1":
            plane.set_active(0)
        elif plane.get_active() == "0":
            plane.set_active(1)
        airplane_list[index] = plane
        self.dl.update_plane_file(airplane_list)