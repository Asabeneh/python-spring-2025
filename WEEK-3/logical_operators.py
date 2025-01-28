"""
Logical Operators
- Logical operators are used to combine conditional statements.
- Logical operators are used to determine the logic between variables or values.
- and, or, not are the logical operators in Python.

John is  a student.
Marta is a doctor. 

John is not a student
John and Marta are students.
John or Marta is a student.
John and Mart are not students.


"""

print(3 > 2 and 2 > 1) # True
print(3 > 2 and 2 < 1) # False
print(3 < 2 and 2 < 1) # False

print(3 > 2 or 2 > 1) # True
print(3 > 2 or 2 < 1)  # True
print(3 < 2 or 2 < 1) # False

print(4 == 2 ** 2 and 100 <= 10 ** 2)
print(3 >= 3)
print(not True)
print(not False)
print(not not True)
print(not 2 == 2)
print( not(3 > 2 and 2 > 1)) # False

print(2 is 2)
print(2 is not 2)
print(2 is not 4)
print('land' in 'Finland')
print('Py' in 'Python')
print('Does milk exist in the shopping list: ', 'Milk' in ['Tomatoes', 'Potatoes','Coffee','Honey', 'Milk'])

