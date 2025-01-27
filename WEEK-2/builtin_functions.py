'''
We have many builtin functions in python:
print()
len()
type
input()
str()
int()
float()
round()
dir()
min()
max()
sum()
range()
abs()
list()
tuple()
dict()
id()
dir()
'''

# Print function
print([1, 2, 3], 2025, True, 'Asab', sep='\n')
print('Apple', 'Avocado','Mango','Orange', 'Guava', sep='\n')

print('Mathewos','Daniel','John', sep=', ')
print('Mathewos','Daniel','John')


# len()
print(len('cat'))
print(len('love'))
print(len('i love u'))
print([[1, 2, 3], [4, 5,6],[8, 7,9]])
print(len({1, 2, 3}))
print(len((1, 2, 3)))
print(len({'name':'asab','age':250}))

# type - allow us to know the data type -
'''
Data types:
- Number (int, float, complex number)
... 3 -2 -1 0 1 2 3 ....
float: -0.1, 0.25, 0.5, 0.75
complex: 1 + 2j, 4 - 3j

Booleans: True or False
Strings: any text or data under a single or double quote
List
Set
Tuple
Dict
'''

print('what is the type of 10', type(10))
print('what is the type of 3.14', type(3.14))
print('what is the type of 3 + 2j', type(3 + 2j))

print(type(True))
print(type(False))
print(type(1 > 0))
print(type('cat'))
print(type('I love people and Python'))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2, 3}))
print(type({'name':'asab','age':250}))

# input()

""" birth_year = input('Enger your birth year: ')

print('You were born in ' + birth_year  + '.')
age = 2025 - int(birth_year)
print(age)
print('Your age is ', age) """


'''
bmi = mass / h*h

'''
""" 
height = float(input('What is your height?'))
mass = float(input('What is your weight? '))

print(type(height), type(mass))
bmi = mass / (height ** 2)

print(bmi)
print(round(bmi, 3)) """

# print(dir(10))
print(dir('We love Pyhton'))
print('We love Pyhton'.split())
print('We love Pyhton'.swapcase())
print('We love Pyhton'.lower())
print('We love Pyhton'.upper())

print(dir([1, 3,4]))

print(min(-5, 10, 0, -20,  20, 30, 5))
print(max(-5, 10, 0, -20,  20, 30, 5))
print(sum([-5, 10, 0, -20,  20, 30, 5, 30]))

print(range(0, 11, 1))
print(list(range(5, 51, 5)))
print(list(range(0, 1001, 100)))

print(list(range(1, 102, 2)))
print(list(range(0, 102, 2)))


print(abs(-10))

'''
list()
tuple()
dict()
id()
dir()
set()
'''
print(list('cat'))
print(list())
print(list((1, 2, 3)))
print(tuple())
print(tuple([1, 2, 3]))
print(set([1, 2, 3, 3, 4, 5]))

print(set(['Finland','Sweden','Sweden','Finland','Norway','Finland','Sweden']))
print(len(['Finland','Sweden','Sweden','Finland','Norway','Finland','Sweden']))
print(len(set(['Finland','Sweden','Sweden','Finland','Norway','Finland','Sweden'])))
print(dict())
print(list({'name':'asab','age':250}))
