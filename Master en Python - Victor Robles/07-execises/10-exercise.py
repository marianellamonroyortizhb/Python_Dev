"""
Exercise 9
    - Count the number of students that passed an exam.
"""

print("Exercise 10")

count_pass = 0
count_fail = 0

for student in range (1,16):
    grade = float(input("Welcome student. Please write your exam grade: "))
    if (grade >= 3):
        count_pass = count_pass + 1
    else:
        count_fail = count_fail + 1
print("Students that passed the exam: " + str(count_pass))
print("Students that missed the exam: " + str(count_fail))