#/usr/local/bin/python3
#
# Luis Cortes
# CS 299
# Lab 7


def get_max(values):
    max_value = values[0]  # Assume first element is highest

    # Iterate through every element in list starting from index 1
    for i in range(1, len(values)):
        if values[i] > max_value:
            max_value = values[i]
    return max_value


def main():
    # Predefined list
    scores_list = [25.0, 35.5, 15.0, 45.5, 55.0, 30.2, 49.4, 21.1, 41.8, 37.0]

    # Step 1
    print("List length: ", len(scores_list))  # Print length of list

    # Step 2
    print("Largest value: ", get_max(scores_list))

    # Step 3
    new_list = []
    for value in scores_list:
        if value >= 25:
            new_list.append(value)
    print("New list: ", new_list)

    # Step 4 (Bonus)
    scores_list.sort()
    print("Ascending order: ", scores_list)

    scores_list = scores_list[::-1]
    print("Descending order: ", scores_list)

if __name__ == "__main__":
    main()


# Results
# ----------------------------------------------------------------------------------------------------------------------
# List length:  10
# Largest value:  55.0
# New list:  [25.0, 35.5, 45.5, 55.0, 30.2, 49.4, 41.8, 37.0]
# Ascending order:  [15.0, 21.1, 25.0, 30.2, 35.5, 37.0, 41.8, 45.5, 49.4, 55.0]
# Descending order:  [55.0, 49.4, 45.5, 41.8, 37.0, 35.5, 30.2, 25.0, 21.1, 15.0]
