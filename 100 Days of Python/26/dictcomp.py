import random
names = ['Alex', 'James','Anshyy','Jay','Ray']
student_score ={student : random.randint(1,100) for student in names if len(names)>2}
print(student_score)
passed_student = {student:score for (student, score) in student_score.items() if score >=60}
print(passed_student)