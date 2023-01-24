#%%
#Fibonacci Sequence
'''retuns the fibonacci sequence of an input number'''

#Initializion Phase
number= int(input('Enter the number--> '))

fibonnaci = [0,1]
primer_D, second_D = 0 , 1
 
#Processing Phase
for f in range(1,number):
    
    adds = primer_D + second_D
    primer_D, second_D = second_D, adds
    
    fibonnaci.append(second_D) 
    
    
 #Termination Phase   
print(fibonnaci)