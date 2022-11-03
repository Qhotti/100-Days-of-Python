from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    y = datetime.today().year
    return render_template('index.html',num=random_number,year=y)

@app.route('/guess/<name>')
def game(name):
    age_website = requests.get(f'https://api.agify.io?name={name}')
    age_json = age_website.json()
    age = age_json['age']
    gender_website = requests.get(f'https://api.genderize.io?name={name}')
    gender_json = gender_website.json()
    gender = gender_json['gender']
    
    return render_template('game.html',age = age,name = name,gender = gender)


@app.route('/blog/<num>')
def get_blog():
    blog_url = 'https://api.npoint.io/784561d8419648a3bfba'
    response=requests.get(blog_url)
    posts = response.json()
    return render_template('blog.html',posts = posts)

if __name__ == "__main__":
    app.run(debug=True)


