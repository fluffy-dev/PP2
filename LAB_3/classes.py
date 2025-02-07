from abc import ABC, abstractmethod


class Echo:
    
    __slots__ = ("string")

    def __init__(self):
        self.string: str = ""

    def get_string(self, *args):
        self.string = input(*args)

    def print_string(self, *args):
        print(*args, self.string)

print()
if __name__ == "__main__1":
    echo_copy = Echo()
    echo_copy.get_string("enter string: ")
    echo_copy.print_string("this is your string:")


class Shape(ABC):
    def __init__(self, length: int):
        self.length = length

    @abstractmethod 
    def area(self):
        pass

class Square(Shape):
    def __init__(self, length: int):
        super().__init__(length)

    def area(self) -> int:
        return self.length**2
print()
if __name__ == "__main__":
    square_copy = Square(4)
    print("area of squre 4 to 4:", square_copy.area())


class Rectangle(Shape):
    def __init__(self, length: int, width: int):
        super().__init__(length)
        self.width = width

    def area(self) -> int:
        return self.length*self.width

print()
if __name__ == "__main__":
    rectangle_copy = Rectangle(4, 5)
    print("area of 4 to 5 rectangle:", rectangle_copy.area())
    



class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def show(self) -> tuple:
        return self.x, self.y
    
    def move(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def dist(self, point) -> float:
        return ((self.x-point.x)**2+(self.y-point.y)**2)**0.5

    def __str__(self):
        return f"coors of point x: {self.x}; y: {self.y}"

print()
if __name__ == "__main__":
    first_point = Point(1, 4)
    second_point = Point(-3, 6)
    print("first point", first_point)
    print("second_point", second_point)
    print("dist between is: ", first_point.dist(second_point))


class Account:
    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance

    def check_balance(self):
        print("current balance is:", self.balance)

    def deposit(self, income: int):
        if income > 0:
            self.__balance += income
            print(f"{income} added to your balance")
            self.check_balance()
        else:
            print("income can't be negative")

    def withdraw(self, withdraw_amount: int):
        if withdraw_amount > self.__balance:
            print("you can't withdraw that much money, you just don't have so")
        else:
            self.__balance -= withdraw_amount
            print("successfully")


print()
if __name__ == "__main__":
    rauan_acc = Account("Rauan", 100)
    print(rauan_acc.balance)
    rauan_acc.deposit(40)
    rauan_acc.withdraw(100)
    rauan_acc.check_balance()
    rauan_acc.withdraw(100)
    rauan_acc.check_balance()


def check_to_prime(x:int) -> bool:
    for i in range(2, int(x**0.5)+2):
        if x%i == 0:
            return False
    return True


def find_primes(numbers: list) -> list:
    return list(filter(check_to_prime, numbers))

print()
if __name__=="__main__":
    my_numbers = list(range(1, 100, 4))
    print("current list:", my_numbers)

    print("prime numbers from list:", find_primes(my_numbers))


