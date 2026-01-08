num = [1,2,3,4,5,6,7,8,9,10]

# func = lambda n : n * n
def func(n):
    return n*n

ans = list(map(func, num))

print(ans)