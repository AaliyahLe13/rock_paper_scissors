#Rules for this game
#Rock beats Scissors, Scissors beats Paper, Paper beats Rock
print("=======================")
print("  Rock Paper Scissors")
print("=======================")

print("Hello! welcome to a Rock, Paper, and Scissors game!")
print("Please select the following: ")
print("1 for Rock ✊\n2 for Paper ✋\n3 for Scissors ✌️")

player = int(input("Enter a number between 1 and 3: "))

import random

computer = random.randint(1, 3)
print(computer)

while player != 1 and player != 2 and player != 3:
    print("Woops! You did enter a number between 1 to 3, please try again")
    player = int(input("Enter a number between 1 and 3: "))


if player == 1 and computer == 3:
    print("\nYou chose: ✊")
    print("CPU chose: ✌️")
    print("The Player Won!")
elif player == 3 and computer == 2:
    print("\nYou chose: ✌️")
    print("CPU chose:✋")
    print("The Player Won!")
elif player == 2 and computer == 1:
    print("\nYou chose: ✋")
    print("CPU chose:✊")
    print("The Player Won!")
elif player == 1 and computer == 1:
    print("\nYou chose: ✊")
    print("CPU chose:✊")
    print("Is a Tie!")
elif computer == 1 and player == 3:
    print("\nYou chose:✌️ ")
    print("CPU chose:✊")
    print("The Computer Won!")
elif computer == 3 and player == 2:
    print("\nYou chose:✋")
    print("CPU chose:✌️")
    print("The Computer Won!")
elif computer == 2 and player == 2:
    print("\nYou chose: ✋")
    print("CPU chose:✋")
    print("Is a Tie!")
elif computer == 2 and player == 1:
    print("\nYou chose:✊")
    print("CPU chose:✋")
    print("The Computer Won!")
elif computer == 3 and player == 3:
    print("\nYou chose:✌️ ")
    print("CPU chose:✌️")
    print("Is a Tie!")
else:
    print("Oh no! Error!")

