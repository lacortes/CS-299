#!/usr/local/bin/python3
# Luis Cortes
# CS 299
# Lab 6
from math import sqrt, atan, degrees
import sys


# Calculates side 'c' for a right triangle and returns its value
def get_c_side(a, b):
    add = a**2 + b**2
    return sqrt(add)


# Calculates angle BAC and returns radian value
def get_angle(a, b):
        # Tan = opp / hyp
        div = a / b
        return atan(div)  # theta = arctan(a / b)


def solver_entry():
    print("=====================")
    print("   Triangle Solver   ")
    print("=====================")
    # Ask user for side values
    a_side = float(input("Enter side for a: "))
    b_side = float(input("Enter side for b: "))

    # Save c value
    c_side = get_c_side(a_side, b_side)
    print("Side for c: ", c_side)

    # Turn radian value into degrees
    degree = degrees(get_angle(a_side, b_side))
    print("Degrees of angle BAC: ", degree)


def is_prime(number):
    for fact in range(2, number):
        if number % fact == 0:
            # print("Not prime")
            return False
    # print("Prime number")
    return True


def prime_entry():
    number = int(input("Enter a number: "))

    while number > 1:

        if is_prime(number):
            print("{0} is prime".format(number))
        else:
            print("{0} is not prime".format(number))
        print()
        number = int(input("Enter a number: "))


    print("Goodbye!")


def main():
    if len(sys.argv) < 2:
        print("Usage: lab_6_luis_cortes <triangle, prime>")
    else:
        # Get script argument
        argument = str(sys.argv[1])

        if argument == "triangle":
            solver_entry()
        elif argument == "prime":
            prime_entry()
        else:
            print("INVALID ARGUMENT! Enter: <triangle, prime>")


if __name__ == "__main__":
    main()


########################################################################################################################
# Problem 1
########################################################################################################################
# Test 1
# ----------------------------------------------------------------------------------------------------------------------
# =====================
#    Triangle Solver
# =====================
# Enter side for a: 7.5
# Enter side for b: 7.5
# Side for c:  10.606601717798213
# Degrees of angle BAC:  45.0


# Test 2
# ----------------------------------------------------------------------------------------------------------------------
# =====================
#    Triangle Solver
# =====================
# Enter side for a: 7.5
# Enter side for b: 10
# Side for c:  12.5
# Degrees of angle BAC:  36.86989764584402


# Test 3
# ----------------------------------------------------------------------------------------------------------------------
# =====================
#    Triangle Solver
# =====================
# Enter side for a: 6.0
# Enter side for b: 4.5
# Side for c:  7.5
# Degrees of angle BAC:  53.13010235415598


########################################################################################################################
# Problem 2
########################################################################################################################
# Test 1
# ----------------------------------------------------------------------------------------------------------------------
# Enter a number: 1
# Goodbye!


# Test 2
# ----------------------------------------------------------------------------------------------------------------------
# Enter a number: 2
# 2 is prime
#
# Enter a number: 17
# 17 is prime
#
# Enter a number: 27
# 27 is not prime
#
# Enter a number: 61
# 61 is prime
#
# Enter a number: 237
# 237 is not prime
#
# Enter a number: 255
# 255 is not prime
#
# Enter a number: -1
# Goodbye!
