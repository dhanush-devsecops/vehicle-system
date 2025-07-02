class Device:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def show(self):
        print(f"Brand is:",self.brand)
        print(f"Model is:",self.model)
        print(f"Year is:",self.year)
class Mobile(Device):
    def __init__(self,brand,model,year,sim_slots):
        super().__init__(brand,model,year)
        self.sim_slots=sim_slots
    def show(self):
        super().show()
        print(f"Sim_Slots are:",self.sim_slots)
class Laptop(Device):
    def __init__(self,brand,model,year,ram):
        super().__init__(brand,model,year)
        self.ram=ram
    def show(self):
        super().show()
        print(f"Ram is:",self.ram)
class Tablet(Device):
    def __init__(self,brand,model,year,stylus_support):
        super().__init__(brand,model,year)
        self.stylus_support=stylus_support
    def show(self):
        super().show()
        print(f"Stylus support is:",self.stylus_support)
devices=[ Mobile("Apple","iphone-15",2023,"2"),
         Laptop("Dell","XPS-15",2017,"8-Gb Ram"),
         Tablet("Samsung","Tab-S8",2022,"True")
         ]
for device in devices:
    print("---------")
    device.show()