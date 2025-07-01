class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def show(self):
        print(f"Brand is:",self.brand)
        print(f"Model is:",self.model)
        print(f"Year is:",self.year)
class Car(Vehicle):
    def __init__(self,brand,model,year,fuel_type,doors):
        super().__init__(brand,model,year)
        self.fuel_type=fuel_type
        self.doors=doors
    def show(self):
        super().show()
        print(f"Fuel_Type is:",self.fuel_type)
        print(f"Doors:",self.doors)
class Bike(Vehicle):
    def __init__(self,brand,model,year,cc,gear):
        super().__init__(brand,model,year)
        self.cc=cc
        self.gear=gear
    def show(self):
        super().show()
        print(f"CC:",self.cc)
        print(f"Gear:",self.gear)

print("***CAR***")
c=Car("Ferrari","Model-5",1984,"Petrol","5")
c.show()

print("***BIKE***")
b=Bike("Gt-650","model-7",1976,"350-CC","6")
b.show()