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

height = float(input('What is your height?'))
mass = float(input('What is your weight? '))

'''
bmi = mass / h*h

'''
print(type(height), type(mass))
bmi = mass / (height ** 2)

print(bmi)
print(round(bmi, 3))
