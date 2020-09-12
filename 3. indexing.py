fruits = ["a","b","c"]
indices = [0,1,2]

for i in indices:
    print(i, fruits[i])

for i in indices:
    index = len(fruits)-1-i
    print(i, index, fruits[index])
    
