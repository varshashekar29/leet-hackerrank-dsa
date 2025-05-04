#Palindrome Checker using loop (numbers and strings).

#For numbers

num=int(input("Enter a number "))
final_num=num
reverse_num=0

while num>0:
    digit=num%10
    reverse_num=reverse_num*10+digit
    num=num//10

if reverse_num==final_num:
    print(final_num,"is palindrome")
else:
    print(final_num,"is not a palindrome")