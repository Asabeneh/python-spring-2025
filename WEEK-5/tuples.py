"""
Tuples - immuatable

count, index, clear, del

"""

empty_tuple = ()
print(type(empty_tuple))

values = ('Asab', True, 250, 250, 250, 'Python')
for value in values:
    print(value)
    
print(values[0])
print(values[1])
print(values[2])

print(250 in values)
print(values[1:3])

print(values.index('Python'))
print(values.count(250))

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
print(list(fruits_and_vegetables))
print(set(fruits_and_vegetables))

libs = ('Python', 'Numpy','Pandas','Django', 'SciPy','item ', 'item', 'item')
py, np, pd, _, scpy, *rest = libs
print(py)
print(np)
print(pd)
print(scpy)
print(rest)

