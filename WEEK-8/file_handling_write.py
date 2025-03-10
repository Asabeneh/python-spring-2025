
from countries_data import countries_data
import json
from pprint import pprint

def fetch_data(url):
    import requests
    response = requests.get(url)
    data = response.json()
    return data
url = 'https://restcountries.com/v3.1/all'
data = fetch_data(url)

def create_flags():
    with open('flags.txt', 'w') as f:
        for country in data:
            flag = country['flags']['svg']
            f.write(f'{flag}\n')
# create_flags()

def create_csv_file():
    with open('data.tsv', 'w', encoding='utf-8') as f:
        f.write('name   capital population  flag\n')
        for country in data:
            name = country['name']['common']
            capital = '' if country.get('capital') == None  else  country.get('capital')[0]
            population = country['population']
            flag = country['flags']['svg']
            f.write(f'{name}    {capital}   {population}    {flag}\n')


lst = []
for country in data:
    name = country['name']['common']
    capital = '' if country.get('capital') == None  else  country.get('capital')[0]
    population = country['population']
    flag = country['flags']['svg']
    latlng = country['latlng']
    lst.append(
        {
        "name":name,
        "capital":capital,
        "population":population,
        "flag":flag,
        "latlng":latlng
    },
    )


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(lst, f, ensure_ascii=False, indent = 4)


            


      

 