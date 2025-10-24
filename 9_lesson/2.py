class Car:
    def __init__(self, brand, color, fuel):
        self.brand = brand
        self.color = color
        self.fuel = fuel
    def drive(self, h):
        fl = h * 0.5
        if fl <= self.fuel:
            self.fuel -= fl
            print(f"Fuel: {self.fuel}%")
        else:
            print("You do not have enough fuel for this travel")

car1 = Car("Ford", "blue", 100)
car1.drive(100)
car1.drive(1000)
car1.drive(40)
