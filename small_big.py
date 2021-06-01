largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try :
         if num == "done":
             break
         else:
             num = int(num)
         if largest == None:
            largest = num
            smallest = num
         if largest < num :
            largest = num
         if smallest > num :
           smallest = num
    except:
          print("Invalid input")
print("Maximum is", largest)
print("Minimum is", smallest)
