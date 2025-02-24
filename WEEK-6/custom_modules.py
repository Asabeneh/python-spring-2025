def do_something(task):
    return f'I am {task}'

def add_two_nums (a, b):
    return a  + b

def make_square(n):
    return n ** 2

def sum_list(lst):
    return sum(lst)
    

def sum_all_nums(*args):
    return sum(args)

def print_person_info(first_name, last_name, age, country, title):
    return f'I am {first_name} {last_name}. I am {age} years old. I live in {country}. I am a {title}.'

def calculate_weight(mass, gravity = 9.81):
    return round(mass * gravity, 1)

