from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == "POST":
        email=request.form['email']
        user = User.query.filter_by(email=email).first()
        
        if email == user.email:
            error = "There is already an account with that email registered!"
            return render_template("login.html",error=error)
        
        else:
        
        
            new_user = User(
                name = request.form['name'],
                email=request.form['email'],
                password=generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8))
                
            db.session.add(new_user)
            db.session.commit()
            
            login_user(new_user)
        
            return redirect(url_for("secrets"))
    
    return render_template("register.html", logged_in=current_user.is_authenticated)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login',methods=['POST','GET'])
def login():
    
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        print(user)
        
        if email == False:
            error = "Account doesn't exist, try again."
            return render_template("login.html",error=error)
        else:
        #Check stored password hash against entered password hashed.
        
            if check_password_hash(user.password, password) == False:
                error = "Password wrong, try again."
                return render_template("login.html",error=error)
            
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('secrets'))
    
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    username = request.args.get("name")
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static','files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
