'''
List is a collection of items, indexed, ordered, muttable
'''

empty_list = []
print(empty_list)
print(len(empty_list))

nums = [1, 2, 3, 4]
print(nums)
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(len(nums))

last_index = len(nums) - 1
print(nums[last_index])

print(nums[-1])
print(nums[-2])
print(nums[-3])
print(nums[-4])

print(nums[0:2])
print(nums[1:3])
print(nums[:3])
print(nums[1:])
print(nums[-3:-1])

'''
List methods:
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

'''


fi, sw, *others =  ['Finland', 'Sweden', 'Norway','Denmark','Iceland']
print(fi)
print(fi, sw, others)

shopping_list = ['Tomatoes','Potatoes', 'Milk', 'Coffee', 'Sugar', 'Tea']
print(len(shopping_list))
print(shopping_list)
shopping_list.append('Cheese')
shopping_list.append('Yoghurt')
shopping_list.extend(['Banana','Guava','Apple', 'Mango'])
print(shopping_list)

nums = [1, 2, 3, 4]
nums.insert(0, 11)
print(nums)

shopping_list.insert(0,'Salmon')
print(shopping_list)




'''
reverse, copy, sort, clear

'''

countries = ['Finland', 'Sweden', 'Norway','Denmark','Iceland']

print(sorted(countries))
print(countries)



positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)


del countries[2:4]

print(countries)

'''
What is the differences between bultin functions and methods?

'''