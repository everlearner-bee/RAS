#Dictionaries, they are defined by key : value pairs

student = {'name':'Erastus','Adm':'ci/00030/017'}
print(student['Adm'])

# working with dictionaries

student = {'name':'Erastus','Adm':'ci/00030/017'}

#  adding new values to dictionaries

student['age'] = 22
student['nationality'] = 'kenyan'

print(student)

# modyfying values in dictionaries

robot = {'vector_1': 9,"vector_2":8,'speed':'medium'}

if robot['speed'] == "slow":
    vector_change = 3
elif robot['speed'] == "medium" :
    vector_change = 10
else:
    vector_change = 6

robot['vector_1'] = robot['vector_1'] - vector_change
print(robot)

print(f"this is the new vector postion for vector 1, {robot['vector_1']}")

# removing key value pairs, we use the del function followed by dic'name and key

del robot['vector_2']

print(robot)
 

#  using get() to access specific values
# get function can be used to pass two arguments i.e when a key doesnt exist in a dictionary, it passes the second argument

robot_2 = robot.get('vector_1',"vector 2 may not exist")
print(robot_2)

# Looping through dictionaries
# method 1

names = {'Erastus':'Andedo',
'Tonny':'Blair',
'Sydney':'Andedo',
'Emmanuel':'Andedo',
}

for fname,lname in names.items():
    print(f"first name:{fname}")
    print(f"last name :{lname}")


# method 2 using the key() method

names = {'Erastus':'Andedo',
'Tonny':'Blair',
'Sydney':'Andedo',
'Emmanuel':'Andedo',
}

for name in names.keys():
    print(f"first name is:{name.upper()}")

for name in names.values():
    print(name.upper())

#monday session working with dictionaries and looping in a particular order

names = {'Erastus':'Andedo',
'Tonny':'Blair',
'Sydney':'Andedo',
'Emmanuel':'Andedo',
}
 
for person in sorted(names.keys()):
    print(person)

for person in set(names.values()):
    print(person.upper())










