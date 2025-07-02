class Person:
    def __init__(self,name,age,village):
        self.name=name
        self.age=age
        self.village=village
    def show(self):
        print(f"Name is:",self.name)
        print(f"Age is:",self.age)
        print(f"Village is:",self.village)
class Doctor(Person):
    def __init__(self,name,age,village,speciality):
        super().__init__(name,age,village)
        self.speciality=speciality
    def show(self):
        super().show()
        print(f"Speciality is:",self.speciality)
class Patient(Person):
    def __init__(self,name,age,village,disease):
        super().__init__(name,age,village)
        self.disease=disease
    def show(self):
        super().show()
        print(f"Disease is:",self.disease)
class Nurse(Person):
    def __init__(self,name,age,village,nurse_id):
        super().__init__(name,age,village)
        self.nurse_id=nurse_id
    def show(self):
        super().show()
        print(f"Nurse ID is:",self.nurse_id)
def display_details(Person):
    print("---------")
    Person.show()

d=Doctor("Dr.Dhanush",24,"Huzurnagar","Orthopedix")
p=Patient("G.Dinnu",32,"Hyderabad","Fever")
n=Nurse("N.Dhanya",27,"Khammam","6655")

hospital=[d,p,n]

for person in hospital:
    print("----------------")
    person.show()


