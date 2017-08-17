

def main():
    scores = []
    score = int(input("Enter integer: "))

    while score >= 0:
        if score < 50:
            scores.append(score)
        score = int(input("Enter integer: "))

    if len(scores) > 0:
        sum = 0
        for number in scores:
            sum += number
        average = sum / len(scores)
        print("Average: ", average)
    else:
        print("No Average")

if __name__ == "__main__":
    main()