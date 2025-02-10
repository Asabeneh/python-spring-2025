'''
Builtin functions

'''

def do_something(acitivity):
    return f'I am {acitivity}'
    

print(do_something('teaching'))
print(do_something('studying'))
print(do_something('singing'))

'''
add_two_nums 
two params, a, and b 
it should return the sum of a and b
'''

def add_two_nums(a, b):
    return a + b

print(add_two_nums(3, 2))
print(add_two_nums(99, 1))


'''
name: make_square 
parameter: n
return the square of n

'''
def make_square(n):
    return n ** 2 

print(make_square(3))
print(make_square(4))
print(make_square(5))
print(make_square(10))

'''
calculate_area_of_rectangle
length, width 
return: area of the rectangle: length * width
'''

def calculate_area_of_rectangle (length, width):
    return length * width

print(calculate_area_of_rectangle(20, 10))

    
'''
calculate_weight of body:
parameter: mass, gravity
weight = mass x gravity 
round it to 1 decimal point
it is good if it has a default gravity

'''

def calculate_weight(mass, gravity = 9.81):
    weight = mass * gravity
    return round(weight, 1)

print(calculate_weight(75))
print(calculate_weight(75, 1.62))

