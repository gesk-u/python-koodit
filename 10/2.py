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
# filling up 'cars' with 10 new cars with random 'max_speed'
for i in range(10):
    max_speed = random.randint(100, 200)
    cars.append(Car(f"ABC-{i + 1}", max_speed))

hours = 0
race = Race("Race", 10000, cars)

while True:
    hours+=1
    race.hour_passes()
    winners = race.race_finished()

    if winners:
        race.print_status()
        print(f"Race finished in {hours} hours!")
        for winner in winners:
            print(f"Winner {winner.num}")
        break
