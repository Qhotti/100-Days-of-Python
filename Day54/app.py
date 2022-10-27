import time
from flask import Flask
app=Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye") #when client goes to website/bye 'say goodbye'
def say_bye():
    return "<p>Goodbye</p>"

# def delay_decorator(function):   #function is say_hello()
#     def wrapper_function():
#         time.sleep(2)
#         #do something before
#         function()
#         #do something after
#     return wrapper_function

# @delay_decorator  #basically is decorated_function = delay_decorator(say_hello)
# def say_hello():
#     print('hello')
    
