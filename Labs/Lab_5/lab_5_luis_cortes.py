#!/usr/local/bin/python3
# Luis  Cortes
# Lab 5
# CS 299
import sys
import random


def investment():

    # Get user input
    balance = float(input("Enter initial balance: "))
    rate = float(input("Enter interest rate: "))
    years = int(input("Enter number of years: "))

    while years > 0:
        interest = balance * (rate/100)
        balance = balance + interest
        years -= 1
    print("Balance after years: ${0:.2f}".format(balance))


def random_gen():
    # Ask user for input
    count = int(input("How many random numbers you'd generate: "))

    for iteration in range(0, count):
        ran_number = random.randint(1, 50)
        print(ran_number, end=" ")


def lotto():
    # Hold number of cards
    tickets = []

    num_of_tickets = int(input("How many tickets: "))

    # Generate tickets
    for x in range(0, num_of_tickets):
        ticket = []

        # Generate five lucky numbers
        for x in range(0, 5):
            # Generate number from 1 - 47
            ticket.append(random.randint(1, 47))

        # Generate MEGA number
        ticket.append(random.randint(1, 27))
        tickets.append(ticket)

    # Print out every ticket
    for n in tickets:
        print("Ticket: ", n[:-1], end=" ")
        print("MEGA: ", n[-1])


def main():
    # Check if user enters an argument to the script
    if len(sys.argv) < 2:
        print("Usage: lab_5_luis_cortes <investment, random, lotto>")
    else:
        # Get script argument
        argument = str(sys.argv[1])

        if argument == "investment":
            investment()
        elif argument == "random":
            random_gen()
        elif argument == "lotto":
            lotto()
        else:
            print("INVALID ARGUMENT! Enter: <investment, random, lotto>")


if __name__ == "__main__":
    main()


#######################################################################################################################
# Problem 1
#######################################################################################################################
# Test 1
# ---------------------------------------------------------------------------------------------------------------------
# Enter initial balance: 500
# Enter interest rate: 3.5
# Enter number of years: 5
# Balance after years: $593.84

# Test 2
# ---------------------------------------------------------------------------------------------------------------------
#  Enter initial balance: 100
# Enter interest rate: 5.6
# Enter number of years: 8
# Balance after years: $154.64

# Test 3
# ---------------------------------------------------------------------------------------------------------------------
# Enter initial balance: 750
# Enter interest rate: 89.3
# Enter number of years: 3
# Balance after years: $5087.60

#######################################################################################################################
# Problem 2
#######################################################################################################################
# Test 1
# ---------------------------------------------------------------------------------------------------------------------
# How many random numbers you'd generate: 5
# 44 33 13 20 41

# Test 2
# ---------------------------------------------------------------------------------------------------------------------
# How many random numbers you'd generate: 10
# 31 28 15 30 17 19 36 19 31 4

# Test 3
# ---------------------------------------------------------------------------------------------------------------------
# How many random numbers you'd generate: 33
# 8 43 30 41 42 36 30 4 41 50 3 44 30 24 28 8 10 41 3 4 32 19 25 2 39 39 41 2 11 3 49 42 29

#######################################################################################################################
# Problem 3
#######################################################################################################################
# Test 1
# ---------------------------------------------------------------------------------------------------------------------
# How many tickets: 5
# Ticket:  [21, 13, 32, 24, 40] MEGA:  8
# Ticket:  [6, 34, 21, 9, 16] MEGA:  13
# Ticket:  [33, 46, 40, 27, 28] MEGA:  23
# Ticket:  [26, 23, 26, 40, 26] MEGA:  13
# Ticket:  [16, 20, 21, 20, 16] MEGA:  23

# Test 2
# ---------------------------------------------------------------------------------------------------------------------
# How many tickets: 3
# Ticket:  [21, 28, 41, 46, 47] MEGA:  12
# Ticket:  [43, 2, 13, 11, 1] MEGA:  18
# Ticket:  [36, 28, 40, 41, 32] MEGA:  12

# Test 3
# ---------------------------------------------------------------------------------------------------------------------
# How many tickets: 2
# Ticket:  [35, 6, 10, 18, 13] MEGA:  16
# Ticket:  [17, 8, 2, 34, 7] MEGA:  9
