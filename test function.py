Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def hello(friend):
    print('Hi, {}'.format(friend))

    
hello(Weera)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    hello(Weera)
NameError: name 'Weera' is not defined
hello('Weera')
Hi, Weera
def land(width,long):
    cal = width * long
    cal_wa = cal/4
    print('ที่ดินผืนนี้กว้าง: {} เมตร ยาว: {} เมตร'.format(width,long))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางเมตร'.format(cal))

    
def land(width,long):
    cal = width * long
    cal_wa = cal/4
    print('ที่ดินผืนนี้กว้าง: {} เมตร ยาว: {} เมตร'.format(width,long))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))

    
land(5,10)
ที่ดินผืนนี้กว้าง: 5 เมตร ยาว: 10 เมตร
ที่ดินผืนนี้มีพื้นที่: 50 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 12.5 ตารางวา
land(8,20)
ที่ดินผืนนี้กว้าง: 8 เมตร ยาว: 20 เมตร
ที่ดินผืนนี้มีพื้นที่: 160 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 40.0 ตารางวา
def land(width,long):
    cal = width * long
    cal_wa = cal/4
    print('ที่ดินผืนนี้กว้าง: {} เมตร ยาว: {} เมตร'.format(width,long))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))
    return cal_wa

res=land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
print(res)
18.75
def land(width,long,price=900000):
    cal = width * long
    cal_wa = cal/4
    print('ที่ดินผืนนี้กว้าง: {} เมตร ยาว: {} เมตร'.format(width,long))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))
    return cal_wa*price

result=land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
print(result)
16875000.0
def land(width,long,price=900000):
    cal = width * long
    cal_wa = cal/4
    print('ที่ดินผืนนี้กว้าง: {} เมตร ยาว: {} เมตร'.format(width,long))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))
    calprice=cal_wa*price
    return 'ที่ดินผืนนี้มีราคา:{:,.2f} บาท'.format(calprice)

result=land(5,15,1000000)
ที่ดินผืนนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
print(result)
ที่ดินผืนนี้มีราคา:18,750,000.00 บาท
print(land(5,15))
ที่ดินผืนนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
ที่ดินผืนนี้มีราคา:16,875,000.00 บาท
from decimal import Decimal
1e6
1000000.0
1e7
10000000.0
x=Decimal('100000000')
'{:.2e)'.format(x)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    '{:.2e)'.format(x)
ValueError: unmatched '{' in format spec
'{:.2e}'.format(x)
'1.00e+8'
def greet_user():
    """Display a simple greeting"""
    print('Hello!')

    
greet_user(Weeraphandh)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    greet_user(Weeraphandh)
NameError: name 'Weeraphandh' is not defined
greet_user()
Hello!
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, "+ username +"!")

    
greet_user('Weera')
Hello, Weera!
greet_user('Weeraphandh')
Hello, Weeraphandh!
greet_user('Maleephandh')
Hello, Maleephandh!
greet_user('Diana')
Hello, Diana!
greet_user('Brandon')
Hello, Brandon!
def describe_pet(animal,name):
    """Display information about a pet."""
    print(f'I have a {animal}.')
    print("\nI have a"+ animal +".")
    print("I have a {}".format(animal))
    print("Its name is"+ animal +".")
    print(f'Its name is {name}.')
    print("Its name is {}.".format(name))

    
describe_pet(bird,Lisa)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    describe_pet(bird,Lisa)
NameError: name 'bird' is not defined
describe_pet('bird',Lisa)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    describe_pet('bird',Lisa)
NameError: name 'Lisa' is not defined. Did you mean: 'list'?
describe_pet('bird','Lisa')
I have a bird.

I have abird.
I have a bird
Its name isbird.
Its name is Lisa.
Its name is Lisa.
def describe_pet(animal,name):
    """Display information about a pet."""
    print(f'\nI have a {animal}.')
    print("\nI have a" + animal +".")
    print("\nI have a {}.".format(animal))
    print("\nIts name is" + name +".")
    print(f'\nIts name is {name}.')
    print("\nIts name is {}.".format(name))

    
describe_pet('bird','Lisa')

I have a bird.

I have abird.

I have a bird.

Its name isLisa.

Its name is Lisa.

