import random

'''
1 = rock
-1 = paper
0 = scissor
'''

while True:

    computer = random.choice([1, -1, 0])

    youDict = {"r" : 1, "p" : -1, "s" : 0}
    reverseDict = {1 : "Rock", -1 : "Paper", 0 : "Scissor"}

    youInput = input("r for Rock\np for Paper\ns for Scissor\nEnter your choice: ")

    yourChoice = youDict[youInput]

    if (computer == yourChoice):
        print("Its a draw :/")

    else:
        if (computer == 1 and yourChoice == -1):
            print(f"You chose {reverseDict[yourChoice]} AND computer chose {reverseDict[computer]}\nYOU WIN!!")
        elif (computer == 1 and yourChoice == 0):
            print(f"You chose {reverseDict[yourChoice]} AND computer chose {reverseDict[computer]}\nYOU LOOSE :(")
        
        elif (computer == -1 and yourChoice == 1):
            print(f"You chose {reverseDict[yourChoice]} AND computer chose {reverseDict[computer]}\nYOU LOOSE :(")
        elif (computer == -1 and yourChoice == 0):
            print(f"You chose {reverseDict[yourChoice]} AND computer chose {reverseDict[computer]}\nYOU WIN!!")

        elif (computer == 0 and yourChoice == -1):
            print(f"You chose {reverseDict[yourChoice]} AND computer chose {reverseDict[computer]}\nYOU LOOSE :(")
        elif (computer == 0 and yourChoice == 1):
            print(f"You chose {reverseDict[yourChoice]} AND computer chose {reverseDict[computer]}\nYOU WIN!!")

        else:
            print("Error. Run again.")
    user = input("Enter 'y' to play again or 'n' to exit: ")
    if (user == "n"):
        break