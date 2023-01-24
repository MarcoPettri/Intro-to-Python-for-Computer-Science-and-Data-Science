'''The game randomly selects two numbers between 1 and 10.
    It display the selected numbers and asks the player for the product of both numbers'''

from random import randrange

#Initialization Phase
print('Welcome the multiplication Game')
count = 0 #Correct answers count
while True:
    
    first_integer, second_integer = randrange(1,11), randrange(1,11)
    
#Processing Phase
    print('\n-1 to get out of the game')
    question = int(input(f'what is the product of {first_integer} and {second_integer}? --> '))

#Termintation Phase    
    if question == -1 :
        print(f'You have scored {count} hits')
        print('See you soon!')
        break
    elif question == (first_integer * second_integer) :
        print(f'Your answer is correct the result is {first_integer * second_integer}')
        count += 1
    else:
        print(f'Incorrect,the result of the multiplicaction is {first_integer * second_integer}')
            
