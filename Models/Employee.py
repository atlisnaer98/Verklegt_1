class Employee():
    #ssn,name,address, home_phone, mobile_phone, email_address,role,rank,licence, active
    def __init__(self, ssn, name, address, home_phone, mobile_phone, email_address, role, rank, licence, active):
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

    def get_name(self):
        return self.__name

    def get_ID_number(self):
        return self.__ssn

    def get_address(self):
        return self.__address
    
    def get_home_phone(self):
        return self.__home_phone

    def get_mobile_number(self):
        return self.__mobile_phone

    def get_email_address(self):
        return self.__email_address
    
    def get_job_title(self):
        return self.__role
    
    def get_rank(self):
        return self.__rank
    
    def get_licence(self):
        return self.__licence
    
    def get_activity(self):
        return self.__active
