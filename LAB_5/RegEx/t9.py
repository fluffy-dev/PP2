import re

def insert_spaces_before_capitals(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

print(insert_spaces_before_capitals("ThisIsAJustString"))
