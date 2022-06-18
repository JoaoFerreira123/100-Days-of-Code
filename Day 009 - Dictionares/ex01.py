# Write a program that converts their scores to grades. 
# By the end of your program, you should have a new dictionary called student_grades 
# that should contain student names for keys and their grades for values.
# This is the scoring criteria:

#Scores 91 - 100: Grade = "Outstanding"
#Scores 81 - 90: Grade = "Exceeds Expectations"
#Scores 71 - 80: Grade = "Acceptable"
#Scores 70 or lower: Grade = "Fail"

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

students_grades = {}

for i in student_scores:
    if student_scores[i] >= 91 and student_scores[i]<= 100:
        students_grades[i] = "Outstanding"
    elif student_scores[i] >= 81 and student_scores[i] <= 90:
        students_grades[i] = 'Exceeds Expectations'
    elif student_scores[i] > 71 and student_scores[i] <= 80:
        students_grades[i] = 'Acceptable'
    else:
        students_grades[i] = 'Fail'

print(students_grades)