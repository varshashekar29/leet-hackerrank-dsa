#Count consonant in a string.

str="HAi how do you do"
count=0
for char in str:
    if char!="a" and char!="e" and char!="i" and char!="o" and char!="u":
        if char.isalpha():
            print(char)
            count+=1
print(count,"consonants are present in the string")

# --------------------------------------------------------------------------------------------------------------------------
# text = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0

# for char in text:
#     if char in vowels:
#         count += 1

# print("Number of vowels:", count)
