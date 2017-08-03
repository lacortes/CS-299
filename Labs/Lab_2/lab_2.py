#!/usr/local/bin/python3

# Luis Cortes
# CS 299
# Lab 2
# 08/01/2017

def calculate_bmi(weight, height):
    return weight / (height**2) * 703

def main():
    # Ask user for input
    weight = float( input("Enter weight in lbs: ") )
    height = float( input("Enter height in inches: ") )

    # Print information to console
    print("Weight: {0}lbs".format(weight))
    print("Height: {0}inches".format(height))
    print("BMI: {0:.2f}".format(calculate_bmi(weight, height)))


if __name__ == "__main__":
    main()


'''
========================
+ First Input          +
========================
Enter weight in lbs: 102
Enter height in inches: 56
Weight: 102.0lbs
Height: 56.0inches
BMI: 22.87

========================
+ Second Input         +
========================
Enter weight in lbs: 160.5
Enter height in inches: 71
Weight: 160.5lbs
Height: 71.0inches
BMI: 22.38

========================
+ Third Input          +
========================
Enter weight in lbs: 250
Enter height in inches: 67.5
Weight: 250.0lbs
Height: 67.5inches
BMI: 38.57

========================
+ Fourth Input         +
========================
Enter weight in lbs: 155
Enter height in inches: 66
Weight: 155.0lbs
Height: 66.0inches
BMI: 25.01

+======================+
+        Bonus         +
+======================+

+--------+
| TEST 1 |
+--------+
Enter weight in lbs: 0
Enter height in inches: 1
Weight: 0.0lbs
Height: 1.0inches
BMI: 0.00

+--------+
| TEST 2 |
+--------+
Enter weight in lbs: 5
Enter height in inches: 0
Weight: 5.0lbs
Height: 0.0inches
Traceback (most recent call last):
  File "./lab_2.py", line 22, in <module>
    main()
  File "./lab_2.py", line 18, in main
    print("BMI: {0:.2f}".format(calculate_bmi(weight, height)))
  File "./lab_2.py", line 8, in calculate_bmi
    return weight / (height**2) * 703
ZeroDivisionError: float division by zero

+--------+
| TEST 3 |
+--------+
Enter weight in lbs: 0
Enter height in inches: 0
Weight: 0.0lbs
Height: 0.0inches
Traceback (most recent call last):
  File "./lab_2.py", line 22, in <module>
    main()
  File "./lab_2.py", line 18, in main
    print("BMI: {0:.2f}".format(calculate_bmi(weight, height)))
  File "./lab_2.py", line 8, in calculate_bmi
    return weight / (height**2) * 703
ZeroDivisionError: float division by zero

+--------+
| TEST 4 |
+--------+
Enter weight in lbs: -34
Enter height in inches: 66
Weight: -34.0lbs
Height: 66.0inches
BMI: -5.49

+--------+
| TEST 5 |
+--------+
Enter weight in lbs: 56lbs
Traceback (most recent call last):
  File "./lab_2.py", line 22, in <module>
    main()
  File "./lab_2.py", line 12, in main
    weight = float( input("Enter weight in lbs: ") )
ValueError: could not convert string to float: '56lbs'

'''
