#Reverse a number using while loop.

num=int(input("Enter the number "))
reversed_digit=""
while num>0:
    digit=num%10
    reversed_digit+=str(digit)
    num=num//10

print(reversed_digit)

# # ------------------------------------------------------------------------------------------------------------

# num=int(input("Enter the number "))
# reverse=0

# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num=num//10
# print(reverse)