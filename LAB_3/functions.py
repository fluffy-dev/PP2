from itertools import permutations
import random

def gram_to_ounce(grams: float) -> float:
    return 28.3495231 * grams

if __name__ == "__main__":
    print(f"100 grams is {gram_to_ounce(100)} ounces")


def fahrenheit_to_celcius(fahrenheit: float) -> float:
    return  (5 / 9) * (fahrenheit - 32)

print()
if __name__ == "__main__":
    print(f"400 fahrenheit is {fahrenheit_to_celcius(400)} celcius")


def puzzle_solver(heads: int, legs: int):
    """
    one chicken have 2 legs and 1 head
    one rabbit have 4 legs and 1 head
    
    so heads amount is a amount of all animals

    if A is a amount of chickens and B is amount of rabbits, we have such that system of equations:
    A+B = heads
    A*2+B*4 = legs

    if we reduce this system we have:
    A = heads-B
    (heads-B)*2+B*4 = legs

    from this we have:

    heads*2+B*2 = legs

    (legs-2*heads)/2 = B

    """
    amount_of_rabbits = (legs-2*heads)/2
    amount_of_chicken = heads-amount_of_rabbits
    return amount_of_rabbits, amount_of_chicken

print()
if __name__ == "__main__":
    heads = 35
    legs = 94
    print("rabbits; chickens")
    print(puzzle_solver(35, 94))


def is_prime(x: int):
    for i in range(2, int(x**0.5)+2):
        if x%i==0:
            return False
    return True


def find_primes(numbers: list):
    return list(filter(is_prime, numbers))


print()
if __name__ == "__main__":
    my_list = list(range(1, 90, 3))
    print(my_list)
    print(find_primes(my_list))



def all_permutations(string: str):
    return ["".join(permutation) for permutation in permutations(string)]

print()
if __name__ == "__main__":
    print(all_permutations("abc"))



def reverse_string(string: str):
    return " ".join(string.split()[::-1])

print()
if __name__ == "__main__":
    print("This is my string")
    print(reverse_string("This is my string"))


def find_33(numbers: list):
    for i in range(1, len(numbers)):
        if numbers[i-1] == 3 and numbers[i] == 3:
            return True

    return False


print()
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 3, 3]
    print(my_list)
    print("contains 33:", find_33(my_list))


def find_007(numbers: list):
    pattern = [0, 0, 7]
    
    for i in numbers:
        if not pattern:
            return True

        if pattern[0] == i:
            pattern.pop(0)

    if pattern:
        return False
    return True


print()
if __name__ == "__main__":
    my_list = [1, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 7]
    print(my_list)
    print("is spy:", find_007(my_list))



def calculate_volume(radius: float) -> float:
    return 3.14*(3/4)*radius**3

print()
if __name__ == "__main__":
    print("radius is 4")
    print("volume is", calculate_volume(4))


def find_unique(numbers: list):
    
    result = []
    for i in numbers:
        if i not in result:
            result.append(i)

    return result


print()
if __name__ == "__main__":
    my_list = [1, 1, 1, 1, 1, 2, 3, 4]
    print(my_list)
    print(find_unique(my_list))



def show_histogram(numbers: list[int]):
    for i in numbers:
        print("*"*i)

print()
if __name__ == "__main__":
    my_list = [4, 9, 5]
    show_histogram(my_list)



def guess_number():
    number = random.randint(1, 100)
    print("number between 1, 100")
    print("log_2 (100) is 7 ;)")
    while running:
        guess = int(input("take a guess: "))
        if guess < number:
            print("too low")
        elif guess > number:
            print("too high")
        else:
            print("your right number was", number)
            running = False


