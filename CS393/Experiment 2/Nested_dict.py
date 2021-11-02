x = {1:{'a':'apple'},2:{'b':'ball'},3:{'c':'cat'}}
k = input("Enter a value ")
flag = 0
for i in x.values():
    for j in i.keys():
        if(j==k):
            print(i.values())
            print(list(x.keys())[list(x.values()).index(i)])
            flag = 1
            break
    if(flag==1):
        break
if(flag == 0):
    print("Not Found")
