data = {
    'A' : 1, 
    'B' : 2, 
    'C' : 3, 
    'D' : 4, 
    'E' : 5
}

for key in data.keys():
    data[key] = data[key] + 100

print(data)