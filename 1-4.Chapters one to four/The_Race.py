#The Race of a Tortoise and a Hare
'''Simulates the race of a tortoise and a hare in a 70-position meadow.'''

import random

def Tortoise():
    '''Returns the Turtle's movemenst'''
   
    movement = random.randrange(1,20) 
     
    if movement <= 5  : #Fast Plod
        return 3
    elif 5 < movement <= 7 : #Slip
        return -6
    elif 7 < movement <= 10 : #Slow plod
        return 1
    elif 10 < movement <= 12 : #Sleep
        return 0
    elif 12 < movement <= 14 : #Big Hop
        return 9
    elif 14 < movement <= 15 : #Big Slip
        return -12
    elif 15 < movement <= 17 : #Small Hop
        return 1
    else : #Small Slip
        return -2

def Hare():
    '''Returns the Hare's movements'''
    
    movement = random.randrange(1,20)
     
    if movement <= 5  : #Fast Plod
        return 3
    elif 5 < movement <= 7 : #Slip
        return -6
    elif 7 < movement <= 10 : #Slow plod
        return 1
    elif 10 < movement <= 12 : #Sleep
        return 0
    elif 12 < movement <= 14 : #Big Hop
        return 9
    elif 14 < movement <= 15 : #Big Slip
        return -12
    elif 15 < movement <= 17 : #Small Hop
        return 1
    else : #Small Slip
        return -2

#Initialization Phase
print('BANG!!!!!','AND THEY\'RE OFF!!!!!', sep= '\n')

tortoise_Square = 0  #Initialises the Turtle's position
hare_Square = 0  #initialises the Hare's position

for square in range(1,71) : #Creates the 70 positions of the race
        
   
#Processing Phase   
    print()
    while True: 
        #returns the round winner
        
        tortoise_Square += Tortoise() 
        hare_Square += Hare()

        if square in (tortoise_Square,hare_Square): #Check if there is a winner or a tie
                break
        else :
            tortoise_Square = hare_Square = square
               
        print( '|'*30,'-.'*15 ,sep= '\n') #Displays the path and the obstacles of the race
        
#Termination Phase   
    if  tortoise_Square == hare_Square :
       
        if square == 70 :
            while True : 
                #Breaks the tie in case it happens at the end of the race
                
                tortoise_Square += Tortoise()
                hare_Square += Hare()
        
                if square in (tortoise_Square,hare_Square): 
                    break
                
                else : 
                    tortoise_Square = hare_Square = square 
        
        else : #Shows the draw and gives the position to the tortoise. 
            print()
            print(f'{"-"*30:>13}')
            print(f'{"|     There is a tie!        |":>14}')
            print('~'*30)
            print(f'{"Square":>2}{" | tortoise |":>13}{" Hare   |":>11}')
            print('~'*30)
            print(f'''{square:>5}{" | I'll win |":>14}{" I'll win |":>11}''') 
            print(f'''{square:>5}{" | I'll win |":>14}{" OUCH!!! |":>11}''')
            print('~'*30)
    
    
    if square == tortoise_Square : 
        #If the tortoise won, shows the square and its position 
           
        print()
        print('~'*30)
        print(f'{"Square":>2}{" | tortoise |":>13}{" Hare   |":>11}')
        print('~'*30)
        print(f'''{square:>5}{" | I'll win |":>14}{"|":>11}''') 
        print('~'*30)
        
        
        if tortoise_Square == 70 : #Check if it's the winner of the race, and shows the result
            print('-'*25)
            print(f'|{"° Winner! °":>15}{"|":>10}')
            print('~'*25)
            print(f'|{" TORTOISE WINS!!! YAY!! ":>12}{"|":>1}')
            print('-'*25)
           


    
    elif square == hare_Square :
            #If the hare won, shows the square and its position
            print()
            print('~'*30)
            print(f'{"Square":>2}{" | tortoise |":>4}{" Hare   |":>11}')
            print('~'*30)
            print(f'''{square:>5}{"|":>3}{"| I'll win |":>22}''') 
            print('~'*30)
            

            if hare_Square == 70 : #Check if it's the winner of the race, and shows the result
                print('-'*25)
                print(f'|{"°Winner!°":>15}{"|":>10}')
                print('~'*25)
                print(f'|{" Hare Wins!!! YAY!! ":>22}{"|":>3}')
                print('-'*25)