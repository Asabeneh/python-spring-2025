

# Higher order functions: function that take another function as a parameter or return return function

def make_square(n):
    return n * n

def make_cube(n, func):
    return func(n) * n

print(make_cube(3, make_square))


def do_math(a, b):
    def add_two_nums():
        return a  + b 
    return add_two_nums
    # def multiply_two_nums():
    #     return a *  b
    # return {
    #     'add_two_nums':add_two_nums, 
    #     'multiply_two_nums':multiply_two_nums
    # }

print(do_math(10, 20)['add_two_nums']())
print(do_math(10, 20)['multiply_two_nums']())

