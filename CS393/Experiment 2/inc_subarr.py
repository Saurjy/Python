Temp = input()
test_list = Temp.split()
for i in range(len(test_list)):
    test_list[i] = int(test_list[i])
test_list=[ 4, 6, 1, 2, 3, 4, 1, 2, 3]
p_max=0
p_flag=0
for i in range(len(test_list)):
    print(i)
    max = 0
    for j in range(i,len(test_list)):
        if(test_list[j]>test_list[j-1]):
            max+=1
            flag = i-1
        else:
            break
    if(max>p_max):
        p_max=max
        p_flag=flag
print(p_flag,p_max+p_flag)
