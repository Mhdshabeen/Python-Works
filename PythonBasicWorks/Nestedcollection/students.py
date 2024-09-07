

student=[
    {"id":100,"name":"shabeen","course":"python","mark":150},
    {"id":101,"name":"ahamad","course":"stack","mark":200},
    {"id":102,"name":"rintu","course":"data science","mark":250},
    {"id":103,"name":"sjorge","course":"java","mark":350},
    {"id":104,"name":"sam","course":"c++","mark":300},
    {"id":105,"name":"jhon","course":"django","mark":400},
    {"id":106,"name":"roshan","course":"cse","mark":450},
    {"id":107,"name":"shzz","course":"civil","mark":50},
    {"id":108,"name":"aboo","course":"mech","mark":550}
    ]
# print all tudents name
student_name=[dicts.get("name") for dicts in student]

# print(student_name)

# print all cources in the list once

courses=[dicts.get("course") for dicts in student]

# print(set(courses))

# students name with cource django

django_student=[stud.get("name") for stud in student if stud.get("course")=="django"]

# print(django_student)

# print students name in mark range 200-400

stundet_with_mark=[stud.get("name") for stud in student if stud.get("mark") in range(200,401)]

# print(stundet_with_mark)

# print the student with highest mark

# mark_student=[stud.get("mark") for stud in student ]

# higest=[max(mark_student)]

# student_names=[stud.get("name") for stud in student if stud.get("mark")==higest[0]]

# print(student_names)

max_mark=max(student,key=lambda stud:stud.get("mark"))

# print(max_mark)

sort_student_by_marks_accending=sorted(student,key= lambda stud:stud.get("mark"))

# print(sort_student_by_marks_accending)

sort_student_by_marks_desending=sorted(student,key= lambda stud:stud.get("mark"),reverse=True)

# print(sort_student_by_marks_desending)

# total mark of students

total=sum([stud.get("mark") for stud in student])


print(total)