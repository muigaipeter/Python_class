#for loop used to iterate
#for loop syntax
#for itemname in the list(sequence):
#run      some  code

#looping through a sequence(lists)
names = ['Raila','Uhuru','Ruto','Mudavadi']
for name in names:
    print(name)

#looping through a string
for letter in 'kenyan' :
    print(letter)



#using break statement with the for loop
for leader in  names:
     print(leader)
     if leader == 'Raila' and 'Uhuru':
         print('iam am Rao')
         break


#using continue statement with for loop
for leader in names:
    if leader == 'Uhuru':
        continue
    print(leader)

# The range() functions

#for num in range(10):
  #  print(num)
#adding a starting point to the range function

for num in range(5,10):
    print(num)

#adding an increment value
for num in range(0,50,5):
    print(num)

#range(<start value\optional>,<the maximum value>,<increment value>)

for name in names:
    print(name)
else:
    print('The loop has endeded')

#Nested loops
#The inner loop will be executed one time for each iteration of the outer loop



cars    =   ['subaru','Audi','Toyota']
countries =   ['Germany','Uk','japan']
for car in cars:
    for country in countries:
        print(car,country)

