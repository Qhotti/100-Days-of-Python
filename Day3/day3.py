#basic if and else 

#print('Welcome to the rollercoaster!')
#height = int(input('What is your height in cm?'))
#
#if height >= 120:
#    print('go in da rollercoaster G')
#else:
#    print('hit the gym and get taller')


#Challenge 1: Is this number even or odd?

#number = int(input("Which number do you want to check? "))
#
#remainder = number % 2
#
#if remainder >= 1:
#    print('this number is odd')
#else:
#    print('this number is even')

# More advance roller coaster
#print('Welcome to the rollercoaster!')
#height = int(input('What is your height in cm? '))
#
#if height >= 120:
#    print('go in da rollercoaster G')
#    age = int(input('What is your age? '))
#    if age < 12:
#        print('pay me $5')
#    elif age <= 18:
#        print('you owe $7')
#    else:
#        print('you owe $12')
#else:
#    print('hit the gym and get taller')



#Challenge 2: BMI Calculator 2

#height = float(input("enter your height in m: "))
#weight = float(input("enter your weight in kg: "))
#result = round(weight / (height ** 2))
#
#if result <= 18.5:
#    print(f"Your BMI is {result} and you're underweight. Get some gains at the gym.")
#elif result <= 25:
#    print(f"Your BMI is {result} and you are average weight. 👍🏼")
#elif result <= 30:
#    print(f"Your BMI is {result} and you are slightly overweight. 🤷🏼‍♂️")
#elif result <= 35:
#    print(f"Your BMI is {result} and you are obese. 😬")
#else:
#    print(f"Your BMI is {result} and you are clinically obese. GG ")

#Challenge 3: Leap year Calculator, kinda rough but it works with 100% accuracy.

#year = int(input("Which year do you want to check? "))
#
#leap1 = year % 4
#leap2 = year % 100
#leap3 = year % 400
#
#check1 = leap1 % 2
#check2 = leap2 % 2
#check3 = leap3 % 2
#
#if leap1 == 0:
#    if check1 == 0:
#        if check2 == 0:
#            if check3 == 0:
#                print('it is a leap year')
#else:
#    print('not a leap year')

#better version of this (supplied by teach)

#year = int(input("Which year do you want to check? "))
#
#if year % 4 == 0:
#    if year % 100 == 0:
#        if year % 400 == 0:
#            print('Leap year')
#        else:
#            print('not leap year')
#    else:
#        print('leap year')
#else:
#    print('leap year')


##rollercoaster with picture bill
#print('Welcome to the rollercoaster!')
#height = int(input('What is your height in cm? '))
#
#bill = 0
#
#if height >= 120:
#    print('go in da rollercoaster G')
#    age = int(input('What is your age? '))
#    if age < 12:
#        bill = 5
#        print('child tickets are $5')
#    elif age <= 18:
#        bill = 7
#        print('youth tickets are $7')
#    else:
#        bill = 12
#        print('adult tickets are $12')
#    wants_photo = input(' Do you want a photo? Y or N.')
#    if wants_photo == "Y" or "y":
#        bill += 3
#    
#    
#    print(f'Your final bill is {bill}')
#        
#        
#
#else:
#    print('hit the gym and get taller')
#
#

# Pizza price calc. Works good but could be simplified.
#print("Welcome to Python Pizza Deliveries!")
#size = input("What size pizza do you want? S, M, or L ")
#add_pepperoni = input("Do you want pepperoni? Y or N ")
#extra_cheese = input("Do you want extra cheese? Y or N ")
#
#bill = 0
#
#if size == "S":
#    bill += 15
#    if add_pepperoni == "Y":
#        bill += 2
#    if extra_cheese == "Y":
#            bill += 1
#
#elif size == "M":
#    bill += 20
#    if add_pepperoni == "Y":
#            bill += 3
#    if extra_cheese == "Y":
#            bill += 1
#elif size == "L":
#    bill += 25
#    if add_pepperoni == "Y":
#            bill += 3
#    if extra_cheese == "Y":
#            bill += 1
#print (f'Your final bill is: ${bill}')     

# roller coaster but with mid life crisis 💀
#print('Welcome to the rollercoaster!')
#height = int(input('What is your height in cm? '))
#
#bill = 0
#
#if height >= 120:
#    print('go in da rollercoaster G')
#    age = int(input('What is your age? '))
#    if age < 12:
#        bill = 5
#        print('child tickets are $5')
#    elif age <= 18:
#        bill = 7
#        print('youth tickets are $7')
#    elif age >= 45 and age <= 55:
#        bill = 0
#        print('You are having a midlife crisis! You get free tickets!')
#    else:
#        bill = 12
#        print('adult tickets are $12')
#    wants_photo = input(' Do you want a photo? Y or N.')
#    if wants_photo == "Y":
#        bill += 3
#    
#    
#    print(f'Your final bill is {bill}')
#        
#        
#
#else:
#    print('hit the gym and get taller')

