# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""
from __future__ import division
from __future__ import print_function


def bounds_tester(low, high):
    """Robust number tester.

    Tests the input bounds to ensure number
    """
    a = False
    while not a:
        try:
            if int(low) >= 0 and int(high) >= 0 and \
            int(high) > int(low):
                a = True
            elif int(low) >= int(high):
                print("Your upperbound must be greater than your lowerbound")
            else:
                print("Your values must be positive")
        except:
            print("Please input numbers only!")

    return [low, high]


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    Each guess, print what the guess is Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    This will be quite hard, especially hard if you don't have a good diagram!

    Debugging helpers:
      * GUARD is there to make it only run a few times so that you can see
        what's happening.
      * time.sleep(0.5) makes it pause for half a second.
      You don't need to use both together, and should remove them both before
      you submit. The tests will be checking that they aren't in there.
      (You should remove them from the file, not comment them out, the
      tests aren't that smart yet.)
    """
    print("\nwelcome to the algorithmic guesser, watch it perform magic!")
    print("First we need to set an upper and lower bound")
    bounds = bounds_tester(low, high)
    low = bounds[0]
    high = bounds[1]
    guessed = False
    tries = 0

    while not guessed:
        tries = tries + 1
        guess = int((int(high)-int(low))/2+int(low))
        print(guess)
        if guess == actual_number:
            print(actual_number)
            guessed = True
        elif guess < actual_number:
            low = guess
        else:
            high = guess
    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
