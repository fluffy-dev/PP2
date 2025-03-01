import re

def snake_to_camel(s):
    camelCase = re.sub(r'_(.)', lambda x: x.group(1).upper(), s)
    return camelCase[0].lower() + camelCase[1:]


print(snake_to_camel("Bekassyl_Amanshaev_kanyshovich"))