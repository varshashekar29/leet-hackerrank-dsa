#Palidrome for string can be done through slicing and loop
#while checking palidrome convert all the string into lower case

# string=input("Enter string ")
# string2=string.lower()
# reversed=string[::-1]

# if string2==reversed:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# -----------------------------------------------------------------------------------------------------------------------

string=input("Enter string ")
string2=string.lower()
reverse=""

for char in string2:
    reverse=char+reverse

print(reverse)
if reverse==string2:
    print("Palindrome")
else:
    print("Not a palindrome")