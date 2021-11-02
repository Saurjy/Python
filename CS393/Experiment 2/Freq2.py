N = int(input())
Temp = input()
test_list = Temp.split()
for i in range(len(test_list)):
    test_list[i] = int(test_list[i])
Li1=[]
Li2=[]
y = []
for i in test_list:
    if i not in y:
        y.append(i)
max = 0
for i in test_list:
    freq = test_list.count(i)
    if freq > max:
        max = freq
for i in y:
    if(test_list.count(i) == max):
        Li1.append(i)
        Li2.append(max)
print (Li1)
print (Li2)
S1 = str(Li1[0])
S2 = str(Li2)
print (S1)
print (S2)
