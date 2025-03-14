'''
- Numbers (int, float, complex)
- Boolean (True or False)
- Strings
- List
- Sets
- Tuples
- Dictionaries
'''

# Strings - any data under single, double or triple quote 
# String can be a single character or multiple pages size

print('cat')
print(len('cat'))
print('cat'.upper())
print('cat paradize application'.title())
print(len('cat paradize application'))
print('cat paradize application'.split())
print(len('cat paradize application'.split()))

print('I love people and Python')
statement = 'I love people and Python'
words = statement.split()
print(words, len(words))

print('love' in 'I love people and Python')
print('people' in 'I love people and Python')
print('I love people and Python'.startswith('I love'))
print('I love people and Python'.endswith('Python'))

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
full_name = first_name + ' ' +  last_name
full_name = f'{first_name} {last_name}'
print(full_name)

print('My name is ' + full_name +'. I am ' + str(age) + ' years old.' )
print(f'My name is {full_name}. I am {age} years old.')
'''

My name is Asabeneh Yetayeh. I am 250 years old.

'''
# Escape characters \ \n \t

print('Asabeneh', 'Yetayeh', 250, sep='\n')
print(f'My name is {full_name}.\nI am {age} years old.')

print("I don't like to stay a day without Python")
print('I don\'t like to stay a day without Python')
print('Some people say "AI will replace many jobs soon"')
print("Some people say 'AI will replace many jobs soon'")
print("Some people say \"AI will replace many jobs soon\"")

print('Day 1 \t Day 2 \t Day 3')
print('10 \t 5 \t 12')
print('10 \t 5 \t 12')
print('10 \t 5 \t 12')



first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
age = 250
heigth = 1.753456
formated_string = 'I am %s %s. I am a %s instructor. I am %d years old. I am %.2f meter tall.' %(first_name, last_name, language, age, heigth)
print(formated_string)

print(f'I am {first_name} {last_name}. I am a {language} instructor. I am {age} years old. I am {heigth:.2f} meter tall.')
# print('I am {first_name} {last_name}. I am a {language} instructor. I am {age} years old. I am {heigth:.2f} meter tall.'.format(first_name, last_name, language, age, heigth)
 
print('I am {} {}. I am {} instructor. I am {} years old. I am {:.2f} meter tall.'.format(first_name, last_name, language, age, heigth))

print('People like {} {}'.format('melon' , 'water'))

a = 3 
b = 4 
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} x {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} ^ {b} = {a ** b}')

pet = 'cat'
print(pet[0])
print(pet[1])
print(pet[2])
length = len(pet)
print(length)
last_index = length - 1
print(pet[last_index])
print(pet[-1])
print(pet[-2])
print(pet[-3])

lang = 'Python'
print(lang[0:2])
print(lang[2:5])  # tho
print(lang[2:])
print(lang[:3])

print('cat'[::-1])
word = 'civic'
print(pet == pet[::-1])

challenge = 'thirty days of python'
print(challenge.capitalize())
print(challenge.count('t'))

dna_sequence = 'CCGAGAGCAAGTAGGGCACCCTGTAGTTCGAAGCGGAACTATTTCGAGGGGCGAGCCCACATCGTCTCTTCTGCGGATGACTTAACACGCTAGGGAGGTGGAGTCGATTCCATCGATGGTTATAAATCAAAAAATCGGAACGCTGTCTGGAGGATGAATCTAACGGTGCGTATCTCGATCGCTCAGTCGCTTTTCGTACTGCGCGAAAGTTCGCACCGCTCATACACTTGGTTCCGAAGCCTGTCCTGATATATGAATCCAAACTAGAGCGGGGCTCTTGACGTTTGGAGTTGTAAATATCTAATATTCCAATCGGCTTTTACGTGCACCACCGCGGGCGGCTGACGAGGGACTCACACCGAGAAACTAGACAGTTGCGCGCTGGAAGTAGCGCCGGCTAAGAAAGACGCCTGGTACAGCAGGACTATGAAACCCGTACAAAGGCAACATCCTCACTTCGGTGAATCGAAACGCGGCATCAAGGTTACTTTTTGGATACCTGAAACAAAACCCATCGTAGTCCTTAGACTTGGGACACTTTCACCCCTAGGGCCCATATCTGGAAATAGACGCCAAGTTCAATCCGTACTCCGACGTACGATGGAACAGTGTGGATGTGACGAGCTTCATTTATACCCTTCGCGCGCCGGACCGGGGTCCGCAAGGCGCGGCGGTGCACAAGCAATTGACAACTAACCACCGTGTATTCGTTATGGCACCAGGGAGTTTAAGCCGAGTCAATGGAGCTCGCAATACAGAGTTTACCGCATCTTGCCCTAACTGACAAACTGTGATCGACCACAAGCCAAGCCATTGCCTCTTAGACACGCCGTTACAGTGATTATGAAAACTTTGCGGGGCATGGCTACGACTTGTTCAGCCACGTCCGAGGGCAGAAACCTATCCCCATTTGTATGTTCAGCTATCTTCTACCCATCCCCGGAGGTTAAGTAGGTTGTGAGATGCGGAAGAGGCTCTCGATCATCCCGTGGGACATCAA'
total = len(dna_sequence)

number_of_a = dna_sequence.count('A')
print(number_of_a)
print(total, number_of_a / total)
# C, G , T, and their proportion

print('car'[::-1])
# Palindrome words => civic => civic, level => level, eye => eye 
print('level'[::-1] == 'level')

print('python for everone'.capitalize())
print('Python For Everone'.lower())
print('python for everone'.upper())
print('python for everone'.replace('python', 'AI'))
print('python for everone'.split())
print('I love Python. I love people. I teach Programming.'.split())
print('I love Python. I love people. I teach Programming.'.lower().replace('.', '').split())
print('I love Python. I love people. I teach Programming.'.split('.'))
print('I love Python. I love people. I teach Programming.'.split('love'))
print('     python for everone      ')
print('     python for everone'.rstrip())
print('     python for everone'.lstrip())
print('python for everone'.startswith('python '))
print('python for everyone'.endswith('everyone'))

challenge = 'thirty\tdays\tof\tpython'
print(challenge)
print(challenge.expandtabs(8))
print(challenge.expandtabs(15))

print('python for everyone'.find('y'))
print('python for everyone'.rfind('y'))
print('python for everyone'.find('z'))

if 'python for everyone'.find('z') == -1:
    print('We do not find the value')

print('python for everyone'.index('y'))
print('python for everyone'.rindex('y'))

if 'z' in 'python for everyone':
    'python for everyone'.index('z')
else:
    print('It is not found')

print('abc'.isalpha())
print('abc123'.isalpha())
print('abc123'.isalnum())

challenge = '\u00B2' # 1/2
print(challenge.isdigit())   # 

num = '10'
print(num.isnumeric()) # False

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ', '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

print('SunNy'.swapcase())



