import re

def lowercase_and_underscore(s):
    return re.findall(r'[a-z]+_+[a-z]+', s)

print(lowercase_and_underscore("abc_def ghi_jkl mno_pqr _jugec_"))