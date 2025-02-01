
num1 = float(input(""))
do = input("")
b = float(input(""))

if do == "+" :
    c = num1 + b
elif do == "-" : 
    c = num1 - b
elif do == "*" :
    c = num1*b
else :
    c = num1/b
    
print(c)