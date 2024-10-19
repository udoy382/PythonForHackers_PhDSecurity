"""
dict = {
    'name':'Udoy',
    'age':30
}

print(dict)
print(dict['name'])

dict2 = {}
print(dict2)

dict2['id'] = 1
print(dict2)

for thing in dict:
    print(thing)
    print(dict[thing])
"""

# EXERCISES >

"""
student_grades = {}

off = False
while not off:
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")

    student_grades[name] = grade
    print("Student added successfully!")

    add_another = input("Would you like to add another student: Y or N > ").lower()

    if add_another == "y":
        pass
    else:
        off = True

print(student_grades)
"""