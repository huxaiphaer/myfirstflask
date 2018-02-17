from flask import Flask, render_template
from data import Articles

app = Flask(__name__)


Articles = Articles()


@app.route('/')
def index():
    return render_template('home.html')


# this for the about section
@app.route('/about')
def about():
    return render_template('about.html')

# this for the articles section
@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)

@app.route('/articles/<string:id>/')
def article(id):
    return render_template('article.html', id=id)

if __name__ == '__main__':
    app.run()
