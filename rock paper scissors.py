import random

# import randint from random

def play_a_round():

    # getComputerChoice
    
    computerChoice = random.randint(1,3)

    
    # getUserChoice
    
    userChoice = int(input("Make a choice: (1) rock, (2) paper, (3) scissors: "))

    
    # show user the computer's choice
    
    print("The computer chose ", computerChoice)

    
    # determine winner

    if userChoice == computerChoice:
        print ("The game is a draw! We must play again.")
        return True # The game is a draw and we must play again
    
    elif userChoice == 1 and computerChoice == 2:
        print("Sorry! You have lost the game.")

    elif userChoice == 1 and computerChoice == 3:
        print("Congratulations! You have won the game.")

    elif userChoice == 2 and computerChoice == 1:
        print("Congratulations! You have one the game.")

    elif userChoice == 2 and computerChoice == 3:
        print("Sorry! You have lost the game.")

    elif userChoice == 3 and computerChoice == 1:
        print("Sorry! You have lost the game.")

    elif userChoice == 3 and computerChoice == 2:
        print("Congratulations! You have won the game")
        
        # which player won
        return False # There is a winner
    
    

def play():

    play_again = True

    while play_again:
        play_again = play_a_round()

play()
