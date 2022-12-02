
# nesting and dictionaries

# student_1 = {'name': "Erastus", "age":26}
# student_2 = {'name': "tonny", "age":23}
# student_3 = {'name': "sydo", "age":20}

# # for student,age in student_1.items():
# #     print(student)
# overal = [student_1,student_2,student_3]

# for students in overal:
#     print(students)

# #creating a nest of students

students = []
for student in range(30):
    new_student = {'name': 'Ronny',"class":"4 west"}
    students.append(new_student)


for studen in students[:3]:
    if studen['name'] == 'Ronny':
        studen['name']= 'Erastus'
        studen['class'] = '3 west'

for student in students[:6]:
    print(student)
print(len(students))

#  a list in a dictionary

hotels = {'kisumu':['kisumu hotel','imperial hotel'],
'nairobi':'Radisson blue',
'mombasa':['the english point','mama ntilie']}

for location,name in hotels.items():
    print(f"In {location},we have such hotels,{name}")




