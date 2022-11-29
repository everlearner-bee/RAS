
# nesting and dictionaries

# student_1 = {'erastus': 26}
# student_2 = {'tonny': 23}
# student_3 = {'syd': 20}

# overal = [student_1,student_2,student_3]

# for students in overal:
#     print(overal)

#creating a nest of students

students = []
for student in range(30):
    new_student = {'name': 'Ronny',"class":"4 west"}
    students.append(new_student)

for studen in students[:8]:
    print(studen)
print(len(students))

