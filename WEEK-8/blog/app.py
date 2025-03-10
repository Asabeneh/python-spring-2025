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
    return '''

<div style="text-align:center; color:red; width: 50%; margin: 25px auto;">
<ul>
<li>
<a href="/">Home</a>
</li>
<li>
<a href="/about">About</a>
</li>
<li>
<a href="/contact">Contact</a>
</li>
<li>
<a href="/cats">Cats</a>
</li>
<li>
<a href="/api/v1/cats">Cats API</a>
</li>
</ul>
<h1>Welcome to Web Dev with Pytyhon</h1>
<small> Year: 2025</small>
</div>
'''


@app.route('/about')
def about():
    return '''
<div style="text-align:center; color:red; width: 50%; margin: 25px auto;">
<ul>
<li>
<a href="/">Home</a>
</li>
<li>
<a href="/about">About</a>
</li>
<li>
<a href="/contact">Contact</a>
</li>
<li>
<a href="/cats">Cats</a>
</li>
<li>
<a href="/api/v1/cats">Cats API</a>
</li>
</ul>
<h1>About Us</h1>
<p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
</p>
</div>
'''

@app.route('/contact')
def contact():
    return '''
<div style="text-align:center; color:red; width: 50%; margin: 25px auto;">
<ul>
<li>
<a href="/">Home</a>
</li>
<li>
<a href="/about">About</a>
</li>
<li>
<a href="/contact">Contact</a>
</li>
<li>
<a href="/cats">Cats</a>
</li>
<li>
<a href="/api/v1/cats">Cats API</a>
</li>
</ul>
<h1>Contact Us</h1>
<form>
<input placeholder='Ener name' /> <br />
<label>You message</label> <br />
<textarea></textarea> <br />
<button>Send</button>
</form>
</div>
'''

@app.route('/api/v1/cats')
def cats_api():
    return minify_cats_data()


@app.route('/cats')
def cats():
        cats = minify_cats_data()
        return render_template('cats.html', cats = cats)


  





if __name__ == '__main__':
    app.run(host='localhost', port = 5000, debug = True)
