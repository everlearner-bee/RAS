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