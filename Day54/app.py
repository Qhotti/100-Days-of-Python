# import time
# from flask import Flask
# app=Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/bye") #when client goes to website/bye 'say goodbye'
# def say_bye():
#     return "<p>Goodbye</p>"

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


#challenge 1
# import time
# current_time = time.time()

# def speed_calc_decorator(function):
#     def thing():
#         time1 = time.time()
#         function()
#         time2= time.time()
#         tt = time2 - time1
#         print(f'{function.__name__} run speed: {tt}')
#     return thing

# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i

# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i

# fast_function()
# slow_function()