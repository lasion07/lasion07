list_a = {1,2,3,4,7,8}
list_b = {1,2,5}

def check(list_a,list_b):
    return (list_a & list_b) == list_b


print(check(list_a,list_b))