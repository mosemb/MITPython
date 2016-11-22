epsilon = 0.01
numGuesses= 0
low = 0.0
while True:
    print("Enter the first number: ") 
    x=int(raw_input())
    
    if x<0:
        print ('Too small')
    elif x>=100:
        print ("Too big, try again")
    else:
        print 'acceptable'
        break
           
high = x
ans= (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))


    
          
          
                      
        