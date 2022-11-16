from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf.csrf import CSRFProtect
from wtforms.validators import DataRequired,Email,Length
from flask_bootstrap import Bootstrap




app = Flask(__name__)

csrf = CSRFProtect(app)
csrf.init_app(app)
Bootstrap(app)

app.config['SECRET_KEY'] = 'burger'

secret_email = 'admin@email.com'
secret_password = '12345678'

class SignupForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email(message=("That's not a valid email address!"))])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8,message='Must be at least 8 characters long')])
    submit = SubmitField('Log In')
    




@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login.html", methods=['GET', 'POST'])
def login_page():
    form = SignupForm()
    if form.validate_on_submit():
        if form.email.data == secret_email and form.password.data == secret_password:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    
    return render_template('login.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)