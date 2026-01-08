words = ["apple", "bat", "dog", "elephant", "cat", "fish"]

func = lambda word : len(word) < 4

ans = list(filter(func, words))

print(ans)