import random
import time
from flask import Flask
app=Flask(__name__)


# def make_bold(function):
#     def wrapped_function():
#         tag = function()
#         bold =(f'<b>{tag}</b>')
#         return bold
#     return wrapped_function

# def make_emphasis(function):
#     def wrapped_function():
#         tag = function()
#         emphasis =(f'<em>{tag}</em>')
#         return emphasis
#     return wrapped_function

# def make_underlined(function):
#     def wrapped_function():
#         tag = function()
#         underlined =(f'<u>{tag}</u>')
#         return underlined
#     return wrapped_function




# @app.route("/")
# def hello_world():
#     return "<h1 style='text-align: center'>Hello, World!</h1><img src='https://media0.giphy.com/media/5TLkBMHcYgNeNPPvlK/giphy.gif?cid=ecf05e47zc2gfs50f4inzmf7lb1lw1yokixf2orn660r8vse&rid=giphy.gif&ct=g' width = 400>"

# #different path routes
# @app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underlined
# def say_bye():
#     return "<p>Goodbye</p>"

# @app.route('/<name>/<int:number>')        #turns website.com/josh into a usable variable
# def greet(name,number):
#     return f'Hello {name} , you are {number} years old.'


# if __name__ == '__main__':
#     app.run(debug=True)
    
    
    
# class User:
#     def __init__(self,name):
#         self.name = name
#         self.is_logged_in = False
        
# def decorator(function):
#     def wrapper(*args):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper

# @decorator
# def create_blog_post(user):
#     print(f"this is {user.name}'s new blog post")

# new_user = User('qhotti')
# new_user.is_logged_in = True
# create_blog_post(new_user)

#challenge 1:


# def logging_decorator(function):
#     def wrapper(*args):
#         t = function(*args)
#         print(f'You called {function.__name__}{args}')
#         print(f'It returned: {t}')
#     return wrapper


# @logging_decorator
# def thing(n1,n2):
#     return n1 + n2

# thing(1,2)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1> <img src='https://c.tenor.com/bZEUn3ywcQQAAAAd/stormcastle-count-down.gif' width = 500>"

number = random.randint(0,9)

@app.route('/<int:guess>')
def guess(guess):
    if guess > number:
        return "<h1 style='color:red'>Too high!</h1> <img src='https://media.giphy.com/media/igHg5yS08NvCwsvH0Z/giphy.gif' width = 500>"
    elif guess < number:
        return "<h1 style='color:blue'>Too low!</h1> <img src='https://media.giphy.com/media/xT39D0hEGnzxFDbHri/giphy.gif' width = 500>"
    else:
        return "<h1 style='color:green'>You did it!</h1> <img src='https://media.giphy.com/media/KQtInHuMoci6A/giphy.gif' width = 500>"


if __name__ == '__main__':
    app.run(debug=True)