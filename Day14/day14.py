import random
from game import data
from logo import logo, vs

person_1 = {}
person_2 = {}
score = 0
def random_people(): #generates random person from list
    person_1.clear()
    person_1.update(random.choice(data))
    person_2.clear()
    person_2.update(random.choice(data))


def compare():
    if person_1['follower_count'] > person_2['follower_count']:
        return 'A'
    else:
        return 'B'




def game():
    game_active = True
    
    while game_active == True:
        
        random_people()
        compare()
        print(logo)
        print('Compare A:', person_1['name'] + ',','a', person_1['description'] + ',', 'from', person_1['country'] + '.')
        print(vs)
        print('Compare B:', person_2['name'] + ',','a', person_2['description'] + ',', 'from', person_2['country'] + '.')
        user_input = input('Who has more followers? A or B: ')
        if user_input == compare():
            global score
            score += 1
            print(f'Correct! Current score: {score}')
            game()
        else:
            game_active = False
            print(f'Sorry but that is incorrect. Final score: {score}')
            exit()
            
game()        


    


