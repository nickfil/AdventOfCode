def readInput():
    f = open("input.txt", "r")
    input = []
    for line in f.readlines():
        input.append(line.strip())
    return input

def main():
    input = readInput()
    sums = []
    counter = 0
    for num in input:
        if (not num):
            sums.append(counter)
            counter = 0
        else:
            counter += int(num)
    sums.append(counter)
    print('Part 1: ' + str(max(sums)))

    sums.sort()
    topThreeSum = sums[-1] + sums[-2] + sums[-3]
    print('Part 2: ' + str(topThreeSum))


if __name__ == "__main__":
    main()