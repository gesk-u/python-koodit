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

# a new car (registration number ABC-123, maximum speed 142 km/h).
car = Car("ABC-123", 142)
# print out all the properties of the new car
print(car.__dict__)
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"After acceleration: {car.cur_speed} km/h")
# the emergency brake by forcing a -200 km/h
car.accelerate(-200)
print(f"After braking: {car.cur_speed} km/h")

car.accelerate(60)
car.drive(7)
print(car.t_dist)
car.drive(2)
print(car.t_dist)

# empty list
cars = []
# filling up 'cars' with 10 new cars with random 'max_speed'
for i in range(10):
    max_speed = random.randint(100, 200)
    cars.append(Car(f"ABC-{i + 1}", max_speed))

# breaks while loop if the race is over
race_over = False
# Number of hour race has taken
hours = 0

while not race_over:
    # Add ah hour after every circle
    hours += 1
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        # all cars drive for 1 hour before the next loop
        car.drive(1)
        # winning condition
        if car.t_dist >= 10000:
            print(f"Car {car.num} won the race after {hours} hours!")
            race_over = True
            break

header = ["Car", "Max Speed", "Current Speed", "Distance(km)"]
table = []
for car in cars:
    table.append([car.num, car.max_speed, car.cur_speed, car.t_dist])

# print out the table
print(tabulate(table, headers=header, tablefmt="grid"))