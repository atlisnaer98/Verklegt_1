class Employee():
    #ssn,name,address, home_phone, mobile_phone, email_address,role,rank,licence, active
    def __init__(self, ssn = "", name = "", address = "", home_phone = "", mobile_phone = "", email_address = "", role = "", rank = 0, licence = "", active = 1):
        #ssn,name,address, homephone, mobilephone, email_address,job_title,rank,licence, active
        self.__ssn = ssn
        self.__name = name
        self.__address = address
        self.__home_phone = home_phone
        self.__mobile_phone = mobile_phone
        self.__email_address = email_address
        self.__role = role
        self.__rank = rank
        self.__licence = licence
        self.__active = active


    def __str__(self):
        return "{},{},{},{},{},{},{},{},{},{}".format(self.__ssn, self.__name, self.__address, self.__home_phone,self.__mobile_phone, self.__email_address, self.__role, self.__rank, self.__licence, self.__active)
        
    def get_ID_number(self):
        return self.__ssn

    def set_ssn(self, new_ssn):
        self.__ssn = new_ssn

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_address(self):
        return self.__address

    def set_address(self, new_address):
        self.__address = new_address
    
    def get_home_phone(self):
        return self.__home_phone
    
    def set_home_phone(self, new_phone):
        self.__home_phone = new_phone

    def get_mobile_number(self):
        return self.__mobile_phone

    def set_mobile_number(self, new_mobile):
        self.__mobile_phone = new_mobile

    def get_email_address(self):
        return self.__email_address

    def set_email_address(self, new_email):
        self.__email_address = new_email
    
    def get_job_title(self):
        return self.__role

    def set_job_title(self, new_job):
        self.__role = new_job
    
    def get_rank(self):
        return self.__rank

    def set_rank(self, new_rank):
        self.__rank = new_rank
    
    def get_licence(self):
        return self.__licence

    def set_licence(self, new_licence):
        self.__licence = new_licence
    
    def get_activity(self):
        return self.__active

    def set_activity(self, new_active):
        self.__active = new_active
