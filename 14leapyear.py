#Leap Year Checker

# ✅ Corrected Leap Year Logic:
# There are two valid ways a year can be a leap year:

# 1️⃣ If a year is divisible by 4, and not divisible by 100,
# → ✅ It is a leap year
# (Eg: 2024 → divisible by 4, not by 100)

# 2️⃣ If a year is divisible by 4, divisible by 100, and also divisible by 400,
# → ✅ It is a leap year
# (Eg: 2000 → divisible by 4, 100, and 400)

# 💡 Any other case → ❌ Not a leap year

year=int(input("Enter the year "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("It's a leap year")

        else:
            print("It is not a leap year")
    else:
        print("It's a leap year")
else:
    print("It is not a leap year")

