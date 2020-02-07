import random
guess = random.randint(1,100)
print (guess)
chances = 0

for i in range(1,10):
    if chances <= i:
        print ("hi enter a number")
        num = int(input())
        chances = chances+1
        if num == guess:
            print ("you are genius")

        elif num < guess:
            print ("enter a higher number")
            chances_left = 10 - chances
        elif num > guess:
            print ("enter a lower number")
    else:
        print("Invalid Input! Try a number. \n")
