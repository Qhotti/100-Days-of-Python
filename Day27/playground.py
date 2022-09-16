#def add(*args):        #unspecified amount of inputs
#    
#    print(args[0])      # first in line
#    total = 0
#    for n in args:
#        total += n
#    return total
#        
#print(add(4,5,6,9,14,15,19,42))
#
#
#def calculate(n,**kwargs):            #turns into a dictionary
#    print(kwargs)
#    # for key,value in kwargs.items():
#    #     print(key)
#    #     print(value)
#    n+= kwargs['add']
#    n*= kwargs['multiply']
#    print(n)
#    
##calculate(add=3, multiply = 5)
#calculate(2,add=3, multiply = 5)

class Car:
    def __init__(self,**kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.seats = kw.get('seats')
        self.color = kw.get('color')
        
my_car = Car(make = 'nissan', seats = 4, color = 'fortnite')
print(my_car.color)
        