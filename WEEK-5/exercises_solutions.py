"""
Loops
Write a for loop that prints all the even numbers between 0 and 20.
Use a while loop to calculate the sum of numbers from 1 to 100. Print the result.

"""

""" for i in range(2, 21, 2):
    print(i) """
from countries import countries
from pprint import pprint
i = 1
total = 0
while i <= 100:
    total = total + i
    i = i + 1
print(total)


nums = range(1, 21)
for i in nums:
    if i % 2 == 0:
        print(i)

print(list(range(2, 21, 2)))

'''

Lists
Given the list numbers = [10, 20, 30, 40, 50], write code to:

Append the number 60 to the list.
Remove the number 30 from the list.
Print the final list.



'''
numbers = [10, 20, 40, 30, 50]
numbers.append(60)
numbers.remove(30)
print(numbers)

'''
Write a program that takes a list of integers as input and returns a new list with only the unique elements (no duplicates).

Example
input_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
result = unique_elements(input_list)
print(result)
Expected Output:
[1, 2, 3, 4, 5]

'''


def unique_elements(lst):
    return list(set(lst))


input_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
print(unique_elements(input_list))

"""
Dictionaries
Create a dictionary called student with the following key-value pairs:
"name": "Matti"
"age": 19
"grade": "A" Then, update the "age" to 29 and add a new key "city" with the value "Helsinki". Print the updated dictionary.

Write a function that takes a dictionary as input and returns the key with the maximum value. For example, for {"a": 10, "b": 20, "c": 15}, the function should return "b".

"""
student = {
    "name": "Matti",
    "age": 19,
    "grade": "A"
}
pprint(student)
student['age'] = 29
student['city'] = 'Helsinki'
pprint(student)


def find_key_with_max_value(dct):
    dct = {"a": 10, "b": 20, "c": 15}
    sorted_dct = sorted(dct.items(), key=lambda item: item[1])
    return sorted_dct[-1]


test_input = {"a": 10, "b": 20, "c": 15, 'e': 100, 'f': 300, 'n': -20, 'r': 40}
print(find_key_with_max_value(test_input))


# max_value_with_key = max(test_input.items(), key=lambda item: item[1])
# print(max_value_with_key)

items = test_input.items()
print(items)
print(max(items, key=lambda item: item[1]))

'''
Functions
Write a function called is_palindrome that takes a string as input and returns True if the string is a palindrome (reads the same backward as forward), and False otherwise.

Create a function called calculate_area that takes two arguments (length and width) and returns the area of a rectangle. If no arguments are provided, assume the shape is a square with a default side length of 5.

'''

txt = 'The eve was great. We ewe the eye with civic racecar, the radar redder redivider refer rotor.'


def is_palindrome(txt):
    return txt == txt[::-1]


def filter_palindrome_words(txt):
    txt = txt .lower().replace(',', '').replace('.', '')
    words = txt.strip().split()
    palindromes = []
    for word in words:
            if is_palindrome(word):
                palindromes.append(word)
    return palindromes

print(filter_palindrome_words(txt))


def calculate_area(length = 8, width = None):
    if width == None:
        return length * length
    return length * width

print(calculate_area())

def calculate_weight(mass, gravity = 9.81):
    return mass * gravity

print(calculate_area(75))
print(calculate_area(75, 1.62))
'''
Write a program that uses a loop to create a dictionary where the keys are numbers from 1 to 10, and the values are the squares of the keys. For example, the key 2 should have the value 4.


'''
dct = {}
for key in range(1, 11):
    value = key * key
    dct[key] = value
print(dct)

def is_even(n):
    return n % 2 == 0

def filter_list(lst, is_even):
    evens = []
    for num in lst:
        if is_even(num):
            evens.append(num)
    return evens

print(filter_list([1, 2, 3,10, -5, -8, 0, 4, 5], is_even))

'''
Create a function a function that takes a list of countries and a letter and it will return a tuple with the first item list of countries that starts with the letter, the second item is the numberof countries

 
output
print(xyz_func(countries, 'F')) # (['Finland', 'Fiji','France'], 3)


'''
for country in countries:
    if country.startswith('C'):
        print(country)



"""
'A': [],
'B':[],
'C': []
 .
 .
 .
 'F':['Finland', 'Fiji','France'],

"""
