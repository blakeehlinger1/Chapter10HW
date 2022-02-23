

class patient:
    def __init__(self,iD,name,address,phone,vet):
        self.__id_ = iD
        self.__name_ = name
        self.__addy_ = address
        self.__phone_ = phone
        self.__veteran = vet

    def get__id_(self):
        return self.__id_
    def get__name_(self):
        return self.__name_
    def get__addy(self):
        return self.__addy_
    def get__phone_(self):
        return self.__phone_
    def get__veteran(self):
        return self.__veteran
