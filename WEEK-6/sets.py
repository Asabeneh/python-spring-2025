
empty_set = set()

print(empty_set, type(empty_set), len(empty_set))

nums = {1, 2, 3, 4, 5}
print(type(nums))
print(len(nums))

print(0 in nums)
print(1 in nums)

for num in nums:
    print(num)

nums.add(6)

print(nums)
nums.update({7, 8, 9, 10})
print(nums)

nums.remove(6)
print(nums)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes

print(fruits)

A = { 1, 2, 3, 4, 5, 10, 11, 12}
B = {1, 2, 3, 4, 5, 6, 7, 8}

'''
AUB = {1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12}
AnB = { 1, 2, 3, 4, 5}
A\B = {10, 11, 12}
B\A = {6, 7, 8}
A Δ B = ( A ∖ B ) ∪ ( B ∖ A ) = {6, 7, 8, 10, 11, 12}

'''
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))
print(A.issubset(B))
print(A.isdisjoint(B))

'''
Data types:
Number(int, float, complex)
Booleans(True or False)
String-has order, access using index
List - mutable, has order, access using index
Tuple- Immutable, has order, access using index
Set - Doesn't allow duplicates, does not have order, mutable
dictionaries: key and value pair, mutable 
'''