'''
NumPy
Pandas
Matplotlib
skitlearn
'''

from pprint import pprint
from functools import reduce
from utils.fetch_data import fetch_data
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np

countries_url = 'https://restcountries.com/v3.1/all'

countries = fetch_data(countries_url)
world_population = reduce(lambda acc, cur: acc + cur['population'], countries, 0)
# print(world_population)

cats_url = 'https://api.thecatapi.com/v1/breeds'
cats = fetch_data(cats_url)


txt = ''
for cat in cats:
    txt += cat['description'] + ' '
words = txt.lower().replace('.', ' ').replace(',', ' ').split()

cleaned_words = [ word for word in words if word not in STOPWORDS]

txt = ' '.join(cleaned_words)
# Create and generate a word cloud image:
wordcloud = WordCloud(background_color='white').generate(txt)

# Display the generated image:
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("on")
# plt.savefig('cats_worldcloud.png') 
# plt.show()

# print(STOPWORDS)

x = np.arange(-100, 100)
y = np.array(x) ** 2 
# y = 2x 

# plt.scatter(x, y)
# plt.show()

weigth_min = []
for cat in cats:
    lowest, highest = cat['weight']['metric'].split(' - ')
    value = int(lowest)
    weigth_min.append(value)
print(min(weigth_min))