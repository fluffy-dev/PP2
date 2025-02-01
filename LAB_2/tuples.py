fruit_tuple = ("grape", "orange", "pear", "grape", "pear")
print(fruit_tuple)

fruit_tuple = ("grape", "orange", "pear")
print(fruit_tuple[1])

fruit_tuple = ("grape", "orange", "pear")
print(fruit_tuple[-1])

large_fruit_tuple = ("grape", "orange", "pear", "watermelon", "kiwi", "peach", "plum")
print(large_fruit_tuple[2:5])

print(large_fruit_tuple[:4])

print(large_fruit_tuple[2:])

modified_tuple = ("grape", "orange", "pear")
temp_list = list(modified_tuple)
temp_list[1] = "watermelon"
modified_tuple = tuple(temp_list)

print(modified_tuple)

print(*modified_tuple)

for item in modified_tuple:
    print(item)

tuple_a = ("x", "y", "z")
tuple_b = (10, 20, 30)

combined_tuple = tuple_a + tuple_b
print(combined_tuple)

fruit_multiply = ("grape", "orange", "pear") * 2
print(fruit_multiply)

fruits = ("grape", "orange", "pear")
print(fruits[0])

print(len(fruits))

print(fruits[-1])

print(large_fruit_tuple[2:5])
