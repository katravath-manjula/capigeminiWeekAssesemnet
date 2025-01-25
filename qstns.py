#*Temperature conversioon#
#ef temperature('fahrenhit' )

sn = input("Enter the student name: ")
marks = int(input("Enter the marks: "))

if marks > 90:
    grade = "A"
elif 75 <= marks <= 90:
    grade = "B"
elif 50 <= marks < 75:
    grade = "C"
else:
    grade = "D"

print(f"Student Name: {sn}")
print(f"Marks: {marks}")
print(f"Grade: {grade}")






