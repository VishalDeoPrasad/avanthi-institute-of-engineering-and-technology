words = ["apple", "banana", "cherry", "date"]  

func = lambda word : word.upper()

ans = list(map(func, words))

print(ans)