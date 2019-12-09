class Airplane():

    def __init__(self, registration_number="",planeID = "",plane_type= "", model="",capacity = 0, active = 1,):
        ''' Active = 1, inactive = 0 '''
        self.__registration_number = registration_number
        self.__planeID = planeID
        self.__plane_type = plane_type
        self.__model = model
        self.__capacity = capacity
        self.__active = active
            
    def __str__(self):
        return "{},{},{},{},{},{}".format(self.__registration_number, self.__planeID, self.__plane_type, self.__model, self.__capacity, self.__active)

    def get_registration_number(self):
        return self.__registration_number

    def set_registration_number(self,new_regID):
        self.__registration_number = new_regID

    def get_plane_ID(self):
        self

    def get_model(self):
        return self.__model

    def set_model(self, new_model):
        self.__model = new_model

    def get_active(self):
        return self.__active

    def set_active(self, new_status):
        self.__active = new_status

    # Hæ
