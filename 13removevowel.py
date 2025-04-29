#Accept a string ➝ remove all vowels.

string=input("Enter the string: ")

vowels="aeiouAEIOU"
final_string=""

for char in string:
    if char not in vowels:
        final_string+=char

print(final_string)

