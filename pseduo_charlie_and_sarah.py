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
import random
import pandas as pd
import csv

#dataSet = pd.read_csv('https://github.com/pkLazer/password_rank/blob/master/4000-most-common-english-words-csv.csv')
with open('/Users/charlie/Downloads/4000-most-common-english-words-csv.csv',newline ='') as f:
    reader = csv.reader(f)
    global data 
    data = list(reader)


#data = ["charlie"]
wordSkeleton = []
previousGuesses = []
hanger = [[' ' for _ in range(6)] for _ in range(7)]
rows = len(hanger)
cols = len(hanger[0])
wordSelected = str(data[random.randrange(len(data))]).replace("[","").replace("]","").replace("'","")
numWrongGuesses = 0
gameOver = False

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

    if numWrongGuesses == 0:
        print(" ", hanger[0][1], hanger[0][2], hanger[0][3], hanger[0][4])
        print(" ",hanger[1][1], "  ", hanger[1][1])
        print("      ", hanger[1][4])
        print("      ", hanger[2][4])
        print("      ", hanger[3][4])
        print("      ", hanger[4][4])
        print("      ", hanger[5][4])
        print(hanger[6][1], hanger[6][2], hanger[6][3], hanger[6][4], hanger[6][5])

    elif numWrongGuesses == 1:
        hanger[2][1] = 'O'

        print(" ", hanger[0][1], hanger[0][2], hanger[0][3], hanger[0][4])
        print(" ", hanger[1][1], "  ", hanger[1][1])
        print(" ", hanger[2][1],"  ", hanger[1][4])
        print("      ", hanger[2][4])
        print("      ", hanger[3][4])
        print("      ", hanger[4][4])
        print("      ", hanger[5][4])
        print(" ", hanger[6][1], hanger[6][2], hanger[6][3], hanger[6][4], hanger[6][5])

    elif numWrongGuesses == 2:
        hanger[3][1] = '|'
        hanger[4][1] = '|'


        print(" ", hanger[0][1], hanger[0][2], hanger[0][3], hanger[0][4])
        print(" ", hanger[1][1], "  ", hanger[1][1])
        print(" ", hanger[2][1],"  ", hanger[1][4])
        print(" ", hanger[3][1],"  ", hanger[2][4])
        print(" ", hanger[4][1],"  ", hanger[3][4])
        print("    ",hanger[5][1], hanger[4][4])
        print("      ", hanger[5][4])
        print(" ", hanger[6][1], hanger[6][2], hanger[6][3], hanger[6][4], hanger[6][5])
    
    elif numWrongGuesses == 3:
        hanger[3][0] = '\\'

        print(" ", hanger[0][1], hanger[0][2], hanger[0][3], hanger[0][4])
        print(" ", hanger[1][1], "  ", hanger[1][1])
        print(" ",hanger[2][1],"  ", hanger[1][4])
        print(hanger[3][0], hanger[3][1],"  ", hanger[2][4])
        print(" ",hanger[4][1],"  ", hanger[3][4])
        print("      ", hanger[4][4])
        print("      ", hanger[5][4])
        print(" ",hanger[6][1], hanger[6][2], hanger[6][3], hanger[6][4], hanger[6][5])

    elif numWrongGuesses ==4:
        hanger[3][2] = '/'
        
        print(" ", hanger[0][1], hanger[0][2], hanger[0][3], hanger[0][4])
        print(" ", hanger[1][1], "  ", hanger[1][1])
        print(" ",hanger[2][1],"  ", hanger[1][4])
        print(hanger[3][0], hanger[3][1],hanger[3][2],"", hanger[2][4])
        print(" ",hanger[4][1],"  ", hanger[3][4])
        print("      ", hanger[4][4])
        print("      ", hanger[5][4])
        print(" ",hanger[6][1], hanger[6][2], hanger[6][3], hanger[6][4], hanger[6][5])
       

    elif numWrongGuesses == 5:
        hanger[5][0] = '/'

        print(" ", hanger[0][1], hanger[0][2], hanger[0][3], hanger[0][4])
        print(" ", hanger[1][1], "  ", hanger[1][1])
        print(" ",hanger[2][1],"  ", hanger[1][4])
        print(hanger[3][0], hanger[3][1], hanger[3][2],"", hanger[2][4])
        print(" ",hanger[4][1],"  ", hanger[3][4])
        print("      ", hanger[4][4])
        print(hanger[5][0],"    ", hanger[5][4])
        print(" ",hanger[6][1], hanger[6][2], hanger[6][3], hanger[6][4], hanger[6][5])

    elif numWrongGuesses == 6:
        hanger[5][2] = '\\'

        print(" ", hanger[0][1], hanger[0][2], hanger[0][3], hanger[0][4])
        print(" ", hanger[1][1], "  ", hanger[1][1])
        print(" ",hanger[2][1],"  ", hanger[1][4])
        print(hanger[3][0], hanger[3][1], hanger[3][2],"", hanger[2][4])
        print(" ",hanger[4][1],"  ", hanger[3][4])
        print("      ", hanger[4][4])
        print(hanger[5][0]," ",hanger[5][2],"", hanger[5][4])
        print(" ",hanger[6][1], hanger[6][2], hanger[6][3], hanger[6][4], hanger[6][5])

def checkIfGameOver():
    lettersRemaining = len(wordSelected)
    for value in wordSkeleton:
        if value != "_":
            lettersRemaining -= 1
    if lettersRemaining == 0:
        print("You win")
        exit()
    if numWrongGuesses > 5:   
         print(f"You lose, the word was {wordSelected}")
         exit()
    

def guessAndCheck():
    goodGuess = False
    shouldAppend = True
    index = 0
    _letterGuess = input("Type in a letter: ").lower()
    for guess in previousGuesses:
        if _letterGuess == guess:
            guessAndCheck()
            shouldAppend = False
            return
    if len(_letterGuess) > 1:
        guessAndCheck()
        shouldAppend = False
    if _letterGuess.isdigit() == True:
        guessAndCheck()
        shouldAppend = False
    for letter in wordSelected:
        if _letterGuess == letter:
            wordSkeleton[index] = letter
            goodGuess = True
        index += 1
    if not goodGuess:
        global numWrongGuesses
        numWrongGuesses += 1
    if shouldAppend == True:
        previousGuesses.append(_letterGuess)  
    print(wordSkeleton)
    print("Previous Guesses: ",previousGuesses)
    print(numWrongGuesses)

def setup():
    for letter in wordSelected:
        wordSkeleton.append("_")

setup()
while not gameOver:
     checkIfGameOver()
     guessAndCheck()
     printHanger(hanger)
     
         

