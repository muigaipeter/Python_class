#list is a ordered and changeable
fruits=['banana','orange','mango']
print(type(fruits))

# indexing /accessing items in a list
print(fruits[0])

# changing item value
fruits[0]="pineapple"
print(fruits)

# looping through a list
for fruit in  fruits:
    print(fruit)

# check if item exitst in a list
if"guava" in fruits:

    print("mango exist in the fruits list")

else:
    print("mango does not exist")
#length

# checking the number of items in a list using the length method
print(len(fruits))

# adding an item at the end of a list

# syntax: list.append("item")
fruits.append("avacado")
print(fruits)
# insert()
fruits.insert(1,"apple")

print(fruits)
fruits.remove("mango")
print(fruits)

del fruits[0]
print(fruits)

# copying a list


names=["kenya","uganda","tanzania","rwanda"]

countries=names.copy()
print(countries)
eacountries=list(names)

print(names)

# creating an empty list

# method1
cars=[]

# method 2
cars=list()
