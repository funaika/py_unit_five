#random number guessing game
#kalen funai
#11/06/2023

import random
def getNumber():
    '''
    the function generates a random number 1-100
    :return: random number 1-100
    '''
    randomNumber = random.randint(1,100)                  #generates random number
    return randomNumber                                         #returns random number



def getGuess():
    '''
    this function gets the users guess of the number
    :return: users guess
    '''
    while True:
        try:
            userGuess = int(input("Guess an number 1-100!"))    #gets user to input their guess
            if 1 < userGuess < 100:                             #validates number input is 1-100
                return userGuess                                #returns users guess
            else:
                print("Please enter a valid number 1-100.")
        except ValueError:
            print("Please enter a valid number 1-100.")


def guessingGame():
    '''
    this function tells the user if they guessed correctly and keeps track of number of guesses
    :return: number guesses user has made
    '''
    compNumber = getNumber()                                   #uses getNumber function to generate number 1-100
    numberGuesses = 0

    while True:
        userGuess = getGuess()                                 #uses getGuess function to get users guess
        numberGuesses += 1                                     #adds together guesses when getGuess function is called
        if userGuess == int(compNumber):
            print("Congrats, you guessed the right number! It's", compNumber, ", you won!")
            return numberGuesses
        elif userGuess > int(compNumber):
            print("You guessed too high, try again.")
        elif userGuess < int(compNumber):
            print("You guessed too low, try again.")


def main():
    '''
    this function makes the game loop 3 times and calculates and gives the users average guesses per game
    :return: average number of user guesses per game
    '''
    totalGuesses = 0
    numberOfGames = 3                                          #sets amount of times game will loop

    for x in range(numberOfGames):                             #loops the game numberOfGames times
        totalGuesses += guessingGame()

    averageGuesses = totalGuesses / numberOfGames              #calculates the average number of guesses
    print("Your average number of guesses per games is", averageGuesses)

main()