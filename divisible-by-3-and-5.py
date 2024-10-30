x = int ( input ("Enter a number: ") ) #ask the user to enter x

for i in range (x+1):
    if ( i % 3 == 0 and i % 5 == 0): #check if the nb is divisible by both 3 and 5
        print( i ," is divisible by both 3 and 5 ") #print the nb