#from pickle import TRUE
import PatientClass as p
import ProcedureClass as Pro

 #write a program that will create a patient instances as shown below:

def main():

    iD = 1
    name = "Matt Jones"
    address = "123 Main st, Waco TX 76706"
    phone = "254-555-7415"
    vet = True

    pat = p.patient(iD,name,address,phone,vet)

    pat.get__id_()
    pat.get__name_()
    pat.get__addy()
    pat.get__phone_()
    pat.get__veteran()

    procedure = "Physical Exam"
    date = "2/15/2022"
    practicioner = "Dr.Irvine"
    charge = 250
    patid = 1

   # p.patient(iD) == Pro.Procedure(patid)
    procedure1 = Pro.Procedure(procedure, date, practicioner, charge, patid)

    procedure1.get_Name()
    procedure1.get_Date()
    procedure1.get_Practictioner()
    procedure1.get_Charges()
    procedure1.get_patid()

    procedure = "MRI"
    date = "2/15/2022"
    practicioner = "Dr. Hamilton"
    charge = 1500
    patid = 1

    procedure2 = Pro.Procedure(procedure, date, practicioner, charge, patid)
    procedure2.get_Name()
    procedure2.get_Date()
    procedure2.get_Practictioner()
    procedure2.get_Charges()
    procedure2.get_patid()

    print()

    procedure = "CT Scan"
    date = "2/17/2022"
    practicioner = "Dr. Drey"
    charge = 1200
    patid = 2

    procedure3 = Pro.Procedure(procedure, date, practicioner, charge, patid)
    procedure3.get_Name()
    procedure3.get_Date()
    procedure3.get_Practictioner()
    procedure3.get_Charges()
    procedure3.get_patid()

    print("  *** Patient Bill *** ")
    print("Name:", pat.get__name_())
    print("Address:", pat.get__addy())
    print("Phone:", pat.get__phone_())
    print()

    total_charge = 0
    if pat.get__id_() == procedure1.get_patid():
        print("Name:", procedure1.get_Name())
        print("Date:", procedure1.get_Date())
        print("Practictioner:", procedure1.get_Practictioner())
        print("Charge:", "${:.2f}".format(procedure1.get_Charges()))
        print()

        total_charge += procedure1.get_Charges()
    if pat.get__id_() == procedure2.get_patid():
        print("Name:", procedure2.get_Name())
        print("Date:", procedure2.get_Date())
        print("Practictioner:", procedure2.get_Practictioner())
        print("Charge:", "${:.2f}".format(procedure2.get_Charges()))
        print()
        total_charge += procedure2.get_Charges()

    if pat.get__id_() == procedure3.get_patid():
        print("Name:", procedure3.get_Name())
        print("Date:", procedure3.get_Date())
        print("Practictioner:", procedure3.get_Practictioner())
        print("Charge:", "${:.2f}".format(procedure3.get_Charges()))

        print()
        total_charge += procedure3.get_Charges()
      
    if pat.get__veteran() == True:
        total_charge *= .60
    else:
        total_charge

    print("Total Charges:", "${:.2f}".format(total_charge))
        

main()
