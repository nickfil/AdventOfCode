def listComparisonCounter(lst):
    c = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            c+=1
    return c

def transformToRollingWindowSum(lst, windowSize):
    flatList = []
    for i in range(len(lst)-windowSize+1):
        tempSum = 0
        for j in range(windowSize):
            tempSum+=lst[i+j]
        flatList.append(tempSum)
    return flatList


f = open("input.txt", "r")
sonarMeasurements = []
for line in f.readlines():
    sonarMeasurements.append(int(line))

counter = listComparisonCounter(sonarMeasurements)

print("Simple linear comparison answer: " + str(counter))

rollingWindowList = transformToRollingWindowSum(sonarMeasurements, 3)
counter = listComparisonCounter(rollingWindowList)

print("Rolling window of 3 sum answer: " + str(counter))

