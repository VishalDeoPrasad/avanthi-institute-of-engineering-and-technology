data = {
    'A' : 1, 
    'B' : 2, 
    'C' : 3, 
    'D' : 4, 
    'E' : 5
}

for val in data.values():
    if val == 2:
        print("Value Exists")
        break
    else:
        print("Value Not Found")

