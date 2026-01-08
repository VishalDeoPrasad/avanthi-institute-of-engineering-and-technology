num = [3,5,54,34,5,57,68,8,53,34,45,567]

func = lambda n : n > 50

new_num = list(filter(func, num))

print(new_num)