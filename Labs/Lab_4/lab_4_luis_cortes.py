# #!/usr/local/bin/python3
# Luis Cortes
# Lab 4
# 08/08/2017


def check_grade(grade):
    if 90 <= grade <= 100:
        print("Grade: A")
    elif 80 <= grade <= 89:
        print("Grade: B")
    elif 70 <= grade <= 79:
        print("Grade: C")
    elif 60 <= grade <= 69:
        print("Grade: D")
    elif 0 <= grade <= 59:
        print("Grade: F")
    else:
        print("NO GRADE")


def main():
    print("====================")
    print("    Grade Report    ")
    print("====================")

    # number of tries
    tries = 3
    while tries >= 1:
        user_grade = input("Enter a score between 0 - 100: ")

        # Validate input
        if user_grade.isdigit():
            check_grade(int(user_grade))
            break

        tries -= 1
    else:
        print("INVALID INPUT!")

    print("Goodbye!")


if __name__ == "__main__":
    main()

#  Test 1
# ----------------------------------------------------------------------------------------------------------------------
# ====================
#     Grade Report
# ====================
# Enter a score between 0 - 100: 100
# Grade: A
# Goodbye!

#  Test 2
# ----------------------------------------------------------------------------------------------------------------------
# ====================
#     Grade Report
# ====================
# Enter a score between 0 - 100: 85
# Grade: B
# Goodbye!

#  Test 3
# ----------------------------------------------------------------------------------------------------------------------
# ====================
#     Grade Report
# ====================
# Enter a score between 0 - 100: 75
# Grade: C
# Goodbye!

#  Test 4
# ----------------------------------------------------------------------------------------------------------------------
# ====================
#     Grade Report
# ====================
# Enter a score between 0 - 100: 69
# Grade: D
# Goodbye!

#  Test 5
# ----------------------------------------------------------------------------------------------------------------------
# ====================
#     Grade Report
# ====================
# Enter a score between 0 - 100: 50
# Grade: F
# Goodbye!

#  Test 6
# ----------------------------------------------------------------------------------------------------------------------
# ====================
#     Grade Report
# ====================
# Enter a score between 0 - 100: -1
# Enter a score between 0 - 100: -1
# Enter a score between 0 - 100: -1
# INVALID INPUT!
# Goodbye!

#  Test 7
# ----------------------------------------------------------------------------------------------------------------------
# ====================
#     Grade Report
# ====================
# Enter a score between 0 - 100: 101
# NO GRADE
# Goodbye!