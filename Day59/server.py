from flask import Flask, render_template
import requests

app = Flask(__name__)

posts = requests.get('https://api.npoint.io/473932feaee539582ce9').json()





@app.route('/')
@app.route('/index.html')
def home():
    return render_template("index.html",posts=posts)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/post.html/<int:id>')
def post(id):
    return render_template("post.html",posts=posts,id = id)

@app.route('/contact.html')
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)