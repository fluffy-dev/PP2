counter = 2
while counter <= 8:
    print(counter)
    counter += 2

counter = 1
while counter <= 8:
    if counter == 5:
        print("Loop interrupted at 5")
        break
    counter += 1

counter = 0
while counter <= 8:
    counter += 1
    if counter == 4:
        print("Skipping 4")
        continue
    print(counter)

counter = 2
while counter <= 8:
    print(f"Current number: {counter}")
    counter += 2
else:
    print("Loop completed, counter is greater than 8")
