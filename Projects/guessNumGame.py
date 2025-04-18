import random

print("Welcome to Guessing Game")

target = random.randint(1,100)

while True :
    userChoice = int(input("Guess the target or Quit(Q) :"))
    if userChoice == "Q":
        print("Game Over")
        break


    userChoice = int(userChoice)
    if userChoice == target :
        print("Congratulations , You guessed it right!")
        break
    elif userChoice < target :
        print("Your guess is too low , Try again!")
    else :
        print("Your guess is too high , Try again!")

print("------GAME OVER--------")