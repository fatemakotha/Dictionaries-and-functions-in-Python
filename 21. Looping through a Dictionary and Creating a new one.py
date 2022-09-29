#Looping through a Dictionary and Creating a new one:
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for each in student_scores:
    score = student_scores[each]
    print(score)
    #prints:
    # 81
    # 78
    # 99
    # 74
    # 62
    if score > 90:
        student_grades[each] = "Outstanding" #for "Hermione", student_grades["Hermione"] = "Outstanding"
    elif score > 80:
        student_grades[each] = "Exceeds expectations" #for "Harry", student_grades["Harry"] = "Exceeds expectations"
    elif score > 70:
        student_grades[each] = "Acceptable"
    elif score < 90:
        student_grades[each] = "Fail"


print(student_grades)
#prints:
# {'Harry': 'Exceeds expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}