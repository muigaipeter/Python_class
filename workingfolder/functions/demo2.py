#defuining a fuvnction that tajkes a list as an aurguments
def loop_list(listname):
    for item in listname:
        print(item)
fruits  =   ['banana','mango','guava']
loop_list(fruits)

#returning a value from a function
def sqrt(num):
    return num*num

num5    =   sqrt(5)
print(num5)

def add(num):
    return num+num
num   = add(9)
print(num)

def mod(num1,num2):
    return num1%num2
get_mod =   mod(3,2)
print(get_mod)
