from countries_data import countries_data as countries
from pprint import pprint

""" def find_most_spoken_languages(data, n = 10):
    lst = []
    for country in data:
        languages = country['languages']
        lst.extend(languages)
    unique_lst = set(lst)
    dct = {}
    for lang in unique_lst:
        count = len([item for item in lst if lang == item ])
        dct[lang] = count
    items = dct.items()
    sorted_items = sorted(items, key=lambda item:item[1], reverse=True)
    ten_most_spoken_languages = sorted_items[:n]
    return ten_most_spoken_languages

print(find_most_spoken_languages(countries_data))
 """

languages = {}
for country in countries:
    for language in country['languages']:
        if language in languages:
            languages[language] += 1
        else:
            languages[language] = 1
items = languages.items()
sorted_items = sorted(items, key=lambda item: item[1], reverse=True)
print(sorted_items[:10])

   



from countries_data import countries
from pprint import pprint

def find_most_populated_countries (data, n = 10):
    sorted_population = sorted(countries, key=lambda country:country['population'],reverse= True)
    return sorted_population[:10]





