#Grade Calculator: Accept marks and print the grade using the following scale:
# 90–100: A+
# 80–89: A
# 70–79: B
# 60–69: C
# Below 60: Fail

student_name=(input("Enter student name: "))
student_marks=int(input("Enter student marks: "))

if student_marks<100 and student_marks>90:
    print(student_name,"has secured A+ grade")
elif student_marks<89 and student_marks>80:
    print(student_name,"has secured A grade")
elif student_marks<79 and student_marks>70:
    print(student_name,"has secured B grade")
elif student_marks<69 and student_marks>60:
    print(student_name,"has secured C grade")
elif student_marks<60:
    print(student_name,"has failed in exam")