import ast
a = (input())#{10:{'a':'11'},5:{'b':'21'},7:{'c':'9'},3:{'d':'15'},11:{}}
x = ast.literal_eval(a)
k = input("Enter a value ")
flag = 0
flag1 = 0
for i in x.values():
    if not bool(i):
        flag1 = list(x.keys())[list(x.values()).index(i)]
    for j in i.keys():
        if(j==k):
            print("seat no =",*i.values())
            print("compartment no =",list(x.keys())[list(x.values()).index(i)])
            flag = 1
if(flag == 0):
    print("Not Found")
if(flag1 != 0):
    print("empty compartment no =",flag1)
else:
    print("No Empty Compartment")
