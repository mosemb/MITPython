# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
import os

WORDLIST_FILENAME = 'C:\\Users\mose\\OneDrive\\Python MIT\\Problem set 3 Week 3\\HangMan\\words.txt'
#open('C:/Users/mose/OneDrive/Python MIT/Problem set 3 Week 3/HangMan.words.txt', 'r')
#'C:/Users/mose/OneDrive/Python MIT/Problem set 3 Week 3/HangMan.words.txt'

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    #inFile = os.open(WORDLIST_FILENAME, os.O_RDONLY)
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    
    
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

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
    
    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guesses = 8
    lettersGuessed = []
    lettercount = []
    lettercountProduct = []
    lettersinBoth = []
    sumletters = []

    
    countword = 0
    secretWord = chooseWord(wordlist)
   # letersum = sum(bytearray(stringproduct))
    secretwordsum = sum(bytearray(secretWord))
    #sumlett = sum(sumletters)
    
    print 'Welcome to the game Hangman!' 
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    #print secretWord
    #print  secretwordsum
    
    
    while guesses<=8 and guesses>=1 :
        print 'You have '+ str(guesses) + ' guesses left'
        print 'Available letters are '+ getAvailableLetters(lettersGuessed)
        letter = raw_input('Please Guess a letter ')
        
        #if letter == '':
            
        
        if letter not in lettersGuessed:
            lettersGuessed.append(letter)
        elif letter == '':
             print 'You entered nothing.'     
        else:
            print 'Letter already guesed'
            
      
        
        if letter in secretWord and letter in lettersGuessed:
            lettersinBoth.append(letter)           
    
        if letter in secretWord:
            t=secretWord.count(letter)
            lettercount.append(t)
            
            f=t*letter 
            g = f.split()  
             
            #lettersGuessed.append(letter)
        try:      
           if f not in lettercountProduct:
              lettercountProduct.append(f)
              dg = sum(bytearray(f))
              sumletters.append(dg)  
        except Exception:
             pass
           
                
                
        #print str(lettersGuessed) + ' ' + "Letters guessed "
       # print str(lettersinBoth) + ' ' + "Letters in both "
       # print  str(lettercount) + ' ' + 'Letter count'
       # print str(lettercountProduct)+ ' '+ 'Letter count product'
       # print str(sumletters)+ ' '+ 'sum letters ' 
        sumlet = sum(sumletters)
       # print sumlet
        
        
        
        if letter in secretWord and letter !='':
            print 'Good Guess ' + getGuessedWord(secretWord, lettersGuessed)
            guesses = guesses
            secretWord.count(letter) 
        elif letter not in secretWord:
            print 'Ooops that letter not in my word ' + getGuessedWord(secretWord, lettersGuessed)
            guesses -=1
            
           
            
        #if letter  not in getAvailableLetters(lettersGuessed):
            #lettersGuessed.remove(letter)
            #print 'Ooops you have already guessed that letter ' + getGuessedWord(secretWord, lettersGuessed)
             
        elif isWordGuessed(secretWord, lettersGuessed) ==True and guesses >=1:
            print 'Good Guess ' + getGuessedWord(secretWord, lettersGuessed)
            print 'Congs you have won'
            break
            
        #for i , bt in enumerate(lettercountProduct):
            
                 
             
        if guesses<1:
            print 'Sorry you have run out of guesses'
            print 'The word to guess was  '+ secretWord 
            break
            
       
            
        if sumlet == secretwordsum:
            print 'You have won'
            break
            
            
        
    #gt = getAvailableLetters(lettersGuessed) 
    #tr = getGuessedWord(secretWord, lettersGuessed)
    #tp = isWordGuessed(secretWord, lettersGuessed)
    
    
    


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

 #secretWord = chooseWord(wordlist).lower()
 #hangman(secretWord)
