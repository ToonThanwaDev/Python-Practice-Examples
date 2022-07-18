# Roll Dice Game
# 1,2,3,4,5,6

import random
# Enter the dice number
myrandom = random.randrange(1, 7) # 1-6
k = 1
correct = False

while True:
    number = int(input('Put your answer: '))
    correct = (number == myrandom) # true / false
    
    if not correct:
        if (number > myrandom):
            print('less than')
        if (number < myrandom):
            print('more than')
    if correct:
        print('You got 100,000 BATH')
        break
    if number < 0 or k == 3:
        break
    k += 1

if not correct:
    print('Sorry you lose')
    print('Answer =', myrandom)