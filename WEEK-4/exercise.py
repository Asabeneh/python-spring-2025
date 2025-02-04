''''
Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100


'''

for i in range(11):
    print(f'{i} x {i} = {i * i}')

'''
Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.


'''

for lb in ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(lb)