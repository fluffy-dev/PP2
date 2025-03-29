def all_true(tpl):
    return all(tpl)

print(all_true((True, True, 1, "hello")))  
print(all_true((True, False, 1))) 
