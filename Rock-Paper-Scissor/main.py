import random # importing random module
randomNumber = random.randint(1, 3) # generating random number between the range 0 and 10
# 1 - Rock
# 2 - Paper
# 3 - Scissors
choices = ["Rock", "Paper", "Scissors"]

# About the game
print("Rock Paper Scissors Game")
print("Enter Q or q to quit")

# Loop to keep the game running
while True:
    userInput = input("Rock, Paper or Scissors?\n: ") # getting user's input
    if userInput.lower() == "q": # checking if the user wants to exit
        print("The computer picked " + choices[randomNumber]) # printing the random number
        break 
    else: # if the user does not quit
        if userInput.lower() == "rock" and randomNumber == 2:
            print("Computer Won. Computer Picked " + choices[randomNumber-1])
        elif userInput.lower() == "paper" and randomNumber == 3:
            print("Computer Won. Computer Picked " + choices[randomNumber-1])
        elif userInput.lower() == "paper" and randomNumber == 1:
            print("Computer Won. Computer Picked " + choices[randomNumber-1])
        else:
            print("You Won. Computer Picked " + choices[randomNumber])
            break
