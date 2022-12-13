def increment_map(m):
    ret_map = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    zeroes = m[0]
    for key in reversed(sorted(m)):
        if(key==0):
            continue
        else:
            ret_map[key-1] = m[key]
    ret_map[6]+=zeroes
    ret_map[8]=zeroes
    return ret_map


f = open("input.txt", "r")
initial = []
for line in f.readlines():
    initial.extend(list(map(int,line.split(','))))

print("Initial population: " + str(len(initial)))
total_days = 256
population_map = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
for each in initial:
    population_map[each]+=1
print(population_map)

for i in range(total_days):
    population_map = increment_map(population_map)
    print("Day " + str(i+1) + ": " + str(sum(population_map.values())))
