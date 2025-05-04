#Print Fibonacci series up to n terms.
#F(n)=F(n-1)+F(n-2)

num=int(input("Enter the number "))
a=0
b=1
count=0

print("Fibnocci Series:")

while count<num:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    count+=1
    



