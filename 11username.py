#Accept user’s first and last name ➝ print full name in reverse order.

first_name=input("Enter first name: ")
last_name=input("Enter last name: ")

full_name=first_name+" "+last_name

reverse_name=full_name[::-1]
print(reverse_name,"is the reversed name")