'''
Dictionary:

{
    'key':'value'
}

'''
from pprint import pprint
empty_dict = {}
print(len(empty_dict), type(empty_dict))

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'is_married': True,
    'age': 250,
    'skills':['Python','MySQL','MongoDB'],
    'address': {
        'country':'Finland',
        'city':'Helsinki',
        'street_name':'space street',
        'zipcode':'02770'
    }
}

""" print(len(person))
for key in person:
    print(key, person[key]) """
print(len(person))
print(person['first_name'])
print(person.get('first_name'))

if 'nationality' in person:
    print(person['nationality'])
else:
    person['nationality'] = 'Ethiopian'
    
person['age'] = 55
pprint(person)


person['skills'].append('JavaScript')
person['skills'].append('Node.js')
pprint(person)

print(person.keys())
keys = list(person.keys())
print(keys)
values = list(person.values())
print(values)
print(person.items())

items = list(person.items())
print(items)
print('items will be printed out')

""" dct = {}
for item in items:
    k, v = item
    dct[v] = k
    print(k, v) """
    
    
del person['first_name']
person.pop('last_name')

pprint(person)
person = {}

copied_dict = person.copy()


