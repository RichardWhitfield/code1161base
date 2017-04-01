"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
from __future__ import division
from __future__ import print_function
import random


def number_tester(low, high):
    """Robust testing function.

    Check input values for suitability
    """
    a = False
    while not a:
        guessedNumber = raw_input("Your guess: ")
        try:
            if int(guessedNumber) >= low and int(guessedNumber) <= high:
                a = True
            else:
                print("Your guess was outside of your bounds")
        except:
            print("That wasn't a number!")
    return guessedNumber


def bounds_tester():
    """Robust number tester.

    Tests the input bounds to ensure number
    """
    a = False
    while not a:
        lowerBound = raw_input("Enter a lower bound: ")
        upperBound = raw_input("Enter an upper bound: ")
        try:
            if int(lowerBound) >= 0 and int(upperBound) >= 0 and \
            int(upperBound) > int(lowerBound):
                a = True
            elif int(lowerBound) >= int(upperBound):
                print("Your upperbound must be greater than your lowerbound")
            else:
                print("Your values must be positive")
        except:
            print("Please input numbers only!")

    return [lowerBound, upperBound]


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nwelcome to the advance guessing game!")
    print("First we need to set an upper and lower bound")
    bounds = bounds_tester()
    lowerBound = int(bounds[0])
    upperBound = int(bounds[1])
    print("OK guess number between {} and {} ?".format(lowerBound, upperBound))
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)
    actualNumber = random.randint(lowerBound, upperBound)
    guessed = False

    while not guessed:
        guessedNumber = number_tester(lowerBound, upperBound)
        guessedNumber = int(guessedNumber)
        if guessedNumber == actualNumber:
            print("you got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("too small, try again ")
        else:
            print("too big, try again   ")
    return "You got it!"


if __name__ == "__main__":
    advancedGuessingGame()
