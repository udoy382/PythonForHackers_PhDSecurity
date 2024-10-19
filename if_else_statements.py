"""
fnum = input("What is the first number: ")
snum = input("What is the second number: ")

if fnum > snum:
    print("the first number is larger!")
elif snum > fnum:
    print("the second number is larger.")
else:
    print("The numbers are equal!")
"""

# EXERCISE:
"""
score = int(input("What is your score? "))

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
elif score <= 60:
    print("Grade F")
else:
    print("Oops! Something went wrong. Please try again")
"""

# Nested if statement ~
"""
score = int(input("What is your score? "))

if score >= 90:
    age = int(input("What is your age? "))
    if age < 10:
        print("Your grade is an A+")
    else:
        print("Your grade is an A")
elif score >= 80:
    age = int(input("What is your age? "))
    if age < 10:
        print("Your grade is an B+")
    else:
        print("Your grade is an B")
elif score >= 70:
    age = int(input("What is your age? "))
    if age < 10:
        print("Your grade is an C+")
    else:
        print("Your grade is an C")
elif score >= 60:
    age = int(input("What is your age? "))
    if age < 10:
        print("Your grade is an D+")
    else:
        print("Your grade is an D")
elif score <= 60:
    print("Grade F")
else:
    print("Oops! Something went wrong. Please try again")
"""
