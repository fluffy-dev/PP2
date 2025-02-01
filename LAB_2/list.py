fruit_list = ["grape", "orange", "pear"]

new_fruit_list = ["grape", "orange", "pear"]
print(new_fruit_list)

new_fruit_list = ["grape", "orange", "pear", "grape", "pear"]
print(new_fruit_list)

new_fruit_list = ["grape", "orange", "pear"]
print(new_fruit_list[1])

letters = ["x", "y", "z"]
numbers = [10, 20, 30]

combined_list = letters + numbers
print(combined_list)

fruit_types = ["grape", "orange", "pear"]
print(fruit_types[1])

fruit_types = ["grape", "orange", "pear"]
fruit_types[0] = "watermelon"

fruit_types.append("pineapple")

fruit_types.insert(1, "strawberry")

fruit_types.remove("orange")

print(fruit_types[-1])

large_fruit_list = ["grape", "orange", "pear", "watermelon", "kiwi", "peach", "plum"]
print(large_fruit_list[2:5])

print(len(large_fruit_list))

large_fruit_list.sort()
print("Sorted list:", large_fruit_list)

large_fruit_list.reverse()
print("Reversed list:", large_fruit_list)

count_grape = large_fruit_list.count("grape")
print("Count of 'grape':", count_grape)

large_fruit_list.clear()
print("Cleared list:", large_fruit_list)
