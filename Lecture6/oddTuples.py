def oddTuples(aTup):
    tup = ()
    for i ,a in enumerate(aTup):
        if (i+1)%2 !=0:
            tup = tup +(a,)
    return tup
    
    #[:len(tup)+1]
           
            
    
            