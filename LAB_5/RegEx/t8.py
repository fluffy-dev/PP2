import re

def split_at_uppercase(s):
    return re.split(r'(?=[A-Z])', s)

print(split_at_uppercase("BekassylAmanshaevKanyshovich"))