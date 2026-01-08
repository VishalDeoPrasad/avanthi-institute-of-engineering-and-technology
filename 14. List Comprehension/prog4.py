num = [1,2,3,4,5,6,7,8,9,10]

num_list = []
for n in num:
    if n % 2 == 0:
        num_list.append("Even")
    else:
        num_list.append("Odd")

print(num_list)