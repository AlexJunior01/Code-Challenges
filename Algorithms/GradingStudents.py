def gradingStudents(grades):
    new_grade = []
    for grade in grades:
        new_grade.append(roundingGrade(grade))
    
    for grade in new_grade:
        print(grade)


def roundingGrade(grade):
    if grade < 38:
        return grade
    
    if (grade + 1) % 5 == 0:
        return grade+1
    elif (grade + 2) % 5 == 0:
        return grade+2
    else:
        return grade


n_students = int(input())
grades = []

for i in range(n_students):
    grades.append(int(input()))

gradingStudents(grades)