Its name is Lisa.
def describe_pet(animal,name):
    """Display information about a pet."""
    print(f'\nI have a {animal}.')
    print("\nI have a " + animal +".")
    print("\nI have a {}.".format(animal))
    print("\nIts name is " + name +".")
    print(f'\nIts name is {name}.')
    print("\nIts name is {}.".format(name))

    
describe_pet('bird','Lisa')

I have a bird.

I have a bird.

I have a bird.

Its name is Lisa.

Its name is Lisa.

Its name is Lisa.
def describe_pet(animal,name):
    """Display information about a pet."""
    print(f'\nI have a {animal}.')
    print("\nI have a " + animal +".")
    print("\nI have a {}.".format(animal))
    print("\nIts name is " + name +".")
    print(f'\nIts name is {name}.')
    print("\nIts name is {}.".format(name))

    
describe_pet(animal='bird',name='Lisa')

I have a bird.

I have a bird.

I have a bird.

Its name is Lisa.

Its name is Lisa.

Its name is Lisa.
describe_pet(name='Lisa',animal='bird','foy')
SyntaxError: positional argument follows keyword argument
describe_pet(name='Lisa',animal='bird')

I have a bird.

I have a bird.

I have a bird.

Its name is Lisa.

Its name is Lisa.

Its name is Lisa.
describe_pet('Lisa','bird')

I have a Lisa.

I have a Lisa.

I have a Lisa.

Its name is bird.

Its name is bird.

Its name is bird.
def describe_pet(animal,name):
    """Display information about a pet."""
    print(f'I have a {animal}.') #F string เป็นการเขียนที่ดีที่สุด รวดเร็วและได้รูปแบบการเขียนปกติมากกว่าแบบที่สองและแบบที่สาม
    print("\nI have a"+ animal +".") #แบบที่สอง
    print("I have a {}".format(animal)) #แบบที่สาม
    print("Its name is"+ animal +".")
    print(f'Its name is {name}.')
    print("Its name is {}.".format(name))

    

describe_pet(name='Lisa',animal='bird')
I have a bird.

I have abird.
I have a bird
Its name isbird.
Its name is Lisa.
Its name is Lisa.
def describe_pet(animal,name):
    """Display information about a pet."""
    print(f'\nI have a {animal}.') #F string เป็นการเขียนที่ดีที่สุด รวดเร็วและได้รูปแบบการเขียนปกติมากกว่าแบบที่สองและแบบที่สาม
    print("\nI have a "+animal+".") #แบบที่สอง
    print("\nI have a {}".format(animal)) #แบบที่สาม
    print("\nIts name is "+animal+".")
    print(f'\nIts name is {name}.')
    print("\nIts name is {}.".format(name))

    
describe_pet(name='Lisa',animal='bird')

I have a bird.

I have a bird.

I have a bird

Its name is bird.

Its name is Lisa.

Its name is Lisa.
def describe_pet(animal,name):
    """Display information about a pet."""
    print(f'\nI have a {animal}.') #F string เป็นการเขียนที่ดีที่สุด รวดเร็วและได้รูปแบบการเขียนปกติมากกว่าแบบที่สองและแบบที่สาม
    print("\nI have a "+animal+".") #แบบที่สอง
    print("\nI have a {}.".format(animal)) #แบบที่สาม
    print("\nIts name is "+name+".")
    print(f'\nIts name is {name}.')
    print("\nIts name is {}.".format(name))

    
describe_pet(name='Lisa',animal='bird')

I have a bird.

I have a bird.

I have a bird.

Its name is Lisa.

Its name is Lisa.

Its name is Lisa.
def describe_pet(animal='dog',name):
    """Display information about a pet."""
    print(f'\nI have a {animal}.') #F string เป็นการเขียนที่ดีที่สุด รวดเร็วและได้รูปแบบการเขียนปกติมากกว่าแบบที่สองและแบบที่สาม
    print("\nI have a "+animal+".") #แบบที่สอง
    print("\nI have a {}.".format(animal)) #แบบที่สาม
    print("\nIts name is "+name+".")
    print(f'\nIts name is {name}.')
    print("\nIts name is {}.".format(name))
    
SyntaxError: parameter without a default follows parameter with a default
def describe_pet(name,animal='dog'):
    """Display information about a pet."""
    print(f'\nI have a {animal}.') #F string เป็นการเขียนที่ดีที่สุด รวดเร็วและได้รูปแบบการเขียนปกติมากกว่าแบบที่สองและแบบที่สาม
    print("\nI have a "+animal+".") #แบบที่สอง
    print("\nI have a {}.".format(animal)) #แบบที่สาม
    print("\nIts name is "+name+".")
    print(f'\nIts name is {name}.')
    print("\nIts name is {}.".format(name))

    
