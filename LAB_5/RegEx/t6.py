import re

def replace_space_comma_dot_with_colon(s):
    return re.sub(r'[ .,]', ':', s)

print(replace_space_comma_dot_with_colon("Hello, my name is Bekassyl."))