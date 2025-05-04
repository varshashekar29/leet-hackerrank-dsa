#Print center aligned pyramid

rows=int(input())

for i in range(1,rows+1):
    print(" "*(rows-i),end="") #one space is given to align pyramid to center
    for j in range(1,i+1):
        print(j,end=" ")
    print()