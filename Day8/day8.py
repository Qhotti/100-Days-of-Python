#def greet(name):
#    print('hello')
#    print('welcome to walgreens')
#    print('please leave')
#
#greet()
#
#
#def greet_with_name(name):
#    print(f'hello {name}')
#    print('welcome to walgreens ')
#    print('please leave ')
#    
#greet_with_name('kody')


#more than 1 input

#def greet_with(name, location):
#    print(f'Hello {name}')
#    print(f'What is it like in {location}? ')
#greet_with(name = 'kody' , location = 'poopville')

#challenge 1: paint can calc
#def paint_calc(height,width,cover):
#    result = round(test_h * test_w / coverage)
#    print(f"You'll need {result} cans of paint.")
#
#
#
#test_h = int(input("Height of wall: "))
#test_w = int(input("Width of wall: "))
#coverage = 5
#paint_calc(height=test_h, width=test_w, cover=coverage)

#Challenge 2: Prime Number calc

#def prime_checker(number):
#    is_prime = True
#    for i in range (2,number):
#        if number % i == 0:
#            is_prime = False
#    if is_prime:
#        print("It's a prime number.")
#    else:
#        print("It's not a prime number.")
#
#n = int(input("Check this number: "))
#prime_checker(number=n)


#final challenge: Caesar Cipher

from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
number = len(list(text))
def encrypt(t, s):
    cipher_text = ''
    for letter in t:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")
    

def decrypt(t, s):
    decipher_text = ''
    for letter in t:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        decipher_text += new_letter
    print(f"The decoded text is {decipher_text}")
    


if direction == 'encode':
    encrypt(t=text, s=shift)
else:
    decrypt(t=text, s=shift)






