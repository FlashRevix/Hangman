import random
import csv
import os

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
hasLastLick = True

def startMiniGame():
    global numWrongGuesses
    global gameOver 
    guess = input("Let's flip a coin. Heads or tails? (h/t) ")
    _num = random.randrange(1,3)
    coinFlipStatus = ""
    if _num == 1:
        coinFlip = 'h'
        coinFlipStatus = "heads"
    elif _num == 2:
        coinFlip = 't'
        coinFlipStatus = "tails"
    if guess == coinFlip:
        numWrongGuesses -= 1
        gameOver = False
        printHanger(hanger)
        for value in wordSkeleton:
            print(value, end=' ')
        print()
        for guess in previousGuesses:
            print(guess, end = " ")
        print()
        startGame()
    else:
        print(f"You lose, it was {coinFlipStatus}, and the word was {wordSelected}")
        exit()
    
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
        if hasLastLick:
            print("You lose, but here is one last try")
        else:
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
    for _ in wordSelected:
        wordSkeleton.append("_")
        print("_", end=" ")
    print()

def startGame():
    global numWrongGuesses
    global hasLastLick
    while not gameOver:
        checkIfGameOver()
        if not gameOver:
            guessAndCheck()
            os.system('clear')
            printHanger(hanger)
            for value in wordSkeleton:
                print(value, end=' ')
            print()
            for guess in previousGuesses:
                print(guess, end = " ")
            print()
        elif gameOver and hasLastLick and numWrongGuesses > 5:
            hasLastLick = False
            startMiniGame()
        else:
            exit()

            
setup()
startGame()

