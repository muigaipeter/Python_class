Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello world")
Hello world
>>> print('hello  world')
hello  world
>>> #this i s a comment
>>> print(oooo)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(oooo)
NameError: name 'oooo' is not defined
>>> print("muigai peter is my name")
muigai peter is my name
>>> #this is just but a comment
>>> """multiple line comment
"""
'multiple line comment\n'
>>> name="peter"
>>> type(name)
<class 'str'>
>>> name = 23
>>> type(name)
<class 'int'>
>>> Name = "Peter"
>>> print (Name)
Peter
>>> print(name)
23
>>> _name = "_peter"
>>> print(_name)
_peter
>>> X = "JUMP"
>>> Y = "RUN"
>>> print(X+y)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(X+y)
NameError: name 'y' is not defined
>>> print(X+Y)
JUMPRUN
>>> print (X + "and " + Y)
JUMPand RUN
>>> print(X + " and " + Y)
JUMP and RUN
>>> JUMP and RUN
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    JUMP and RUN
NameError: name 'JUMP' is not defined
>>> z = 23
>>> print (X + " an)d " +  X + z
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print (X + " and " +  X + z)
TypeError: can only concatenate str (not "int") to str
>>> print (X + " and " +  X + str(z))
JUMP and JUMP23
>>> print (X + " and " +  X + str (z))
JUMP and JUMP23
>>> print (X + " and " +  X + " " +str(z))
JUMP and JUMP 23
>>> number
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    number
NameError: name 'number' is not defined
>>> 
