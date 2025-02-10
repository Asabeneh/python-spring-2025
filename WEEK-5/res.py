from pprint import pprint

user = {
    'first_name': 'Asabeneh',
    'username': 'asab',
    'email': 'asabeneh@gmail.com',
    'password': '123123123',
    'avatar': 'https://avatars.githubusercontent.com/u/9008063?v=4'
}

users = [
    {
        'first_name': 'Asabeneh',
        'username': 'asab',
        'email': 'asabeneh@gmail.com',
        'password': '123123123',
        'avatar': 'https://avatars.githubusercontent.com/u/9008063?v=4'
    },
    {
        'first_name': 'John',
        'username': 'john',
        'email': 'john@gmail.com',
        'password': '123123123',
        'avatar': ''
    },
    {
        'first_name': 'Sara',
        'username': 'sara',
        'email': 'sara@gmail.com',
        'password': '123123123',
        'avatar': ''
    }
]
for user in users:
    print(f'''Hello {user['first_name']}, Wish you a happy new year!
          ''')
