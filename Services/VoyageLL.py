from Models.Voyage import Voyage
import datetime
import dateutil.parser
from datetime import timedelta
from datetime import datetime
from InformationLayerClasses.API import Data_main
from Models.Destination import Destination
class VoyageLL():
        
    def __init__(self, sending):
        self.dl = sending
    
    def get_all_voyages(self):
        all_voyage_list = self.dl.get_all_voyages()
        return all_voyage_list


    def get_date_voyages(self,from_date,to_date):
        voyage_list = []
        all_voyage_list = self.dl.get_all_voyages()
        for voyage in all_voyage_list:
            dep_date = dateutil.parser.parse(voyage.get_departure())
            arr_date = dateutil.parser.parse(voyage.get_arrival())
            if (from_date <= dep_date and dep_date < to_date) or (from_date <= arr_date and arr_date < to_date):
                voyage_list.append(voyage)
        return voyage_list  
    
    def get_voyages_on_date(self,date):
        voyage_list = []
        all_voyage_list = self.dl.get_all_voyages()
        for voyage in all_voyage_list:
            parseddate = dateutil.parser.parse(voyage.get_departure())
            if date.year == parseddate.year and date.month == parseddate.month and date.day == parseddate.day:
                voyage_list.append(voyage)
        return voyage_list  

    def get_voyages_for_employee(self,ID,voyage_list):
        ''' takes staff ID and returns all the voyages for a specific employee'''
        voyage_list_for_emp = []
        for voyage in voyage_list:
            if ID == voyage.get_captain() or ID == voyage.get_copilot() or ID == voyage.get_fsm() or ID == voyage.get_fa1 or ID == voyage.get_fa2():
                voyage_list_for_emp.append(voyage)
        return voyage_list_for_emp

    def add_voyage(self,voyage):
        self.dl.add_voyage(voyage)

    def assign_crew(self,voyage_list):
        self.dl.update_voyage_file(voyage_list)

    def change_voyage(self,voyage_list,index,plane):
        voyage = voyage_list[index]
        voyage.set_aircraft_id(plane)
        voyage_list[index] = voyage
        self.dl.update_voyage_file(voyage_list)

    def get_crew(self,voyage):
        crew = [voyage.get_captain(), voyage.get_copilot(), voyage.get_fsm(), voyage.get_fa1(), voyage.get_fa2()]
        return crew

    def get_voyage_status(self,voyage):
        time = datetime.now()
        dep_time = dateutil.parser.parse(voyage.get_departure())
        arr_time = dateutil.parser.parse(voyage.get_arrival())
        if arr_time < time: #The voyage is over
            return "Over"
        elif dep_time > time: #The voyage has not started
            return "Not started"
        elif dep_time < time and arr_time > time: #The voyage is in progress
            whole_time = arr_time - dep_time
            flight_time = whole_time - timedelta(hours=1)
            one_way_time = flight_time // 2
            time_left = arr_time - time
            if time_left < one_way_time + timedelta(hours=1) and time_left > one_way_time:
                return "Landed in destination"
            else:
                if time_left < one_way_time:
                    return "On the way to Reykjavik"
                else:
                    return "On the way to the destination"
        else:
            return "Invalid"

    def count_dest_flights(self,dest,place,date,start = 0):
        voyage_list = self.dl.get_all_voyages()
        voyage_list_today = self.get_voyages_on_date(date)
        counter = start
        for voyage in voyage_list_today:
            voy_time = dateutil.parser.parse(voyage.get_departure())
            if dest == voyage.get_arriving_at() and date > voy_time:
                counter += 2
        if place == "away":
            if counter < 1:
                return "00"
            elif counter < 10:
                return "0" + str(counter)
            else:
                return str(counter)
        elif place == "home":
            counter += 1
            if counter < 10:
                return "0" + str(counter)
            else:
                return str(counter)

    def update_flight_nums(self):
        voyage_list = self.dl.get_all_voyages()
        dest_list = self.dl.get_all_dest()
        for dest in dest_list:
            start = 0
            for voyage in voyage_list:
                voy_time = dateutil.parser.parse(voyage.get_departure())
                if voyage.get_arriving_at() == dest.get_destination():
                    start = 0
                    voyage_list_today = self.get_voyages_on_date(voy_time)
                    for voyage_2 in voyage_list_today:
                        voy2_time = dateutil.parser.parse(voyage_2.get_departure())
                        if voy_time > voy2_time and voyage_2.get_arriving_at() == dest.get_destination():
                            start += 2
                    away_string = self.to_string(start,"away")
                    home_string = self.to_string(start,"home")
                    away_number = "NA" + dest.get_flight_number() + away_string
                    home_number = "NA" + dest.get_flight_number() + home_string
                    voyage.set_flight_number_away(away_number)
                    voyage.set_flight_number_home(home_number)
        self.dl.update_voyage_file(voyage_list)

    def get_departure(self):
        voyage_list = self.dl.get_all_voyages()
        departure_list = []
        for voyage in voyage_list:
            if voyage.get_departure() not in departure_list:
                departure_list.append(voyage.get_departure())
        return departure_list

    def to_string(self,start,place):
        counter = start
        if place == "away":
            if counter < 1:
                return "00"
            elif counter < 10:
                return "0" + str(counter)
            else:
                return str(counter)
        elif place == "home":
            counter += 1
            if counter < 10:
                return "0" + str(counter)
            else:
                return str(counter)