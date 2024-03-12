#  Lab 7 Dice Game
#  Marquis Neely
# March 11, 2024
#  Basic dice game including two players and one dice roll per player. Victory goes to player with the highest dice roll.

# add libraries needed
import random

# the main function
def main():
    print()

    # initialize variables
    endProgram = 'no'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'

    # call to inputNames
    playerOne, playerTwo = inputNames(playerOne, playerTwo)

    # while loop to run program again
    while endProgram == 'no':

        # populate variables
        winnersName = 'NO NAME'
        p1number = 0
        p2number = 0

        # call to rollDice
        winnersName = rollDice(p1number, p2number, playerOne, playerTwo, winnersName)

        # call to displayInfo
        displayInfo(winnersName)

        endProgram = input('Do you want to end program? (yes/no): ')


# this function gets the players names
def inputNames(playerOne, playerTwo):
    playerOne = input("Enter player one's name: ")
    playerTwo = input("Enter player two's name: ")
    return playerOne, playerTwo

# this function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo, winnersName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)
    print(playerOne, "rolled:", p1number)
    print(playerTwo, "rolled:", p2number)

    if p1number > p2number:
        winnersName = playerOne
    elif p2number > p1number:
        winnersName = playerTwo
    else:
        winnersName = "TIE"

    return winnersName

# this function displays the winner
def displayInfo(winnersName):
    print("The winner is", winnersName)

if __name__ == "__main__":
    main()
