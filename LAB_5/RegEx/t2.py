import re

def a_and_2_3_b(s):
    return re.fullmatch(r'a[b]{2,3}', s) is not None

print(a_and_2_3_b("abb"))  # True
print(a_and_2_3_b("abbbb"))  # False