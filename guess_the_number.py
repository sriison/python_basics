import random

randNum = random.randint(1, 100)
guesses = 0

for i in range(1, 8):
    guesses = guesses + 1
    print("hi human guess a number 1-100! \n")
    guess = input()

    if guess.isdigit():
        if int(guess) > randNum:
            print("your guess is too high \n")

        elif int(guess) < randNum:
            print("your guess is too low \n")

        elif int(guess) == randNum:
            print("duuude you're a genius \n")
            print("you needed " + str(guesses) + " guesses")

    else:
        print("Invalid Input! Try a number. \n")