import math
from countries import countries
from pprint import pprint
from math import pi, factorial as fact, pow, sqrt, tau, floor, ceil

print('countries:', countries)

languages = []
for country in countries:
    pass
    # pprint(country['languages'])


def calculate_circle_area(radius):
    return round(pi * radius * radius, 2)


print(calculate_circle_area(100))


""" import math
print(math.ceil(3.14))
print(math.floor(3.14))
print(math.factorial(5)) # 5 * 4 * 3 * 2 * 1
print(math.pow(2, 5))  # 2 ** 5
print(math.sqrt(2), 2 ** 0.5) # 2 ** 0.5
print(math.sqrt(4)) """


print(ceil(3.14))
print(floor(3.14))
print(fact(5))  # 5 * 4 * 3 * 2 * 1
print(pow(2, 5))  # 2 ** 5
print(sqrt(2), 2 ** 0.5)  # 2 ** 0.5
print(sqrt(4))


def make_square(n): return n * n


print(make_square(10))
print(make_square(9))

languages = []
for country in countries:
    country['languages']

print(languages)
