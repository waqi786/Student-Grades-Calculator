student_dictionaries = {
    "Ali" : 71,
    "Waqar" : 80,
    "Bilal" : 60,
    "Abrar" : 90,
    "Rashid" : 92,
    "Adeel" : 85,
    "Nabeel" : 75,
    "Umar" : 50,
}

student_grades = {}
for student in student_dictionaries:
    score = student_dictionaries[student]
    if 91 <= score <= 100:
        student_grades[student] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
