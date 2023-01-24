#%%
#Prime Factorization 
'''Returns the divisors and prime factors of the number'''

#Initialization Phase
number = int(input('Enter the number to gets its divisors and prime factors: '))
numberD = number #Decomposition  of the number
divisors = [] #Divisors
factors = [] #Prime Factors
fac = 2     #Factor Initialisation

#Processing Phase
for n in range(1, number +1): #Obtaining The divisors
    if (number % n) == 0:
        divisors.append(n)
        
while numberD > 1 :   #Obtaining Prime Factors
   
    if numberD % fac == 0 :
            factors.append(fac)
            numberD //= fac
    else :
        fac += 1
            
#Termination Phase
print(f'The divisors of the number {number} are {divisors} and its prime factors {factors}')