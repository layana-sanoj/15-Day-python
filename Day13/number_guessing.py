# python picks a number between 0 and 100
#the user has to guess the number
#the program will say "too high" or "too low" until the user guesses the number correctly

import random 
num= random.randint(0,100)
print("Welcome to the guessing game!")
print("I have picked a number between 0 and 100.")
print("Try to guess it!")
while True:
    g=input("Enter your guess: (or type 'q' to quit) ")
    if g.lower()=='q':
        print("Thanks for playing!")
        break
    g=int(g)
    if g==num:
        print("congratulations! You guessed the number!")
        break
    elif g<num:
        print("too low!")
    else:
        print("too high!")
