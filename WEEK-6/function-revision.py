def do_something(task):
    return f'I am {task}'

print(do_something('learning'))
print(do_something('playing'))
print(do_something('reading'))
print(do_something('writing'))

def add_two_nums (a, b):
    return a  + b

def make_square(n):
    return n ** 2

def sum_list(lst):
    return sum(lst)
    
'''
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

'''

print(sum_list([10, 20, 30]))

def sum_all_nums(*args):
    return sum(args)

print(sum_all_nums(1, 2, 3, 4, 10, 200, -100, 400))

def print_person_info(first_name, last_name, age, country, title):
    return f'I am {first_name} {last_name}. I am {age} years old. I live in {country}. I am a {title}.'

print(print_person_info(first_name='Asab', country='Finland', age= 250,  last_name='Yeta',title = 'Fullstack developer'))

'''
return values:
- boolean
- string
- list

'''

def calculate_weight(mass, gravity = 9.81):
    return round(mass * gravity, 1)

print(calculate_weight(75))
print(calculate_weight(75, 1.62))

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Python Spring 2025','Asabeneh','Matti','Eero','Matheos', 'Judit'))

def kwarg_example(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


kwarg_example(first_name ='Asab', last_name = 'Yeta', age = 250, skils = ['Python', 'JS'])

