class Employee():
    
    def __init__(self, name, ID_number, address, home_phone, mobile_number, email_address, job_title, active, available):
        self.name = name
        self.ID_number = ID_number
        self.address = address
        self.home_phone = home_phone
        self.mobile_number = mobile_number
        self.email_address = email_address
        self.job_title = job_title
        self.active = active
        self.available = available

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{}".format(self.name, self.ID_number, self.address, self.home_phone,self.mobile_number, self.email_address, self.job_title, self.active, self.available)
