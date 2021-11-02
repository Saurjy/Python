D = 20
B = 7
F = 3
T = 5
sum = 0
while(D!=0):

    if(D>B):

        D = D - B + F
        sum = sum + ((B+F)*T)
        print(sum)

    elif(D<B):

        sum = sum + (D*T)
        D = 0;
        print(sum)

    elif(D==B):

        sum = sum + (B*T)
        D = 0
        print(sum)
