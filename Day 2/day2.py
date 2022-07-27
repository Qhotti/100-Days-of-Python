# challenge 1: prints the sum of the two digit number

#two_digit_number = input("Type a two digit number: ")

#fn = two_digit_number[0]
#sn = two_digit_number[1]

#print(int(fn) + int(sn)) 


# Challenge 2: BMI calculator
#height = input("enter your height in m: ")
#weight = input("enter your weight in kg: ")
#
#nw = float(weight)
#nh = float(height)
#
#result = nw / (nh ** 2)
#
#print(int(result))





## Challenge 3: Your life in weeks calculator (kinda did it the hard way skull, easier way would be to do 90 years minus input then use that output times the days, months and years.)
#age = input("What is your current age?")
#
#
#td = 32850 
#tw = 4680
#tm = 1080
#
#d = int(age) * 365
#w = int(age) * 52
#m = int(age) * 12
#
#dr = int(td - d)
#wr = int(tw - w)
#mr = int(tm - m)
#
#print(f"You have {dr} days, {wr} weeks, and {mr} left.")


#FINAL Challenge: Tip Calculator

bill = float(input('How much was the bill? '))

split = int(input('How many people to split the bill? '))

tip = int(input('What percentage for the tip? '))

tip_percentage = (tip / 100) + 1

total = round((bill / split) * tip_percentage, 2)

print(f"Each person pays {total}. ")



