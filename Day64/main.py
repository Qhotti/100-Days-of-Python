from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired,Optional
import requests
import os

app = Flask(__name__)
API_KEY = os.environ.get('MOVIEDB_API_KEY_TOP_10')

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)




class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250),nullable=False, unique=True)
    year = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float,nullable=True)
    ranking = db.Column(db.Float,nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)
    
    
    def __repr__(self):
        return f'<{self.title}>'
    


class UpdateForm(FlaskForm):
    rating = IntegerField('Rating (ex. 6.9)',validators=[DataRequired()])
    review = StringField('Review',validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class AddForm(FlaskForm):
    movie_name = StringField('Movie Name')
    submit = SubmitField('Submit')




@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.ranking).all()
    for i in range(len(all_movies)):

        all_movies[i].ranking = len(all_movies) - i
        
    db.session.commit()
    return render_template("index.html",movies=all_movies)


@app.route("/add",methods=['GET','POST'])

def add():
    form=AddForm()
    
    title=form.movie_name.data
    
    
    parameters={
        'api_key': API_KEY,
        'query': title,
    }
    if form.validate_on_submit():
        response = requests.get('https://api.themoviedb.org/3/search/movie',params=parameters)
        json = response.json()
        return render_template('select.html',json=json)
    
    
    
    
    return render_template("add.html",form=form)

@app.route('/add/<int:id>')
def movie(id):
    movie_id = id
    parameters={
        'api_key': API_KEY,
    }
    
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}',params=parameters)
    json = response.json()
    year = json['release_date'].split("-", 1)[0][-4:]
    img = json['poster_path']
    new_movie = Movie(title=json['original_title'], year = year, description=json['overview'], img_url=f'https://image.tmdb.org/t/p/w500{img}' )
    db.session.add(new_movie)
    db.session.commit()
    

    
    
    return redirect(url_for('home'))
    
    
    

    
    


@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    
    info= Movie.query.filter_by(id=id).all()
    form=UpdateForm()
    
    movie = Movie.query.get(id)
    
    if form.validate_on_submit():

        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('edit.html',form=form,info=info)


@app.route('/delete/<int:id>')
def delete(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
