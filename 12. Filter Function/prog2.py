num = [1,2,3,4,5,6,7,8,9,10]

func = lambda n : n%2 != 0

odd = list(filter(func, num))

print(odd)