nums = [1, 2, 3, 4, 5] # [1, 4, 9, 16, 25]
countries = ['Finland', 'Sweden','Norway']  # ['Helsinki', 'Stockholm', 'Oslo']

new_ist = [ num for num in nums if num % 2 == 0 ]
print(new_ist)
""" new_lst = []

for num in nums:
    new_lst.append(num * num)

print(new_lst) """

from countries import countries
countries_with_land = [country for country in countries if 'land' in country]
print(countries_with_land)

country_codes = [country.upper()[:3] for country in countries ]
print(country_codes)