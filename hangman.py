import random
import csv
import PySimpleGUI as sg


with open('/Users/charlie/Downloads/4000-most-common-english-words-csv.csv',newline ='') as f:
    reader = csv.reader(f)
    global data 
    data = list(reader)

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
    global gameOver
    lettersRemaining = len(wordSelected)
    for value in wordSkeleton:
        if value != "_":
            lettersRemaining -= 1
    if lettersRemaining == 0:
        print("You win")
        gameOver = True
    if numWrongGuesses > 5:   
         print(f"You lose, the word was {wordSelected}")
         gameOver = True
    
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
        return
    if _letterGuess.isdigit() == True:
        guessAndCheck()
        shouldAppend = False
        return
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

def setup():

    for letter in wordSelected:
        wordSkeleton.append("_")
        print("_", end=" ")
    print()

setup()
while not gameOver:
     checkIfGameOver()
     if not gameOver:
        guessAndCheck()
        printHanger(hanger)
        for value in wordSkeleton:
            print(value, end=' ')
        print()
        for guess in previousGuesses:
            print(guess, end = " ")
        print()
     elif gameOver:
         exit()

##LAST LICK MINI GAME
         

