class Airplane():

    def __init__(self, registration_number, model, active = 1,):
        ''' Active = 1, inactive = 0 '''
        self.__registration_number = registration_number
        self.__model = model
        self.__active = active
            
    def __str__(self):
        return "{},{},{}".format(self.__model, self.__registration_number, self.__active,)

    def get_registration_number(self):
        return self.__registration_number

    def get_model(self):
        return self.__model

    def get_active(self):
        return self.__active
