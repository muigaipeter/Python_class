#
class Parent():
    def __init__(self,first_name,last_name):
        self.firstname  =   first_name
        self.last_name  =   last_name

    def print_names(self):
        print(self.firstname,self.last_name)
    def hair_color(self):
        print('grey')

class Child(Parent):
    def __init__(self,first_name,last_name):
        self.firstname=first_name
        self.last_name=last_name

        def hair_color(self):
            print('black')

C1  =   Child('john', 'Doe')

C1.print_names()
C1.hair_color()


#p1  =   Parent('samson','Berkly')
#p1.print_names()
#The child is called joe Doe,the parent is called is called samson Berkly

