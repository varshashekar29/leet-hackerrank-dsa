#Armstrong Number Checker
#A number is called an Armstrong number if the sum of the cubes of its digits (or nth powers for n digits) is equal to the number itself.

# 153
# Digits = 1, 5, 3
# Check: 1+125+27=153 is a armstrong number

num=int(input("Enter number "))
final_num=num
cube=0

while num>0:
    digit=num%10
    cube+=(digit*digit*digit)
    num=num//10

print("The cube number is",cube)

if final_num==cube:
    print("This is armstrong number")
else:
    print("Not a armstrong number")




