#BMI Calculator: Accept height (in meters) and weight (in kg), calculate BMI, and tell if the person is underweight, normal, overweight, or obese.

name=input("Enter your name: ")
weight=float(input("Enter your weight in kg "))
height=float(input("Enter your height in meters "))

bmi=weight/(height**2)

if bmi<18.5:
    print("You are underweight")
elif bmi<25:
    print("You are normal weight")
elif bmi<30:
    print("You are overweight")
else:
    print("You are obese")