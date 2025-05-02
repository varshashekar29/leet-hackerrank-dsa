#Accept a number and check if it’s even or odd and greater than 50.

num=int(input("Enter a number "))

if num%2==0:
    if num>50:
        print("The number is greater than 50 and it is even")
    else:
        print("The number is even but it is not greater than 50")
else:
    if num>50:
        print("The number is greater than 50 and it is odd")
    else:
        print("The number is odd but it is not greater than 50")
