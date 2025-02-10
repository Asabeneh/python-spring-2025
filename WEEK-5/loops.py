from countries import countries
from pprint import pprint

""" for i in range(1, 11):
    print(f'{i} x {i} = {i * i}') """
    

nums = [-2, 3, 0, 4, -8, 4, 5, 6]

for num in nums:
    if num == 0:
        break 
    # print(num)
    
nums = [2, 3, 0, 4, -8, 4, 5, 6]

# print('break if there is a negative')
for num in nums:
    if num < 0:
        break
    # print(num)
    
# print('continue if there is a negative')
for num in nums:
    if num < 0:
        continue
    # print(num)
    
    
countries_with_more_words = []
for country in countries:
    words = country.split()
    if len(words) > 1:
        countries_with_more_words.append(country)

# pprint(countries_with_more_words)
 
    


# For loop and while loop
'''
initial
condition
increment/decrement


'''

for i in range(10, -1, -1):
    print(i)
    

print('Loop using while loop')
i = 0 
while i <= 10:
    print(i)
    i = i + 1
    
    
i = 10
while i >= 0:
    print(i)
    i = i - 1
    
    

nums = []
while True:
    value = int(input('Enter a number: '))
    if value == 0:
        break 
    if value < 0:
        continue
    nums.append(value)

print(nums)

