#!/usr/local/bin/python3

import sys

def main(argv):
    if len(argv) <= 1:
        print("Usage BonusLab <radius> <height>")
        sys.exit()


    # Uncomment this to use command line aguments
    radius = float(argv[1])

    # Uncommnet this to use command line arguments
    height = float(argv[2]) 

    print("Wlcome to Area and Volume calculator")
    pi = 3.14159


    # Uncomment this to not use command line args
    # radius = input("Please enter radius: ")
    # radius = float(radius)

    # Uncomment this to not use command line args
    # height = input("Please enter height: ")
    # height = float(height)

    base_area = pi * radius**2
    cylinder_volume = base_area * height

    # Display information back to user
    print("Base Area = {0}".format(base_area))
    print("Clynder Volume = {0}".format(cylinder_volume))


if __name__ == "__main__":
    main(sys.argv)