#love calculator
#print("Welcome to the Love Calculator!")
#name1 = input("What is your name? \n")
#name2 = input("What is their name? \n")
#
#lowercase_name12 = name1 + name2
#lowercase_names = lowercase_name12.lower()
#
#t = lowercase_names.count('t')
#r = lowercase_names.count('r')
#u = lowercase_names.count('u')
#e = lowercase_names.count('e')
#
#l = lowercase_names.count('l')
#o = lowercase_names.count('o')
#v = lowercase_names.count('v')
#e = lowercase_names.count('e')
#
#true = str(t + r + u + e)
#love = str(l + o + v + e)
#
#truelove = int(true + love)
#
#if truelove < 10 or truelove > 90:
#    print (f"Your score is {truelove}, you go together like coke and mentos.")
#elif truelove > 40 or truelove < 50:
#    print (f"Your score is {truelove}, you are alright together.")
#else:
#    print(f'Your score is {truelove}')
#

#Final Challenge: Adventure game. I had lots of fun with this one.
print('''
                    ..oo$00ooo..                    ..ooo00$oo..
                .o$$$$$$$$$'                          '$$$$$$$$$o.
             .o$$$$$$$$$"             .   .              "$$$$$$$$$o.
           .o$$$$$$$$$$~             /$   $\              ~$$$$$$$$$$o.
         .{$$$$$$$$$$$.              $\___/$               .$$$$$$$$$$$}.
        o$$$$$$$$$$$$8              .$$$$$$$.               8$$$$$$$$$$$$o
       $$$$$$$$$$$$$$$              $$$$$$$$$               $$$$$$$$$$$$$$$
      o$$$$$$$$$$$$$$$.             o$$$$$$$o              .$$$$$$$$$$$$$$$o
      $$$$$$$$$$$$$$$$$.           o{$$$$$$$}o            .$$$$$$$$$$$$$$$$$
     ^$$$$$$$$$$$$$$$$$$.         J$$$$$$$$$$$L          .$$$$$$$$$$$$$$$$$$^
     !$$$$$$$$$$$$$$$$$$$$oo..oo$$$$$$$$$$$$$$$$$oo..oo$$$$$$$$$$$$$$$$$$$$$!
     {$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$}
     6$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$?
     '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
      o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o
       $$$$$$$$$$$$$$;'~`^Y$$$7^''o$$$$$$$$$$$o''^Y$$$7^`~';$$$$$$$$$$$$$$$
       '$$$$$$$$$$$'       `$'    `'$$$$$$$$$'     `$'       '$$$$$$$$$$$$'
        !$$$$$$$$$7         !       '$$$$$$$'       !         V$$$$$$$$$!
         ^o$$$$$$!                   '$$$$$'                   !$$$$$$o^
           ^$$$$$"                    $$$$$                    "$$$$$^
             'o$$$`                   ^$$$'                   '$$$o'
               ~$$$.                   $$$.                  .$$$~
                 '$;.                  `$'                  .;$'
                    '.                  !                  .`  ''')

print("Welcome to Gotham.")

path1 = input('You are walking down a sketchy ally and you see some dudes ahead of you. They approach you and demand you give up your wallet. Do you give them your money(1) or do you run past them?(2) ')

if path1 == '1':
    print('They rip the wallet from your hands and shoot you. GAME OVER')
    exit()

else:
    print('Little did they know, You were the fastest kid at school. You blast past them and lose them.')
    
path2 = input('You slow down to catch your breath and you notice a tall black figure beating down an old woman. You approach to assess the situation further. Its batman. The old lady was loitering for longer than 10 mins as stated by the sign. Do you mind your business(1) or do you step in and help the old woman?(2) ')

if path2 == '1':
    print('You walked away. Good choice.')
else:
    print('You ask batman to give the lady a break. Batman stops and looks over at you. he says "looks like you have been loitering around here as well." Before you could rebuttal, Batman runs at you at full speed and you combust into a red mist. GAME OVER')
    exit()
path3 = input('You think youve had enough for tonight so you head home. You approach a crosswalk. Do you hit the button and wait several minutes to cross the intersection (1), J walk (2) J run(3) ')

if path3 == '1':
    print('You wait around 5 minutes and cross. Home sweet home. You fly into bed, clothes falling off your body midair. Staring at the ceiling, gunshots and sirens going off outside your home. You start thinking about how rent is exceeding 3k even in this neighborhood. You remember that your wife left you for a richer man. You remember that you are balding. These thoughts keep you up so you decide to go watch some youtube to remove the bad thoughts. You sit down in your chair and your computer is gone. Your desk is even on bricks like a car with no tires.   YOU WIN?')
elif path3 == '2':
    print('You look both ways and see no cars. You walk across the street. The street light behind you casts a shadow in the shape of the bat symbol. Its the final thing you see before Batman steps on your head, killing you instantly. GAME OVER')
else:
    print('You have enough strength left to run at peak speed. Meanwhile, a man driving faded Nissian Altima reached peak speed as well and hit you full speed, a red mist falls onto the only thing that remains of yours, your adidas.')
    
print('Thanks for playing.')