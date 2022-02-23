#write a class named Procedure that represents a medical procedure that has been performed on a patient. 
# The Procedure class should have the following attributes - Name of the procedure, Date of the procedure, 
# Name of the practitioner who performed the procedure, Charges for the procedure and patient ID. 
# The Procedure class’s __init__ method should accept an argument for each attribute. 
# The Procedure class should have accessor methods only for each attribute.

class Procedure:
    def __init__(self,NameProcedure,Date,Practictioner,Charges,patientID):
        self.__Name_ = NameProcedure
        self.__Date_ = Date
        self.__Practioner_ = Practictioner
        self.__Charges_ = Charges
        self.__patid_ = patientID
    def get_Name(self):
        return self.__Name_
    def get_Date(self):
        return self.__Date_
    def get_Practictioner(self):
        return self.__Practioner_
    def get_Charges(self):
        return self.__Charges_
    def get_patid(self):
        return self.__patid_