#!/usr/local/bin/python3
from math import sqrt
# Luis Cortes	
# CS299
# Lab 3
# 08/03/2017

def main():
    # Banner
    print("Quadratic Formula Solver")
    print("=========================")

    # Ask user for coefficients
    a = int(input("Enter a coefficient: "))
    b = int(input("Enter b coefficient: "))
    c = int(input("Enter c coefficient: "))

    # Check a is 0, if 0 then exit program
    if a == 0:
        print("Not a quadratic equation")
        exit()

    # Verify real roots exist
    if (b**2) < (4*a*c):
        print("No real roots")
        exit()

    # Verify real roots exist
    real = sqrt(b*b - 4*a*c)

    # Make b negative
    neg_b = -b

    # Root with addition
    root_one = ( neg_b + real ) / (2 * a)

    # Root with sutraction
    root_two = ( neg_b - real) / (2 * a)

    if root_one == root_two:
        print("Roots are the same: ", root_one)
    else:
        print("Root one: {0:.2f}\nRoot two: {1:.2f}".format(root_one, root_two))

if __name__ == "__main__":
    main()

'''
---------------------------------------------------
Case 1
---------------------------------------------------
Quadratic Formula Solver
=========================
Enter a coefficient: 2
Enter b coefficient: -1
Enter c coefficient: -1
Root one: 1.00
Root two: -0.50

---------------------------------------------------
Case 2
---------------------------------------------------
Quadratic Formula Solver
=========================
Enter a coefficient: 3
Enter b coefficient: 11
Enter c coefficient: 4
Root one: -0.41
Root two: -3.26

---------------------------------------------------
Case 3
---------------------------------------------------
Quadratic Formula Solver
=========================
Enter a coefficient: 3
Enter b coefficient: 11
Enter c coefficient: 0
Root one: 0.00
Root two: -3.67

---------------------------------------------------
Case 4
---------------------------------------------------
Quadratic Formula Solver
=========================
Enter a coefficient: 4
Enter b coefficient: 0
Enter c coefficient: -7
Root one: 1.32
Root two: -1.32

---------------------------------------------------
Case 5
---------------------------------------------------
Quadratic Formula Solver
=========================
Enter a coefficient: 1
Enter b coefficient: 4
Enter c coefficient: 4
Roots are the same:  -2.0

---------------------------------------------------
Case 6
---------------------------------------------------
Quadratic Formula Solver
=========================
Enter a coefficient: 0
Enter b coefficient: 4
Enter c coefficient: 5
Not a quadratic equation

---------------------------------------------------
Case 7
---------------------------------------------------
Quadratic Formula Solver
=========================
Enter a coefficient: 1
Enter b coefficient: 2
Enter c coefficient: 3
No real roots
'''
