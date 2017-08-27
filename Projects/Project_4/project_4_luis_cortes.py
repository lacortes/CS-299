# /usr/local/bin/python3
# Luis Cortes
# CS 299
# Project 4

file_name = []  # Keep track of file name used


def get_temp():
    tries = 3

    print("Hint: 'NoCalTemp.txt or 'SoCalTemp.txt'")
    # Try until user enters valid file
    while tries > 0:
        try:
            file_path = input("Enter a file name: ")
            file_name.append(file_path)

            file = open(file_path, "r")  # Open file to read
            temperatures = []  # Store list of read in temperatures

            print("Reading in contents ... ")

            # Read in contents line by line
            for line in file:
                if line == "\n":  # Skip empty lines
                    continue

                line = line.split()  # Split line into tokens
                # Cast string tokens to floats
                for index in range(len(line)):
                    temperatures.append(float(line[index]))
            print("... Contents read.")
            file.close()
            return temperatures
        except FileNotFoundError:
            tries -= 1
            print("File not found! Try again") if tries > 0 else print("Goodbye!")


def get_highest(temperatures):
    high = temperatures[0]  # Assume element at fist index is highest
    for temp in temperatures:
        if temp > high:
            high = temp
    return high


def get_lowest(temperatures):
    low = temperatures[0] # Assume element at fist index is lowest
    for temp in temperatures:
        if temp < low:
            low = temp
    return low


def get_average(temperatures):
    sum_ = 0.00

    # Add up all the numbers
    for numbers in temperatures:
        sum_ += numbers
    return sum_ / len(temperatures)


def main():
    read_in_list = get_temp()

    print("Getting lowest value.")
    lowest = get_lowest(read_in_list)

    print("Getting highest value")
    highest = get_highest(read_in_list)

    print("Getting Average")
    average = get_average(read_in_list)

    print("Writing to file. ")
    file_out_path = ""

    if file_name[0] == "SoCalTemp.txt":
        file_out_path = "SoCalOutput.txt"
    elif file_name[0] == "NoCalTemp.txt":
        file_out_path = "NoCalOutput.txt"

    file_out = open(file_out_path, "w")

    file_out.write("Lowest: "+str(lowest)+"\n")
    file_out.write("Highest: "+str(highest)+"\n")
    file_out.write("Average: "+str(average))

    file_out.close()

    print("Finished")

if __name__ == "__main__":
    main()