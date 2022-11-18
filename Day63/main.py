from flask import Flask, render_template, request, redirect, url_for
# import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# try:
#     cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# except sqlite3.OperationalError:
#     pass

# cursor.execute("INSERT INTO books VALUES(1, 'The Hobbit', 'J.R.R. Tolkien', '10')")
# db.commit()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    title = db.Column(db.String(250),nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float,nullable=False)
    
    def __repr__(self):
        return f'<{self.title}>'
    




@app.route('/', methods=['GET', 'POST'])
def home():
    
    if request.method == 'POST':
        with app.app_context():

            new_book=Books(title=request.form.get('b-title'),author=request.form.get('b-author'),rating=request.form.get('b-rating'))

            db.session.add(new_book)    
            db.session.commit()

    all_books = db.session.query(Books).all()
    
    
    
    
    return render_template('index.html',books=all_books)

@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    book = Books.query.filter_by(id=id).all()
    
    if request.method == 'POST':
        book_to_update = Books.query.get(id)
        book_to_update.rating = request.form.get('new-rating')
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('edit.html',b=book)



@app.route("/add")
def add():
    return render_template('add.html')


@app.route('/delete/<int:id>')
def delete(id):
    
    book_id = request.args.get('id')
    print(book_id)
    
    book_to_delete = Books.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

