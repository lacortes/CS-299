#!/usr/local/bin/python3

# Luis Cortes
# CS 299
# Lab 1
# 07/27/17

def main():
    # Prompt user to enter name
    name = input("Please enter your name: ")

    # Prompt user to enter age
    age = input("Please enter your age: ")
    age = int(age)

    # Prompt user to enter company name
    company_name = input("Please enter company name: ")

    # Prompt user to enter salary 
    salary = input("Please enter salary: ")
    salary = int(salary)

    # Display the information back to the user
    print("My name is {0}, my age is {1}\nI hope to work for {2}, and earn ${3} per year"
        .format(name, age, company_name, salary))

if __name__ == "__main__" : 
    main()

# OUTPUT    
'''
Please enter your name: Luis Cortes
Please enter your age: 23
Please enter company name: Target
Please enter salary: 120000
My name is Luis Cortes, my age is 23
I hope to work for Target, and earn $120000 per year
'''