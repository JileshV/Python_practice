import random

corrNumber = random.randint(1, 100)

# print(corrNumber)

userNumber = int(input("Guess the number computer just chose between 1 & 100: "))
guessCount = 1

while True:

    if (0 < userNumber <= 100):
        if (userNumber > corrNumber):
            userNumber = int(input("The number is higher than the Computer number\nGuess a smaller number(1-100): "))
            guessCount += 1
        
        elif (userNumber < corrNumber):
            userNumber = int(input("The number is lower than the Computer number\nGuess a higher number(1-100): "))
            guessCount += 1
        
        elif (userNumber == corrNumber):
            break

    elif(userNumber > 100 or userNumber <= 0):
        choice = input("The number is not between 1 & 100, please enter valid number.\nPress 'y' to continue or 'n' to exit: ")
        if (choice == 'n'):
            exit()
        userNumber = int(input("Enter a valid number between 1 & 100: "))

print(f"You guessed the number right!\nYou took {guessCount} guesses to guess the number!")
