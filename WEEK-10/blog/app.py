from flask import Flask, render_template

from mysql.connector import connect

# Connect to server
db = connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database='blog_db'
    )

# Get a cursor



app = Flask(__name__)
cursor = db.cursor()
cursor.execute('SHOW DATABASES')
for item in cursor:
    print(item)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/blogs')
def blogs():
    cursor.execute('SELECT * FROM blogs')
    blogs = cursor.fetchall()
    formatatted_blogs = [{
            'id': blog[0],
            'title': blog[1],
            'subtitle': blog[2],
            'category': blog[3],
            'cover_image': blog[4],
            'created_at': blog[5],
            'content': blog[6],
            'tags': blog[7],
            'views': blog[8],
            'likes': blog[9],
            'comments': blog[10]
        } for blog in blogs]
    return render_template('blogs.html', data = formatatted_blogs)

@app.route('/blogs/add')
def add_blog():
    return render_template('add-blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host='localhost', port = 5000, debug = True)


