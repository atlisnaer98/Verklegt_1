class Employee():
    
    def __init__(self, ID_number, name, address, home_phone, mobile_number, email_address, job_title, rank, licence, active):
        #ssn,name,address, homephone, mobilephone, email_address,job_title,rank,licence, active
        self.ID_number = ID_number
        self.name = name
        self.address = address
        self.home_phone = home_phone
        self.mobile_number = mobile_number
        self.email_address = email_address
        self.job_title = job_title
        self.rank = rank
        self.licence = licence
        self.active = active


    def __str__(self):
        return "{},{},{},{},{},{},{},{},{},{}".format(self.ID_number, self.name, self.address, self.home_phone,self.mobile_number, self.email_address, self.job_title, self.rank, self.licence, self.active)

    def get_name(self):
        return self.name

    def get_ID_number(self):
        return self.ID_number

    def get_address(self):
        return self.address
    
    def get_home_phone(self):
        return self.home_phone

    def get_mobile_number(self):
        return self.mobile_number

    def get_email_address(self):
        return self.email_address
    
    def get_job_title(self):
        return self.job_title
    
    def get_rank(self):
        return self.rank
    
    def get_licence(self):
        return self.licence
    
    def get_activity(self):
        return self.active
