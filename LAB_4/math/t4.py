def area_of_parallelogram(base, height):
    return base * height

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = area_of_parallelogram(base, height)
print("Expected Output:", area)