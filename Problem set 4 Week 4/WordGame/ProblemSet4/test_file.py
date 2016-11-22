word = "vie"
WORDLIST_FILENAME = 'C:\\Users\\mose\\OneDrive\\Python MIT\\Problem set 4 Week 4\\WordGame\\ProblemSet4\\words.txt'
hand = {'i': 1, 'n': 1, 'e': 1, 'l': 2, 'v': 2}
#wordList = ['bul', 'bulls', 'chi']

inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
wordList = []
for line in inFile:
    wordList.append(line.strip().lower())
    
list1 = []
for i in word:
    if i not in hand.keys():
        list1.append(False)
    else:
        list1.append(True)
anded_list1 = all(list1)

print list1 , anded_list1, word in wordList

list2= []
list2.append(anded_list1)
list2.append(word in wordList)

print list2 
print all(list2)
print sum (hand.values()) 





         
             
        
