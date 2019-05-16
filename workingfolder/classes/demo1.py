#is a blue print in oop
#an object/instance
#syntax
#class name_of_the_class():
    #the blue print attributes


class Person():
    name    =   'Developer'

d1  =   Person()
d2  =   Person()

print(d1.name)
print(d2.name)


#all classes has a function called _init_()
# which is always executed when the class is being initiated
#Use the _init_() function to assign values to properties or other operations that are neccessary




class Animal():
    def __init__(self,name):
        self.thename   =   name

    def sound(self):
        if self.thename == 'cutty':
             print('mweeew')

    def kitty(self):
         if self.thename    ==  'cutty':
             print('such a playerful cat')
    def fear(self):
        if self.thename ==   'Betty':
            print('betty is not feeling well')
    def white(self):
        if self.thename ==  'cutty':
            print('cutty is a deaf cat')


    def sounds(self):
        if self.thename == 'bob':
            print('woooof')

cat =   Animal('cutty')
print(cat.thename)
cat2=   Animal('Betty')
print(cat.thename)
print('bob is a nice puppy')
dog =   Animal('bob')



cat.sound()
cat.kitty()
cat2.fear()
cat.white()
dog.sounds()



