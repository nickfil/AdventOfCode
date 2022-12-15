def readInput():
    f = open("input.txt", "r")
    input = []
    for line in f.readlines():
        input.append(line.strip())
    return input

def stripToSensorsBeacons(lst):
    sensors, beacons = [], []
    for line in lst:
        firstHalf = line.split(':')[0].replace('Sensor at ', '')
        firstHalf = firstHalf.replace('x=', '')
        firstHalf = firstHalf.replace('y=', '')
        secondHalf = line.split(':')[1].replace(' closest beacon is at ', '')
        secondHalf = secondHalf.replace('x=', '')
        secondHalf = secondHalf.replace('y=', '')

        sensors.append((int(firstHalf.split(',')[0]), int(firstHalf.split(',')[1])))
        beacons.append((int(secondHalf.split(',')[0]), int(secondHalf.split(',')[1])))

    return sensors, beacons

def getNonViablePositionsForY(sensors, beacons, yOfInterest):
    hashtags = set()
    for i in range(len(sensors)):
        maxDistance = abs(sensors[i][0] - beacons[i][0]) + abs(sensors[i][1] - beacons[i][1])
        
        for y in range(sensors[i][1]-maxDistance, sensors[i][1] + maxDistance):
            if y != yOfInterest:
                continue
            for x in range(sensors[i][0]-maxDistance, sensors[i][0]+maxDistance):
                curDistance = abs(sensors[i][0] - x) + abs(sensors[i][1] - y)
                if curDistance <= maxDistance:
                    hashtags.add((x, y))

    return hashtags

def isPositionViable(sensors, beacons, curX, curY):
    for i in range(len(sensors)):
        maxDistance = abs(sensors[i][0] - beacons[i][0]) + abs(sensors[i][1] - beacons[i][1])
        curDistance = abs(sensors[i][0] - curX) + abs(sensors[i][1] - curY)
        
        if curDistance <= maxDistance:
            return False
        
    return True

def getPossiblePoints(sensors, beacons):
    p = set()
    for i in range(len(sensors)):
        maxDistance = abs(sensors[i][0] - beacons[i][0]) + abs(sensors[i][1] - beacons[i][1])
        # from top to right       
        x, y = sensors[i][0], sensors[i][1] - maxDistance - 1
        while y != sensors[i][1]:
            p.add((x, y))
            x += 1
            y += 1
        # from right to bottom
        x, y = sensors[i][0] + maxDistance + 1, sensors[i][1]
        while x != sensors[i][0]:
            p.add((x, y))
            x -= 1
            y += 1
        # from bottom to left
        x, y = sensors[i][0], sensors[i][1] + maxDistance + 1
        while y != sensors[i][1]:
            p.add((x, y))
            x -= 1
            y -= 1
        # from left to top
        x, y = sensors[i][0] - maxDistance - 1, sensors[i][1]
        while x != sensors[i][0]:
            p.add((x, y))
            x += 1
            y -= 1
    
    return p

def part1(sensors, beacons):
    TEST_Y = 10
    Y = 2000000
    hashtags = getNonViablePositionsForY(sensors, beacons, Y)
    counter = 0
    for item in hashtags:
        if item not in beacons:
            counter +=1

    print("Part 1: ", counter)
    

def part2(sensors, beacons):
    TEST_MAX = 20
    MAX = 4000000
    points = getPossiblePoints(sensors, beacons)
    counter = 0
    for point in points:
        print(int((counter / len(points))* 100), "% of points tested", end='\r')
        counter += 1
        if 0 > point[0] or point[0] > MAX or 0 > point[1] or point[1] > MAX:
            continue
        
        if isPositionViable(sensors, beacons, point[0], point[1]):
            print("Part 2: ", 4000000*point[0] + point[1])
            exit()
    

def main():
    sensors, beacons = stripToSensorsBeacons(readInput())
    part1(sensors, beacons)
    part2(sensors, beacons)

if __name__ == "__main__":
    main()
