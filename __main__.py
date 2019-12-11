from UI.User import User

def main():
    ui = User()
    ui.printing_picture()
    ui.main_menu() 
    #ui.get_all_airplane()
    #ui.get_all_dest()
    #ui.get_all_employee()
    #ui.get_cabin_crew()
    #ui.add_dest()
    #ui.get_pilots()
    #ui.add_plane()
    #ui.add_employee()
    

    
if __name__ == '__main__':
    main()

print("I liiike")

"""
from InformationLayerClasses.Voyage_repository import Voyage_repository

repo = Voyage_repository()

voyage_list = repo.get_all_past_flights()
voyage_list = repo.add_all_upcomig_flights(voyage_list,26)
repo.update_voyage_file(voyage_list)
"""
