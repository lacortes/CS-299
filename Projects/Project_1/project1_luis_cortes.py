# Luis Cortes
# CS 299
# Project 1


def calculate_bmi_metric(weight=0.0, height=1.0):
    if height > 0:
        return weight / (height**2)
    else:
        print("Invalid data!")
        exit()


def calculate_bmi_english(weight=0.0, height=1.0):
    if height > 0:
        return weight / (height**2) * 703
    else:
        print("Invalid data!")
        exit()


def check_bmi(bmi):
    if 0 < bmi <= 24:
        print("Normal")
    elif 25 <= bmi <= 29:
        print("Overweight")
    elif 30 <= bmi <= 39:
        print("Obese")
    else:
        print("Extreme Obese")


def main():
    # Title Screen
    print("=================================================")
    print("           Body Mass Index Calculator            ")
    print("=================================================")

    # Ask user to choose which system to use (Metric or English)
    print("(1) Metric System")
    print("(2) English System")
    system = int(input("Choose a system: "))

    if system == 1:  # User chose Metric System
        # Ask user for input
        weight = float(input("Enter weight in kgs: "))
        height = float(input("Enter height in meters: "))

        bmi = round(calculate_bmi_metric(weight, height), 2)
        check_bmi(bmi)
    elif system == 2:  # User chose English System
        # Ask user for input
        weight = float(input("Enter weight in lbs: "))
        height = float(input("Enter height in inches: "))

        bmi = round(calculate_bmi_english(weight, height), 2)
        check_bmi(bmi)
    else:
        print("Wrong choice")

if __name__ == "__main__":
    main()

# Test 1
# ----------------------------------------------------------------------------------------------------------------------
# =================================================
#            Body Mass Index Calculator
# =================================================
# (1) Metric System
# (2) English System
# Choose a system: 2
# Enter weight in lbs: 150
# Enter height in inches: 70
# Normal

# Test 2
# ----------------------------------------------------------------------------------------------------------------------
# =================================================
#            Body Mass Index Calculator
# =================================================
# (1) Metric System
# (2) English System
# Choose a system: 2
# Enter weight in lbs: 180
# Enter height in inches: 65
# Extreme Obese

# Test 3
# ----------------------------------------------------------------------------------------------------------------------
# =================================================
#            Body Mass Index Calculator
# =================================================
# (1) Metric System
# (2) English System
# Choose a system: 1
# Enter weight in kgs: 120
# Enter height in meters: 1.7
# Extreme Obese

# Test 4
# ----------------------------------------------------------------------------------------------------------------------
#  == == == == == == == == == == == == == == == == == == == == == == == == =
# Body Mass Index Calculator
# == == == == == == == == == == == == == == == == == == == == == == == == =
# (1) Metric System
# (2) English System
# Choose a system: 1
# weight in kgs: 180
# height in meters: 1.62
# Extreme Obese


# Test 5
# ----------------------------------------------------------------------------------------------------------------------
# =================================================
#            Body Mass Index Calculator
# =================================================
# (1) Metric System
# (2) English System
# Choose a system: 2
# Enter weight in lbs: 0
# Enter height in inches: 1
# Normal

# Test 6
# ----------------------------------------------------------------------------------------------------------------------
# =================================================
#            Body Mass Index Calculator
# =================================================
# (1) Metric System
# (2) English System
# Choose a system: 2
# Enter weight in lbs: 1
# Enter height in inches: 0
# Invalid data!

# Test 7
# ----------------------------------------------------------------------------------------------------------------------
# =================================================
#            Body Mass Index Calculator
# =================================================
# (1) Metric System
# (2) English System
# Choose a system: 1
# Enter weight in kgs: 0
# Enter height in meters: 0
# Invalid data!

# Test 8
# ----------------------------------------------------------------------------------------------------------------------
# =================================================
#            Body Mass Index Calculator
# =================================================
# (1) Metric System
# (2) English System
# Choose a system: 3
# Wrong choice