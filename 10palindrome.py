#Check if the string is a palindrome.

# string="Malayalam" #Since python is case sensitive we should convert it to one case
# string2=string.lower()
# palindrome=(string2[::-1])

# if string2==palindrome:
#     print("Given string",string,"is palindrome")
# else:
#     print("Given string",string,"is not a palindrome")

# -----------------------------------------------------------------------------------------------------------------------

def check_palindrome(string):
    string2=string.lower()
    reversed_string=string2[::-1]
    if reversed_string == string2:
        print("Given string",string,"is palindrome") 
    else:
        print("Given string",string,"is not a palindrome") 

string=input("Enter a string: ")
check_palindrome(string)