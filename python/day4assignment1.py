# Create a class Appliance with brand and power consumption.
#  Inherit Fan, AC, and Heater classes from it, each with a method show_details() displaying their specific features and inherited ones.

class Appliances:
    def __init__(self,brand,power):
        self.brand=brand
        self.power=power
    

    def show_details(self):
        print("specific feature of the aplliances")

class fan(Appliances):
    def __init__(self,brand,power,height):
        super().__init__(brand,power)
        self.height=height
    def show_details(self):
        print(f"Fan - Brand: {self.brand}, Power: {self.power}W, Height: {self.height}cm")    

class heater(Appliances):
    def __init__(self,brand,power):
        super().__init__(brand,power)
    def show_details(self):
        print(f"Heater - Brand: {self.brand}, Power: {self.power}W")    

                    

fan = fan("CoolBreeze", 75, 42)
heater = heater("Warmmee", 1500)


print(fan.show_details())
print(heater.show_details())

