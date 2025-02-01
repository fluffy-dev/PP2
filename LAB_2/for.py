fruit_list = ["grape", "orange", "pear"]
for fruit in fruit_list:
    print(f"Fruit: {fruit}")

for fruit in fruit_list:
    if fruit == "orange":
        continue
    print(f"Skipped orange, current fruit: {fruit}")

for _ in range(4):  # Использую другой диапазон
    print("Loop Iteration")

for fruit in fruit_list:
    if fruit == "orange":
        print("Stopping loop at orange")
        break
    print(f"Fruit before stop: {fruit}")

for _ in [10, 20, 30]:  # Просто другая структура для прохода
    pass  # Пустой блок для синтаксического примера
