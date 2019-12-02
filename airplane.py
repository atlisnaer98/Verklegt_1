class airplane():

    def __init__(self, registration_number, model, active = 1, available, pilot):
        ''' Active = 1, inactive = 0 '''
            self.registration_number = registration_number
            self.model = model
            self.active = active
            
    def __str__(self):
        return "{},{},{}".format(self.model, self.registration_number, self.active,)
    

airplane1 = airplane("a203", 10000, 250, 1, "yes", "hans")
print(airplane1) 