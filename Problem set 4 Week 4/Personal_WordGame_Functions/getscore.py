def getscore(word , n):
    #word = raw_input("Enter a word ").lower() 
    SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
    scoresum = []
    for i , j in enumerate(word):
        if j in SCRABBLE_LETTER_VALUES.keys():
            scoresum.append(SCRABBLE_LETTER_VALUES[j])
    sum_word = sum(scoresum)*len(word)
    if len(word)== n:
        return sum_word + 50
    else:
        return sum_word            
            