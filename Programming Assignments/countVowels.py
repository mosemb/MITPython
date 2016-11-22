
def vowels(s):
    countvowel = 0
    for i in s:
       
        if i== 'a'or i=='e'or i=='i' or i=='o' or i=='u':
            countvowel +=1        
    
    return 'Number of vowels:'.replace("'","") + str(countvowel).replace("'","")               
            
            