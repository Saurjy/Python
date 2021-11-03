Sen = input("Enter The Sentence : ")
List = Sen.split()
List2 = []
[List2.append(i) for i in List if i not in List2]
Dictionary = dict((x,0)for x in List2)
for i in List:
    Dictionary[i] = Dictionary[i] + 1
for i in range (len(List2)):
    print(List2[i] , "=",Dictionary[List2[i]])
