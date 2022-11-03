from flask import Flask, render_template
import requests

posts = requests.get('https://api.npoint.io/784561d8419648a3bfba').json()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",posts=posts)

@app.route('/post/<int:id>')
def post(id):
    return render_template('post.html',posts=posts,id = id)

if __name__ == "__main__":
    app.run(debug=True)
