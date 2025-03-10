from countries_data import countries
try:
    print([1, 2,3][2])
except Exception as e:
    print(e)
""" 
nums = [1, 2, 3]
one, two, three = nums
countries = ['Finland', 'Sweden', 'Norway','Iceland','Denmark','Estonia']
fin, _, nor, *rest = countries
print(rest) """

print(countries)
for index, country in enumerate(countries):
    print(f'{index + 1}. {country}')

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
countries  = ['Finland', 'Sweden', 'Norway','Denmark', 'Estonia']
cities = ['Helsinki', 'Stockholm', 'Oslo']

print(list(zip(countries, cities)))

from pprint import pprint
fruits_vegs = []
for fruit, veg in zip(fruits, vegetables):
    fruits_vegs.append({
        'fruit':fruit,
        'veg':veg
    })
pprint(fruits_vegs)


