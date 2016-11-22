import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    stu = string.ascii_lowercase
    
    list1 = []
    for i , a in enumerate( lettersGuessed):
        d=a.lower()
        list1.append(d)
    lettersGuessed = list1
    
    list5 = []
    for i , a in enumerate(stu):
        if stu[i] in stu:
            list5.append(stu[i])

    for i in stu:
        if i in lettersGuessed:
            list5.remove(i)
            
    b2 =''.join(list5)
    
    return b2 
    
    
    
    
    
    
    
    
    
