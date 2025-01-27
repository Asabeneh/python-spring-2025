
# Assignment operator
a = 3
b = 4
total = a + b
difference = a - b
product = a * b
remainder = a % b 
div = a / b
exponentaiton = a ** b

print(f'The sum  of {a} and {b} is {total}')
print(f'The difference of {a} and {b} is {difference}')
print(f'The product of {a} and {b} is {product}')
print(f'The remainder of {a} divided by {b} is {remainder}')

'''

3 x 4 = 12

'''
print(f'{a} +  {b} = {total}')
print(f'{a} - {b} = {difference}')
print(f'{a} x {b} = {product}')
print(f'{a} / {b} = {div}')
print(f'{a} ^ {b} = {exponentaiton}')

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country  = 'Finland'
city = 'Helsinki'
age = 250
job_positon = 'Fullstack Engineer'
is_married = True
height = 1.75
educations = ['']
skills = ['HTML','CSS','JavaScript','Python']
mass = 76
gravity = 9.81

num1 = 3
num2 = 4
full_name = first_name  + ' ' +  last_name


'''
I am Asabeneh Yetayeh. I am 250 years old. I am a Fullstack Engineer and Instructor. I live in Helsinki, Finland. I weight 76 killo gram and  I am 1.75 meter tall.
''' 

print('I am ' + full_name + ' I am ' + str(age))

print(f'I am {full_name}. I am {age} years old. I am a {job_positon} and Instructor. I live in {city}, {country}. I weight {mass} killo gram and  I am {height} meter tall.')