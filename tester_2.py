import datetime
import dateutil.parser
from datetime import timedelta
parseddate = dateutil.parser.parse("2019-11-30T0:00:00")
print(parseddate+timedelta(days=1))
print(datetime.datetime(2019,11,2))
#x = datetime.datetime(parseddate)
#y = x.date
#print(y)