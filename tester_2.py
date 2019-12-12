import datetime
import dateutil.parser
from datetime import timedelta
from Services.VoyageLL import VoyageLL
from InformationLayerClasses.API import Data_main
"""
parseddate = dateutil.parser.parse("2019-11-30T0:00:00")
print(parseddate+timedelta(days=1))
print(datetime.datetime(2019,11,2))
#x = datetime.datetime(parseddate)
#y = x.date
#print(y)
year,month,day = parseddate.year,parseddate.month,parseddate.day
print(year)
a = "2019-11-10"
b = a[:3]
print(b)

dep_time = dateutil.parser.parse("2019-11-30T0:00:00")
arr_time = dateutil.parser.parse("2019-11-30T0:10:00")
time = arr_time - dep_time
print(time//2)
"""
dl = Data_main
vLL = VoyageLL(dl)

vLL.update_flight_nums()