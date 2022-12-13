def calculate_fuel_increasing(num):
    return num*(num+1)/2

f = open("input.txt", "r")
initial = []
for line in f.readlines():
    initial.extend(list(map(int,line.split(','))))

distances_per_position = {}

# populate points
for i in range(len(initial)):
    cur_distance = 0
    for each in initial:
        absolute_distance = abs(each-i)
        cur_distance += calculate_fuel_increasing(absolute_distance)
    if i not in distances_per_position:
        distances_per_position[i] = cur_distance

print(min(distances_per_position.values()))
    