describe_pet('Lisa','bird')

I have a bird.

I have a bird.

I have a bird.

Its name is Lisa.

Its name is Lisa.

Its name is Lisa.
describe_pet('Lisa')

I have a dog.

I have a dog.

I have a dog.

Its name is Lisa.

Its name is Lisa.

Its name is Lisa.
def describe_pet(name,animal='dog'): #ถ้าเราใส่ค่าเริ่มต้นไว้จะไม่มีผลอะไรถ้าเราระบุค่าanimalที่เราต้องการ จะมีผลต่อเมื่อเราไม่ได้ใส่ค่าanimal
    """Display information about a pet."""
    print(f'\nI have a {animal}.') #F string เป็นการเขียนที่ดีที่สุด รวดเร็วและได้รูปแบบการเขียนปกติมากกว่าแบบที่สองและแบบที่สาม
    print("\nI have a "+animal+".") #แบบที่สอง
    print("\nI have a {}.".format(animal)) #แบบที่สาม
    print("\nIts name is "+name+".")
    print(f'\nIts name is {name}.')
    print("\nIts name is {}.".format(name))

    
describe_pet('bird')

I have a dog.

I have a dog.

I have a dog.

Its name is bird.

Its name is bird.

Its name is bird.
def describe_pet(name,animal=None): #ถ้าเราใส่ค่าเริ่มต้นไว้จะไม่มีผลอะไรถ้าเราระบุค่าanimalที่เราต้องการ จะมีผลต่อเมื่อเราไม่ได้ใส่ค่าanimal
    """Display information about a pet."""
    print(f'\nI have a {animal}.') #F string เป็นการเขียนที่ดีที่สุด รวดเร็วและได้รูปแบบการเขียนปกติมากกว่าแบบที่สองและแบบที่สาม
    print("\nI have a "+animal+".") #แบบที่สอง
    print("\nI have a {}.".format(animal)) #แบบที่สาม
    print("\nIts name is "+name+".")
    print(f'\nIts name is {name}.')
    print("\nIts name is {}.".format(name))

    
describe_pet('Lisa','bird')

I have a bird.

I have a bird.

I have a bird.

Its name is Lisa.

Its name is Lisa.

Its name is Lisa.
describe_pet('Lisa')

I have a None.
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    describe_pet('Lisa')
  File "<pyshell#97>", line 4, in describe_pet
    print("\nI have a "+animal+".") #แบบที่สอง
TypeError: can only concatenate str (not "NoneType") to str
def describe_pet(animal,name=None): #ถ้าเราใส่ค่าเริ่มต้นไว้จะไม่มีผลอะไรถ้าเราระบุค่าanimalที่เราต้องการ จะมีผลต่อเมื่อเราไม่ได้ใส่ค่าanimal
    """Display information about a pet."""
    print(f'\nI have a {animal}.') #F string เป็นการเขียนที่ดีที่สุด รวดเร็วและได้รูปแบบการเขียนปกติมากกว่าแบบที่สองและแบบที่สาม
    print("\nI have a "+animal+".") #แบบที่สอง
    print("\nI have a {}.".format(animal)) #แบบที่สาม
    print("\nIts name is "+name+".")
    print(f'\nIts name is {name}.')
    print("\nIts name is {}.".format(name))

    

describe_pet('Lisa','bird')

I have a Lisa.

I have a Lisa.

I have a Lisa.

Its name is bird.

Its name is bird.

Its name is bird.
describe_pet('bird')

I have a bird.

I have a bird.

I have a bird.
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    describe_pet('bird')
  File "<pyshell#101>", line 6, in describe_pet
    print("\nIts name is "+name+".")
