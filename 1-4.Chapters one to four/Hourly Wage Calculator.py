#Hourly Wage Calculator

while True :
    old_Hourly_wage = int(input('Enter the hourly wage: '))
    porcentage =  int(input('Enter the increasing or decreasing percentage per year: '))
    year = int(input('Enter intruduce the years: '))
                                
    for Year in range(1,year + 1):
        new_Hourly_Wage = old_Hourly_wage * (1 + porcentage / 100) ** Year

        print(f'{new_Hourly_Wage:.2f}')
    
    
    question = input('Other Operations? \n(y/n)--> ') 
    
    if question == 'n' : break 
    
    print('OK')