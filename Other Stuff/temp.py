x = {10:{'a' : '11'},5:{'b':'21'},7:{'c':'9'},3: {'d':'15'}, 11:{}}
k = input("Enter a value ")
flag = 0
flag1 = 0
for i in x.values():
    if not bool(i):
        flag1 = list(x.keys())[list(x.values()).index(i)]
print(flag1) 
