def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    secretWord = secretWord.lower()
    list1 = []
    for i , a in enumerate( lettersGuessed):
        d=a.lower()
        list1.append(d)
    lettersGuessed = list1
    
    #print lettersGuessed 
    
    list5 = []
    for i , a in enumerate(secretWord):
        if secretWord[i] in lettersGuessed:
            b= True
            list5.append(b)
        else:
            b=False
            list5.append(b)
    gu = all(list5)  
    return gu 

        
