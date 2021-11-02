import numpy
Rows = int(input("Enter the number of rows : "))
Cols = int(input("Enter the number of coloumns : "))
Mat=[]
for i in range(Rows):
    col = []
    for j in range(Cols):
        col.append(int(input("Enter the value : ")))
    Mat.append(col)
print(numpy.transpose(Mat))
