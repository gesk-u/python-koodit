class DogClass:
    created = 0
    def __init__(self, name, birth_year, sound):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
        DogClass.created += 1
    def bark(self, times):
        for i in range(times):
            print(self.sound)
        return


dog1 = DogClass("Bubbles", 2022, "Yip yip yip")

dog2 = DogClass("Nuggets", 2010, "Bark")

print(f"First dog is named {dog1.name}")
print(f"Second dog is named {dog2.name}")
dog1.bark(3)

print(f"Dogs created: {DogClass.created}")

