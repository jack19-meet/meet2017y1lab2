Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a = 5
>>> b = 10
>>> type(a)
<class 'int'>
>>> a = 10
>>> b = 5
>>> a = b
>>> b = a
>>> a
5
>>> b
5
>>> a = 5
>>> b = 10
>>> a = b
>>> a
10
>>> b
10
>>> c = a
>>> c
10
>>> four = '4'
>>> print(four*3)
444
>>> print(“Hi,” + myName’)
SyntaxError: invalid character in identifier
>>> print('hi' "+" 'student')
hi+student
>>> print(“Hi,” + my_name)
SyntaxError: invalid character in identifier
>>> print('Hi, student)
      
SyntaxError: EOL while scanning string literal
>>> print('Hi, student)rint('Hi, studentrint('Hi, student
					 
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> print('Hi, student')
Hi, student
>>> my_name = student
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    my_name = student
NameError: name 'student' is not defined
>>> my_name = 'student'
>>> print('HI,' + my_name)
HI,student
>>> my_age = '15'
>>> print(‘I am ‘ + my_age + ‘years
old’)
SyntaxError: invalid character in identifier
>>> print(‘iam ‘ + my_age + ‘years
old’)
SyntaxError: invalid character in identifier
>>> print( "iam" + my_age + "years_old')
       
SyntaxError: EOL while scanning string literal
>>> print( "iam" + my_age + "years_old")
iam15years_old
>>> score = 1
>>> total = score = (count * 2)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    total = score = (count * 2)
NameError: name 'count' is not defined
>>> total = score + ('count' * 2)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    total = score + ('count' * 2)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> total = score + (count * 2)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    total = score + (count * 2)
NameError: name 'count' is not defined
>>> count = 4
>>> total = score + (count * 2)
>>> print(total)
9
>>> 
