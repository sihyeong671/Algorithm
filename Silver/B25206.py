total_grade = 0
total_subject_grade = 0
N = 20
for _ in range(20):
    subject, num, grade = input().split()
    if grade == "A+":
        subject_grade = 4.5
    elif grade == "A0":
        subject_grade = 4
    elif grade == "B+":
        subject_grade = 3.5
    elif grade == "B0":
        subject_grade = 3
    elif grade == "C+":
        subject_grade = 2.5
    elif grade == "C0":
        subject_grade = 2
    elif grade == "D+":
        subject_grade = 1.5
    elif grade == "D0":
        subject_grade = 1
    elif grade == "F":
        subject_grade = 0

    if grade == "P":
        continue
    total_subject_grade += float(num) * subject_grade
    total_grade += float(num)
print(total_subject_grade / total_grade)