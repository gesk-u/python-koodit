from math import pi

def main():
    diameter1 = float(input("Diameter 1 (cm): "))
    price1 = float(input("Price 1(euros): "))
    diameter2 = float(input("Diameter 2 (cm): "))
    price2 = float(input("Price 2 (euros): "))

    per_sq_m1 = calc_p(diameter1, price1)
    per_sq_m2 = calc_p(diameter2, price2)
    print(f"The price of the pizza number 1 per square meter: {per_sq_m1}")
    print(f"The price of the pizza number 2 per square meter: {per_sq_m2}")
    if per_sq_m1 > per_sq_m2:
        print(
            f"Pizza number 2 with diameter {diameter2} cm "
            f"and price {price2} euros provides better value for money"
        )
    elif per_sq_m2 > per_sq_m1:
        print(
            f"Pizza number 1 with diameter {diameter1} cm "
            f"and price {price1} euros provides better value for money"
        )
    else:
        print("Both pizzas cost the same")

def calc_p(diameter, price):
    r_meters = diameter/200
    area = pi * r_meters**2
    return price/area
main()