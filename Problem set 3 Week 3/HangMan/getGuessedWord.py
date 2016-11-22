def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secretWord = secretWord.lower()
    list1 = []
    for i , a in enumerate( lettersGuessed):
        d=a.lower()
        list1.append(d)
    lettersGuessed = list1
    
    list5 = []
    for i , a in enumerate(secretWord):
        if secretWord[i] in lettersGuessed:
            b= secretWord[i]
            list5.append(b)
        else:
            b= '_'
            list5.append(b)
     
    return ' '.join(list5)
    
