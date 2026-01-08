words = ["Python", "map", "function", "example"] 

func = lambda word : len(word)

ans = list(map(func, words))

print(ans)