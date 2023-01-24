
#%%

for row in range(11):

    for column in range(row):
        print('*' , end='')

    print()

print()
for r in range(11,0,-1) :
    
    for colum in range(r):
            print('*',end= '')
    print()

for t in range(11):
    print((' '*t) + ('*' *(11-t)))


for t in range(11,0,-1):
    print((' ' *t) + ('*' *(11-t)))
print('\n')

for row in range (1,11):
    
    for two in range (0,row) :
        print('*' ,end= '')
    for space in range(0,11-row):
            print(' ', end='')
    
    for colum in range(0,11-row):
        print('*' ,end= '')

    for space in range(0,2*row):
            print(' ', end='')
    
    for two in range (0,11-row) :
        print('*',end= '')
    
    for space in range(0,11-row):
            print(' ', end='')
    
    for colum in range(0,row):
        print('*' ,end= '')
    print()