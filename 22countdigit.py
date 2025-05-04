#Count number of digits in a number.

num=int(input())
count=0

while num>0:
    digit=num%10
    count+=1
    num=num//10

print(count)
