#Take a string ➝ count total alphabets, digits, and special characters.

string=input("Enter the string: ")

alphabet=digits=special_character=0

for char in string:
    if char.isalpha():
        alphabet+=1
    elif char.isdigit():
        digits+=1
    else:
        special_character+=1

print("The total number of alphabets:",alphabet)
print("The total number of digits:",digits)
print("The total number of special_character:",special_character)
