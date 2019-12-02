class airplane():

    def __init__(self, registration_number, model, active = 1,):
        ''' Active = 1, inactive = 0 '''
            self.registration_number = registration_number
            self.model = model
            self.active = active
            
    def __str__(self):
        return "{},{},{}".format(self.model, self.registration_number, self.active,)

    def get_registration_number(self):
        return self.registration_number

    def get_model(self):
        return self.model

    def get_active(self):
        return self.active

    

airplane1 = airplane("a203", 10000, 250, 1, "yes", "hans")
print(airplane1) 