dist = len("[1] Create      [2] Change info")
other_dist = len("Destination")
print("-"*((dist-other_dist)//2))
print(" "*(dist//4)+"Destination")
print("-"*dist)
print("[1] Create\t[2] Change info")
print("[3] List destinations")
selection = int(input("Select an option: "))

if selection == 1:
    try: 
        name = input("Name: ")
        IDnumber = int(input("ID number: "))
    
    except ValueError:
        print("suckers my titters")

else:
    print("suck a tit")
    
"""import datetime

timi = datetime.datetime.now().isoformat()

print(timi)"""