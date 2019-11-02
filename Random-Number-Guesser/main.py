import random # importing random modules
randomNumber = random.randint(0, 10) # generating random number between the range 0 and 10

# About the game
print("Random Number Guessing Game")
print("Guess a number between 0 and 10")
print("Enter Q or q to quit")

# Loop to keep the game running
while True:
    userInput = input("Guess Random Number: ") # getting user's input
    if userInput.lower() == "q": # checking if the user wants to exit
        print("The number was " + str(randomNumber)) # printing the random number
        break 
    else: # if the user does not quit
        if (int(userInput) == randomNumber): # if the user guess the random number
            print("You guessed it!")
            break
        elif (int(userInput) > randomNumber): # if the user guesses a number higher than the randomNumber
            print("Guess Lower")
        else: # if the user guess a number lower than the randomNumber
            print("Guess Higher")
