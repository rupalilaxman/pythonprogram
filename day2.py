Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> r = range(1,100)
>>> type(r)
<class 'range'>
>>> # in python 2 it returns list, to convert range to list in python 3 we use list() method
>>> list(r)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> r = range(5) # takes 0 as default argument if only 1 argument is given
>>> list(r)
[0, 1, 2, 3, 4]
>>> # range gives output till second argument - 1
>>> # for range(5) we get 0..4 , 5 is not included
>>> range(1,10,5) # third argument of range is step
range(1, 10, 5)
>>> list(range(1,10,5))
[1, 6]
>>> # sum method gives the sum of numbers in a list
>>> sum(list(range(1,10)))
45
>>> sum([1,2,3.2])
6.2
>>> sum(['a', 'b'])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    sum(['a', 'b'])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> # sum adds 0 with each element of the list
>>> import math
>>> math.sqrt(9)
3.0
>>> math.sqrt(3)
1.7320508075688772
>>> len(int)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    len(int)
TypeError: object of type 'type' has no len()
>>> len([1,2,3,4,5])
5
>>> len('rohit s')
7
>>> len(str(123456789))
9
>>> a = 1
>>> # to prove that int is also an object in python we can use id() that returns the identity of that object
>>> id(a)
266328240
>>> # note this id
>>> a = a+1
>>> a
2
>>> id(a)
266328256
>>> #note that id of 1 and 2 is different since these are two different objects
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'math', 'r']
>>> # dir functions gives the list of all variables and methods that we can use
>>> s = "rohit"
>>> type(s)
<class 'str'>
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> # dir(str) gave all the methods that we can use with string
>>> isinstance(1, int)
True
>>> # isinstance is used to check if the object belongs to that type/class
>>> isinstance(1, bool)
False
>>> isinstance(1, float)
False
>>> # ** is used for power
>>> 3 ** 2
9
>>> # strings can be multiplied with integers
>>> 'rohit ' * 5
'rohit rohit rohit rohit rohit '
>>> # list can also be multiplied with integers
>>> [1,2,3] * 5
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ###### DATA TYPES ###########
>>> 
>>> ## Numbers ##
>>> 
>>> # numbers can be very large
>>> a = 2 ** 12345
>>> a

