#Count vowels in a string.

str="Isn't it so beautiful"
sum=0
for char in str:
    if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
        print(char)
        sum+=1

print("Total number of vowels are",sum)

# ----------------------------------------------------------------------------------------------------------------
# text = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0

# for char in text:
#     if char in vowels:
#         count += 1

# print("Number of vowels:", count)
