import math

def area_of_regular_polygon(n_sides, side_length):
    return (n_sides * side_length ** 2) / (4 * math.tan(math.pi / n_sides))

n_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = area_of_regular_polygon(n_sides, side_length)
print("The area of the polygon is:", round(area, 2))