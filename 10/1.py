class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.cur_floor = bottom
    def floor_up(self):
        if self.cur_floor < self.top:
            self.cur_floor += 1
            print(f"Elevator is now on floor {self.cur_floor}")
        else:
            print("Elevator is already at the top floor!")

    def floor_down(self):
        if self.cur_floor > self.bottom:
            self.cur_floor -= 1
            print(f"Elevator is now on floor {self.cur_floor}")
        else:
            print("Elevator is already at the bottom floor!")

    def go_to_floor(self, number):
        if number < self.bottom or number > self.top:
            print("Invalid floor number.")
            return
        print(f"Moving from floor {self.cur_floor} to floor {number}...")
        while self.cur_floor < number:
            self.floor_up()
        while self.cur_floor > number:
            self.floor_down()
        print(f"Arrived at floor {self.cur_floor}!\n")


class Building:
    def __init__(self, bottom, top, elv_num):
        self.bottom = bottom
        self.top = top
        self.elevators = []
        for i in range(elv_num):
            elevator = Elevator(bottom, top)
            self.elevators.append(elevator)
        print(f"Building created with {elv_num} elevators.\n")
    def run_elv(self, elv_num, dest_floor):
        if elv_num < 1 or elv_num > len(self.elevators):
            print("Invalid elevator number.")
            return
        print(f"Running Elevator {elv_num}:")
        elevator = self.elevators[elv_num - 1]
        elevator.go_to_floor(dest_floor)
    def fire_alarm(self):
        print("FIRE ALARM!")
        for i, elevator in enumerate(self.elevators, start=1):
            print(f"Elevator {i}:")
            elevator.go_to_floor(self.bottom)
        print("All elevators are now at the bottom floor.")



def main():
    building = Building(0, 10, 3)  # floors 0–10, 3 elevators

    # Run some elevators
    building.run_elv(1, 5)
    building.run_elv(2, 8)
    building.run_elv(3, 3)

    # Trigger fire alarm
    building.fire_alarm()


if __name__ == "__main__":
    main()