low=0
high = 99
middle = (high+low)//2

while True:
    print("Enter the first number: In the range 0 to 99 ") 
    x=int(raw_input())
    
    if x<0:
        print ('Too small')
    elif x>=100:
        print ("Too big, try again")
    else:
        break
while True:
    print ("Is your number " + str(middle))
    y=raw_input("Enter letter 'h' to represent high.Enter letter 'l' to represent low.Enter letter 'c' to represent correct. Otherwise sytem will stay in loop ")
    #middle = (high+low)//2

    
    if y=='h':
        high = middle
        middle = (high+low)//2
    elif y=='l':
        low = middle
        middle = (high+low)//2
    elif y=='c':
        print("Game over. Your secret number was: "+str(middle))
        break
    else:
        print "Sorry we do not get it"
        middle = (high + low)//2
                
            
    
            