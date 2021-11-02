x = [1, 2, 3, 2, 3, 4, 4, 2, 1]
print (x)
y = []
for i in x:
    if i not in y:
        y.append(i)
print (y)
