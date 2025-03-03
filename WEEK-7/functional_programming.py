# map, filter, reduce

from countries_data import countries_data
from pprint import pprint
from functools import reduce
nums = [1, 2, 3, 4, 5] # [1, 4, 9, 16, 25]

""" new_lst = []
for num in nums:
    new_lst.append(num ** 2)

new_lst = [ num ** 2 for num in nums] """



new_lst = list(map(lambda n: n ** 2, nums))
print(new_lst)

countries = list(map(lambda country: {
    'name':country['name'],
    'capital':country['capital'],
    'population':country['population']
}, countries_data))
# pprint(countries)


populations = list(map(lambda country:country['population'], countries_data))
# print(populations)
world_population = sum(populations)
print('{:,}'.format(world_population))



print('==== Country with Land =====')
countries_with_land = list(filter(lambda country: 'land' in country['name'], countries_data))
# pprint(countries_with_land)

print('==== Reduce result =====')

nums = [1, 2, 3, 4, 5]
total = reduce(lambda acc, cur: acc + cur, nums, 0)
print(total)

world_population = reduce(lambda acc, cur: acc + cur['population'], countries_data, 0)
print(world_population)