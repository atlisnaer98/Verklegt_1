class Employee():
    
    def __init__(self, ID_number, name, address, home_phone, mobile_number, email_address, job_title, rank, licence, active):
        #ssn,name,address, homephone, mobilephone, email_address,job_title,rank,licence, active
        self.__ID_number = ID_number
        self.__name = name
        self.__address = address
        self.__home_phone = home_phone
        self.__mobile_number = mobile_number
        self.__email_address = email_address
        self.__job_title = job_title
        self.__rank = rank
        self.__licence = licence
        self.__active = active


    def __str__(self):
        return "{},{},{},{},{},{},{},{},{},{}".format(self.__ID_number, self.__name, self.__address, self.__home_phone,self.__mobile_number, self.__email_address, self.__job_title, self.__rank, self.__licence, self.__active)

    def get_name(self):
        return self.__name

    def get_ID_number(self):
        return self.__ID_number

    def get_address(self):
        return self.__address
    
    def get_home_phone(self):
        return self.__home_phone

    def get_mobile_number(self):
        return self.__mobile_number

    def get_email_address(self):
        return self.__email_address
    
    def get_job_title(self):
        return self.__job_title
    
    def get_rank(self):
        return self.__rank
    
    def get_licence(self):
        return self.__licence
    
    def get_activity(self):
        return self.__active
