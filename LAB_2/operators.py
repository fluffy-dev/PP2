
print("Arithmetic Operators:")
x = 10
y = 3
print(5 + 2) 
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 // 2)
print(5 ** 2)
print(5 % 2)
print("\n")

#Assignment Operators
print("Assignment Operators:")
a = b = c = d = e = f = g = 5
a += 3 
print(a)
b -= 2  
print(b)
c *= 4 
print(c)
d /= 2  
print(d)
e %= 3 
print(e)
f //= 2  
print(f)
g **= 2
print(g)
print("\n")

# Comparison Operators
print("Comparison Operators:")
a = 10
b = 20
print(a == b)  
print(a != b)  
print(a > b)  
print(a < b)  
print(a >= b) 
print( a <= b)  
print("\n")

# Logical Operators
print("Logical Operators:")
c = True
d = False
print("c and d:", c and d)  
print("c or d:", c or d)    
print("not c:", not c)     
print("\n")

x = 5
y = 7
if x == 5 and y == 7 :
    print("x equals 5 and y equals 7")
if x == 5 or y == 9 :
    print("x equals 5 or y equals 9")

# Bitwise Operators
print("Bitwise Operators:")
e = 5  #101
f = 3  #011
print("e & f (AND):", e & f)   
print("e | f (OR):", e | f)    
print("e ^ f (XOR):", e ^ f)   
print("~e (NOT):", ~e)         
print("e << 1 (Сдвиг влево):", e << 1)
print("e >> 1 (Сдвиг вправо):", e >> 1)
print("\n")

# Membership Operators
print("Membership Operators:")
lst = [1, 2, 3, 4, 5]
print("2 in lst:", 2 in lst)  
print("7 not in lst:", 7 not in lst)  
print("\n")

# Identity Operators
print("Identity Operators:")
g = [1, 2, 3]
h = [1, 2, 3]
i = g
print("g is i:", g is i)  
print("g is h:", g is h)  
print("g is not h:", g is not h)
