a = int(input("tedad danesh amozan ra benevisid: "))

grades = []
for i in range(a):
    grade = float(input("nomre danesh amoz {}: ".format(i + 1)))
    grades.append(grade)

average_grade = sum(grades) / a
min_grade = min(grades)

print("Ave grade:", average_grade)
print("Mini grade:", min_grade)
