#Perfect Number
'''Returns its divisors and determines if it is a Perfect Number '''

number = int(input('Enter the number: '))

divisors = []

for n in range(1, number +1):
    if (number % n) == 0:
        divisors.append(n)
        

if (sum(divisors) - number) == number:
    print(f'The number {number} is a perfect Number and these are its divisors {divisors}')
else :
    print(f'The number {number} is not a Perfect Number, these are its divisors {divisors}')