#!/usr/local/bin/python3
#
# Luis Cortes
# Project 2
# CS 299
import random


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


# Problem 1
def number_guessing():
    print("=====================")
    print("    Guessing Game    ")
    print("=====================")

    hidden_number = random.randint(1, 100)
    guesses = 5
    previous_guess = -1
    already_guessed = False

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
                print("Congratulations! You guessed correctly!")
                break
            else:
                print("oops!")

        guesses -= 1
        previous_guess = number_guessed
        print()

    print("\nSorry out of tries.\nCorrect number is: ", hidden_number)


# Problem 2
def perfect_number(number):

    sum_ = 0
    for num in range(1, number):
        if number % num == 0:  # Number is evenly divisible
            sum_ += num

    if sum_ == number:
        print("{0} is a perfect number!".format(number))
    else:
        print("{0} is not a perfect number!".format(number))


def main():
    # number_guessing()
    perfect_number(9)

if __name__ == "__main__":
    main()
