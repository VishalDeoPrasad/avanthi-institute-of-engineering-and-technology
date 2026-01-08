words = ["madam", "racecar", "hello", "world", "level", "python"]

func = lambda word : word == word[::-1]

ans = list(filter(func, words))

print(ans)