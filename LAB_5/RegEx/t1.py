import re 

def a_and_b(s):
    return re.fullmatch(r'a[b]*', s) is not None

print(a_and_b("a"))  
print(a_and_b("abbb"))  
print(a_and_b("ac"))  
print(a_and_b("bb"))  
