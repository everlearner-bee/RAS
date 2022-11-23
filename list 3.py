
#this is a code on working with lists a revision of my code

animals = ["lion","zebra",'girrafe','buffalo','rhino']
#so working with list i will explore some of the functions like append,del,remove,pop,

animals.append('goat')
message = f"this is a list of some of the animals the students listed, {animals}"
print(animals)
print(message)

#del function
del animals[3]
print(animals)

animals.insert(3,'monkey')
print(animals)
#pop function is used to remove a value that can later be used, ie it stores the removed value
animals.pop(2)
print(animals)

#remove function

animals.remove("lion")
#this is a code on working with lists a revision of my code

animals = ["lion","zebra",'girrafe','buffalo','rhino']
#so working with list i will explore some of the functions like append,del,remove,pop,

animals.append('goat')
message = f"this is a list of some of the animals the students listed, {animals}"
print(animals)
print(message)

#del function
del animals[3]
print(animals)

animals.insert(3,'monkey')
print(animals)
#pop function is used to remove a value that can later be used, ie it stores the removed value
animals.pop(2)
print(animals)

#remove function

animals.remove("lion")
print(animals)

#working with lists for loops

for animal in animals:    
    print(f"all this animals can be found at the serengeti, {animal}")

print("loops dont really have alot of work")

#making numerical lists using range function

for number in range(4,10):
    print(number)

#making a list of number using range function and list function
#list function wraps the entire range in the list
value = list(range(1,7))
print(value)

#example a list of odd numbers

odd_numbers = list(range(1,22,2))
print(odd_numbers)

#example of cubed value from 1 to 10 starting with an empty list

cubes = []  

for values in range(1,11):
    cube = values**3
    cubes.append(cube)

print(cubes)

#copying a list

animals_copied = animals [:]

animals_copied.append("ilama")
print(animals_copied)

#tuples these are lists that do not change and they are defined by ()

new_animals = ("elephant",'buffalo','dog','sheep','gorrilla')
print(new_animals[4])



