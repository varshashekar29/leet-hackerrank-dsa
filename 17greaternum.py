# Take two numbers, check which is greater and if they are both odd or even.


def check_even_odd(num):
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")



num1=int(input("Enter the first number "))
num2=int(input("Enter the second number "))

if num1>num2:
    print(num1,"is greater number")
    check_even_odd(num1)
else:
    print(num2,"is greater number")
    check_even_odd(num2)



