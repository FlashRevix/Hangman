"""
PSEUDOCODE 1: text --> outline

Step 1) import dictonary as data set
Step 2) create function to print hangman board, randomly pick word from dictonary
Step 3) take guesses from player 
Step 4) compute their input, print if right or hang if wrong, let them know if they win or lose

PSEUDOCODE 2: flow chart with symbols 
input -> 

PSEUDOCODE 3: 

previousGuesses = []
correctGuesses=[]
word = dataset[random(len(dataset)+1)]
for i in word:
    print("_")
tempGuess = input("Type in a letter")
for i in word:
    if tempGuess = word[i]:
        correct
        

Input guess


def updateWord(Str, word)

def printLayout(Str word, )
    for i in word
        
        print("_")
    
"""
previousGuesses = []
correctGuesses= []
hanger = [7][6]
word = dataset[random(len(dataset)+1)]

for i in word:
    print("_")

tempGuess = input("Type in a letter")
for i in word:
    if tempGuess == word[i]:
        correctGuesses.append(tempGuess) 
    previousGuesses.append(tempGuess)  

def updateWord(Str, word)

def printHanger(hanger):
    hanger[0][1] = "-"
    hanger[0][2] = "-"
    hanger[0][3] = "-"
    hanger[0][4] = "-"
    hanger[1][1] = "|"
    hanger[1][4] = "|"
    hanger[2][4] = "|"
    hanger[3][4] = "|"
    hanger[4][4] = "|"
    hanger[5][4] = "|"
    hanger[6][1] = "-"
    hanger[6][2] = "-"
    hanger[6][3] = "-"
    hanger[6][4] = "-"
    hanger[6][5] = "-"

    if 