#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result
#Functions syntax
#def name_of_the_function():
    #code to be run

def cat():
    print('mweeeeoouu')
cat()

def dog(name):
    print(name + ' wooooooofs')
dog('bosco')


def my_name(name    =   'Developer'):
    if name == 'Developer':
        print('iam a developer')
    else:
        print(name + 'is a developer')
#my_name()
my_name('peter')