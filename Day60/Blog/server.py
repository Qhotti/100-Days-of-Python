import os
import smtplib
from flask import Flask, render_template,request
import requests

app = Flask(__name__)

posts = requests.get('https://api.npoint.io/473932feaee539582ce9').json()

EMAIL = os.environ.get('MY_EMAIL')
PASSWORD = os.environ.get('MY_PASSWORD')
API_KEY=os.environ.get('CAT_GIF_API_KEY')



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

@app.route('/contact.html',methods=['GET'])
def contact():
    return render_template("contact.html")

@app.route('/contact.html',methods=['POST'])
def receive_data():
    name=request.form['username']
    email=request.form['email']
    number=request.form['phone-number']
    message=request.form['message']
    
    
    headers={
        'x-api-key': API_KEY
    }
    
    parameters={
        'mime_types': 'gif'
    }
    cat=requests.get('https://api.thecatapi.com/v1/images/search',headers=headers,params=parameters).json()
    
    gif=cat[0]['url']

    with smtplib.SMTP('smtp-mail.outlook.com', port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs=EMAIL,
            msg=f'Subject:Message from Blog\n\nName: {name}\nEmail: {email}\nPhone Number: {number}\nMessage: {message}') 
    return render_template("successful.html",gif=gif)

if __name__ == "__main__":
    app.run(debug=True)