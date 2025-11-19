class Food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
    def print_info(self):
        print(f"Name: {self.name}; Calories: {self.calories};")

class Fruit(Food):
    def __init__(self, name, calories, is_sweet):
        super().__init__(name, calories)
        self.is_sweet = is_sweet
    def print_info(self):
        super().print_info()
        print(f"Sweet: {self.is_sweet}")

class Vegetable(Food):
    def __init__(self, name, calories, is_leafy):
        super().__init__(name, calories)
        self.is_leafy = is_leafy
    def print_info(self):
        super().print_info()
        print(f"Leafy: {self.is_leafy}")

class Store:
    def __init__(self, products):
        self.products= {
            products.name : products
        }
    def available(self):
        for name, product in self.products.items():
            product.print_info()
            print()
    def add_food(self, product):
        self.products[product.name] = product
    def buy_product(self, product_name):
        name = product_name.lower()
        if name in self.products:
            return self.products[name]
        return None


class Smoothie:
    def __init__(self, name, store):
        self.name = name
        self.cocktail = []
        self.store = store
    def bought(self, product):
        bought = self.store.buy_product(product)
        if bought:
            self.cocktail.append(bought)
            print(f"{bought.name} is added to cocktail!")
        else:
            print(f"{product} is not available")
    def print_info(self):
        total_calories = 0
        for i in range(len(self.cocktail)):
            if self.cocktail[i].calories:
                total_calories += self.cocktail[i].calories
        print(f"{self.name};\nTotal_calories: {total_calories}")






mango = Fruit("mango", 14, True)
apple = Fruit("apple", 10, True)
tomato = Vegetable("tomato", 15, False)
cucumber = Vegetable("cucumber", 5, False)
cheese = Food("cheese", 80)
store1 = Store(mango)
store1.add_food(apple)
store1.add_food(tomato)
store1.add_food(cucumber)
store1.add_food(cheese)

store1.available()

cocktail_name = input("How do you want to call your cocktail? ").capitalize()
cocktail = Smoothie(cocktail_name, store1)
print("You are in the store and you are looking for some products to add in your cocktail")

print("These are available products for you:")
store1.available()

while True:
    product_to_cocktail = input("What product do you want to buy? or press Enter to escape ").lower()
    if product_to_cocktail == "":
        break
    cocktail.bought(product_to_cocktail)


print(f"Alright your {cocktail.name} cocktail is ready come to our store again if you wand another one")

cocktail.print_info()