TypeError: can only concatenate str (not "NoneType") to str
def describe_pet(animal,name=None): #ถ้าเราใส่ค่าเริ่มต้นไว้จะไม่มีผลอะไรถ้าเราระบุค่าanimalที่เราต้องการ จะมีผลต่อเมื่อเราไม่ได้ใส่ค่าanimal
    """Display information about a pet."""
    print(f'\nI have a {animal}.') #F string เป็นการเขียนที่ดีที่สุด รวดเร็วและได้รูปแบบการเขียนปกติมากกว่าแบบที่สองและแบบที่สาม
    print("\nI have a "+animal+".") #แบบที่สอง
    print("\nI have a {}.".format(animal)) #แบบที่สาม
    if name:
        print("\nIts name is "+name+".")
    if name:
        print(f'\nIts name is {name}.')
    if name:
        print("\nIts name is {}.".format(name))

        
describe_pet('Lisa','bird')

I have a Lisa.

I have a Lisa.

I have a Lisa.

Its name is bird.

Its name is bird.

Its name is bird.
describe_pet('bird')

I have a bird.

I have a bird.

I have a bird.
def describe_pet(animal,name=None): #ถ้าเราใส่ค่าNoneซึ่งpythonรู้จักซึ่งไม่ใช่string
    """Display information about a pet."""
    print(f'\nI have a {animal}.') #F string เป็นการเขียนที่ดีที่สุด รวดเร็วและได้รูปแบบการเขียนปกติมากกว่าแบบที่สองและแบบที่สาม
    print("\nI have a "+animal+".") #แบบที่สอง
    print("\nI have a {}.".format(animal)) #แบบที่สาม
    print(f'\nIts name is {name}.')
    print("\nIts name is {}.".format(name))

    
describe_pet('bird')

I have a bird.

I have a bird.

I have a bird.

Its name is None.

Its name is None.
def describe_pet(animal,name=None): #ถ้าเราใส่ค่าเริ่มต้นไว้จะไม่มีผลอะไรถ้าเราระบุค่าanimalที่เราต้องการ จะมีผลต่อเมื่อเราไม่ได้ใส่ค่าanimal
    """Display information about a pet."""
    print(f'\nI have a {animal}.') #F string เป็นการเขียนที่ดีที่สุด รวดเร็วและได้รูปแบบการเขียนปกติมากกว่าแบบที่สองและแบบที่สาม
    print("\nI have a "+animal+".") #แบบที่สอง
    print("\nI have a {}.".format(animal)) #แบบที่สาม
    if name:
        print("\nIts name is "+name+".")
    if name:
        print(f'\nIts name is {name}.')
    if name:
        print("\nIts name is {}.".format(name))

        
describe_pet('bird','Wee')

I have a bird.

I have a bird.

I have a bird.

Its name is Wee.

Its name is Wee.

Its name is Wee.
describe_pet('bird')

I have a bird.

I have a bird.

I have a bird.
def get_full_name(first,last):
    """Return a neatly formatted full name."""
    full_name=first+' '+last
    return full_name.title()

get_full_name('Wee','Malee')
'Wee Malee'
Engineer=get_full_name('Wee','Malee')
print(Engineer)
Wee Malee
def get_full_name(first,last):
    """Return a dictionary of information about a person."""
    person={'first': first,'last':last}
...     return person
... 
>>> get_full_name('Wee','Malee')
{'first': 'Wee', 'last': 'Malee'}
>>> Engineer=get_full_name('Wee','Malee')
>>> print(Engineer)
{'first': 'Wee', 'last': 'Malee'}
>>> def get_full_name(first,last):
...     """Return a dictionary of information about a person."""
...     person={'first': first,'last':last}
...     return person.title()
... 
>>> get_full_name('Wee','Malee')
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    get_full_name('Wee','Malee')
  File "<pyshell#131>", line 4, in get_full_name
    return person.title()
AttributeError: 'dict' object has no attribute 'title'
>>> def get_full_name(first,last):
...     """Return a dictionary of information about a person."""
...     person={'first': first,'last':last}
...     return f'My name is {person[first]} and My Surname is {person[last]}.'
... 
>>> get_full_name('Wee','Malee')
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    get_full_name('Wee','Malee')
  File "<pyshell#134>", line 4, in get_full_name
    return f'My name is {person[first]} and My Surname is {person[last]}.'
KeyError: 'Wee'
>>> def get_full_name(first,last):
...     """Return a dictionary of information about a person."""
...     person={'first': first,'last':last}
...     return f'My name is person[first] and My Surname is person[last].'
... 
>>> get_full_name('Wee','Malee')
'My name is person[first] and My Surname is person[last].'
>>> def get_full_name(first,last):
...     """Return a dictionary of information about a person."""
...     person={'first': first,'last':last}
