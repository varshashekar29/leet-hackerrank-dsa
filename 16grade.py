#Accept a grade (A, B, C, D) and print corresponding message.

student_name=input("Enter student name ")
student_grade=input("Enter grade ")

if student_grade=="A":
    print(student_name,"is excellent in his studies")
elif student_grade=="B":
    print(student_grade,"is good in his studies")
elif student_grade=="C":
    print(student_grade,"is just pass in studies")
else:
    print(student_grade,"is bad at his studies")



