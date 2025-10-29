class Animals:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def sound(self):
        return "AAA"
    def print_name(self):
        print(f"Name: {self.name}")
class Lion(Animals):
    def sound(self):
        return "Roar, roar"
class Elephant(Animals):
    def sound(self):
        return "Pawoo!"
class Snake(Animals):
    def sound(self):
        return "Shhhhh"

class Zoo:
    def __init__(self):
        self.total = 0
        self.animals = []

    def add_animal(self, animal):
        self.total += 1
        self.animals.append(animal)

    def get_info(self):
        print(f"We have {self.total} animals in the Zoo")
        for i in self.animals:
            print(f"Name: {i.name}; Species: {i.species}")

    def all_cry(self):
        for i in self.animals:
            print(i.sound())




lion1 = Lion("Leo", "leo")
elph1 = Elephant("Pullo", "African forest elephant")
snake1 = Snake("Lady", "King cobra")

lion1.sound()
elph1.sound()
snake1.sound()

zoo = Zoo()
zoo.add_animal(lion1)
zoo.add_animal(elph1)
zoo.add_animal(snake1)

zoo.get_info()

zoo.all_cry()


