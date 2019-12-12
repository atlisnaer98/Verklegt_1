import datetime
import dateutil.parser
from datetime import datetime


# dist = len("[1] Create      [2] Change info")
# other_dist = len("Destination")
# print("-"*((dist-other_dist)//2))
# print(" "*(dist//4)+"Destination")
# print("-"*dist)
# print("[1] Create\t[2] Change info")
# print("[3] List destinations")
# selection = int(input("Select an option: "))

# if selection == 1:
#     try: 
#         name = input("Name: ")
#         IDnumber = int(input("ID number: "))
    
#     except ValueError:
#         print("suckers my titters")

# else:
#     print("suck a tit")
    
# import datetime

# timi = datetime.datetime.now()

# print(timi)


# year,month,day,hour,minute = 2019,12,20,6,0
# to_date = datetime.datetime(year,month,day,hour,minute,0)

# #print(to_date.day)

# name = 'Hvað! segir1 þú gott'
# if name.isalpha():
#     print("")


# namesplit = name.split()



# num = '21313123 sdf'
# if num.isdigit():
#     print("cunt")

import string

email_list = ['.']

x = input("Enter email addresss")
first, last = x.split('@')
if '@' in x and False == first.isdigit() and False == last.isdigit():
    if first.isalpha() or first in '.':
        print('hór')
        if last.isalpha() or '.' in last:
            print('cunt')
else:
    print("bitch")
# else:
#     print("Tuss")
print(first)
print(last)