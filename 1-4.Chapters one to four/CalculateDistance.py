#Calculate Distancia
'''Display the difference in distance between the world record
    and the athlete's current jump distance 
    in meters,decimeters,centimeters and millimeters'''

while True :
    
    #Initilaization Phase
    wordRecord = 8.85 #wordl record jumping
    athlete = float(input('Enter the athlete\'s jump distance in metres: '))
    difference = wordRecord - athlete

    #Processing Phase
    meters = (difference/1) * (10**3 /10**3) 
    decimeters = (difference/1) * (10**4 /10**3) #Converion from metres to decimetres
    centimeters = (difference/1) * (10**5 /10**3) #conversion from metres to centimetres
    millimeters = (difference/1) * (10**6 /10**3) #conversion from metres to millimetres

    #Termination Phase
    print(f'You need to jump: {difference:.1f} additional meters to improve the world record.')
    print(f'Meters= {meters:.1f} \nDecimeter= {decimeters:.1f} \nCentimeters= {centimeters:.1f} \nMillimeters= {millimeters:.1f}')
    
    question = input('wants to ake another conversion(y/n): ')
    
    if question in ('y','Y') :
        pass
    else :
        print('see you later')
        break