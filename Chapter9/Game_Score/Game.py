'''
1 = rock
-1 = paper
0 = scissor
'''
import random

def RPS_Game():
    score_count = 0
    while True:
        computer = random.choice([1, -1, 0])

        youDict = {"r" : 1, "p" : -1, "s" : 0}
        reverseDict = {1 : "Rock", -1 : "Paper", 0 : "Scissor"}

        youInput = input("r for Rock\np for Paper\ns for Scissor\nEnter your choice: ")

        yourChoice = youDict[youInput]

        if (computer == yourChoice):
            print(f"You chose {reverseDict[yourChoice]} AND computer chose {reverseDict[computer]}\nIts a draw :/")

        else:
            if (computer == 1 and yourChoice == -1):
                print(f"You chose {reverseDict[yourChoice]} AND computer chose {reverseDict[computer]}\nYOU WIN!!")
                score_count += 1
            elif (computer == 1 and yourChoice == 0):
                print(f"You chose {reverseDict[yourChoice]} AND computer chose {reverseDict[computer]}\nYOU LOOSE :(")
            
            elif (computer == -1 and yourChoice == 1):
                print(f"You chose {reverseDict[yourChoice]} AND computer chose {reverseDict[computer]}\nYOU LOOSE :(")
            elif (computer == -1 and yourChoice == 0):
                print(f"You chose {reverseDict[yourChoice]} AND computer chose {reverseDict[computer]}\nYOU WIN!!")
                score_count += 1

            elif (computer == 0 and yourChoice == -1):
                print(f"You chose {reverseDict[yourChoice]} AND computer chose {reverseDict[computer]}\nYOU LOOSE :(")
            elif (computer == 0 and yourChoice == 1):
                print(f"You chose {reverseDict[yourChoice]} AND computer chose {reverseDict[computer]}\nYOU WIN!!")
                score_count += 1

            else:
                print("Error. Run again.")
        user = input("Enter 'y' to play again or 'n' to exit: ")
        if (user == "n"):
            print(f"Your Score: {score_count}")
            break

    #Saving High Score
    with open("Game_Score\High_score.txt") as f:
        c = f.read()
    if (score_count >= int(c)):
        print(f"Your score is a High score: {score_count}")
        with open("Game_Score\High_score.txt", "w") as f:
            f.write(str(score_count))
    elif(int(c) >= score_count):
        print(f"High Score: {c}")


u = input("Start the game? (y/n): ")
if (u == "y"):
    RPS_Game()