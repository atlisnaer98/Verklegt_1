class airplane():

    def __init__(self, model, registration_number, active, available, pilot):
            self.model = model
            self.registration_number = registration_number
            self.active = active
            self.available = available
            self.pilot = pilot
            
    def __str__(self):
        return "{},{},{},{},{}".format(self.model, self.registration_number, self.active, self.available, self.pilot)
    

airplane1 = airplane("a203", 10000, 250, 1, "yes", "hans")
print(airplane1)