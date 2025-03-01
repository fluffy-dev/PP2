import re

def sentence_and_a_last_b(s):
    return re.fullmatch(r'a.*b', s) is not None

print(sentence_and_a_last_b("kjhbgvab"))
print(sentence_and_a_last_b("anjhvgbbb  _ahvgeb"))