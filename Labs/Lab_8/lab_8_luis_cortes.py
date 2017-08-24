# /usr/local/bin/python3
# Luis Cortes
# CS 299
# Lab 8


def read_in_temps_and_convert(file_path):
    # Open file
    path = file_path
    file = open(path, "r")
    temperatures = []  # Store list of read in temperatures

    # Read in contents and store in list
    for line in file:
        line = line.split()

        # Convert strings to floats and convert to Celsius
        for index in range(len(line)):
            new_temp = f_to_c(float(line[index]))  # Convert fahrenheit to celsius
            new_temp = round(new_temp, 2)  # Round float to 2 decimal places
            line[index] = new_temp

        temperatures.append(line)  # Add list of floats

    file.close()
    return temperatures


def write_temps(file_path, temperatures):
    file = open(file_path, "w")

    for line in temperatures:
        for word in line:
            file.write(str(word)+" ")
        file.write("\n")

    file.close()


def f_to_c(f_temp):
    return (f_temp - 32.00) * (5.00/9.00)


def main():
    try:
        temperatures = read_in_temps_and_convert("temperatures.txt")
        write_temps("temperaturesC.txt", temperatures)
    except FileNotFoundError:
        print("File Not Found!")

if __name__ == "__main__":
    main()