def bobword(s):
    
    for i in s:
        a= s.count('bob',0,len(s))
    return  a
    
def bobword2(s2):
    count1 = 0
    sub = 'bob'
    lensub = len(sub)
    for i in range(len(s2)):
        if s2[i:i+lensub]==sub:
            count1+=1
    return count1        
                            