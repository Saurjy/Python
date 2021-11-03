word = input("Enter The String : ")
List = [char for char in word]
Search_word = List[0]
i = 0
for i in range(1,len(List),+1):
    if(Search_word == List[i]):
        List[i]='$'
Word = "".join(List)
print(Word)
