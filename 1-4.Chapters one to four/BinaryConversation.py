#Binary Conversation
'''Converts a decimal number to binary'''

#Initialition Phase
number = int(input('Enter the decimal number: ')) 
num = number #Number Decomposition
conver = [] #Conversion of the number

#Processing Phase
while True :
    
    if num > 1 :
       
        conver += [num % 2]
        num //= 2
        
    else :
        conver.append(num)
        conver.reverse()
        break

#Termination Phase
print(f'The number {number} is in binary {conver}')
print(bin(number))