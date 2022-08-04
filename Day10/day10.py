#functions with outputs

#def format_name(f_name, l_name):
#    formated_f_name = f_name.title()
#    formated_l_name = l_name.title()
#    
#    return (f'{formated_f_name} {formated_l_name}')
#
#formated_string = format_name('kody', 'pudney')
#
#print(formated_string)


#multiple return

#def format_name(f_name, l_name):
#    if f_name == '' or l_name == '':
#        return
#
#    formated_f_name = f_name.title()
#    formated_l_name = l_name.title()
#    
#    return (f'Result: {formated_f_name} {formated_l_name}')
#
#formated_string = format_name(input('what is your first name? '), input('what is your last name? '))
#
#print(formated_string)

#challenge 1: Days in Month calc
#def is_leap(year):
#    if year % 4 == 0:
#        if year % 100 == 0:
#            if year % 400 == 0:
#                return True
#            
#            else:
#                return False
#        else:
#            return True
#    else:
#        return False
#
#def days_in_month(user_year, user_month):
#  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#  
#  if is_leap(year) and user_month == 2:
#        return 29
#  else:
#    return (month_days[user_month - 1])  
#
#year = int(input("Enter a year: "))
#month = int(input("Enter a month: "))
#days = days_in_month(year, month)
#print(days)
#

#Final Challenge: Calculator
from art import logo

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    '+': add,
    '-': sub,
    '*': multiply,
    '/': divide,
}
def calculator():
    print(logo)
    
    
    num1 = float(input('Whats the first number?: '))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input('Pick an operation: ')
        num2 = float(input('Whats the next number?: '))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        if input(f'Type "y" to continue calculating with {answer}: or type n to start a new calculation: ') == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()