>>> # 3 types of numbers
>>> # int, float and complex
>>> a = 1; type(a)
<class 'int'>
>>> a = 2.0; type(a)
<class 'float'>
>>> a = 2 + 3j; type(a)
<class 'complex'>
>>> 
>>> # A floating point number is accurate up to 15 decimal places
>>> a = 0.1234567890123456789
>>> a
0.12345678901234568
>>> # notice that it is trimmed
>>> 
>>> ## DATA TYPE 2 - LIST ##
>>> #  All the items in a list do not need to be of the same type.
>>> 
>>> a = [1, 2.3, "abc" ]
>>> b = list(range(1,100))
>>> b[1:10]
[2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> # b[start_position: end_position]
>>> b[0]
1
>>> b[1]
2
>>> b[10]
11
>>> # similar to range the last end_position of list is not included
>>> 
>>> b[0:3]
[1, 2, 3]
>>> b[99:]
[]
>>> b[98:]
[99]
>>> b[100]
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    b[100]
IndexError: list index out of range
>>> b[99]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    b[99]
IndexError: list index out of range
>>> b
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> b[-1]
99
>>> b[-2]
98
>>> b[-2:] # last two elements of the list
[98, 99]
>>> b[:2] # first two elements of the list
[1, 2]
>>> # to print the whole list we use 'b' or 'b[:]'
>>> c = b
>>> c[0] = 5
>>> b[0]
5
>>> # same object is referenced by b and c
>>> # to copy the list in a pythonic way we use
>>> c = b[:]
>>> c[0] = 6
>>> b[0]
5
>>> # to print list in reverse
>>> b[4::-1] # print first five numbers in reverse
[5, 4, 3, 2, 5]
>>> b[0] = 1
>>> b[4::-1]
[5, 4, 3, 2, 1]
>>> # note that we did not specify the second argument since we know second argument is not included
>>> b[4:0:-1]
[5, 4, 3, 2]
>>> # reverse of the whole list
>>> b[::-1]
[99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> 
>>> 
>>> ## DATA TYPE 3 - TUPLE ##
>>> 
>>> a = (1,2,3)
>>> type(a)
<class 'tuple'>
>>> # tuple is immutable,once defined it cannot be changed
>>> b = (1,3,2.5,"abc")
>>> # tuples can contain heterogeneous items
>>> b[1]
3
>>> a[0:1]
(1,)
>>> a[0:]
(1, 2, 3)
>>> # similar to list tuples can be indexed and sliced
>>> # [:] this is called slicing
>>> a[0] = 2
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    a[0] = 2
TypeError: 'tuple' object does not support item assignment
>>> # tuples cannot be modified
>>> 
>>> 
>>> 
>>> ## DATA TYPE - 4 : STRINGS ###
>>> 
>>> s = "i am rohit shende, i work at vmware software india pvt. ltd. "
>>> a
(1, 2, 3)
>>> s
'i am rohit shende, i work at vmware software india pvt. ltd. '
>>> # i already told you about ' " '''
>>> # strings can also be sliced
>>> 
>>> s[0:5]
'i am '
>>> s[5:10]
'rohit'
>>> s[5]
'r'
>>> s[-1]
' '
>>> s[-2]
'.'
>>> s[:-5:-1]
' .dt'
>>> s[:-12:-1]
' .dtl .tvp '
>>> # reverse of a string
>>> r = s[5:10]
>>> r
'rohit'
>>> r[::-1]
'tihor'
>>> # strings are also immutable
>>> r[0] = 'R'
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    r[0] = 'R'
TypeError: 'str' object does not support item assignment
>>> r.capitalize
<built-in method capitalize of str object at 0x015B9C60>
>>> r.capitalize()
'Rohit'
>>> r.lower()
'rohit'
>>> r.upper()
'ROHIT'
>>> 
>>> 
>>> 
>>> ## DATA TYPE 5 - SET ##
>>> 
>>> # Set is an unordered collection of unique items.
>>> s = {1,2,2,3,4,5}
>>> s
{1, 2, 3, 4, 5}
>>> type(s)
<class 'set'>
>>> s
{1, 2, 3, 4, 5}
>>> # Set have unique values. They eliminate duplicates.
>>> s[1]
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    s[1]
TypeError: 'set' object does not support indexing
>>> 
>>> 
>>> 
>>> # Since, set are unordered collection, indexing has no meaning. Hence the slicing operator [] does not work.
>>> 
>>> 
>>> s
{1, 2, 3, 4, 5}
>>> t = {1,2,3}
>>> t
{1, 2, 3}
>>> t = {1,2,6}
>>> t
{1, 2, 6}
>>> s.union(t)
{1, 2, 3, 4, 5, 6}
>>> s.intersection(t)
{1, 2}
>>> 
>>> s - t
{3, 4, 5}
>>> 
>>> t - s
{6}
>>> 
>>> ## DATA TYPE 6 - DICTIONARY ##
>>> 
>>> # Dictionary is an unordered collection of key-value pairs.
>>> 
>>> d = {'one':1 , 'two':2 }
>>> type(d)
<class 'dict'>
>>> d
{'one': 1, 'two': 2}
>>> d[1] # return error since there is no key '1'
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    d[1] # return error since there is no key '1'
KeyError: 1
>>> d['one']
1
>>> d['one'] = 3
>>> d['one']
3
>>> d.get('one')
3
>>> # difference between indexing and get function
>>> d.get('three')
>>> d['three']
Traceback (most recent call last):
  File "<pyshell#197>", line 1, in <module>
    d['three']
KeyError: 'three'
>>> 
>>> # get returns None when key is absent and does not raise a KeyError
>>> 
>>> 
>>> d
{'one': 3, 'two': 2}
>>> del d['one']  # deleting item from dict
>>> d[1]='one'
>>> d
{'two': 2, 1: 'one'}
>>> del d # deleting the dictionary or any object
>>> d
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> 
>>> 
>>> 
>>> ## TYPE Conversions ###
>>> 
>>> # int to float
>>> a =1
>>> b = 2.0
>>> c = a + b
>>> type(c)
<class 'float'>
>>> c
3.0
>>> d = float(a)
>>> type(d)
<class 'float'>
>>> d
1.0
>>> 
>>> # float to int
>>> int(d)
1
>>> int(c)
3
>>> x = 2.3452
>>> int(x)
2
>>> # converting to string from int/float
>>> x
2.3452
>>> str(x)
'2.3452'
>>> a
1
>>> str(a)
'1'
>>> 
>>> # str to float/int
>>> int("123")
123
>>> float("2.34")
2.34
>>> # string + int
>>> "a" + 1
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    "a" + 1
TypeError: can only concatenate str (not "int") to str
>>> "a" + str(1)
'a1'
>>> 
>>> # list to set
>>> l = [1,2,3,4,5,1,2,3]
>>> set(l)
{1, 2, 3, 4, 5}
>>> # set to list
>>> list({1,2,3,4})
[1, 2, 3, 4]
>>> # to tuple
>>> tuple(l)
(1, 2, 3, 4, 5, 1, 2, 3)
>>> # tuple to list/set
>>> l = tuple(l)
>>> l
(1, 2, 3, 4, 5, 1, 2, 3)
>>> set(l)
{1, 2, 3, 4, 5}
>>> list(l)
[1, 2, 3, 4, 5, 1, 2, 3]
>>> 
>>> 
>>> ## Input and Output
>>> 
>>> # print function
>>> print(1,2,3,4,sep='#',end='&')
1#2#3#4&
>>> # printing variables
>>> a,b,c = 1,2,3
>>> print("a=%d b=%d c=%d",(%a,%b,%c))
SyntaxError: invalid syntax
>>> print("a=%d b=%d c=%d" %(a,b,c))
a=1 b=2 c=3
>>> print("c=%d" %c)
c=3
>>> print(1,2,3,4)
1 2 3 4
>>> x = 123.23463542712
>>> print('The value of x is %3.2f' %x)
The value of x is 123.23
>>> 
>>> # input()
>>> 
>>> y = input("Pls enter a number :")
Pls enter a number :1234
>>> y
'1234'
>>> z = input("enter any string :")
enter any string :hi myself rohit
>>> z
'hi myself rohit'
>>> # getting an integer
>>> x = int(input("Enter an integer:"))
Enter an integer:3
>>> x
3
>>> # getting float
>>> x = int(input("Enter floating number :"))
Enter floating number :3.43
Traceback (most recent call last):
  File "<pyshell#280>", line 1, in <module>
    x = int(input("Enter floating number :"))
ValueError: invalid literal for int() with base 10: '3.43'
>>> x = float(input("Enter floating number :"))
Enter floating number :3.43
>>> x
3.43
>>> 
>>> 
>>> # importing a module
>>> 
>>> import math
>>> math.pi
3.141592653589793
>>> math.sqrt(9)
3.0
>>> 
>>> from math import sqrt
>>> sqrt(25)
5.0
>>> 
>>> from math import sqrt as square_root
>>> square_root(36)
6.0
>>> 
>>> import sys
>>> sys.path  # shows the system path
['', 'C:\\Users\\rshende\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\idlelib', 'C:\\Users\\rshende\\AppData\\Local\\Programs\\Python\\Python37-32\\python37.zip', 'C:\\Users\\rshende\\AppData\\Local\\Programs\\Python\\Python37-32\\DLLs', 'C:\\Users\\rshende\\AppData\\Local\\Programs\\Python\\Python37-32\\lib', 'C:\\Users\\rshende\\AppData\\Local\\Programs\\Python\\Python37-32', 'C:\\Users\\rshende\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages']
>>> 
