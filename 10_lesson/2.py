class Car:
    def __init__(self, plate_number, color):
        self.plate_number = plate_number
        self.color = color

class PaintShop:
    def paint(self, car, color):
        car.color = color

paint_shop = PaintShop()
car = Car("ABC-123", "blue")
print("The car is " + car.color)
paint_shop.paint(car, "red")
print("The car is now " + car.color)