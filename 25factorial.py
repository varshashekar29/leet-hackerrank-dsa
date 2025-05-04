#Factorial Calculator using for loop.

num=int(input())
fact=1

if num>0:
    for i in range(num,1,-1):
        fact*=i
    print(fact)
else:
    print("No factorial for negative numbers")



