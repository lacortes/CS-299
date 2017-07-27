#!/usr/local/bin/python3

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
    salary = float(salary)

    # Display the information back to the user
    print("My name is {0}, my age is {1}\n\
        I hope to work for {2}, and earn ${3} per year".format(name, ))

if __name__ == "__main__" : 
    main()