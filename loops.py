# Use a while loop
# Use a for loop

# function to inform the user about your game:
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#import command to include code that someone else wrote
import random

#a statement that will generate a random number 
#between 1 and 10 by using the randint() function of the random module.
number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

        

# Writing pseudocode
# Before you run the Python script, 
# write out the logic of the while loop in written (non-code) sentences. 
# This technique is called pseudocoding.

#print out Welcome to Guess the Number
#print under The rules are simple. I will think of a number, and you will try to guess it
#value of number is between 1-10
#isGuessRight value is equal to false
#isGuessRight is not equal to true
#input from user to guess is a number between 1 and 10 
#if the input guess number is equal to number
#print out "You guessed. That is correct! You win!"
#else print "You guessed. Sorry, that isn’t it. Try again."

