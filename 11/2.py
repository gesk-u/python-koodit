import random
# to make table
from tabulate import tabulate

# define class "Car"
class Car:
    cur_speed = 0
    t_dist = 0

    # initializer sets the required values
    def __init__(self, num, max_speed, cur_speed = 0, t_dist = 0):
        self.num = num
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.t_dist = t_dist

    # changes cur_s to "current speed + delta" if value is more than max returns max_speed
    # if value is less than 0 returns 0
    def accelerate(self, delta):
        self.cur_speed = max(0, min(self.cur_speed + delta, self.max_speed))
    # multiply speed by time returns distance
    def drive(self, h):
        self.t_dist += self.cur_speed * h

class ElectricCar(Car):
    def __init__(self, num, max_speed, capacity, cur_speed = 0, t_dist = 0):
        super().__init__(num, max_speed, cur_speed = 0, t_dist = 0)
        self.capacity = capacity

class GasolineCar(Car):
    def __init__(self, num, max_speed, volume, cur_speed = 0, t_dist = 0):
        super().__init__(num, max_speed, cur_speed = 0, t_dist = 0)
        self.volume = volume

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars_list = cars

    def hour_passes(self):
        for car in self.cars_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def race_finished(self):
        winners = []
        for car in self.cars_list:
            if car.t_dist >= self.distance:
                winners.append(car)
        return winners

    def print_status(self):
        header = ["Car", "Max Speed", "Current Speed", "Distance(km)"]
        table = []
        for car in self.cars_list:
            table.append([car.num, car.max_speed, car.cur_speed, car.t_dist])
        print(tabulate(table, headers=header, tablefmt="grid"))

# empty list
cars = []
el_c1 = ElectricCar("ABC-15", 180, 52.5)
g_car1 = GasolineCar("ACD-123", 165, 32.5)
el_c1.accelerate(80)
g_car1.accelerate(90)
el_c1.drive(3)
g_car1.drive(3)

print(g_car1.t_dist)
print(el_c1.t_dist)

