#Eggs_Per_Box
''' Place eggs in box, determine the amount of box used 
   and how many eggs would be missing to complete the egg collection'''

 
def eggsInBox() :
 
 ''' Place eggs in box, determine the amount of box used 
   and how many eggs would be missing to complete the egg collection'''

 print('Welcome!')
 
 while True :
  
  #Initialization Phase
  eggs = int(input('Enter the number of eggs to see how many boxes you need to store: '))
  array, boxEggs = [] , []
  missing , count = 6 , 0
  
  #Processing Phase
  for i in range (eggs) :
    array.append(i+1)
     
    if (len(array) % 6) == 0 :
         boxEggs.append([1,2,3,4,5,6])
         missing = 0
         count = 0
    else :
        missing -=  1
        count += 1
        if missing == -1 :
           missing = 5

 #Termination Phase      
  print('Egg cartons ',boxEggs,'\n',
       'The total number of full boxes are', len(boxEggs),'\n',
       'To complete the box,the following are missing = ',missing,'\n',
       'There were',count, 'eggs left in an unfilled carton.')
  
  Conditional = input('''Which of the following would you  like to know?
    A)Another Operation 
    B)Exit the application 
     --> ''')
  
  if  Conditional in ('a','A') :
       pass
  
  else :
        break

 return 'See you later!'


print(eggsInBox())
