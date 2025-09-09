import math

def swap_coordinates(point):
    (x, y) = point

    return (y, x)

def calc_dist(point1, point2):
    d = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    return d

point = (int(input("Give x: ")), int(input("Give y: ")))
sw_point = swap_coordinates(point)
print(sw_point)
print(f"d = {calc_dist(point, sw_point):.2f}")
