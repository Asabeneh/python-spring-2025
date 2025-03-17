'''
loops

'''
from countries_data import countries
print(1)
print(2)
print(3)

print('Happy New Year! 2025')

print(list(range(0, 11)))
""" 
for i in range(1, 6):
    print(f'{i}- Happy New Year! 2025') """


'''
How about if you like to sum all the numbers from 0 to 100

'''
# nums = list(range(0, 101))
# print(nums)
# print(sum(nums))
  
total = 0
for i in range(0, 101):
    total = total + i

print(total)

# total = 0
# total = total + 0 = 0
# total = total + 1 = 1
# total = total + 2 = 3
# total = total + 3 = 6
# total = total + 4 = 10
# total = total + 5 = 15

evens = []
for i in range(0, 100):
    if i % 2 == 0:
        evens.append(i)
print(evens)


odds = []
for i in range(0, 100):
    if i % 2 != 0:
        odds.append(i)
print(odds)

nums = [-2, 3, 0, 4, -8, 4, 5, 6]
positive_nums = []

for num in nums:
    if num > 0:
        positive_nums.append(num)
print(positive_nums)



for country in countries:
    print(country, country.upper(), country.upper()[:3], len(country))

countries_with_land = []
for country in countries:
    if 'land' in country:
        countries_with_land.append(country)
print(countries_with_land)

countries_without_land = []
for country in countries:
    if 'land' not in country:
        countries_without_land.append(country)
print(countries_without_land)



countries_with_land = []
for country in countries:
    if 'land' in country:
        countries_with_land.append(country)
print(countries_with_land)


