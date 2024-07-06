#Rules for this game
#Rock beats Scissors, Scissors beats Paper, Paper beats Rock
print("=======================")
print("  Rock Paper Scissors")
print("=======================")

print("Hello! welcome to a Rock, Paper, and Scissors game!")
print("Please select the following: ")
print("1 for Rock ✊\n2 for Paper ✋\n3 for Scissors ✌️\n4 for Quit")

player = int(input("Enter your choice from the options above: "))

while player < 1 or player > 4:
    print("Woops! You enter a wrong input! Please try again!")
    player = int(input("Enter your choice from the options above: "))

if player == 4:
    print("Thanks for playing! Have a wonderful day!😊")
else:
    if player == 1:
        print("\nYou chose: ✊")
    elif player == 2:
        print("\nYou chose: ✋")
    else:
        print("\nYou chose:✌️ ")


    import random

    computer = random.randint(1, 3)

    if computer == 1:
        print("CPU chose: ✊")
    elif computer == 2:
        print("CPU chose: ✋")
    else:
        print("CPU chose:✌️ ")

    
    #Calculation for the game
    if player == computer: #Ties
        print("It's a Tie!")
    else:
        if player == 1 and computer == 3: #Player paths winning the games 
            print("The Player Won!")
        elif player == 3 and computer == 2: 
            print("The Player Won!")
        elif player == 2 and computer == 1: 
            print("The Player Won!")
        elif computer == 1 and player == 3: #CPU paths of winning the games
            print("The Computer Won!")
        elif computer == 3 and player == 2:
            print("The Computer Won!")
        elif computer == 2 and player == 1:
            print("The Computer Won!")
        else:                                #This is just incase if there is any error
            print("Oh no! Error!")

