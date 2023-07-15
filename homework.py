num_students = int(input("Enter the number of students in the class: "))

grades = []
for i in range(num_students):
    grade = float(input("Enter the grade for student {}: ".format(i + 1)))
    grades.append(grade)

average_grade = sum(grades) / num_students
min_grade = min(grades)

print("Average grade:", average_grade)
print("Minimum grade:", min_grade)
