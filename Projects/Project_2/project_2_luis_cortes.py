#!/usr/local/bin/python3
#
# Luis Cortes
# Project 2
# CS 299
import random
import sys


def ask_user():
    tries = 3
    while tries > 0:
        guess = input("Enter number, range 1 - 100: ")

        # Check if input is a digit
        if guess.isdigit() and 1 <= int(guess) <= 100:
            return int(guess)  # Return input if it s a valid integer
        print("Invalid data!")
        tries -= 1

    print("Goodbye!")
    exit()


# Problem 1
def number_guessing():
    print("=====================")
    print("    Guessing Game    ")
    print("=====================")

    hidden_number = random.randint(1, 100)
    guesses = 5
    previous_guess = -1
    already_guessed = False
    win = False

    while guesses > 0:
        number_guessed = ask_user()

        if previous_guess == number_guessed:
            print("You already entered this number!")
            already_guessed = True

        # Check if user already guessed number
        if not already_guessed:
            if number_guessed < hidden_number:
                print("Guessed too small!")
            elif number_guessed > hidden_number:
                print("Guessed too large!")
            elif number_guessed == hidden_number:
                win = True
                print("Congratulations! You guessed correctly!")
                break
            else:
                print("oops!")

        guesses -= 1
        previous_guess = number_guessed
        print()
    if not win:
        print("\nSorry out of tries.\nCorrect number is: ", hidden_number)


# Problem 2
def perfect_number():
    print("=====================")
    print("   Perfect Number    ")
    print("=====================")
    number = int(input("Enter a number: "))

    if number < 0:
        print("No negative numbers!")
        exit()

    sum_ = 0
    for num in range(1, number):
        if number % num == 0:  # Number is evenly divisible
            sum_ += num

    if sum_ == number:
        print("{0} is a perfect number!".format(number))
    else:
        print("{0} is not a perfect number!".format(number))


def main():
    if len(sys.argv) < 2:
        print("usage: project_2_luis_cortes [guessing] [perfect]")
    else:
        # Get script argument
        argument = str(sys.argv[1])

        if argument == "guessing":
            number_guessing()
        elif argument == "perfect":
            perfect_number()
        else:
            print("usage: [guessing] [perfect]")

if __name__ == "__main__":
    main()


########################################################################################################################
# Problem 1
########################################################################################################################
# Test 1
# ----------------------------------------------------------------------------------------------------------------------
# =====================
#     Guessing Game
# =====================
# Enter number, range 1 - 100: no
# Invalid data!
# Enter number, range 1 - 100: hello
# Invalid data!
# Enter number, range 1 - 100: ok
# Invalid data!
# Goodbye!


# Test 2
# ----------------------------------------------------------------------------------------------------------------------
# =====================
#     Guessing Game
# =====================
# Enter number, range 1 - 100: 1
# Guessed too small!
#
# Enter number, range 1 - 100: 2
# Guessed too small!
#
# Enter number, range 1 - 100: 3
# Guessed too small!
#
# Enter number, range 1 - 100: 4
# Guessed too small!
#
# Enter number, range 1 - 100: 5
# Guessed too small!
#
#
# Sorry out of tries.
# Correct number is:  57


# Test 3
# ----------------------------------------------------------------------------------------------------------------------
# =====================
#     Guessing Game
# =====================
# Enter number, range 1 - 100: 50
# Guessed too small!
#
# Enter number, range 1 - 100: 75
# Guessed too small!
#
# Enter number, range 1 - 100: 87
# Guessed too small!
#
# Enter number, range 1 - 100: 93
# Guessed too small!
#
# Enter number, range 1 - 100: 96
# Congratulations! You guessed correctly!

########################################################################################################################
# Problem 2
########################################################################################################################
# Test 1
# ----------------------------------------------------------------------------------------------------------------------
# =====================
#    Perfect Number
# =====================
# Enter a number: 6
# 6 is a perfect number!


# Test 2
# ----------------------------------------------------------------------------------------------------------------------
# =====================
#    Perfect Number
# =====================
# Enter a number: 28
# 28 is a perfect number!

# Test 3
# ----------------------------------------------------------------------------------------------------------------------
# =====================
#    Perfect Number
# =====================
# Enter a number: 325
# 325 is not a perfect number!

# Test 4
# ----------------------------------------------------------------------------------------------------------------------
# =====================
#    Perfect Number
# =====================
# Enter a number: 496
# 496 is a perfect number!
