import re

def uppercase_and_lowercase(s):
    return re.findall(r'[A-Z]+[a-z]+', s)

print(uppercase_and_lowercase("HddddHHjdjwj jHbhb"))