#Rules for this game
#Scissors cut Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisions Spock
#Spock smashes Scissors, Scissors beat Lizard, Lizard eat Paper, Paper disproves Spock
#Spock vaporizes Rock, Rock breaks Scissors
while True:
    print("======================================")
    print("  Rock Paper Scissors Lizard Spock")
    print("======================================")

    print("Hello! Welcome to a Rock, Paper, Scissors, Lizard, and Spock!!")
    print("Please select the following: ")
    print("1 for Rock ✊\n2 for Paper ✋\n3 for Scissors ✌️\n4 for Lizard 🦎\n5 for Spock 🖖\n6 for Quit")

    import random

    player = int(input("Enter your choice from the option above: "))

    while player < 1 or player > 6:         #This will check if the player enter something wrong
        print("Woops! You enter a wrong input! Please try again!")
        player = int(input("Enter your choice from the option above: "))

    if player == 6:
        break
    else:
        if player == 1:
            print("\nYou chose: ✊")
        elif player == 2:
            print("\nYou chose: ✋")
        elif player == 3:
            print("\nYou chose:✌️ ")
        elif player == 4:
            print("\nYou chose 🦎")
        else:
            print("\nYou chose 🖖")


        computer = random.randint(1, 5)

        if computer == 1:
            print("CPU chose: ✊")
        elif computer == 2:
            print("CPU chose: ✋")
        elif computer == 3:
            print("CPU chose:✌️ ")
        elif player == 4:
            print("CPU chose 🦎")
        else:
            print("CPU chose 🖖")

        #Calculation for the game
        if player == computer:
            print("It's a Tie!")
        else: 
            if player == 1 and computer == 3:                           #All the outcomes winning from the player
                print("Rock breaks Scissors! 🥁 The player won!")       
            elif player == 1 and computer == 4:
                print("Rock crushes Lizard, R.I.P lizard. 🥁 The player won!")
            elif player == 2 and computer == 1:
                print("Oh no! Paper covers Rock! 🥁 The player won!")
            elif player == 2 and computer == 5:
                print("Paper disproves Spock! 🥁 The player won!")
            elif player == 3 and computer == 2:
                print("Snip! Scissors cut Paper! 🥁 The player won!")
            elif player == 3 and computer == 4:
                print("Scissors beats Lizard. 🥁 The player won!")
            elif player == 4 and computer == 2:
                print("Oh! Lizard eats Paper! 🥁 The player won!")
            elif player == 4 and computer == 5: 
                print("Ouch! Lizard poison Spock! 🥁 The player won!")
            elif player == 5 and computer == 1:
                print("Spock vaporize Rock! 🥁 The player won!")
            elif player == 5 and computer == 3:
                print("Spock smashes Scissors! 🥁 The player won!")
            elif computer == 1 and player == 3:                             #All the outcomes winnings from the computer
                print("Rock breaks Scissors! 🥁 The computer won!")
            elif computer == 1 and player == 4:
                print("Rock crushes Lizard, R.I.P lizard. 🥁 The computer won!")
            elif computer == 2 and player == 1:
                print("Oh no! Paper covers Rock! 🥁 The computer won!")
            elif computer == 2 and player == 5:
                print("Paper disproves Spock! 🥁 The computer won!")
            elif computer == 3 and player == 2:
                print("Snip! Scissors cut Paper! 🥁 The computer won!")
            elif computer == 3 and player == 4:
                print("Scissors beats Lizard. 🥁 The computer won!")
            elif computer == 4 and player == 2:
                print("Oh! Lizard eats Paper! 🥁 The computer won!")
            elif computer == 4 and player == 5: 
                print("Ouch! Lizard poison Spock! 🥁 The computer won!")
            elif computer == 5 and player == 1:
                print("Spock vaporize Rock! 🥁 The computer won!")
            elif computer == 5 and player == 3:
                print("Spock smashes Scissors! 🥁 The computer won!")
            else:
                print("Woops! Error")                                               #This just incase if there is any errors

        print("\nThanks for playing! 😊")
    restart = input("Would you like to try again? \"y\" for yes or \"n\" for no: ")

    while restart != "y" and restart != "n":
        print("Wrong input! Please try again if you want to restart the game")
        restart = input("Would you like to try again? \"y\" for yes or \"n\" for no: ")

    if restart == "y":
        print("Yay!")
    else:
        break

print("Thanks for playing! Have a wonderful day!😊")