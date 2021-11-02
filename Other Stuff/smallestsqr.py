from math import sqrt
N = int(input())
x = int(10**N)
for i in range(int(x/10),x-1):
    a = i
    s = a
    j = 0
    flag = 0
    List=[]
    List2=[]
    while(a>0):
        if(a%10 != 0):
            flag = 1
        else:
            flag = 0
            break
        List.append(a%10)
        j+=1
        a=int(a/10)
    if(flag == 0):
        continue
    for k in List:
        List2.append(int(k*k))
    n = sum(List2)
    k = int(sqrt(n))
    if(k*k == n and flag == 1):
        print(s)
        break
