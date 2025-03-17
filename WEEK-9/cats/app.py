from flask import Flask, render_template

def fetch_data(url):
    import requests
    response = requests.get(url)
    data = response.json()
    return data
url = 'https://api.thecatapi.com/v1/breeds'
data = fetch_data(url)

def minify_cats_data():
    lst = []
    for cat in data:
        weight_lowest, weight_highest = cat['weight']['metric'].split(' - ')
        lifespan_lowest, lifespan_highest = cat['life_span'].split(' - ')
        id = cat.get('reference_image_id')
        image_url = f'https://cdn2.thecatapi.com/images/{id}.jpg' if id != None else ''
        lst.append({
            'name':cat['name'],
            'origin':cat['origin'],
            'description':cat['description'],
            'weight':(int(weight_lowest) + int(weight_highest)) / 2,
            'life_span':(int(lifespan_lowest) + int(lifespan_highest))/2,
             'image_url': image_url
        })
    return lst


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/api/v1/cats')
def cats_api():
    return minify_cats_data()


@app.route('/cats')
def cats():
        cats = minify_cats_data()
        return render_template('cats.html', cats = cats)


  





if __name__ == '__main__':
    app.run(host='localhost', port = 5000, debug = True)
