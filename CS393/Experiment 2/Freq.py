N = 14
test_list = [4 ,5 ,5 ,2 ,4 ,5 ,6 ,5 ,2 ,1, 4, 6, 9, 4]
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
        res = i
for i in y:
    if(test_list.count(i) == max):
        Li1.append(i)
        Li2.append(max)
print (Li1)
print (Li2)
