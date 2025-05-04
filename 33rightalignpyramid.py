#Print right aligned pyramid

rows=int(input())

for i in range(1,rows+1):
    print("  "*(rows-i),end="")  #Two spaces are given to push the alignment to right
    for j in range(1,i+1):
        print(j,end=" ")
    print()