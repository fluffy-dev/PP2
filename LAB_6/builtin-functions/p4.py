import time
from math import sqrt

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  
    return sqrt(number)

num = 25100
delay = 2123
print(f"Square root of {num} after {delay} milliseconds is {delayed_sqrt(num, delay)}")
