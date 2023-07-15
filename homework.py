a = int(input("tedad danesh amozan ra benevisid: "))

grades = []
for i in range(a):
    grade = float(input("Enter the grade for student {}: ".format(i + 1)))
    grades.append(grade)

average_grade = sum(grades) / a
min_grade = min(grades)

print("Average grade:", average_grade)
print("Minimum grade:", min_grade)
