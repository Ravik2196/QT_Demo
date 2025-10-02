

import random


random_num = random.randint(1, 10)

def guess_number(random_number):
    num = int(input('Enter a number range between 1 to 10 : '))
    if num > random_number:
        print('You are close think little bit downwards ')
        guess_number(random_number)
    elif num < random_number:
        print('You are close think little bit upwards')
        guess_number(random_number)
    else:
        print('wonderful you have guessed it correctly')



guess_number(random_num)
