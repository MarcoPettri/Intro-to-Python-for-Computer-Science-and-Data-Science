#Inter Values of characters 

'''Adds up the integer values of the characters 
    and compares them'''

StringOne, StringTwo = list(input('Input String one --> ')), list(input('Input String two --> '))
arrayTwo, arrayOne = [], []

 
for i in StringOne :
      value = ord(i)
      arrayOne.append(value)
      
for t in StringTwo :
      value = ord(t)
      arrayTwo.append(value)


if sum(arrayOne) > sum(arrayTwo) :
      print('String One is greater\n','String One\t','String Two \n',
      sum(arrayOne),'\t    >  \t ',sum(arrayTwo))
elif sum(arrayTwo) > sum(arrayOne):
      print('String Two is greater\n','String Two\t','String One \n', 
      sum(arrayTwo),'\t    >  \t ',sum(arrayOne))
else:
      print ('Both are equal\n','String One\t','String Two \n', 
      sum(arrayOne), ' \t    =  \t ',sum(arrayTwo))