# To create a simple Python program that stores a student's information (name, roll number, grades)
# and calculates their average marks and grade using variables and appropriate data types.

# Step 01: Get student information
student_name = input("Enter student Name: ")
roll_number = input("Enter Roll Number: ")

# Step 02: Get subject marks
subject_marks1 = float(input("Enter marks for subject 1: "))
subject_marks2 = float(input("Enter marks for subject 2: "))
subject_marks3 = float(input("Enter marks for subject 3: "))

# Step 03: Calculate average marks
average_marks = (subject_marks1 + subject_marks2 + subject_marks3) / 3

# Step 04: Check if student has passed or failed
if subject_marks1 < 33 or subject_marks2 < 33 or subject_marks3 < 33:
    is_passed = False
else:
    is_passed = True

# Step 05: Determine grade based on average marks
if not is_passed:
    grade = "F"
elif average_marks >= 90:
    grade = "A+"
elif average_marks >= 80:
    grade = "A"
elif average_marks >= 70:
    grade = "B"
elif average_marks >= 60:
    grade = "C"
elif average_marks >= 50:
    grade = "D"
elif average_marks >= 33:
    grade = "E"
else:
    grade = "F"

# Step 06: Display student information
print("\n===================== Student Information ====================")
print(f"Name: {student_name}")
print(f"Roll Number: {roll_number}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Subject Marks: {subject_marks1}, {subject_marks2}, {subject_marks3}")
print(f"Passed: {'Yes' if is_passed else 'No'}")
print(f"Grade: {grade}")
print("==============================================================")

