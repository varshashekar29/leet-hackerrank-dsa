#print reverse number pyramid

rows=int(input("Enter the rows "))

for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

    #end="" ---> Keeps printing on the same line with a space
#     end=""	No space or newline between prints
# end="\t"	Adds a tab
# end="\n"	(default) Moves to a new line
# print() function adds a newline (\n) after each print.
