fruit_set = {"grape", "orange", "pear"}

new_fruit_set = {"grape", "orange", "pear"}
print(new_fruit_set)

for item in new_fruit_set:
    print(item)

new_fruit_set.add("kiwi")
print(new_fruit_set)

new_fruit_set.remove("orange")
print(new_fruit_set)

new_fruit_set.discard("kiwi")
print(new_fruit_set)

for fruit in new_fruit_set:
    print(fruit)

set_a = {"x", "y", "z"}
set_b = {10, 20, 30}

union_set = set_a.union(set_b)
print(union_set)

set_a.update(set_b)
print(set_a)

fruit_check = {"grape", "orange", "pear"}
if "grape" in fruit_check:
    print("Yes, grape is in the set!")

more_fruits = {"watermelon", "kiwi", "plum"}
fruit_check.update(more_fruits)

fruit_check.remove("orange")
fruit_check.discard("watermelon")

car_details = {
    "brand": "Tesla",
    "model": "Model S",
    "year": 2019
}
print(car_details.get("model"))

car_details["year"] = 2025
car_details["color"] = "blue"
car_details.pop("model")
car_details.clear()
