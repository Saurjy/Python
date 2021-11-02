Temp = input("Enter The Entire List or Sentence : ")
Test_list = Temp.split()
Digit_list = [i for i in Test_list if i.isdigit()]
String_list =[i for i in Test_list if i not in Digit_list]
print("The DIGITS are :",Digit_list)
print("The STRINGS are :",String_list)
