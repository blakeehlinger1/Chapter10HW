#from pickle import TRUE
import PatientClass as p
import ProcedureClass as Pro

 #write a program that will create a patient instances as shown below:

def main():

    iD = 1
    name = "Matt Jones"
    address = "123 Main st, Waco TX 76706"
    phone = 254-555-7415
    vet = "TRUE"

    pat = p.patient(iD,name,address,phone,vet)

    print("ID:", pat.get__id_())
    print("Name:", pat.get__name_())
    print("Address:", pat.get__addy())
    print("Phone:", pat.get__phone_())
    print("Veteran:", pat.get__veteran())
    print(pat)
